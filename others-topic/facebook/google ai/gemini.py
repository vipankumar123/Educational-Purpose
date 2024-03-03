# pip install google-generativeai

import google.generativeai as genai

from api import API_KEY

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("what is opposite of tall?")

print(response.text)

