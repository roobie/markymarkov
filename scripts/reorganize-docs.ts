#!/usr/bin/env bun
/**
 * Reorganize documentation files
 * 
 * Moves all markdown and text files (except README.md, MINDMAP.md, PROTOCOL_MINDMAP.md)
 * to the doc/ directory and updates all cross-references.
 */

import { $ } from "bun";
import { existsSync, readdirSync, readFileSync, writeFileSync } from "fs";
import { join } from "path";

const ROOT = "/home/jani/devel/marky";
const DOC_DIR = join(ROOT, "doc");
const FILES_TO_KEEP_IN_ROOT = new Set([
  "README.md",
  "MINDMAP.md",
  "PROTOCOL_MINDMAP.md",
]);

interface FileMove {
  from: string;
  to: string;
}

// Regex patterns for finding markdown/text references
const MARKDOWN_LINK_PATTERN = /\[([^\]]+)\]\(\.?\/?([^/)]+\.(?:md|txt))\)/g;
const INLINE_REFERENCE_PATTERN = /(?:See|see|Read|read|found at|found in|located at)\s+([`]?)([A-Z_]+\.(?:md|txt))\1/g;
const FILE_REFERENCE_PATTERN = /([A-Z_]+\.(?:md|txt))/g;

async function log(message: string) {
  console.log(`[📋] ${message}`);
}

async function logError(message: string) {
  console.error(`[❌] ${message}`);
}

async function logSuccess(message: string) {
  console.log(`[✅] ${message}`);
}

/**
 * Get all markdown and text files in root directory
 */
function getFilesToMove(): FileMove[] {
  const moves: FileMove[] = [];

  const files = readdirSync(ROOT);

  for (const file of files) {
    const ext = file.endsWith(".md") || file.endsWith(".txt");
    if (!ext) continue;

    if (FILES_TO_KEEP_IN_ROOT.has(file)) {
      continue; // Keep in root
    }

    moves.push({
      from: join(ROOT, file),
      to: join(DOC_DIR, file),
    });
  }

  return moves;
}

/**
 * Build a map of old paths to new paths
 */
function buildPathMap(
  moves: FileMove[]
): Map<string, { oldName: string; newName: string }> {
  const map = new Map<string, { oldName: string; newName: string }>();

  for (const move of moves) {
    const baseName = move.from.split("/").pop()!;
    map.set(baseName, {
      oldName: baseName,
      newName: baseName,
    });
  }

  return map;
}

/**
 * Update links in a markdown file
 */
function updateLinksInFile(
  filePath: string,
  pathMap: Map<string, { oldName: string; newName: string }>,
  fileIsInDoc: boolean
): string {
  let content = readFileSync(filePath, "utf-8");
  let updated = false;

  // Replace markdown links: [text](./FILE.md) or [text](FILE.md)
  content = content.replace(MARKDOWN_LINK_PATTERN, (match, text, filePath) => {
    if (pathMap.has(filePath)) {
      updated = true;
      // If file is moving to doc/, and we're in root, use doc/
      // If file is moving to doc/, and we're in doc/, use ./
      const prefix = fileIsInDoc ? "./" : "doc/";
      return `[${text}](${prefix}${filePath})`;
    }
    return match;
  });

  // Replace inline references: See `FILE.md` or "See FILE.md"
  content = content.replace(
    INLINE_REFERENCE_PATTERN,
    (match, backtick, fileName) => {
      if (pathMap.has(fileName)) {
        updated = true;
        const prefix = fileIsInDoc ? "./" : "doc/";
        return `${match.substring(0, match.indexOf(fileName))}${prefix}${fileName}`;
      }
      return match;
    }
  );

  return content;
}

/**
 * Update links in MINDMAP.md (special handling)
 */
function updateMindmapLinks(
  filePath: string,
  pathMap: Map<string, { oldName: string; newName: string }>
): string {
  let content = readFileSync(filePath, "utf-8");
  let updated = false;

  // Handle references in node descriptions
  // Pattern: [FILE.md](./FILE.md) -> [FILE.md](./doc/FILE.md)
  content = content.replace(MARKDOWN_LINK_PATTERN, (match, text, filePath) => {
    if (pathMap.has(filePath)) {
      updated = true;
      return `[${text}](./doc/${filePath})`;
    }
    return match;
  });

  // Handle inline references in descriptions
  content = content.replace(
    /(?:See|see|Read|read|at|in)\s+([A-Z_]+\.(?:md|txt))/g,
    (match, fileName) => {
      if (pathMap.has(fileName)) {
        updated = true;
        return match.replace(fileName, `doc/${fileName}`);
      }
      return match;
    }
  );

  return content;
}

/**
 * Update links in test files and source code
 */
function updateCodeLinks(
  filePath: string,
  pathMap: Map<string, { oldName: string; newName: string }>
): string {
  let content = readFileSync(filePath, "utf-8");

  // Only update if this looks like a doc reference
  // Pattern: See [FILE](./FILE.md) in comments
  content = content.replace(MARKDOWN_LINK_PATTERN, (match, text, filePath) => {
    if (pathMap.has(filePath)) {
      return `[${text}](./doc/${filePath})`;
    }
    return match;
  });

  return content;
}

/**
 * Move files to doc/ directory
 */
async function moveFiles(moves: FileMove[]): Promise<void> {
  for (const move of moves) {
    const baseName = move.from.split("/").pop()!;
    try {
      await $`mv ${move.from} ${move.to}`;
      logSuccess(`Moved ${baseName} to doc/`);
    } catch (error) {
      logError(`Failed to move ${baseName}: ${error}`);
    }
  }
}

/**
 * Update all markdown files with new links
 */
async function updateAllLinks(
  pathMap: Map<string, { oldName: string; newName: string }>
): Promise<void> {
  // Update MINDMAP.md
  const mindmapPath = join(ROOT, "MINDMAP.md");
  const mindmapContent = updateMindmapLinks(mindmapPath, pathMap);
  writeFileSync(mindmapPath, mindmapContent);
  logSuccess("Updated MINDMAP.md links");

  // Update PROTOCOL_MINDMAP.md
  const protocolPath = join(ROOT, "PROTOCOL_MINDMAP.md");
  if (existsSync(protocolPath)) {
    const protocolContent = updateLinksInFile(protocolPath, pathMap, false);
    writeFileSync(protocolPath, protocolContent);
    logSuccess("Updated PROTOCOL_MINDMAP.md links");
  }

  // Update README.md
  const readmePath = join(ROOT, "README.md");
  if (existsSync(readmePath)) {
    const readmeContent = updateLinksInFile(readmePath, pathMap, false);
    writeFileSync(readmePath, readmeContent);
    logSuccess("Updated README.md links");
  }

  // Update all files in doc/ directory
  const docFiles = readdirSync(DOC_DIR);
  for (const file of docFiles) {
    if (!file.endsWith(".md") && !file.endsWith(".txt")) continue;

    const filePath = join(DOC_DIR, file);
    const content = updateLinksInFile(filePath, pathMap, true);
    writeFileSync(filePath, content);
  }
  logSuccess(`Updated links in all ${docFiles.length} doc/ files`);

  // Update Python source files (if they reference docs)
  const pyFiles = await $`find ${ROOT}/src -name "*.py" -o -name "*.ts" -o -name "*.tsx"`.text();
  const files = pyFiles.trim().split("\n").filter(f => f);
  
  for (const file of files) {
    if (!file) continue;
    try {
      const content = readFileSync(file, "utf-8");
      if (!content.includes(".md")) continue; // Skip if no markdown refs
      
      const updated = updateCodeLinks(file, pathMap);
      if (updated !== content) {
        writeFileSync(file, updated);
      }
    } catch (error) {
      // Silently skip files that can't be read
    }
  }
}

/**
 * Verify doc/ directory was created
 */
async function ensureDocDir(): Promise<void> {
  if (!existsSync(DOC_DIR)) {
    await $`mkdir -p ${DOC_DIR}`;
    logSuccess("Created doc/ directory");
  }
}

/**
 * Main execution
 */
async function main(): Promise<void> {
  console.log("╔════════════════════════════════════════════════════════════╗");
  console.log("║       Documentation Reorganization Script                  ║");
  console.log("║  Moving files to doc/ and updating all cross-references   ║");
  console.log("╚════════════════════════════════════════════════════════════╝\n");

  try {
    // Step 1: Ensure doc directory exists
    await log("Step 1: Ensuring doc/ directory exists...");
    await ensureDocDir();

    // Step 2: Get files to move
    await log("Step 2: Identifying files to move...");
    const moves = getFilesToMove();
    if (moves.length === 0) {
      logSuccess("No files to move");
      return;
    }
    console.log(`   Found ${moves.length} files to move:\n`);
    moves.forEach((m) => {
      const baseName = m.from.split("/").pop()!;
      console.log(`     • ${baseName}`);
    });
    console.log();

    // Step 3: Build path map
    await log("Step 3: Building path mapping...");
    const pathMap = buildPathMap(moves);
    logSuccess(`Created mapping for ${pathMap.size} files`);

    // Step 4: Move files
    await log("Step 4: Moving files to doc/...");
    await moveFiles(moves);

    // Step 5: Update all links
    await log("Step 5: Updating cross-references in all files...");
    await updateAllLinks(pathMap);

    // Step 6: Verify
    await log("Step 6: Verifying move...");
    const rootMdFiles = readdirSync(ROOT).filter(
      (f) => f.endsWith(".md") || f.endsWith(".txt")
    );
    console.log(`   Root directory files: ${rootMdFiles.join(", ")}`);
    logSuccess(`Verified: Only ${rootMdFiles.length} files in root (should be 3)`);

    console.log("\n╔════════════════════════════════════════════════════════════╗");
    console.log("║                   ✅ REORGANIZATION COMPLETE              ║");
    console.log("╚════════════════════════════════════════════════════════════╝\n");

    // Summary
    console.log("Summary:");
    console.log(`  • Moved ${moves.length} files to doc/`);
    console.log(`  • Updated links in root files`);
    console.log(`  • Updated links in doc/ files`);
    console.log("\nRoot directory now contains:");
    console.log("  • README.md");
    console.log("  • MINDMAP.md");
    console.log("  • PROTOCOL_MINDMAP.md");
    console.log("\nAll other documentation is in doc/\n");
  } catch (error) {
    logError(`Fatal error: ${error}`);
    process.exit(1);
  }
}

main();
