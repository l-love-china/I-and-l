from 一个库_喵 import 打印, 输入, 打开, 读取, 关闭, 分行拆分, 等于吗, 打开_读取, 打开_写入, 打开_追加, 求长度, 写入, 加法运算, 减法运算, 乘法运算, 除法运算, 次方运算, 大于吗, 小于吗, 大于等于吗, 小于等于吗, 不等于吗, 按位与运算, 按位或运算, 按位非运算, 按位异或运算, 左移运算, 右移运算, 字符串拼接, 字符串转大写, 字符串转小写, 输入并保存到变量
def 主逻辑(二维列表):
    打印("开始执行主逻辑 喵~")
    # 初始化变量
    变量存储区 = {}
    
    # 遍历每一行指令
    for 行 in 二维列表:
        if len(行) == 0:
            continue
            
        # 根据指令类型执行不同操作
        指令码 = 行[0]
        
        # 打印指令 llllllllllllllll
        if 指令码 == "llllllllllllllll":
            if len(行) > 1:
                打印(行[1])
                
        # 读取文件指令 lllllllllllllllI
        elif 指令码 == "lllllllllllllllI":
            if len(行) > 2:
                try:
                    文件名 = 行[1].strip('"')  # 去掉引号
                    变量名 = 行[2].strip('"')  # 去掉引号
                    文件对象 = 打开(文件名, 打开_读取())
                    文件内容 = 读取(文件对象)
                    关闭(文件对象)
                    变量存储区[变量名] = 文件内容
                    打印(f"文件 {文件名} 已读取到变量 {变量名}")
                except Exception as e:
                    打印(f"读取文件失败: {e}")
                    
        # 输入并保存到变量指令 llllllllllllllIl
        elif 指令码 == "lllllllllllllIll":
            if len(行) > 2:
                提示信息 = 行[1].strip('"')  # 去掉引号
                变量名 = 行[2].strip('"')  # 去掉引号
                输入结果 = 输入(提示信息)
                变量存储区[变量名] = 输入结果
                
        # 新建变量指令（无回显） llllllllllllllII
        elif 指令码 == "lllllllllllllIII":
            if len(行) > 2:
                变量名 = 行[1].strip('"')  # 去掉引号
                变量值 = 行[2].strip('"')  # 去掉引号
                变量存储区[变量名] = 变量值
                
        # 打印变量指令 lllllllllllllIll
        elif 指令码 == "lllllllllllllIll":
            if len(行) > 1:
                变量名 = 行[1].strip('"')  # 去掉引号
                if 变量名 in 变量存储区:
                    打印(变量存储区[变量名])
                
        # 退出程序指令 lllllllllllllIlI
        elif 指令码 == "lllllllllllllIlI":
            打印("程序退出 喵~")
            return
            
        # 加法运算指令 llIlllllllllllIIl
        elif 指令码 == "llIlllllllllllIIl":
            if len(行) > 2:
                结果 = 加法运算(float(行[1]), float(行[2]))
                打印(f"加法运算结果: {结果}")
                
        # 减法运算指令 llIlllllllllllIII
        elif 指令码 == "llIlllllllllllIII":
            if len(行) > 2:
                结果 = 减法运算(float(行[1]), float(行[2]))
                打印(f"减法运算结果: {结果}")
                
        # 乘法运算指令 llIllllllllllIlll
        elif 指令码 == "llIllllllllllIlll":
            if len(行) > 2:
                结果 = 乘法运算(float(行[1]), float(行[2]))
                打印(f"乘法运算结果: {结果}")
                
        # 除法运算指令 llIllllllllllIllI
        elif 指令码 == "llIllllllllllIllI":
            if len(行) > 2:
                结果 = 除法运算(float(行[1]), float(行[2]))
                if 结果 is not None:
                    打印(f"除法运算结果: {结果}")
                
        # 次方运算指令 llIllllllllllIlII
        elif 指令码 == "llIllllllllllIlII":
            if len(行) > 2:
                结果 = 次方运算(float(行[1]), float(行[2]))
                打印(f"次方运算结果: {结果}")
                
        # 大于比较指令 llIIlllllllllllIl
        elif 指令码 == "llIIlllllllllllIl":
            if len(行) > 2:
                结果 = 大于吗(float(行[1]), float(行[2]))
                打印(f"大于比较结果: {结果}")
                
        # 小于比较指令 llIIlllllllllllII
        elif 指令码 == "llIIlllllllllllII":
            if len(行) > 2:
                结果 = 小于吗(float(行[1]), float(行[2]))
                打印(f"小于比较结果: {结果}")
                
        # 等于比较指令 llIIllllllllllIII
        elif 指令码 == "llIIllllllllllIII":
            if len(行) > 2:
                结果 = 等于吗(float(行[1]), float(行[2]))
                打印(f"等于比较结果: {结果}")
                
        # 不等于比较指令 llIIlllllllllIlll
        elif 指令码 == "llIIlllllllllIlll":
            if len(行) > 2:
                结果 = 不等于吗(float(行[1]), float(行[2]))
                打印(f"不等于比较结果: {结果}")
                
        # 大于等于比较指令 llIIllllllllllIll
        elif 指令码 == "llIIllllllllllIll":
            if len(行) > 2:
                结果 = 大于等于吗(float(行[1]), float(行[2]))
                打印(f"大于等于比较结果: {结果}")
                
        # 小于等于比较指令 llIIlllllllllIllI
        elif 指令码 == "llIIlllllllllIllI":
            if len(行) > 2:
                结果 = 小于等于吗(float(行[1]), float(行[2]))
                打印(f"小于等于比较结果: {结果}")
                
        # 字符串拼接指令 llIIIlllllllllIIl
        elif 指令码 == "llIIIlllllllllIIl":
            if len(行) > 3:
                字符串1 = 行[1].strip('"')  # 去掉引号
                字符串2 = 行[2].strip('"')  # 去掉引号
                结果变量名 = 行[3].strip('"')  # 去掉引号
                结果字典 = 字符串拼接(字符串1, 字符串2, 结果变量名)
                变量存储区.update(结果字典)
                
        # 字符串转大写指令 llIIIlllllllllIII
        elif 指令码 == "llIIIlllllllllIII":
            if len(行) > 2:
                字符串 = 行[1].strip('"')  # 去掉引号
                结果变量名 = 行[2].strip('"')  # 去掉引号
                结果字典 = 字符串转大写(字符串, 结果变量名)
                变量存储区.update(结果字典)
                
        # 字符串转小写指令 llIIIllllllllIlll
        elif 指令码 == "llIIIllllllllIlll":
            if len(行) > 2:
                字符串 = 行[1].strip('"')  # 去掉引号
                结果变量名 = 行[2].strip('"')  # 去掉引号
                结果字典 = 字符串转小写(字符串, 结果变量名)
                变量存储区.update(结果字典)
            
    打印("主逻辑执行完毕 喵~")