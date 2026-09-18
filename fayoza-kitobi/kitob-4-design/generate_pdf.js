/**
 * A4 PDF yig'adi.
 *
 *   node generate_pdf.js          -> fayoza-rus-tili.pdf       (o'qish uchun, 210x297mm)
 *   node generate_pdf.js --print  -> fayoza-rus-tili-print.pdf (bosmaxona uchun, 3mm bleed)
 *
 * Avval `python3 build.py` ni ishga tushiring — u index.html ni yangilaydi.
 */

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const isPrint = process.argv.includes('--print');
const inputHtml = path.resolve(__dirname, 'index.html');
const outputPdf = path.resolve(
  __dirname,
  isPrint ? 'fayoza-rus-tili-print.pdf' : 'fayoza-rus-tili.pdf'
);

if (!fs.existsSync(inputHtml)) {
  console.error('index.html topilmadi. Avval: python3 build.py');
  process.exit(1);
}

let sourceUrl = `file://${inputHtml}`;
let tempHtml = null;

if (isPrint) {
  // bleed rejimi: body ga .bleed sinfi va kattaroq @page o'lchami qo'shiladi
  const bleedStyle =
    '<style>@page { size: 216mm 303mm !important; margin: 0 !important; }</style>';
  const html = fs
    .readFileSync(inputHtml, 'utf8')
    .replace('</head>', `  ${bleedStyle}\n</head>`)
    .replace('<body>', '<body class="bleed">');
  tempHtml = path.resolve(__dirname, '.print-build.html');
  fs.writeFileSync(tempHtml, html);
  sourceUrl = `file://${tempHtml}`;
}

console.log(`${isPrint ? 'Bosmaxona' : "O'qish"} PDF: ${path.basename(outputPdf)}`);

const chrome = ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser']
  .find((bin) => {
    try {
      execSync(`command -v ${bin}`, { stdio: 'ignore' });
      return true;
    } catch (e) {
      return false;
    }
  });

if (!chrome) {
  console.error('Chrome/Chromium topilmadi.');
  process.exit(1);
}

const cmd = [
  `${chrome} --headless --disable-gpu --no-sandbox`,
  '--no-pdf-header-footer --run-all-compositor-stages-before-draw',
  '--virtual-time-budget=20000',
  `--print-to-pdf="${outputPdf}"`,
  `"${sourceUrl}"`,
].join(' ');

try {
  execSync(cmd, { stdio: ['ignore', 'ignore', 'pipe'] });
  const mb = (fs.statSync(outputPdf).size / 1024 / 1024).toFixed(2);
  console.log(`Tayyor: ${outputPdf} (${mb} MB)`);
  if (isPrint) {
    console.log('Sahifa o‘lchami 216x303mm — 3mm bleed bilan. Bosmaxonaga shu fayl beriladi.');
  }
} catch (err) {
  console.error('PDF yig‘ishda xato:', err.message);
  process.exit(1);
} finally {
  if (tempHtml && fs.existsSync(tempHtml)) fs.unlinkSync(tempHtml);
}
