import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL")

SYSTEM_PROMPT = """你是一个营销专家
根据用户消息的商品信息

请生成：
1. 商品标题（30字以内，包含核心规格）
2. 卖点文案，分三部分：实用场景 / 性价比优势 / 引起共鸣的语句

约束：禁止广告法违禁词，语气正式诚恳
"""

USER_PROMPT = """
以下是参考示例（学习风格和标准，不要照抄示例内容）

{examples}

现在请为以下商品生成：
商品信息：{product}
目标人群：{target_audience}
"""

client = OpenAI(base_url=OPENAI_API_BASE, api_key=OPENAI_API_KEY)

if __name__ == "__main__":
    messages = []
    messages.append({"role": "system", "content": SYSTEM_PROMPT})
    examples = input(">>> 请输入优秀的参考示例: ")
    product_input = input(">>> 请输入商品信息: ")
    target_audience_input = input(">>> 请输入目标人群: ")
    messages.append({"role": "user", "content": USER_PROMPT.format(product=product_input, target_audience=target_audience_input, examples=examples)})
    while(True):
        response = client.chat.completions.create(
            model=OPENAI_API_MODEL,
            messages=messages
        )
        print(response.choices[0].message.content)
        messages.append({"role": "assistant", "content": response.choices[0].message.content})
        user_input = input(">>> 请输入补充信息: (输入quit后退出)")
        if user_input == "quit":
            break
        messages.append({"role": "user", "content": user_input})
