import fitz  # PyMuPDF


def read_pdf_file(file_path: str) -> str:
    doc = fitz.open(file_path)

    all_text = []

    for page_index, page in enumerate(doc):
        page_text = page.get_text()

        if page_text.strip():
            all_text.append(f"\n--- 第 {page_index + 1} 页 ---\n")
            all_text.append(page_text)

    doc.close()

    return "\n".join(all_text)