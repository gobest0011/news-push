import json
import urllib.request
import ssl
import re

# 跳过SSL验证
ssl._create_default_https_context = ssl._create_unverified_context

news = []
news.append("今日新闻摘要")
news.append("====================")
news.append("")

# 方法1：百度热搜
try:
    url = "https://top.baidu.com/board?tab=realtime"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'"word":"([^"]+)"', html)
        news.append("【百度热搜 Top 10】")
        for i, item in enumerate(items[:10], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("百度热搜获取失败: " + str(e))
    news.append("")

# 方法2：今日头条热点
try:
    url = "https://www.toutiao.com/hot-event/hot-board/?origin=web"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read())
        news.append("【今日头条热点】")
        for i, item in enumerate(data.get('data', [])[:10], 1):
            news.append(str(i) + ". " + item.get('Title', ''))
        news.append("")
except Exception as e:
    news.append("头条热点获取失败: " + str(e))
    news.append("")

# 方法3：知乎热榜
try:
    url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=10"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read())
        news.append("【知乎热榜 Top 10】")
        for i, item in enumerate(data.get('data', [])[:10], 1):
            title = item.get('target', {}).get('title', '')
            news.append(str(i) + ". " + title)
        news.append("")
except Exception as e:
    news.append("知乎热榜获取失败: " + str(e))
    news.append("")

# 写入文件
with open("news.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(news))
print("\n".join(news))
