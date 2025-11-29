# --C 语言

## 简介
--C 是一种基于Python开发的解释型编程语言，其独特的设计特点是使用16位数字编码格式，其中大写的"I"代表1，小写的"l"代表0。该语言采用全中文关键字，使代码更易于理解和维护。

## 特点
- 使用16位数字编码格式，用大写的"I"代表1，小写的"l"代表0
- 支持I/O操作、计算操作、逻辑判断、字符串处理等功能
- 新建变量时不显示回显
- 输入内容保存在变量中
- 全中文关键字：所有函数和变量名均采用中文命名，使代码更易理解和维护
- 解释型语言：无需编译，直接运行源代码
- 简单易学：语法简洁明了，适合初学者入门编程
- 基于Python：底层使用Python实现，具有良好的跨平台兼容性

## 目录结构
```
|--c/
├── LICENSE              # MIT许可证
├── MD/                  # 文档目录
│   ├── help_Chiese.md   # 帮助文档
│   └── plan.md          # 开发计划
├── README.md            # 项目说明文件
├── demo/                # 示例代码目录
│   ├── 完整实例.miao     # 完整功能示例
│   └── 示例文件.txt      # 文件读取示例
├── src/                 # 源代码目录
│   ├── main.py          # 主程序入口
│   ├── 一个库_喵.py      # 核心函数库
│   └── 主逻辑_喵.py       # 主逻辑处理
└── test/                # 测试目录
```

## 使用方法
1. 确保已安装Python环境
2. 运行主程序：
   ```bash
   python src/main.py
   ```
3. 按照提示输入代码文件路径和名称
4. 程序会自动执行代码文件中的指令

## 示例演示
项目提供了一个完整的示例文件 `demo/完整实例.miao`，包含了所有功能的使用示例。运行主程序并加载该文件即可看到效果。

## 许可证
本项目采用MIT许可证，详情请查看 [LICENSE](LICENSE) 文件。

## 指令编码说明
每个指令由16位数字组成，分为四组，每组4位：
- 第一组：功能模块分类
- 第二组：具体操作类型
- 第三组和第四组：保留位，默认为l

### 功能模块分类（第一组）
- llll: I/O操作 和变量处理
- llIl: 计算操作
- llII: 逻辑判断
- llIII: 字符串处理
- IIII: 自定义函数（尚未实现）

### I/O操作和变量处理 (llll)
- llllllllllllllll: 打印内容
    - 用法：llllllllllllllll "要打印的字符串"
- lllllllllllllllI: 读取文件
    - 用法：lllllllllllllllI "要读取的文件名" "返回变量名"
- llllllllllllllIl: 输入并保存到变量
    - 用法：lllllllllllllIll "输入提示信息" "变量名"
- llllllllllllllII: 新建变量（无回显）
    - 用法：lllllllllllllIII "变量名" "变量值"
- lllllllllllllIll: 打印变量
    - 用法：lllllllllllllIll "变量名"
- lllllllllllllIlI: 退出程序
    - 用法：lllllllllllllIlI

### 计算操作 (llIl)
- llIlllllllllllIIl: 加法运算
    - 用法：llIlllllllllllIIl 数值1 数值2
- llIlllllllllllIII: 减法运算
    - 用法：llIlllllllllllIII 数值1 数值2
- llIllllllllllIlll: 乘法运算
    - 用法：llIllllllllllIlll 数值1 数值2
- llIllllllllllIllI: 除法运算
    - 用法：llIllllllllllIllI 数值1 数值2
- llIllllllllllIlII: 次方运算
    - 用法：llIllllllllllIlII 底数 指数

### 逻辑判断 (llII)
- llIIlllllllllllIl: 大于比较
    - 用法：llIIlllllllllllIl 值1 值2
- llIIlllllllllllII: 小于比较
    - 用法：llIIlllllllllllII 值1 值2
- llIIllllllllllIII: 等于比较
    - 用法：llIIllllllllllIII 值1 值2
- llIIlllllllllIlll: 不等于比较
    - 用法：llIIlllllllllIlll 值1 值2
- llIIllllllllllIll: 大于等于比较
    - 用法：llIIllllllllllIll 值1 值2
- llIIlllllllllIllI: 小于等于比较
    - 用法：llIIlllllllllIllI 值1 值2

### 字符串处理 (llIII)
- llIIIlllllllllIIl: 字符串拼接
    - 用法：llIIIlllllllllIIl "字符串1" "字符串2" "结果变量名"
- llIIIlllllllllIII: 转大写
    - 用法：llIIIlllllllllIII "字符串" "结果变量名"
- llIIIllllllllIlll: 转小写
    - 用法：llIIIllllllllIlll "字符串" "结果变量名"
使用auto-py-to-exe打包可执行文件
更多详细信息请查看 `MD/help_Chiese.md` 文件。