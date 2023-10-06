# 导入requests和re模块
import requests
import re

# 定义网站的url
url = "https://github.com/Oranges-sama/JAV_DMM_FANZA_Rank/blob/main/original.php"

# 发送get请求，获取网页内容
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    # 获取网页文本
    text = response.text
    # 定义正则表达式，匹配序号和名字
    pattern = r"<span class=\"rank\">(\d+)</span>\n<a href=\".*?\">(.*?)</a>"
    # 使用re.findall方法，找出所有符合条件的结果
    results = re.findall(pattern, text)
    # 打开一个文件，用于写入结果
    with open("top100.txt", "w", encoding="utf-8") as f:
        # 遍历结果列表
        for result in results:
            # 将序号和名字用逗号分隔，写入文件中
            f.write(",".join(result) + "\n")
    # 打印完成信息
    print("Done!")
else:
    # 打印错误信息
    print("Error:", response.status_code)
