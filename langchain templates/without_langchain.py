import openai
from langchain_openai import ChatOpenAI
# Set the client to point to your local Ollama server instead of OpenAI's cloud
client = openai.OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")


def get_completion(prompt, model="qwen3:0.6b"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content


chat = ChatOpenAI(
    temperature=0.0, 
    model="qwen2.5:0.5b", 
    base_url="http://localhost:11434/v1", 
    api_key="ollama"
)

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

template_string = """
Read this customer message and extract:
- Product
- Problem
- Requested help

Return the answer in exactly this format:
Product: ...
Problem: ...
Requested help: ...

Text:
\"\"\"{text}\"\"\"
"""

prompt = template_string.format(text=customer_email)

print(prompt)

response = get_completion(prompt)

print(response)

