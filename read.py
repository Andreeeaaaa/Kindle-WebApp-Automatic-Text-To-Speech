import pytesseract

import settings

def img_to_text():
    pytesseract.pytesseract.tesseract_cmd = settings.WORKSPACE_DIR + r'/etc/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(settings.WORKSPACE_DIR + r'/screenshots_temp/screenshot.png', lang=settings.get_language())
    text = text.replace("\n", " ")
    return text
