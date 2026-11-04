// uso: node render.js saida.png arq1.svg arq2.svg ...
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const [out, ...files] = process.argv.slice(2);
  const imgs = files.map(f => `<div style="margin:8px;border:1px solid #ccc;display:inline-block;width:640px;vertical-align:top"><div style="font:12px sans-serif">${path.basename(f)}</div><img style="width:640px" src="data:image/svg+xml;base64,${fs.readFileSync(f).toString('base64')}"></div>`).join('');
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1340, height: 800 }, deviceScaleFactor: 1 });
  await p.setContent(`<body style="margin:0;background:#eee">${imgs}</body>`); await p.waitForTimeout(300);
  await p.screenshot({ path: out, fullPage: true }); await b.close();
})();
