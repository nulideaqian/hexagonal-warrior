import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL")

SYSTEM_PROMPT = """你是一个营销专家
商品信息如下:
{product_json}

请生成：
1. 商品标题（30字以内，包含核心规格）
2. 卖点文案，分三部分：实用场景 / 大容量优势 / 引起共鸣的语句

约束：禁止广告法违禁词，语气正式诚恳，目标人群：户外博主、大学生
"""

with open("./products.json", "r", encoding="utf-8") as f:
    product = json.load(f)

prompt = SYSTEM_PROMPT.format(
    product_json=json.dumps(product, ensure_ascii=False))

client = OpenAI(base_url=OPENAI_API_BASE, api_key=OPENAI_API_KEY)

if __name__ == "__main__":
    messages = []
    messages.append({"role": "system", "content": prompt})
    for i in range(5):
        user_input = input(">>> ")
        messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model=OPENAI_API_MODEL,
            messages=messages,
            n=2
        )
        print(response.choices[0].message.content)
        print("=" * 40)
        print(response.choices[1].message.content)
        messages.append({"role": "assistant", "content": response.choices[0].message.content})
