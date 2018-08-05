# -*- coding: utf-8 -*-
_author_ = 'zhangqi'
 
import Image
def mod(x,y):
    return x%y;
#将得到的二进制串化成ASCII码
def toasc(str):
    return int(str, 2)
if __name__ == '__main__':
  a=""
  im = Image.open("d:/lena_rgb.bmp")
  f1 = file("D:\\zip1.txt", "r")
  s = f1.read()
  lenth = len(s)
  width = im.size[0]
  height = im.size[1]
  count = 0
  #直接提取最后一位 基于rgb三个图像
  for h in range(0, height):
       for w in range(0, width):
           pixel = im.getpixel((w, h))
           if count ==lenth*8:
               break
           if count%3==0:
               a = a+str((mod(int(pixel[0]),2)))
           elif count%3==1:
               a=a+str((mod(int(pixel[1]), 2)))
           else:
               a=a+str((mod(int(pixel[2]), 2)))
           count+=1
       if count == lenth*8:
           break
  print a#输出二进制
  print len(a)
  #将得到的明文写到文本
  with open("d:/zip2.txt","w") as f:
       for i in range(0,len(a),8):
           str = toasc(a[i:i+8])#化成ASCII码
           print chr(str)#输出明文
           f.write(chr(str))
           str =""
  f.closed


