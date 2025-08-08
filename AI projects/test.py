import ollama

response = ollama.chat(model='qwen2.5-coder:0.5b', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?answer in around 300 words',
    },
])

print(response['message']['content'])



