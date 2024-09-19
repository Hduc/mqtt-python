import openai
import requests
from PIL import Image
from io import BytesIO

# Thay thế 'your-api-key' bằng API Key của bạn từ OpenAI
openai.api_key = ''

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,  # số lượng hình ảnh bạn muốn
        size="512x512"  # kích thước hình ảnh
    )
    image_url = response['data'][0]['url']
    return image_url

def download_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img

# Sử dụng hàm generate_image để tạo hình ảnh
prompt = "a futuristic cityscape"
image_url = generate_image(prompt)
image = download_image(image_url)

# Lưu hình ảnh ra file
image.save('generated_image.png')
image.show()
