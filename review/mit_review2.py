import requests
import json
import time
import random

# API 基本設定
base_url = "https://www.niche.com/api/entity-reviews/"
school_id = "1d755237-c671-478d-8020-63cc46eed935"  # MIT ID
category = "Overall%20Experience"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
}

output_file = "mit_reviews.json"
all_reviews = []

# 爬取多頁評論
for page in range(1, 10):  # 這裡可以調整最大頁數
    print(f"🔍 正在爬取第 {page} 頁...")
    api_url = f"{base_url}?e={school_id}&category={category}&page={page}&limit=20"

    response = requests.get(api_url, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ 第 {page} 頁請求失敗，狀態碼：{response.status_code}")
        break

    data = response.json()
    if "reviews" not in data or not data["reviews"]:
        print("✅ 沒有更多評論，結束爬取")
        break

    for review in data["reviews"]:
        review_data = {
            "Rating": review.get("rating", "N/A"),
            "Review": review.get("body", "").strip(),  # `body` 是評論內容
            "Author": review.get("author", "Anonymous"),
            "Date": review.get("created", "N/A")
        }
        all_reviews.append(review_data)

    # 隨機延遲，防止被封鎖
    time.sleep(random.uniform(2, 5))

# 儲存為 JSON
with open(output_file, mode="w", encoding="utf-8") as file:
    json.dump(all_reviews, file, indent=4, ensure_ascii=False)  # `ensure_ascii=False` 確保非 ASCII 字元能正確存儲

print(f"🎉 所有評論已成功保存到 {output_file}！")
