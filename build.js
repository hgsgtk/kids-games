import { cpSync, mkdirSync, rmSync, existsSync, readdirSync } from "node:fs";

const DIST = "dist";

if (existsSync(DIST)) {
  rmSync(DIST, { recursive: true });
}
mkdirSync(DIST);

const staticDirs = ["assets", "screenshots"];
const staticFiles = ["_headers"];

for (const dir of staticDirs) {
  if (existsSync(dir)) {
    cpSync(dir, `${DIST}/${dir}`, { recursive: true });
  }
}

for (const file of staticFiles) {
  if (existsSync(file)) {
    cpSync(file, `${DIST}/${file}`);
  }
}

for (const file of readdirSync(".")) {
  if (file.endsWith(".html")) {
    cpSync(file, `${DIST}/${file}`);
  }
}

console.log("Build complete → dist/");
