import requests
import pandas as pd
from datetime import datetime

url = "https://api.cnyes.com/media/api/v1/newslist/category/headline?limit=10"
res = requests.get(url).json()

items = res["items"]["data"]

data = []
for item in items:
    title = item["title"]
    link = f'https://www.cnyes.com/news/id/{item["newsId"]}'
    pub_time = datetime.fromtimestamp(item["publishAt"])
    data.append([title, link, pub_time])

df = pd.DataFrame(data, columns=["標題", "連結", "發布時間"])
df.to_csv("news.csv", index=False, encoding="utf-8-sig")

print("✅ 已更新 news.csv")
