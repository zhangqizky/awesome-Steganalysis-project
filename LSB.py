# -*- coding: utf-8 -*-  
_author_ = 'zhangqi'
#取出RGB 值得 lsb  替换
import Image
import matplotlib.pyplot as plt
 
#得到加密文字的二进制形式
def plus(str):
   return str.zfill(8)
def get_key():
   f = file("D:\\zip1.txt", "r")
   str = ""
   s = f.read()
   print s
   for i in range(len(s)):
      str=str+ plus(bin(ord(s[i])).replace('0b', ''))
   print str
   f.closed
   return str
def mod(x,y):
    return x%y;
 
if __name__ == '__main__':
  im = Image.open("d:/lena.jpg")
  plt.subplot(1, 2, 1), plt.title('origin')
  plt.imshow(im), plt.axis('off')
  width = im.size[0]
  height = im.size[1]
  count = 0
  key = get_key()  #得到 文本信息
  #如果嵌入的文字过多导致载体不够大
  if width*height*3<len(key):
      print "please change the image"
      exit()
  #基于最低位lsb嵌入
  for h in range(0, height):
     for w in range(0, width):
        pixel = im.getpixel((w, h))
        a = pixel[0]#R
        b = pixel[1]#G
        c = pixel[2]#B
        if count == len(key):
            break
        #LSB 嵌入过程  替换最后一位
        if count%3==0:
            a= a-mod(a,2)+int(key[count])
        elif count%3==1:
            b = b- mod(b, 2) + int(key[count])
        else:
            c= c-mod(c,2)+int(key[count])
        im.putpixel((w,h),(a,b,c))
        count=count+1
     if count == len(key):#全部潜入完毕
         break
  plt.subplot(1, 2, 2), plt.title('now')#前后两个图片对比
  plt.imshow(im), plt.axis('off')
  plt.show()
  im.save(r"d:/lena_rgb.bmp")
  print "success\n"


