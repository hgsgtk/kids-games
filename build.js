import { cpSync, mkdirSync, rmSync, existsSync, readdirSync } from "node:fs";

const DIST = "dist";

if (existsSync(DIST)) {
  rmSync(DIST, { recursive: true });
}
mkdirSync(DIST);

// Copy static asset directories
const staticDirs = ["assets", "screenshots"];
for (const dir of staticDirs) {
  if (existsSync(dir)) {
    cpSync(dir, `${DIST}/${dir}`, { recursive: true });
  }
}

// Copy static files
const staticFiles = ["_headers"];
for (const file of staticFiles) {
  if (existsSync(file)) {
    cpSync(file, `${DIST}/${file}`);
  }
}

// Copy root index.html
if (existsSync("index.html")) {
  cpSync("index.html", `${DIST}/index.html`);
}

// Copy game HTML files from games/ directory
if (existsSync("games")) {
  mkdirSync(`${DIST}/games`, { recursive: true });
  for (const file of readdirSync("games")) {
    if (file.endsWith(".html")) {
      cpSync(`games/${file}`, `${DIST}/games/${file}`);
    }
  }
}

console.log("Build complete → dist/");
