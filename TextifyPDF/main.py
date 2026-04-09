from pdf2image import convert_from_path
import pytesseract
import cv2
import numpy as np

images = convert_from_path("./sample/pdf-hindi-format.pdf")
lang= 'hin'
"""
Supported Indian Languages for OCR

This project uses Tesseract OCR, which supports multiple Indian languages.
You can specify the language(s) using the `lang` parameter.

Available language codes:
    - Hindi       : hin
    - Punjabi     : pan
    - Gujarati    : guj
    - Tamil       : tam
    - Telugu      : tel
    - Bengali     : ben
    - Marathi     : mar
    - Kannada     : kan
    - Malayalam   : mal
    - Sanskrit    : san

Usage:
    To use a single language:
        lang = "hin"

    To use multiple languages (recommended for mixed text):
        lang = "hin+eng"

Note:
    Make sure the required language data files are installed in Tesseract.
"""

for i, img in enumerate(images):
    img = np.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, lang=lang, config='--oem 3 --psm 6')
    print(text)