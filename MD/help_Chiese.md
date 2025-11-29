# --C 语言帮助文档

每一个函数有个长度，不够的在后面用F填充
退出代码
    l 正常退出
    I 文件不存在

代码使用16位数字编码格式，用大写的"I"代表1，小写的"l"代表0

## 指令编码规则
分为4组，每组4位数字
- 第一组：功能模块分类
- 第二组：具体操作类型
- 第三组和第四组：保留位，默认为l

## 功能模块分类（第一组）
- llll I/O操作 和变量处理
- llIl 计算操作
- llII 逻辑判断
- llIII 字符串处理
- IIII 自定义函数

## I/O操作 和变量处理 (llll)
### 具体操作类型（第二组）
- llll 打印内容
    - 用法：llllllllllllllll "要打印的字符串"
- lllI 读取文件
    - 用法：lllllllllllllllI "要读取的文件名" "返回变量名"
- llIl 输入并保存到变量
    - 用法：lllllllllllllIll "输入提示信息" "变量名"
- llII 新建变量（无回显）
    - 用法：lllllllllllllIII "变量名" "变量值"
- lIll 打印变量
    - 用法：lllllllllllllIll "变量名"
- lIlI 退出程序
    - 用法：lllllllllllllIlI

## 计算操作 (llIl)
### 具体操作类型（第二组）
- llll 加法运算
    - 用法：llIlllllllllllIIl 数值1 数值2
- lllI 减法运算
    - 用法：llIlllllllllllIII 数值1 数值2
- llIl 乘法运算
    - 用法：llIllllllllllIlll 数值1 数值2
- llII 除法运算
    - 用法：llIllllllllllIllI 数值1 数值2
- lIll 次方运算
    - 用法：llIllllllllllIlII 底数 指数

## 逻辑判断 (llII)
### 具体操作类型（第二组）
- llll 等于比较
    - 用法：llIIllllllllllIII 值1 值2
- lllI 不等于比较
    - 用法：llIIlllllllllIlll 值1 值2
- llIl 大于比较
    - 用法：llIIlllllllllllIl 值1 值2
- llII 小于比较
    - 用法：llIIlllllllllllII 值1 值2
- lIll 大于等于比较
    - 用法：llIIllllllllllIll 值1 值2
- lIlI 小于等于比较
    - 用法：llIIlllllllllIllI 值1 值2

## 字符串处理 (llIII)
### 具体操作类型（第二组）
- llll 字符串拼接
    - 用法：llIIIlllllllllIIl "字符串1" "字符串2" "结果变量名"
- lllI 转大写
    - 用法：llIIIlllllllllIII "字符串" "结果变量名"
- llIl 转小写
    - 用法：llIIIllllllllIlll "字符串" "结果变量名"

## 自定义函数 (IIII)
### 具体操作类型（第二组）
- llll 开始自定义
    - 用法：III Illlllllllllll "函数名"
- lllI 结束自定义
    - 用法：III IllllllllllllI

自定义途径还没有制作，等下一个版本