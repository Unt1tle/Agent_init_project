import os
from dotenv import load_dotenv
from openai import OpenAI

from prompts.courseware_prompt import build_courseware_prompt

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("没有找到 OPENAI_API_KEY，请检查 .env 文件")

client = OpenAI(api_key=api_key)


def explain_courseware(course_text: str) -> str:
    prompt = build_courseware_prompt(course_text)

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=prompt,
    )

    return response.output_text