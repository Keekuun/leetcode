"""
输入一个数,如：4
输出对应个数的不同字母，如：‘abcd’
"""
import random

def output_str(num):
    set_str = set()

    while True:
        n = random.randint(97,122)
        set_str.add(chr(n))
        str = ''.join(set_str)
        if len(str) == num:  # 不相等说明生成的字母重复
            break
    print(str,len(str))


flag = True
while flag:
    num = int(input('请输入字母个数：'))
    if num > 27:
        print('只有26个英文字母')
    else:
        flag = False
        output_str(num)
        break