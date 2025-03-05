from bs4 import BeautifulSoup
import requests
import csv
import time
import random

# 設定基礎參數
base_url = "https://www.niche.com/colleges/yale-university/reviews/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
}
output_file = "yale_reviews_housing.csv"  # 儲存爬取結果的檔案
data = []  # 用來儲存所有評論資料
university_name = "Yale University"  # 固定的學校名稱

# 爬取多頁評論
for page in range(1, 5):  # 設定頁數範圍，根據需求調整
    print(f"正在爬取第 {page} 頁...")
    url = f"{base_url}?page={page}&category=Housing"
    try:
        response = requests.get(url, headers=headers)
        
        # 如果 HTTP 響應不是 200，跳出爬取循環
        if response.status_code != 200:
            print(f"無法取得第 {page} 頁，HTTP 狀態碼：{response.status_code}")
            break

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, "html.parser")
        reviews = soup.find_all("div", class_="review")  # 尋找所有評論區塊

        # 檢查是否有評論區塊
        if not reviews:
            print(f"第 {page} 頁沒有找到任何評論，可能到達結尾。")
            break

        # 從每條評論中提取資料
        for review in reviews:
            try:
                # 提取評分
                rating_value = review.find("meta", itemprop="ratingValue")["content"] if review.find("meta", itemprop="ratingValue") else "N/A"
                best_rating = review.find("meta", itemprop="bestRating")["content"] if review.find("meta", itemprop="bestRating") else "N/A"

                # 提取評論內容
                review_text_div = review.find("div", itemprop="reviewBody")
                review_text = review_text_div.text.strip() if review_text_div else "N/A"

                # 儲存資料
                data.append({
                    "University Name": university_name,
                    "Rating": f"{rating_value} / {best_rating}",
                    "Review": review_text
                })
            except Exception as e:
                print(f"第 {page} 頁中的某條評論解析失敗，錯誤：{e}")

        # 隨機延遲，模仿人類行為
        delay = random.uniform(5, 15)  # 延遲範圍從 5 到 15 秒
        print(f"第 {page} 頁爬取完成，延遲 {delay:.2f} 秒後繼續...")
        time.sleep(delay)

    except requests.RequestException as e:
        print(f"請求第 {page} 頁時出現錯誤：{e}")
        break

# 將數據保存為 CSV
try:
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["University Name", "Rating", "Review"])
        writer.writeheader()
        writer.writerows(data)
    print(f"所有評論數據已成功保存到 {output_file}。")
except Exception as e:
    print(f"儲存數據時發生錯誤：{e}")
