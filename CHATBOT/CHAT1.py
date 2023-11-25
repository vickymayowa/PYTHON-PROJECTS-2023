import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "how u doing "}])
print(completion.choices[0].message.content)