from agents.courseware_agent import explain_courseware

def read_courseware_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    
course_text = read_courseware_file("sample_courseware.txt")

result = explain_courseware(course_text)

print(result)