/**
 * OSON RUS TILI — A5 PDF generator.
 *
 *   node generate_pdf.js            -> oson-rus-tili.pdf       (o'qish uchun, A5 148x210mm)
 *   node generate_pdf.js --print    -> oson-rus-tili-print.pdf (bosmaxona uchun, 3mm bleed 154x216mm)
 */

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const isPrint = process.argv.includes('--print');
const inputHtml = path.resolve(__dirname, 'index.html');
const outputPdf = path.resolve(
  __dirname,
  isPrint ? 'oson-rus-tili-print.pdf' : 'oson-rus-tili.pdf'
);

let sourceUrl = `file://${inputHtml}`;
let tempHtml = null;

if (isPrint) {
  // A5 bleed rejimi: 148x210mm + 3mm bleed = 154x216mm
  const bleedStyle =
    '<style>@page { size: 154mm 216mm !important; margin: 0 !important; } .page { width: 154mm !important; height: 216mm !important; padding: 17mm 17mm 15mm 17mm !important; }</style>';
  const html = fs
    .readFileSync(inputHtml, 'utf8')
    .replace('</head>', `  ${bleedStyle}\n</head>`)
    .replace('<body>', '<body class="bleed">');
  tempHtml = path.resolve(__dirname, '.print-build.html');
  fs.writeFileSync(tempHtml, html);
  sourceUrl = `file://${tempHtml}`;
}

console.log(`PDF yaratilmoqda (${isPrint ? 'Bosmaxona (Bleed)' : "A5 O'qish"}): ${path.basename(outputPdf)}...`);

const cmd = [
  'google-chrome --headless --disable-gpu',
  '--no-pdf-header-footer',
  '--run-all-compositor-stages-before-draw',
  '--virtual-time-budget=5000',
  `--print-to-pdf="${outputPdf}"`,
  `"${sourceUrl}"`,
].join(' ');

try {
  execSync(cmd, { stdio: ['ignore', 'ignore', 'pipe'] });
  const mb = (fs.statSync(outputPdf).size / 1024 / 1024).toFixed(2);
  console.log(`Tayyor: ${outputPdf} (${mb} MB)`);
  if (isPrint) {
    console.log('Sahifa o‘lchami 154x216mm (3mm bleed bilan). Bosmaxonaga topshirishga tayyor.');
  }
} catch (err) {
  console.error('PDF yig‘ishda xato:', err.message);
  process.exit(1);
} finally {
  if (tempHtml && fs.existsSync(tempHtml)) fs.unlinkSync(tempHtml);
}
