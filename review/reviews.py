import requests
import json
import time
import random
import os
import sys

# API 設定
BASE_URL = "https://www.niche.com/api/entity-reviews/"
CATEGORIES = [
    "Overall%20Experience", "Student%20Life", "Academics", "Campus",
    "Value", "Food", "Housing"
]

'''
HEADERS_LIST = [
    # 🖥️ Windows - Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",

    # 🖥️ Windows - Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0",

    # 🖥️ Windows - Edge
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    
    # 🍏 macOS - Chrome
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",

    # 🍏 macOS - Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Safari/605.1.15",

    # 📱 iPhone - Safari
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Mobile/14E5239e Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/537.36",

    # 📱 iPhone - Chrome
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",

    # 📱 Android - Chrome
    "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung Galaxy S23) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi Redmi Note 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    
    # 📱 Android - Firefox
    "Mozilla/5.0 (Android 14; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0",
    "Mozilla/5.0 (Android 13; Mobile; rv:119.0) Gecko/119.0 Firefox/119.0",
    "Mozilla/5.0 (Android 12; Mobile; rv:118.0) Gecko/118.0 Firefox/118.0",

    # 📱 Android - Edge
    "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 EdgA/121.0.0.0",
    "Mozilla/5.0 (Linux; Android 13; Samsung Galaxy S23) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 EdgA/120.0.0.0",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi Redmi Note 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36 EdgA/119.0.0.0",

    # 🏢 Googlebot (模擬爬蟲)
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.googlebot.com/bot.html)"
]

'''

# 隨機 User-Agent 避免被封鎖
HEADERS_LIST = [
    # Windows User-Agents
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/118.0.2088.76 Safari/537.36",
    
    # macOS User-Agents
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    
    # iPhone User-Agents
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/537.36",
    
    # Android User-Agents
    "Mozilla/5.0 (Linux; Android 14; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
    
    # iPad User-Agents
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 16_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
    
    # Firefox User-Agents
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:119.0) Gecko/20100101 Firefox/119.0"
]


def get_headers():
    """隨機獲取 User-Agent"""
    return {"User-Agent": random.choice(HEADERS_LIST)}



# 讀取學校 ID
def fetch_school_ids():
    if os.path.exists("/Users/shiaupi/Downloads/mine/data_processing_project/review/school_id.json"):
        with open("/Users/shiaupi/Downloads/mine/data_processing_project/review/school_id.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return {school: info["School ID"] for school, info in data.items() if info["School ID"]}
    return {}

# 記錄未爬取成功的學校
def save_failed_schools(failed_schools):
    with open("failed_schools.json", "w", encoding="utf-8") as file:
        json.dump(failed_schools, file, indent=4, ensure_ascii=False)
    print("🚨 發生 403 封鎖，程式自動結束，未完成的學校已存入 failed_schools.json")

def random_delay(page_number):
    """根據頁數動態調整隨機延遲"""
    
    base_delay = random.uniform(8, 15)  # 增加整體延遲範圍
    if page_number == 1:
        extra_delay = random.uniform(3, 7)  # 第一頁稍微慢一點
    elif page_number < 5:
        extra_delay = random.uniform(8, 12)  # 3~4 頁等較久
    elif page_number < 8:
        extra_delay = random.uniform(12, 18)  # 5~7 頁等超久
    else:
        extra_delay = random.uniform(7, 12)  # 8~11 頁等稍微快一點

    total_delay = base_delay + extra_delay
    print(f"⏳ 等待 {total_delay:.2f} 秒後繼續...")
    time.sleep(total_delay)



def fetch_reviews(school_name, school_id, failed_schools):
    print(f"🏫 爬取 {school_name} ({school_id}) 的評論...")
    all_reviews = {}

    for category in CATEGORIES:
        print(f"📌 爬取 {category} 類別的評論...")
        reviews_list = []

        for page in range(1, 12):
            print(f"🔍 第 {page} 頁...")
            headers = get_headers()
            api_url = f"{BASE_URL}?e={school_id}&category={category}&page={page}&limit=20"

            response = requests.get(api_url, headers=headers)

            if response.status_code == 403:
                print(f"🚨 403 被封鎖，程式即將結束。未爬取的學校將存入 failed_schools.json")
                failed_schools.append({"school_name": school_name, "school_id": school_id})
                save_failed_schools(failed_schools)
                sys.exit(1)  # 立即結束程式
            
            elif response.status_code != 200:
                print(f"❌ {category} - 第 {page} 頁請求失敗 (狀態碼: {response.status_code})，跳過...")
                continue

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

            random_delay(page)  # 使用改進版的隨機延遲

        if reviews_list:
            all_reviews[category] = reviews_list

    if all_reviews:
        save_reviews(school_name, all_reviews)


def save_reviews(school_name, reviews):
    output_dir = "reviews/success"
    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/{school_name.replace(' ', '_')}_reviews.json", "w", encoding="utf-8") as file:
        json.dump(reviews, file, indent=4, ensure_ascii=False)
    print(f"✅ {school_name} 的評論已儲存！")

# 主程式
if __name__ == "__main__":
    school_ids = fetch_school_ids()
    failed_schools = []

    for school, school_id in school_ids.items():
        fetch_reviews(school, school_id, failed_schools)

    print("🎉 所有學校爬取完成！")