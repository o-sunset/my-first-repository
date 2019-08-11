# coding=gbk
mode = str (input('请选择模式1.加密模式，2.解密模式，3.文件加密模式，4.文件解密模式'))#模式选择

#加密模式
if mode == '1':
   s = str(input('请输入加密内容'))
   result = ''
   move_mete = int(input('请输入偏移量'))    #加密输入端
   for i in range(len(s)):
        if i in range(len(s)):
            temp = ord(s[i])
            num =  (temp - 97 + move_mete) % 26
            result = chr(num + 97)
            print(result,end="")       #加密and输出

#解密模式
elif mode =='2':
    s = str(input('请输入解密内容'))
    result = ''
    move_mete = int(input('请输入偏移量'))#解密输入端
    for i in range(len(s)):
        if i in range(len(s)):
            temp = ord(s[i])
            num = (temp - 97 - move_mete) % 26
            result = chr(num + 97)
            print(result,end="")   #解密and输出


#文件加密模式
elif mode == '3':
    with open(str(input('请输入解密文件名'))) as file1:
        data = file1.read()

    result = ''
    move_mete = int(input('请输入偏移量'))  # 加密输入端
    for i in range(len(data)):
        if i in range(len(data)):
            temp = ord(data[i])
            num = (temp - 97 + move_mete) % 26
            result = chr(num + 97)
            print(result, end="") # 加密and输出

            file2 = open('加密.txt', 'a')
            file2.write(result)
            file2.close()            #保存文件

#文件解密模式
elif mode =='4':
    with open(str(input('请输入解密文件名'))) as file1:
        data = file1.read()

    result = ''
    move_mete = int(input('请输入偏移量'))  # 解密输入端
    for i in range(len(data)):
        if i in range(len(data)):
            temp = ord(data[i])
            num = (temp - 97 - move_mete) % 26
            result = chr(num + 97)
            print(result, end="")  # 解密and输出

            file2 = open('解密.txt', 'a')
            file2.write(result)
            file2.close()       #保存文件


elif mode == '666':
    print('哈哈哈，啥也没有')
else:
    print('无效')

