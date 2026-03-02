import os
import pandas as pd
from pdf_reader import pdf_to_images
from extractor import (
    extract_text,
    extract_invoice_number,
    extract_invoice_date,
    extract_total_amount
)

input_folder = "input"
output_folder = "output"

results = []

for file in os.listdir(input_folder):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(input_folder, file)

        images = pdf_to_images(pdf_path)

        full_text = ""

        for img in images:
            text = extract_text(img)
            full_text += text

        invoice_number = extract_invoice_number(full_text)
        invoice_date = extract_invoice_date(full_text)
        total_amount = extract_total_amount(full_text)

        results.append({
            "File": file,
            "Invoice Number": invoice_number,
            "Invoice Date": invoice_date,
            "Total Amount": total_amount
        })

df = pd.DataFrame(results)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_file = os.path.join(output_folder, "invoice_output.xlsx")

df.to_excel(output_file, index=False)

print("Excel file created: invoice_output.xlsx")
