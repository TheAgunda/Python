## 📄 PDF Text Extraction Methods

### ✅ If PDF has selectable text (not scanned)

You can directly extract text using:

- `pdfplumber`
- `PyMuPDF`

These libraries work best for digitally created PDFs.

---

### 🔍 If PDF is scanned (image-based) → Use OCR (Important)

Install required Python packages:

```bash
pip install pytesseract pdf2image
```

### ⚙️ Install Tesseract OCR (Linux)

`sudo apt install tesseract-ocr`

### 🌐 Install Indian Language Packs

```
sudo apt install tesseract-ocr-hin   # Hindi
sudo apt install tesseract-ocr-pan   # Punjabi
sudo apt install tesseract-ocr-tam   # Tamil
```

## 🌐 Supported Indian Languages

This project uses **Tesseract OCR**, which supports multiple Indian languages.

### 📝 Available Language Codes

| Language  | Code  |
| --------- | ----- |
| Hindi     | `hin` |
| Punjabi   | `pan` |
| Gujarati  | `guj` |
| Tamil     | `tam` |
| Telugu    | `tel` |
| Bengali   | `ben` |
| Marathi   | `mar` |
| Kannada   | `kan` |
| Malayalam | `mal` |
| Sanskrit  | `san` |

---

### ⚙️ Usage

#### Single Language

```python
lang = "hin"
```
