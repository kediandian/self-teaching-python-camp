a = input('请输入第一个数字')   #用input函数，让输入的数字赋值到a上
b = input('请输入运算符号')     #用input 函数，让输入的运算符号赋值到b上
c = input('请输入第二个数字')    

a = int(a)                    #将字符串数据转换成数值数据类型
c = int(c)

if b == '+':                  #用if去做流程控制，主要就是控制运算符号
    x = a + c                 
    print(x)

elif b == '-':
    x = a - c
    print(x)

elif b == '*':
    x = a * c
    print(x)

elif b == '/':
    x = a / c
    print(x)

else:                         # 当没有输入正确的运算符的时候，提示错误，运用else
    print('对不起，您的运算符号输入错误')




