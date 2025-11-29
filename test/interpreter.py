def interpret_c_language(file_path):
    """
    解释执行--C语言文件
    根据help_Chiese.md的规范实现基本功能
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line_num, line in enumerate(lines, 1):
            # 移除换行符并分割指令
            parts = line.strip().split(' ', 1)
            if len(parts) < 1:
                continue
                
            instruction = parts[0]
            
            # 打印指令 (16个c)
            if instruction == "cccccccccccccccc":
                if len(parts) > 1:
                    # 提取引号中的内容
                    content = parts[1]
                    if content.startswith('"') and '"' in content[1:]:
                        # 提取双引号中的内容
                        end_quote = content.find('"', 1)
                        if end_quote != -1:
                            text_to_print = content[1:end_quote]
                            print(text_to_print)
                    else:
                        print(content)
                        
    except FileNotFoundError:
        print("错误: 文件不存在")
        return 1
    except Exception as e:
        print(f"执行错误: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("用法: python interpreter.py <文件名>")
    else:
        exit_code = interpret_c_language(sys.argv[1])
        sys.exit(exit_code)