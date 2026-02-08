#!/usr/bin/env bun
/**
 * Update internal links in documentation files
 * 
 * Scans all doc/ files and fixes links between them:
 * - [FILE.md](./FILE.md) -> [FILE.md](.FILE.md)
 * - [FILE.md](FILE.md) -> [FILE.md](.FILE.md)
 * - References like "See FILE.md" -> "See ./FILE.md" (when in doc/)
 */

import { $ } from "bun";
import { readdirSync, readFileSync, writeFileSync } from "fs";
import { join } from "path";

const DOC_DIR = "/home/jani/devel/markymarkov/doc";

interface UpdateResult {
  file: string;
  updated: boolean;
  changes: number;
}

async function log(message: string) {
  console.log(`[📋] ${message}`);
}

async function logSuccess(message: string) {
  console.log(`[✅] ${message}`);
}

/**
 * Update links in a document file
 * Converts absolute paths to relative paths for files in doc/
 */
function updateLinksInDocFile(content: string, fileName: string): string {
  let updated = false;
  let changeCount = 0;

  // Pattern 1: [text](./FILE.md) where FILE is also in doc/
  // Change to: [text](./FILE.md) - keep as is
  
  // Pattern 2: [text](FILE.md) where FILE is also in doc/
  // Change to: [text](.FILE.md) - add ./ for clarity
  content = content.replace(/\[([^\]]+)\]\(([A-Z_]+\.(?:md|txt))\)/g, (match, text, file) => {
    // Check if this is a doc file
    const isDocFile = readdirSync(DOC_DIR).includes(file);
    if (isDocFile) {
      updated = true;
      changeCount++;
      return `[${text}](./${file})`;
    }
    return match;
  });

  // Pattern 3: [text](./FILE.md) - already correct, keep it
  
  // Pattern 4: References to files from root (../../FILE.md or ../FILE.md)
  // These should stay as they navigate to root level
  
  // Pattern 5: Inline references like "See `FILE.md`" 
  content = content.replace(/(`?)([A-Z_]+\.(?:md|txt))\1(?![\w-])/g, (match, backtick, file) => {
    const isDocFile = readdirSync(DOC_DIR).includes(file);
    if (isDocFile && !match.includes("./")) {
      updated = true;
      changeCount++;
      return backtick + "./" + file + backtick;
    }
    return match;
  });

  return content;
}

/**
 * Main execution
 */
async function main(): Promise<void> {
  console.log("╔════════════════════════════════════════════════════════════╗");
  console.log("║       Update Documentation Internal Links                  ║");
  console.log("║   Converting absolute to relative paths in doc/           ║");
  console.log("╚════════════════════════════════════════════════════════════╝\n");

  try {
    // Get all doc files
    const docFiles = readdirSync(DOC_DIR)
      .filter((f) => f.endsWith(".md") || f.endsWith(".txt"))
      .sort();

    if (docFiles.length === 0) {
      logSuccess("No documentation files to update");
      return;
    }

    await log(`Processing ${docFiles.length} documentation files...`);
    console.log();

    const results: UpdateResult[] = [];
    let totalChanges = 0;

    for (const file of docFiles) {
      const filePath = join(DOC_DIR, file);
      const originalContent = readFileSync(filePath, "utf-8");
      const updatedContent = updateLinksInDocFile(originalContent, file);

      if (originalContent !== updatedContent) {
        writeFileSync(filePath, updatedContent);
        const changes = (updatedContent.match(/\.\//g) || []).length -
                       (originalContent.match(/\.\//g) || []).length;
        results.push({
          file,
          updated: true,
          changes: Math.abs(changes),
        });
        totalChanges += Math.abs(changes);
        console.log(`  ✏️  ${file}`);
      }
    }

    console.log();
    if (results.length === 0) {
      logSuccess("All links already correct");
    } else {
      logSuccess(`Updated ${results.length} files with ${totalChanges} link corrections`);
    }

    console.log("\n╔════════════════════════════════════════════════════════════╗");
    console.log("║                   ✅ LINKS UPDATED                        ║");
    console.log("╚════════════════════════════════════════════════════════════╝\n");
  } catch (error) {
    console.error(`[❌] Error: ${error}`);
    process.exit(1);
  }
}

main();
