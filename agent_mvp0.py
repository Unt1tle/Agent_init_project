from agents.courseware_agent import explain_courseware

course_text = """
プラズマとは、電子とイオンが分離して存在する電離気体であり、
核融合や半導体プロセスなど多くの分野で利用されている。
"""

result = explain_courseware(course_text)

print(result)