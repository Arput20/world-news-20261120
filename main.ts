import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const botDir = process.env.MAKEFUN_BOT_DIR || import.meta.dirname || path.dirname(process.argv[1]);
const entryPath = path.join(botDir, 'entry.png');

if (!fs.existsSync(entryPath)) {
  console.error(`Error: entry.png not found at path: ${entryPath}. Note that MAKEFUN_BOT_DIR can point at the bot directory containing entry.png.`);
  process.exit(1);
}

const outputDir = process.env.MAKEFUN_OUTPUT_DIR || '/output';
const destPath = path.join(outputDir, 'entry.png');
const tempPath = path.join(outputDir, `.entry.png.tmp-${crypto.randomUUID()}`);

try {
  fs.mkdirSync(outputDir, { recursive: true });
  fs.copyFileSync(entryPath, tempPath);
  fs.renameSync(tempPath, destPath);
} catch (err) {
  console.error('Error: failed to copy entry.png atomically to output directory:', err);
  try {
    if (fs.existsSync(tempPath)) {
      fs.unlinkSync(tempPath);
    }
  } catch {}
  process.exit(1);
}
