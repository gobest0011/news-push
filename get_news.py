import json
import urllib.request

news = []
news.append("今日新闻摘要")
news.append("====================")
news.append("")

try:
    url = "https://weibo.com/ajax/side/hotSearch"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read())
        news.append("【微博热搜 Top 10】")
        for i, item in enumerate(data["data"]["realtime"][:10], 1):
            news.append(str(i) + ". " + item["raw_title"])
except Exception as e:
    news.append("微博热搜获取失败")

with open("news.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(news))
print("\n".join(news))
