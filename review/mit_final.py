import requests
import json
import time
import random

# API 設定
base_url = "https://www.niche.com/api/entity-reviews/"
school_id = "1d755237-c671-478d-8020-63cc46eed935"  # MIT ID


categories = [
    "Overall%20Experience", "Student%20Life", "Academics", "Campus",
    "Value", "Food", "Housing"
]
headers_list = [  # 多個 User-Agent 避免封鎖
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
]

all_reviews = {}

for category in categories:
    print(f"📌 正在爬取 {category} 類別的評論...")
    reviews_list = []
    
    for page in range(1, 12):  # 爬取最多 11 頁
        print(f"🔍 第 {page} 頁...")
        headers = {"User-Agent": random.choice(headers_list)}
        api_url = f"{base_url}?e={school_id}&category={category}&page={page}&limit=20"

        retry_count = 0
        while retry_count < 4:  # 允許最多 4 次重試
            response = requests.get(api_url, headers=headers)

            if response.status_code == 200:
                break  # 成功取得資料，跳出重試迴圈
            elif response.status_code == 403:
                print(f"⚠️ 第 {page} 頁被封鎖 (403)，等待 60 秒後重試...")
                time.sleep(60)  # 避免連續被封鎖
                retry_count += 1
            else:
                print(f"❌ 第 {page} 頁請求失敗，狀態碼：{response.status_code}")
                retry_count = 3  # 遇到其他錯誤直接跳過該頁
                break

        if response.status_code != 200:
            print(f"🚫 無法爬取 {category} 的第 {page} 頁，跳過...")
            break

        data = response.json()
        if "reviews" not in data or not data["reviews"]:
            print("✅ 沒有更多評論，結束爬取")
            break

        for review in data["reviews"]:
            reviews_list.append({
                "Rating": review.get("rating", "N/A"),
                "Review": review.get("body", "").strip(),
                "Author": review.get("author", "Anonymous"),
                "Date": review.get("created", "N/A")
            })

        # 隨機延遲，模仿人類行為
        delay = random.uniform(7, 18)
        print(f"⏳ 等待 {delay:.2f} 秒後繼續...")
        time.sleep(delay)

    all_reviews[category] = reviews_list

# 儲存為 JSON
output_file = "mit_reviews_by_category.json"
with open(output_file, mode="w", encoding="utf-8") as file:
    json.dump(all_reviews, file, indent=4, ensure_ascii=False)

print(f"🎉 所有評論已成功保存到 {output_file}！")
