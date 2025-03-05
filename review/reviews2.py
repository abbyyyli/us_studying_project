import os
import json
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ✅ 設定 ChromeDriver 路徑
chrome_driver_path = "/Users/shiaupi/Downloads/tibame/HTML/pyetl/chromedriver-mac-x64/chromedriver"

# ✅ 隨機延遲，避免被封鎖
def random_delay(min_delay=10, max_delay=20):
    delay = random.uniform(min_delay, max_delay)
    print(f"⏳ 等待 {delay:.2f} 秒後繼續...")
    time.sleep(delay)

# ✅ 初始化 Selenium WebDriver
def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 無頭模式
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--incognito")  # 無痕模式
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")
    
    # ✅ 設定 ChromeDriver 服務
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# ✅ 讀取 `school_id.json`
def fetch_school_ids():
    if os.path.exists("/Users/shiaupi/Downloads/mine/data_processing_project/review/school_id.json"):
        with open("/Users/shiaupi/Downloads/mine/data_processing_project/review/school_id.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return {school: info["School ID"] for school, info in data.items() if info["School ID"]}
    else:
        print("❌ 未找到 `school_id.json`，請先執行 School ID 爬取程式！")
        return {}

# ✅ 爬取單一學校的評論
def fetch_reviews(driver, school_name, school_id):
    print(f"🏫 正在爬取 {school_name} ({school_id}) 的評論...")

    # ✅ 設定評論 API URL
    base_url = "https://www.niche.com/api/entity-reviews/"
    categories = [
        "Overall%20Experience", "Student%20Life", "Academics", "Campus",
        "Value", "Food", "Housing"
    ]

    all_reviews = {}

    for category in categories:
        print(f"📌 正在爬取 {category} 類別的評論...")
        reviews_list = []
        
        for page in range(1, 12):  # 爬取最多 11 頁
            print(f"🔍 第 {page} 頁...")
            api_url = f"{base_url}?e={school_id}&category={category}&page={page}&limit=20"

            try:
                driver.get(api_url)
                random_delay(7, 15)  # ✅ 隨機延遲，避免封鎖
                
                # ✅ 確保網頁加載完成
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "pre"))
                )

                # ✅ 取得 JSON 內容
                response_text = driver.find_element(By.TAG_NAME, "pre").text
                data = json.loads(response_text)

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

            except Exception as e:
                print(f"⚠️ 無法爬取 {category} 第 {page} 頁: {e}")
                break  # ✅ 若 403，直接跳過

        if reviews_list:
            all_reviews[category] = reviews_list

    # ✅ 檢查是否有評論
    if not all_reviews:
        print(f"🚨 {school_name} 爬取失敗，記錄到 `failed.json`")
        record_failed_school(school_name, school_id)
    else:
        save_reviews(school_name, all_reviews)
        print(f"🎉 {school_name} 的所有評論已成功儲存！")

# ✅ 儲存成功的評論
def save_reviews(school_name, reviews):
    output_dir = "reviews/success"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/{school_name.replace(' ', '_')}_reviews.json"
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(reviews, file, indent=4, ensure_ascii=False)
    print(f"✅ {school_name} 的評論已儲存到 `{output_file}`")

# ✅ 記錄失敗的學校
def record_failed_school(school_name, school_id):
    output_file = "reviews/failed.json"
    
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as file:
            failed_data = json.load(file)
    else:
        failed_data = []

    failed_data.append({"school_name": school_name, "school_id": school_id})

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(failed_data, file, indent=4, ensure_ascii=False)
    print(f"❌ {school_name} 已記錄到 `{output_file}`！")

# ✅ 爬取所有學校
def scrape_all_schools():
    school_ids = fetch_school_ids()
    if not school_ids:
        return

    driver = init_driver()
    
    try:
        for school_name, school_id in school_ids.items():
            fetch_reviews(driver, school_name, school_id)
    finally:
        driver.quit()

# ✅ 執行程式
if __name__ == "__main__":
    scrape_all_schools()
