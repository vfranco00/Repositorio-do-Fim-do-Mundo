// Converte o HTML do livro em PDF A4 usando o Chromium do Playwright.
// Uso: node scripts/pdf.js livro/fim-do-mundo.html livro/fim-do-mundo.pdf
const path = require('path');
let chromium;
try { ({ chromium } = require('playwright')); } catch (e) {
  console.error('Playwright não encontrado. Rode com NODE_PATH=$(npm root -g) ou instale o playwright.');
  process.exit(1);
}
(async () => {
  const [entrada, saida] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(entrada), { waitUntil: 'load', timeout: 120000 });
  await page.pdf({
    path: saida, format: 'A4', printBackground: true,
    margin: { top: '16mm', bottom: '18mm', left: '15mm', right: '15mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#666;font-family:sans-serif">Repositório do Fim do Mundo — página <span class="pageNumber"></span> de <span class="totalPages"></span></div>',
  });
  await browser.close();
  console.log(saida);
})();
