import requests
from bs4 import BeautifulSoup
import json

# 目標網址
url = "https://www.harvard.edu/about/"

# 設定 User-Agent 避免被封鎖
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# 發送 GET 請求
response = requests.get(url, headers=headers)

# 確保請求成功
if response.status_code == 200:
    # 解析 HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 找到主要內容區塊
    main_content = soup.find("main", id="main-content")

    if main_content:
        # 1️⃣ 提取標題（h1, h2, h3）
        headings = [h.get_text(strip=True) for h in main_content.find_all(["h1", "h2", "h3"])]

        # 2️⃣ 提取段落內容，並過濾掉含 "Explore" 的無用內容
        paragraphs = [p.get_text(strip=True) for p in main_content.find_all("p") if "Explore" not in p.get_text()]

        # 3️⃣ 提取所有超連結
        links = [a["href"] for a in main_content.find_all("a", href=True)]

        # 4️⃣ 整理成結構化數據
        data = {
            "headings": headings,
            "content": paragraphs,
            "links": links
        }

        # 5️⃣ 存成 TXT 檔案
        with open("harvard_about.txt", "w", encoding="utf-8") as txt_file:
            txt_file.write("\n".join(headings) + "\n\n")
            txt_file.write("\n".join(paragraphs) + "\n\n")
            txt_file.write("Links:\n" + "\n".join(links))

        # 6️⃣ 存成 JSON 檔案
        with open("harvard_about.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        print("✅ 內容已成功爬取並存入 mit_about.txt 和 harvard_about.json！")
    else:
        print("❌ 找不到主要內容區域！")
else:
    print(f"❌ 請求失敗，狀態碼：{response.status_code}")
