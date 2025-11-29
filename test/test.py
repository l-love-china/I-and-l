list_m = [["cccccccccccccccc","要打印的字符串","FFFFFFFFFFFFFFFF","FFFFFFFFFFFFFFFF"],["cccccccccccccccc","要打印的字符","FFFFFFFFFFFFFFFF","FFFFFFFFFFFFFFFF"]]
行数=1
列数=1
print_a=0
for i in list_m:
    for k in i:
        # 因为技术债只能写屎山
        if 列数==1:
            # 检查是否是打印操作（16个c）
            if k == "cccccccccccccccc":
                print_a=1
            if print_a==1:
                # 打印第二列的内容（要打印的字符串）
                print(i[1])
                print_a=0
        列数+=1
    行数+=1
    列数=1