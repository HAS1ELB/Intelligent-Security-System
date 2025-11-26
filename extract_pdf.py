from pypdf import PdfReader

try:
    reader = PdfReader("systeme_Iot.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    with open("pdf_content.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Extraction successful")
except Exception as e:
    print(f"Error: {e}")
