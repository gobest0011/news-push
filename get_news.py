import json
import urllib.request
import ssl
import re
import os

# 跳过SSL验证
ssl._create_default_https_context = ssl._create_unverified_context

news = []
news.append("今日新闻摘要")
news.append("====================")
news.append("")

# ========== 国内热搜 ==========
# 百度热搜
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
    news.append("百度热搜获取失败")
    news.append("")

# ========== 国内科技新闻 ==========
# IT之家
try:
    url = "https://www.ithome.com/listtech"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<a href="https://www\.ithome\.com/[^"]+"[^>]*>([^<]+)</a>', html)
        news.append("【IT之家】")
        for i, item in enumerate(items[:10], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("IT之家获取失败")
    news.append("")

# 36氪
try:
    url = "https://36kr.com/newsflashes"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'"title":"([^"]+)"', html)
        news.append("【36氪快讯】")
        for i, item in enumerate(items[:10], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("36氪获取失败")
    news.append("")

# 爱范儿
try:
    url = "https://www.ifanr.com"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<h2[^>]*>([^<]+)</h2>', html)
        news.append("【爱范儿】")
        for i, item in enumerate(items[:8], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("爱范儿获取失败")
    news.append("")

# 少数派
try:
    url = "https://sspai.com"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'"title":"([^"]+)"', html)
        news.append("【少数派】")
        for i, item in enumerate(items[:8], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("少数派获取失败")
    news.append("")

# ========== 国外科技新闻 ==========
# The Verge
try:
    url = "https://www.theverge.com/tech"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<h2[^>]*>([^<]+)</h2>', html)
        news.append("【The Verge】")
        for i, item in enumerate(items[:8], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("The Verge获取失败")
    news.append("")

# TechCrunch
try:
    url = "https://techcrunch.com"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<h2[^>]*>([^<]+)</h2>', html)
        news.append("【TechCrunch】")
        for i, item in enumerate(items[:8], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("TechCrunch获取失败")
    news.append("")

# Wired
try:
    url = "https://www.wired.com/category/science"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<h2[^>]*>([^<]+)</h2>', html)
        news.append("【Wired 科学】")
        for i, item in enumerate(items[:8], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("Wired获取失败")
    news.append("")

# 写入文件
with open("news.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(news))
print("\n".join(news))
