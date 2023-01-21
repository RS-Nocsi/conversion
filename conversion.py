# Python实现任意进制与十进制之间的互相转化

# 定义一个名为Unable_to_process_the_data的异常（由于写这些代码的作者是个懒鬼，目前这个自定义的异常好像也没有什么用）
class Unable_to_process_the_data(Exception):
    pass


# 判断字符串中的每个字符是否都小于给定的整数
def bigger_than(n: str, cardinal: int) -> bool:
    # 定义了一个number字典，存储各个字符应该对应的数字（字符串形式）
    number = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", "A": "10", "B": "11",
              "C": "12", "D": "13", "E": "14", "F": "15", "G": "16", "H": "17", "I": "18", "J": "19", "K": "20",
              "L": "21", "M": "22", "N": "23", "O": "24", "P": "25", "Q": "26", "R": "27", "S": "28", "T": "29",
              "U": "30", "V": "31", "W": "32", "X": "33", "Y": "34", "Z": "35"}
    # 用一个列表推导式将n中的每一个字符都转换为数字，用来方便之后参与计算
    n = [number[i] if i in number else i for i in n]
    for i in n:
        # 循环判断每一个数字是否都合法，如果是则返回True，否则返回False
        if int(i) >= cardinal:
            return False
            break
    return True


# 1 将十进制整数转换为任意进制整数（基数小于等于36）
def decimal_to(n: int, cardinal: int = 2) -> str:
    try:
        # 判断n是否为一个整数
        if str(n).isdigit():
            # 判断基数是否在(1,37)这个区间上
            if 1 < cardinal < 37:
                n = int(n)
                # 对n的等于0，大于0，小于0三种情况分类操作
                # n等于0就直接输出0
                if n == 0:
                    return "0"
                # n大于0就继续操作（主代码）
                elif n > 0:
                    # 定义一个名为number的列表，用来之后把计算结果的数字替换成对应的字符
                    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                    # 定义一个名为origin的列表，用来存储计算结果
                    origin = []
                    # 开始计算
                    while n:
                        # 不断的将十进制整数整除以基数，得到的结果参与下一次循环，每次得到的余数存储在origin列表中，直到整除的结果n等于0，循环结束
                        s = n % cardinal
                        origin += [s]
                        n //= cardinal
                    # 把origin列表翻转
                    origin.reverse()
                    # 定义了一个空字符串，用来存储替换后的正确结果
                    result = ""
                    # 遍历origin列表，将列表中的各个值都替换成number列表中对应的字符并加到result字符串内
                    for i in origin:
                        result += str(number[i])
                    # 返回结果
                    return result
                else:
                    # 对于小于0的数就取绝对值再转换，最后用f-string在转换结果的前面加上负号
                    result = decimal_to(str(abs(n)), cardinal)
                    return f"-{result}"
            # 只要出现错误，就抛出Unable_to_process_the_data（无法处理数据）
            else:
                raise Unable_to_process_the_data()
        else:
            raise Unable_to_process_the_data()
    except:
        raise Unable_to_process_the_data()


# 2 将任意进制整数（基数小于等于36）转换为十进制整数
def to_decimal(n: str, cardinal: int = 2) -> "int or str(when_n_is_a_decimal)":
    try:
        # 将字符串中可能存在的各个字符都转换为大写
        n = str(n).upper()
        # 判断是否是小数，如果是就跳到float_to_decimal函数对小数进行处理
        if "." in str(n):
            return float_to_decimal(n, cardinal)
        # 判断是否为0，如果是就直接输出0
        if n == "0":
            return 0
        # 判断是否为负数，如果是就将相反数进行转换，再取相反数
        elif n[0] == "-":
            result = to_decimal(n[1:], cardinal)
            return 0 - int(result)
        # 判断基数是否在(1,37)这个区间上，且数据的各个字符都是合法字符（没有超过基数限制），如果是就继续运行主代码
        elif 1 < cardinal < 37 and bigger_than(n, cardinal):
            # 定义了一个number字典，存储各个字符应该对应的数字（字符串形式）
            number = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", "A": "10",
                      "B": "11", "C": "12", "D": "13", "E": "14", "F": "15", "G": "16", "H": "17", "I": "18", "J": "19",
                      "K": "20", "L": "21", "M": "22", "N": "23", "O": "24", "P": "25", "Q": "26", "R": "27", "S": "28",
                      "T": "29", "U": "30", "V": "31", "W": "32", "X": "33", "Y": "34", "Z": "35"}
            # 用一个列表推导式将n中的每一个字符都转换为数字，用来方便之后参与计算
            n = [number[i] if i in number else i for i in n]
            # 定义一个名为result的空列表，用来存储计算结果
            result = []
            # 开始计算
            for i in range(1, len(n) + 1):
                # 按照每一个数字*基数^权重的方式进行计算，并依次添加到result列表中
                result.append(int(n[-i]) * pow(cardinal, i - 1))
            # 对result每一项求和
            result = sum(result)
            # 返回结果
            return result
        # 只要出现错误，就抛出Unable_to_process_the_data（无法处理数据）
        else:
            raise Unable_to_process_the_data()
    except:
        raise Unable_to_process_the_data()


