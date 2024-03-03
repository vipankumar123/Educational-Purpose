import google.generativeai as genai
from api import API_KEY
import os

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro-vision')

cookie_picture = [{
    'mime_type': 'image/png',
    'data': open('C:/Users/Hy_vipan/Downloads/llllll.jpg', 'rb').read()
}]
prompt = "Do these look store-bought or homemade?"

response = model.generate_content(
    model="gemini-pro-vision",
    content=[prompt, cookie_picture]
)
print(response.text)
