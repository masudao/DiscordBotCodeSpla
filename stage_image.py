from PIL import Image
import requests
import io

def mergeImage(url1, url2):

    image1 = Image.open(io.BytesIO(requests.get(url1).content)).resize((640, 360))
    image2 = Image.open(io.BytesIO(requests.get(url2).content)).resize((640, 360))

    dst = Image.new('RGB', (image1.width + image2.width, image1.height))

    dst.paste(image1, (0,0))
    dst.paste(image2, (image1.width,0))

    dst.save('output.png')
    print("マージ完了")