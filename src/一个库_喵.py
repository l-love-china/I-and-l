import time
def 输入(内容):
    return input(内容)

def 打开(路径, 方式):
    return open(路径, 方式, encoding="utf-8")  # 建议加上编码  喵~

def 读取(操作):
    return 操作.read()
def 关闭(操作):
    操作.close()
def 分行拆分(原始文本: str) -> list[list[str]]:
    """
    把一段用换行符分隔的文本变成二维列表：
    一行一个内层列表，每个空格拆分一次，空行自动跳过。
    """
    return [行.split() for 行 in 原始文本.splitlines() if 行.strip()]
def 打印(内容):
    print(内容)
def 等于吗(值1, 值2):
    return 值1 == 值2
def 打开_读取():
    return "r" #看起来让中文更多github的老外看不懂  喵~
def 打开_写入():
    return "w"
def 打开_追加():
    return "a"
def 求长度(内容):
    return len(内容) #求长度 喵~
def 写入(操作, 内容):
    操作.write(内容)

# IO操作和变量处理函数
def 读取文件并返回变量名(文件名):
    return open(文件名, "r", encoding="utf-8")

def 写入到文件(文件对象, 内容):
    文件对象.write(内容)

def 关闭文件(文件对象):
    文件对象.close()

def 获取文本行数(文本):
    return len(文本.splitlines())

def 获取文本字符数(文本):
    return len(文本)

def 输入并保存到变量(提示信息, 变量名):
    """获取用户输入并保存到变量"""
    用户输入 = input(提示信息)
    return {变量名: 用户输入}

# 计算函数
def 加法运算(数值1, 数值2):
    return 数值1 + 数值2

def 减法运算(数值1, 数值2):
    return 数值1 - 数值2

def 乘法运算(数值1, 数值2):
    return 数值1 * 数值2

def 除法运算(数值1, 数值2):
    if float(数值2) == 0:
        print("错误：除数不能为零")
        return None
    return 数值1 / 数值2

def 次方运算(底数, 指数):
    return 底数 ** 指数

# 逻辑判断函数
def 大于吗(值1, 值2):
    return 值1 > 值2

def 小于吗(值1, 值2):
    return 值1 < 值2

def 大于等于吗(值1, 值2):
    return 值1 >= 值2

def 小于等于吗(值1, 值2):
    return 值1 <= 值2

def 不等于吗(值1, 值2):
    return 值1 != 值2

def 等于比较(值1, 值2):
    return 值1 == 值2

# 按位运算函数
def 按位与运算(值1, 值2):
    return 值1 & 值2

def 按位或运算(值1, 值2):
    return 值1 | 值2

def 按位非运算(值):
    return ~值

def 按位异或运算(值1, 值2):
    return 值1 ^ 值2

def 左移运算(值, 位数):
    return 值 << 位数

def 右移运算(值, 位数):
    return 值 >> 位数

# 字符串处理函数
def 字符串拼接(字符串1, 字符串2, 结果变量名=None):
    """拼接两个字符串，可选择保存到变量"""
    结果 = 字符串1 + 字符串2
    if 结果变量名:
        return {结果变量名: 结果}
    return 结果

def 字符串转大写(字符串, 结果变量名=None):
    """将字符串转换为大写，可选择保存到变量"""
    结果 = 字符串.upper()
    if 结果变量名:
        return {结果变量名: 结果}
    return 结果

def 字符串转小写(字符串, 结果变量名=None):
    """将字符串转换为小写，可选择保存到变量"""
    结果 = 字符串.lower()
    if 结果变量名:
        return {结果变量名: 结果}
    return 结果
def 等待(秒数):
    time.sleep(秒数)
