# coding=gbk
mode = str (input('��ѡ��ģʽ1.����ģʽ��2.����ģʽ��3.�ļ�����ģʽ��4.�ļ�����ģʽ'))#ģʽѡ��

#����ģʽ
if mode == '1':
   s = str(input('�������������'))
   result = ''
   move_mete = int(input('������ƫ����'))    #���������
   for i in range(len(s)):
        if i in range(len(s)):
            temp = ord(s[i])
            num =  (temp - 97 + move_mete) % 26
            result = chr(num + 97)
            print(result,end="")       #����and���

#����ģʽ
elif mode =='2':
    s = str(input('�������������'))
    result = ''
    move_mete = int(input('������ƫ����'))#���������
    for i in range(len(s)):
        if i in range(len(s)):
            temp = ord(s[i])
            num = (temp - 97 - move_mete) % 26
            result = chr(num + 97)
            print(result,end="")   #����and���


#�ļ�����ģʽ
elif mode == '3':
    with open(str(input('����������ļ���'))) as file1:
        data = file1.read()

    result = ''
    move_mete = int(input('������ƫ����'))  # ���������
    for i in range(len(data)):
        if i in range(len(data)):
            temp = ord(data[i])
            num = (temp - 97 + move_mete) % 26
            result = chr(num + 97)
            print(result, end="") # ����and���

            file2 = open('����.txt', 'a')
            file2.write(result)
            file2.close()            #�����ļ�

#�ļ�����ģʽ
elif mode =='4':
    with open(str(input('����������ļ���'))) as file1:
        data = file1.read()

    result = ''
    move_mete = int(input('������ƫ����'))  # ���������
    for i in range(len(data)):
        if i in range(len(data)):
            temp = ord(data[i])
            num = (temp - 97 - move_mete) % 26
            result = chr(num + 97)
            print(result, end="")  # ����and���

            file2 = open('����.txt', 'a')
            file2.write(result)
            file2.close()       #�����ļ�


elif mode == '666':
    print('��������ɶҲû��')
else:
    print('��Ч')

