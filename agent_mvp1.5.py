import sys
from agents.courseware_agent import explain_courseware

def read_courseware_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    

def main():
    if len(sys.argv) < 2:
        print("请在命令后面输入课件文本文件路径")
        print("示例：python main.py sample_courseware.txt")
        return

    file_path = sys.argv[1]

    print(f"正在读取文件：{file_path}")

    course_text = read_courseware_file(file_path)

    print("正在调用课件理解 Agent...\n")

    result = explain_courseware(course_text)

    print(result)

if __name__ == "__main__":
    main()