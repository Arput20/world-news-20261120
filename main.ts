import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const botDir = process.env.MAKEFUN_BOT_DIR || __dirname;
const src = path.join(botDir, 'entry.png');

if (!fs.existsSync(src)) {
  console.error(`Error: Required file '${src}' not found.`);
  process.exit(1);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR || '/output';
try {
  fs.mkdirSync(outDir, { recursive: true });
} catch (err: any) {
  console.error(`Error: Failed to create output directory '${outDir}': ${err.message}`);
  process.exit(1);
}

const dest = path.join(outDir, 'entry.png');
const tempDest = `${dest}.${Date.now()}.${Math.random().toString(36).slice(2)}`;

try {
  fs.copyFileSync(src, tempDest);
  fs.renameSync(tempDest, dest);
} catch (err: any) {
  console.error(`Error: Failed to write output atomically: ${err.message}`);
  try {
    if (fs.existsSync(tempDest)) fs.unlinkSync(tempDest);
  } catch {}
  process.exit(1);
}
