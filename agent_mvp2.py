import sys
from pathlib import Path

from agents.courseware_agent import explain_courseware
from parsers.text_parser import read_text_file
from parsers.pdf_parser import read_pdf_file

def read_courseware_file(file_path: str) -> str:
    suffix = Path(file_path).suffix.lower()

    if suffix == ".txt":
        return read_text_file(file_path)

    if suffix == ".pdf":
        return read_pdf_file(file_path)

    raise ValueError(f"暂不支持这个文件类型：{suffix}")

def main():
    if len(sys.argv) < 2:
        print("请在命令后面输入课件文件路径")
        print("示例：python main.py sample_courseware.txt")
        print("示例：python main.py sample.pdf")
        return

    file_path = sys.argv[1]

    print(f"正在读取文件：{file_path}")

    course_text = read_courseware_file(file_path)

    if not course_text.strip():
        print("没有从文件中读取到文字。")
        print("可能原因：PDF 是扫描版图片，暂时还没有 OCR 功能。")
        return

    print("文件读取完成。")
    print("正在调用课件理解 Agent...\n")

    result = explain_courseware(course_text)

    print(result)


if __name__ == "__main__":
    main()