# 3 将十进制正小数转换为任意进制小数（基数小于等于36）
# 由于写这些代码的作者懒得Debug，该函数暂未对负数支持，且合法性判断以及鲁棒性方面比较欠缺
def float_decimal_to(n: float, cardinal: int = 2, precision: int = 10) -> str:
    try:
        # 判断基数是否在(1,37)这个区间上，如果是就继续
        if 1 < cardinal < 37:
            # 将n转换成浮点数
            n = float(n)
            # 判断是否为0，如果是就直接输出0.0
            if n == 0:
                return "0.0"
            else:
                # 将整数部分单独转换并存在integer变量中
                integer = decimal_to(int(n), cardinal)
                # 取小数部分
                n = n - int(n)
                # 定义一个名为number的列表，用来之后把计算结果的数字替换成对应的字符
                number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                # 定义一个名为origin的列表，用来存储计算结果
                origin = []
                # 开始计算
                while n:
                    # 不断的将十进制小数乘以基数，得到的结果的小数部分参与下一次循环，整数部分存储在origin列表中，直到乘积中的小数部分n等于0，循环结束
                    n *= cardinal
                    origin += [int(n)]
                    n -= int(n)
                # 定义一个名为result的空字符串，用来存储结果
                result = ""
                # 遍历origin列表，将列表中的各个值都替换成number列表中对应的字符并加到result字符串内
                for i in origin:
                    result += str(number[i])
                # 使用三元表达式，如果小数部分不为空（即数字是一个合法的小数），则使用f-string拼接整数部分与小数部分（小数部分用字符串切片保留精度）
                result = f"{integer}.{result[:precision]}" if len(result.strip(" ")) != 0 else integer
                # 返回结果
                return result
        # 只要出现错误，就抛出Unable_to_process_the_data（无法处理数据）
        else:
            raise Unable_to_process_the_data()
    except:
        raise Unable_to_process_the_data()


# 4 将任意进制小数（基数小于等于36）转换为十进制小数
# 由于写这些代码的作者懒得Debug，合法性判断以及鲁棒性方面比较欠缺
def float_to_decimal(n: str, cardinal: int = 2, precision: int = 10) -> "int(when_n_is_a_integer) or str":
    try:
        # 将字符串中可能存在的各个字符都转换为大写
        n = str(n).upper()
        # 判断是不是小数，如果不是，就跳到to_decimal函数对整数进行处理
        if not "." in str(n):
            return to_decimal(n, cardinal)
        else:
            # 判断是否为0，如果是就直接输出0
            if n == "0":
                return "0"
            else:
                # 定义了一个number字典，存储各个字符应该对应的数字（字符串形式）
                number = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", "A": "10",
                          "B": "11", "C": "12", "D": "13", "E": "14", "F": "15", "G": "16", "H": "17", "I": "18",
                          "J": "19", "K": "20", "L": "21", "M": "22", "N": "23", "O": "24", "P": "25", "Q": "26",
                          "R": "27", "S": "28", "T": "29", "U": "30", "V": "31", "W": "32", "X": "33", "Y": "34",
                          "Z": "35"}
                # 取整数部分
                integer = n.split(".")[0]
                # 将整数部分单独转换并存在integer变量中
                integer = to_decimal(integer, cardinal)
                # 取小数部分
                n = n.split(".")[1]
                # 用一个列表推导式将n中的每一个字符都转换为数字，用来方便之后参与计算
                n = [number[i] if i in number else i for i in n]
                # 定义一个名为result的空列表，用来存储计算结果
                result = []
                # 开始计算
                for i in range(1, len(n) + 1):
                    # 按照每一个数字*基数^权重的相反数的方式进行计算，并依次添加到result列表中
                    result.append(int(n[i - 1]) * pow(cardinal, -i))
                # 对result每一项求和并取小数部分
                result = str(sum(result)).split(".")[1]
                # 使用f-string拼接整数部分与小数部分（小数部分用字符串切片保留精度）
                return f"{integer}.{f'{result[:precision]}'}"
    # 只要出现错误，就抛出Unable_to_process_the_data（无法处理数据）
    except:
        raise Unable_to_process_the_data()


# 主程序
if __name__ == "__main__":
    try:
        # 输入相关信息并选择使用哪个函数
        number = input("请输入你要转换的数字：")
        cardinal = int(input("请输入要转换的进制的基数："))
        status = input(
            "请输入模式，十进制转x进制输入1，x进制转十进制输入2，十进制小数转x进制输入3，x进制小数转十进制输入4：")
        if status == "1":
            print(decimal_to(number, cardinal))
        elif status == "2":
            print(to_decimal(number, cardinal))
        elif status == "3":
            precision = int(input("请输入保留小数点后几位（不带四舍五入）："))
            print(float_decimal_to(number, cardinal, precision))
        else:
            precision = int(input("请输入保留小数点后几位（不带四舍五入）："))
            print(float_to_decimal(number, cardinal, precision))

    # 暂时不想处理异常
    except:
        print("无法处理数据")