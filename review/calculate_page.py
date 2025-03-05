import requests
from bs4 import BeautifulSoup
import random
import time

# 基本設置
base_url = "https://www.niche.com/colleges/yale-university/reviews/"
categories = [
    "Overall-Experience",
    "Campus",
    "Housing",
    "Value",
    "Student-Life",
    "Academics",
    "Health-Safety",
    "Party-Scene",
    "Food"
]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
}

# 儲存分類及其頁數
category_pages = {}

# 遍歷每個分類
for category in categories:
    print(f"開始檢測分類：{category}")
    max_pages = 0  # 記錄分類的總頁數
    for page in range(1, 100):  # 假設不超過 100 頁，視實際情況調整
        print(f"檢測 {category} 第 {page} 頁...")
        url = f"{base_url}?page={page}&category={category}"
        try:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print(f"無法取得 {category} 第 {page} 頁，HTTP 狀態碼：{response.status_code}")
                break

            # 使用 BeautifulSoup 解析 HTML
            soup = BeautifulSoup(response.text, "html.parser")
            reviews = soup.find_all("div", class_="review")

            # 如果沒有找到評論，認為到達結尾
            if not reviews:
                print(f"{category} 第 {page} 頁無評論，檢測結束。")
                break

            # 成功解析頁面，更新總頁數
            max_pages = page

            # 隨機延遲以模仿人類行為
            delay = random.uniform(5, 10)
            print(f"{category} 第 {page} 頁檢測完成，延遲 {delay:.2f} 秒後繼續...")
            time.sleep(delay)

        except requests.RequestException as e:
            print(f"請求 {category} 第 {page} 頁時出現錯誤：{e}")
            break

    # 保存該分類的總頁數
    category_pages[category] = max_pages
    print(f"{category} 總頁數為 {max_pages}。\n")

# 輸出所有分類的總頁數
print("各分類的頁數如下：")
for category, pages in category_pages.items():
    print(f"{category}: {pages} 頁")
