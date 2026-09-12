/**
 * Script to generate high-fidelity print-ready A5 PDF for Case Study Booklet
 * Command: node generate_pdf.js
 */

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const inputHtml = path.resolve(__dirname, 'index.html');
const outputPdf = path.resolve(__dirname, 'case_study_booklet_a5.pdf');

console.log('Generating A5 PDF from:', inputHtml);

const chromeCmd = `google-chrome --headless --disable-gpu --no-pdf-header-footer --run-all-compositor-stages-before-draw --print-to-pdf="${outputPdf}" "file://${inputHtml}"`;

try {
  execSync(chromeCmd, { stdio: 'inherit' });
  if (fs.existsSync(outputPdf)) {
    const stats = fs.statSync(outputPdf);
    console.log(`\nSuccessfully created: ${outputPdf}`);
    console.log(`File size: ${(stats.size / 1024 / 1024).toFixed(2)} MB`);
  }
} catch (err) {
  console.error('Error during PDF generation:', err);
  process.exit(1);
}
