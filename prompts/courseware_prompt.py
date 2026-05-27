def build_courseware_prompt(course_text: str) -> str:
    return f"""
你是一个课件理解辅助 Agent。
请根据下面的课件内容，用中文帮助学生理解。

要求：
1. 用一句话总结
2. 列出 3 个重点
3. 解释一个可能难懂的地方
4. 举一个简单例子
5. 出一道小测题，并给出答案

课件内容：
{course_text}
"""