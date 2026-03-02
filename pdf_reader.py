from pdf2image import convert_from_path


def pdf_to_images(pdf_path):

    images = convert_from_path(
        pdf_path,
        poppler_path=r"D:\Project\Automation with Python\Release-25.12.0-0\poppler-25.12.0\Library\bin"
    )

    return images
