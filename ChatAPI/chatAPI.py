import openai

# Replace 'your-api-key-here' with your actual OpenAI API key
openai.api_key = "api key here"

# Example prompt to send to GPT
prompt = "Explain the importance of machine learning in today's technology."

# Sending the prompt to the OpenAI API and getting the response
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Model that supports the chat API
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=100
)

# Printing the response text
print(response.choices[0].message['content'].strip())