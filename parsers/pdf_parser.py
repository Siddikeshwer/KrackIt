import pymupdf


def extract_pdf_text(file) -> str:

    text = ""

    pdf = pymupdf.open(
        stream=file.read(),
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text.strip()