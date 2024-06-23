from bs4 import BeautifulSoup
import requests
import argparse

# 创建命令行参数解析器
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str, help='URL参数')
args = parser.parse_args()

# 获取URL参数
url = args.url

# 发起请求
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

script_tags = soup.find_all('script')

js_urls = []
for script_tag in script_tags:
    src = script_tag.get('src')
    if src:
        if src.startswith('http') or src.startswith('//'):
            if src.startswith('//'):
                src = "https:" + src
        print(src)
