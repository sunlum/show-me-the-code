# _*_ coding: utf-8 _*_

from PIL import Image,ImageFont,ImageDraw,ImageColor

def image_add_num(image,text):
    # 设置字体
    font = ImageFont.truetype("arial.ttf",50)
    # 设置字体颜色
    font_color = ImageColor.colormap.get('red')
    # 将字体加到图片上
    draw = ImageDraw.Draw(image)
    width,height = image.size
    print(width-50,height)
    draw.text((width-50,30),text,font=font,fill=font_color)
    # 保存图片
    image.save("image_2.jpg")


if __name__ == "__main__":
    image = Image.open("image_1.jpg")
    text = "4"
    image_add_num(image,text)