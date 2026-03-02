import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text


def extract_invoice_number(text):

    lines = text.split("\n")

    for line in lines:
        if "Invoice" in line and "No" in line:

            parts = line.split(":")

            if len(parts) > 1:
                invoice = parts[1]

                # remove spaces
                invoice = invoice.replace(" ", "").strip()

                return invoice

    return "Not Found"


def extract_invoice_date(text):

    pattern = r"Date[:\s]*([0-9]{1,2}\s+[A-Za-z]+\s+[0-9]{4})"

    match = re.search(pattern, text)

    if match:
        return match.group(1)

    return "Not Found"


def extract_total_amount(text):

    pattern = r"Total amount.*?\$([0-9,]+\.[0-9]{2})"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group(1)

    return "Not Found"
