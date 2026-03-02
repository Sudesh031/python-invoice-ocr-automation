# Invoice OCR Automation using Python

This project is a simple automation system that extracts important information from invoice PDFs using OCR (Optical Character Recognition).

The program converts invoice PDFs into images, reads the text using Tesseract OCR, and automatically extracts key details like Invoice Number, Invoice Date, and Total Amount. The extracted information is then saved into an Excel file for easy use.

---

## Features

- Extract text from PDF invoices
- Supports single-page and multi-page invoices
- Automatically identifies:
  - Invoice Number
  - Invoice Date
  - Total Amount
- Saves extracted data into Excel
- Simple and modular Python code structure

---

## Technologies Used

- Python
- Tesseract OCR
- pdf2image
- Pillow
- Pandas
- OpenCV

---

## Project Structure

invoice-ocr-project

main.py → Main script that runs the project  
pdf_reader.py → Converts PDF pages into images  
extractor.py → Extracts invoice data using regex  
input/ → Folder where invoice PDFs are placed  
output/ → Folder where results can be stored  

---

## Installation

1. Install Python on your system.

2. Install the required Python libraries:

pip install pandas pytesseract pillow pdf2image opencv-python

3. Install Tesseract OCR and add it to the system PATH.

---

## How to Run the Project

1. Place invoice PDF files inside the **input** folder.

2. Run the main script:

python main.py

3. The extracted invoice data will be saved in an Excel file:

invoice_output.xlsx

---

## Example Output

File: invoice1.pdf  
Invoice Number: 055_03_2526  
Invoice Date: 2 February 2026  
Total Amount: 3,850.00  

---

## Future Improvements

- Extract Vendor Name
- Extract GST / ABN numbers
- Support multiple invoice formats
- Build a GUI for easy use
- Integrate AI-based invoice classification

---

## Author

Sudesh Singh
