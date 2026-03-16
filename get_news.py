import json
import urllib.request
import ssl
import re
import time

ssl._create_default_https_context = ssl._create_unverified_context

news = []
news.append("今日新闻摘要")
news.append("====================")
news.append("")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# ========== 国内热搜 ==========
try:
    url = "https://top.baidu.com/board?tab=realtime"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'"word":"([^"]+)"', html)
        news.append("【百度热搜 Top 10】")
        for i, item in enumerate(items[:10], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("百度热搜获取失败")
    news.append("")

# ========== 今日头条 ==========
try:
    url = "https://www.toutiao.com/api/pc/feed/?category=news_hot&max_behot_time=0"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        data = json.loads(response.read())
        items = [item.get('title', '') for item in data.get('data', [])]
        news.append("【今日头条热点】")
        for i, item in enumerate(items[:10], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("今日头条获取失败")
    news.append("")

# ========== 网易新闻 ==========
try:
    url = "https://news.163.com/special/cm_yaowen20250113/"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'"title":"([^"]+)"', html)
        news.append("【网易新闻】")
        for i, item in enumerate(items[:10], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("网易新闻获取失败")
    news.append("")

# ========== 科技类 ==========
# 36氪
try:
    url = "https://36kr.com/newsflashes"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
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
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'"articleTitle":"([^"]+)"', html)
        if not items:
            items = re.findall(r'"title":"([^"]+)"', html)[:10]
        news.append("【爱范儿】")
        for i, item in enumerate(items[:8], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("爱范儿获取失败")
    news.append("")

# 虎嗅
try:
    url = "https://www.huxiu.com"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<h3[^>]*>([^<]+)</h3>', html)
        news.append("【虎嗅】")
        count = 0
        for i, item in enumerate(items, 1):
            if len(item) > 10 and count < 8:
                news.append(str(count+1) + ". " + item)
                count += 1
        news.append("")
except Exception as e:
    news.append("虎嗅获取失败")
    news.append("")

# 少数派
try:
    url = "https://sspai.com/api/v1/article/index?limit=10&offset=0"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        data = json.loads(response.read())
        items = [item.get('title', '') for item in data.get('data', [])]
        news.append("【少数派】")
        for i, item in enumerate(items[:8], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("少数派获取失败")
    news.append("")

# 威锋网（苹果/数码）
try:
    url = "https://www.wefeng.com"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<h3[^>]*>([^<]+)</h3>', html)
        news.append("【威锋网】")
        count = 0
        for i, item in enumerate(items, 1):
            if len(item) > 5 and count < 8:
                news.append(str(count+1) + ". " + item)
                count += 1
        news.append("")
except Exception as e:
    news.append("威锋网获取失败")
    news.append("")

# ========== 新能源车 ==========
# 易车
try:
    url = "https://www.yiche.com/zaoche/news/"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'"title":"([^"]+)"', html)
        if not items:
            items = re.findall(r'<h3[^>]*>([^<]+)</h3>', html)
        news.append("【易车网】")
        count = 0
        for i, item in enumerate(items, 1):
            if len(item) > 5 and count < 8:
                news.append(str(count+1) + ". " + item)
                count += 1
        news.append("")
except Exception as e:
    news.append("易车获取失败")
    news.append("")

# 网上车市
try:
    url = "https://www.cheshi.com/news/"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<h3[^>]*>([^<]+)</h3>', html)
        news.append("【网上车市】")
        count = 0
        for i, item in enumerate(items, 1):
            if len(item) > 8 and count < 8:
                news.append(str(count+1) + ". " + item)
                count += 1
        news.append("")
except Exception as e:
    news.append("网上车市获取失败")
    news.append("")

# 新浪汽车
try:
    url = "https://auto.sina.com.cn"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'"title":"([^"]+)"', html)
        news.append("【新浪汽车】")
        count = 0
        for i, item in enumerate(items, 1):
            if len(item) > 5 and count < 8:
                news.append(str(count+1) + ". " + item)
                count += 1
        news.append("")
except Exception as e:
    news.append("新浪汽车获取失败")
    news.append("")

# 凤凰网汽车
try:
    url = "https://auto.ifeng.com"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<h3[^>]*>([^<]+)</h3>', html)
        news.append("【凤凰网汽车】")
        count = 0
        for i, item in enumerate(items, 1):
            if len(item) > 8 and count < 8:
                news.append(str(count+1) + ". " + item)
                count += 1
        news.append("")
except Exception as e:
    news.append("凤凰网汽车获取失败")
    news.append("")

# 写入文件
with open("news.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(news))
print("\n".join(news))
