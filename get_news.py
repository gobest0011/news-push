import json
import urllib.request
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context

news = []
news.append("今日新闻摘要")
news.append("====================")
news.append("")

# ========== 国内热搜 ==========
try:
    url = "https://top.baidu.com/board?tab=realtime"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
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
# 36氪（使用API）
try:
    url = "https://36kr.com/api/newsflashes"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read())
        items = [item.get('title', '') for item in data.get('data', [])]
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
        items = re.findall(r'"articleTitle":"([^"]+)"', html)
        if not items:
            items = re.findall(r'<h2[^>]*>([^<]+)</h2>', html)
        news.append("【爱范儿】")
        for i, item in enumerate(items[:8], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("爱范儿获取失败")
    news.append("")

# 极客公园
try:
    url = "https://www.geekpark.com/api/v1/articles"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read())
        items = [item.get('title', '') for item in data.get('data', [])[:10]]
        news.append("【极客公园】")
        for i, item in enumerate(items[:8], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("极客公园获取失败")
    news.append("")

# 虎嗅
try:
    url = "https://www.huxiu.com"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<h3[^>]*>([^<]+)</h3>', html)
        news.append("【虎嗅】")
        for i, item in enumerate(items[:8], 1):
            if len(item) > 5:
                news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("虎嗅获取失败")
    news.append("")

# ========== 新能源车新闻 ==========
# 懂车帝
try:
    url = "https://www.dongche.com/api/news/lists"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read())
        items = []
        if 'data' in data:
            for item in data['data'][:10]:
                if isinstance(item, dict):
                    items.append(item.get('title', item.get('name', '')))
        news.append("【懂车帝】")
        for i, item in enumerate(items[:8], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("懂车帝获取失败")
    news.append("")

# 汽车之家
try:
    url = "https://www.autohome.com.cn/ranking/0-0-0-0-0-0-0-0-1-1-0-1-0-0-1-"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'"title":"([^"]+)"', html)
        news.append("【汽车之家】")
        for i, item in enumerate(items[:8], 1):
            news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("汽车之家获取失败")
    news.append("")

# 电动邦
try:
    url = "https://www.diandian.com.cn/news"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<h3[^>]*>([^<]+)</h3>', html)
        news.append("【电动邦】")
        for i, item in enumerate(items[:8], 1):
            if len(item) > 5:
                news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("电动邦获取失败")
    news.append("")

# 第一电动
try:
    url = "https://www.d1ev.com/news"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        items = re.findall(r'<h3[^>]*>([^<]+)</h3>', html)
        news.append("【第一电动】")
        for i, item in enumerate(items[:8], 1):
            if len(item) > 5:
                news.append(str(i) + ". " + item)
        news.append("")
except Exception as e:
    news.append("第一电动获取失败")
    news.append("")

# 微博汽车（备用）
try:
    url = "https://weibo.com/ajax/feed/listgird?uid=1911003017&feature=0&is_all=1"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read())
        items = [item.get('text', '')[:50] for item in data.get('statuses', [])[:8]]
        news.append("【微博汽车】")
        for i, item in enumerate(items, 1):
            clean = re.sub(r'<[^>]+>', '', item)
            news.append(str(i) + ". " + clean[:40])
        news.append("")
except Exception as e:
    news.append("微博汽车获取失败")
    news.append("")

# 写入文件
with open("news.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(news))
print("\n".join(news))
