from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import re

# 設定 Selenium 瀏覽器
chrome_options = Options()
chrome_options.add_argument("--headless")  # 無頭模式，不開啟瀏覽器
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")

# 使用 set_capability 來設定 performance log
chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

# 設定 WebDriver 路徑
service = Service("/Users/shiaupi/Downloads/tibame/HTML/pyetl/chromedriver-mac-x64/chromedriver")  # 更換為你的 chromedriver 路徑
driver = webdriver.Chrome(service=service, options=chrome_options)

# 目標學校列表
school_names = [
    "Massachusetts Institute of Technology",
    "Harvard University",
    "Stanford University"
]

base_url = "https://www.niche.com/colleges/"
school_ids = {}

for school in school_names:
    school_slug = school.lower().replace(" ", "-")
    school_url = f"{base_url}{school_slug}/reviews/"
    print(f"🔍 正在訪問 {school} 的評論頁面：{school_url}")

    try:
        driver.get(school_url)
        time.sleep(5)  # 等待頁面加載

        # 監聽網頁的所有 Network Requests
        logs = driver.get_log("performance")

        # 遍歷 Network Requests，找到包含 `entity-reviews/?e=` 的請求
        for log in logs:
            try:
                network_log = json.loads(log["message"])["message"]
                if network_log["method"] == "Network.requestWillBeSent":
                    url = network_log["params"]["request"]["url"]
                    if "entity-reviews/?e=" in url:
                        match = re.search(r"entity-reviews/\?e=([a-f0-9-]+)", url)
                        if match:
                            school_id = match.group(1)
                            school_ids[school] = school_id
                            print(f"✅ {school} 的 School ID：{school_id}")
                            break
            except:
                continue

        if school not in school_ids:
            print(f"❌ 未找到 {school} 的 School ID")

    except Exception as e:
        print(f"⚠️ {school} 發生錯誤：{e}")

# 關閉瀏覽器
driver.quit()

# 儲存 School ID
with open("school_ids.json", "w", encoding="utf-8") as f:
    json.dump(school_ids, f, indent=4)

print("🎉 所有 School ID 已成功保存到 school_ids.json！")
