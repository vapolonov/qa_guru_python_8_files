from PyPDF2 import PdfReader


def test_pdf_number_of_pages():
    reader = PdfReader("resources/docs-pytest-org-en-latest.pdf")
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    assert number_of_pages == 412

    page = reader.pages[3]
    text = page.extract_text()
    print(text)
    assert "399" in text


test_pdf_number_of_pages()
