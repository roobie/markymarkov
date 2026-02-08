#!/usr/bin/env bun
import { $ } from "bun";
import fs from "fs";

// Replace whole-word occurrences of `markymarkov` with `markymarkov` using sed
// Usage:
//   bun run scripts/replace-markymarkov.ts        # perform replacement
//   bun run scripts/replace-markymarkov.ts --dry-run   # show files that would be changed
//   bun run scripts/replace-markymarkov.ts --ext md,py,js  # limit to extensions (comma separated)

const args = process.argv.slice(2);
const dryRun = args.includes("--dry-run") || args.includes("-n");
const extArgIndex = args.findIndex(a => a === "--ext" || a === "-e");
let exts = [
  "py","md","txt","rst","json","toml","yaml","yml",
  "js","ts","html","css","sh","cfg","ini","rb","go","java","c","cpp","rs"
];
if (extArgIndex !== -1 && args[extArgIndex + 1]) {
  exts = args[extArgIndex + 1].split(",").map(e => e.trim().replace(/^\./, "")).filter(Boolean);
}

async function main() {
  // Detect OS
  const os = (await $`uname -s`).text();
  const isDarwin = os.trim() === "Darwin";

  // Run find to list all files, excluding .git and .venv
  const findCmd = $`find . -type f -not -path './.git/*' -not -path './.venv/*' -print0`;
  const findResult = await findCmd;
  const out = findResult.stdout?.toString() || "";
  if (!out) {
    console.log("No files found by find command.");
    return;
  }

  // Parse null-delimited list
  const allFiles = out.split('\0').filter(Boolean);

  // Filter by extension
  const lowerExts = exts.map(e => e.toLowerCase());
  const candidateFiles = allFiles.filter(f => {
    const idx = f.lastIndexOf('.');
    if (idx === -1) return false;
    const ext = f.slice(idx + 1).toLowerCase();
    return lowerExts.includes(ext);
  });

  if (candidateFiles.length === 0) {
    console.log('No candidate files matching extensions. Nothing to do.');
    return;
  }

  // Search inside files for whole-word 'markymarkov'
  const filesWithMarky: string[] = [];
  const wordRE = /(^|[^A-Za-z0-9_])markymarkov([^A-Za-z0-9_]|$)/; // conservative word boundary

  for (const file of candidateFiles) {
    try {
      const content = await Bun.file(file).text();
      if (wordRE.test(content)) filesWithMarky.push(file);
    } catch (e) {
      // ignore unreadable files
    }
  }

  if (filesWithMarky.length === 0) {
    console.log("No files with the word 'markymarkov' found (matching extensions). Nothing to do.");
    return;
  }

  console.log(`Found ${filesWithMarky.length} file(s) containing the word 'markymarkov'.`);

  if (dryRun) {
    for (const f of filesWithMarky) console.log(f);
    console.log('\nDry run complete. No files were modified.');
    return;
  }

  // Prepare sed expression using sed word anchors
  const sedExpr = "s/\\<markymarkov\\>/markymarkov/g";

  for (const file of filesWithMarky) {
    try {
      if (isDarwin) {
        // BSD sed requires an argument to -i
        await $`sed -i '' -e ${sedExpr} ${file}`;
      } else {
        await $`sed -i -e ${sedExpr} ${file}`;
      }
      console.log(`Updated: ${file}`);
    } catch (e) {
      // Fallback: perform JS replacement
      try {
        const content = await Bun.file(file).text();
        const replaced = content.replace(/(^|[^A-Za-z0-9_])markymarkov([^A-Za-z0-9_]|$)/g, (m, p1, p2) => `${p1}markymarkov${p2}`);
        if (replaced !== content) {
          await Bun.write(file, replaced);
          console.log(`Updated (JS): ${file}`);
        }
      } catch (err) {
        console.error(`Failed to update ${file}: ${err}`);
      }
    }
  }

  console.log('\nReplacement complete.');
  console.log('Note: this used sed with word anchors (\\< \\>) to match whole words.');
}

main().catch(err => {
  console.error('Error:', err);
  process.exit(1);
});
