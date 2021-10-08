import random
import datetime

def ident_generator():
    # 身份证号的前两位，省份代号
    province = ('11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35',
                '36', '37', '41', '42', '43', '44', '45', '46', '50', '51', '52', '53', '54', '61', '62', '63', '64',
                '65', '71', '81', '82')
    # 第3-第6位为市和区的代码。这里傻瓜式的设置为随机4位数(我知道这里没有0000-0999)
    district = random.randint(1000, 9999)
    # 第7-第14位出生的年月日的代码，这里设置的是，大于等于18岁左右，小于68岁左右
    birthdate = (datetime.date.today() - datetime.timedelta(days=random.randint(6500, 25000)))
    # 第15-第16位为户籍所在地派出所。这里傻瓜式的设置为随机2位数
    police_station = random.randint(10, 99)
    # 第17位性别
    gender = random.randrange(0, 9, 1)

    # 拼接出身份证号的前17位
    ident = province[random.randint(0, 33)] + str(district) + birthdate.strftime("%Y%m%d") + str(police_station) + str(
        gender)

    # 将前面的身份证号码17位数分别乘以不同的系数，系数见coe，然后将这17位数字和系数相乘的结果相加。用加出来和除以11，看余数是多少？
    coe = {1: 7, 2: 9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2, 8: 1, 9: 6, 10: 3, 11: 7, 12: 9, 13: 10, 14: 5, 15: 8, 16: 4,
           17: 2}
    summation = 0

    # ident[i:i+1]使用的是python的切片获得每位数字
    for i in range(17):
        summation = summation + int(ident[i:i + 1]) * coe[i + 1]

    # 用余数对照key得到校验码，比如余数为2，则校验码（第18位）为X
    key = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    check_code = key[summation % 11]

    return ident + check_code


if __name__ == '__main__':
    ids = ident_generator()
    print(ids)