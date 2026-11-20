import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
let botDir = process.env.MAKEFUN_BOT_DIR;

if (!botDir) {
  try {
    fs.accessSync(scriptDirectory, fs.constants.W_OK);
    botDir = scriptDirectory;
  } catch {
    botDir = '/bot';
  }
}

const sourcePath = path.join(botDir, 'entry.png');
if (!fs.existsSync(sourcePath)) {
  console.error(`Error: Could not locate entry.png in ${botDir}`);
  process.exit(1);
}

const targetDirectory = process.env.MAKEFUN_OUTPUT_DIR || '/output';
try {
  fs.mkdirSync(targetDirectory, { recursive: true });
} catch (err: any) {
  console.error(`Error: Failed to establish output directory '${targetDirectory}': ${err.message}`);
  process.exit(1);
}

const targetPath = path.join(targetDirectory, 'entry.png');
const temporaryPath = path.join(targetDirectory, `entry.png.tmp.${Date.now()}.${Math.random().toString(36).slice(2)}`);

try {
  fs.copyFileSync(sourcePath, temporaryPath);
  fs.renameSync(temporaryPath, targetPath);
  console.log(`Successfully delivered entry.png to ${targetPath}`);
} catch (err: any) {
  console.error(`Error: Atomic write operation failed: ${err.message}`);
  try {
    if (fs.existsSync(temporaryPath)) {
      fs.unlinkSync(temporaryPath);
    }
  } catch {}
  process.exit(1);
}
