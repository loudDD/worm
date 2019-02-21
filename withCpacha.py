from PIL import Image
from io import BytesIO
import requests
import pytesseract

res = requests.get("http://www.baidu.com/img/bd_logo1.png")

img = Image.open(BytesIO(res.content))#打开二进制文件
img.show()#打开图片（新窗口）

