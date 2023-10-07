# 导入requests和re模块
import requests
import re

# 定义文件的路径
path = "original.php"

# 定义正则表达式，匹配序号和名字
pattern = r"<span class=\"rank\">(\d+)</span>\s*<a href=\"[^\"]+\"><img src=\"[^\"]+\" alt=\"([^\"]+)\"></a>"

# 使用try...except语句来捕获并处理可能发生的异常
try:
    # 打开文件，读取内容
    with open(path, "r", encoding="utf-8") as f:
        response = f.read()

    # 使用re.findall方法，找出所有符合条件的结果
    results = re.findall(pattern, response)

    # 判断是否有匹配结果
    if results:
        # 打开一个文件，用于写入结果
        with open("top100.txt", "w", encoding="utf-8") as f:
            # 获取当前的年份和月份
            from datetime import datetime
            year = datetime.now().year
            month = datetime.now().month
            # 写入日期字符串
            f.write(f"<DATE:{year}.{month}>\n")
            # 遍历结果列表
            for result in results:
                # 将序号和名字用-号分隔，写入文件中
                f.write("-".join(result) + "\n")
        # 打印完成信息
        print("Done!")
        # 读取文件内容
        with open("top100.txt", "r", encoding="utf-8") as f:
            content = f.read()
            # 打印文件内容
            print(content)
    else:
        # 打印没有匹配结果的信息
        print("No matches found.")
except Exception as e:
    # 打印异常信息
    print("An error occurred:", e)
