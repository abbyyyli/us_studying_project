import requests
from bs4 import BeautifulSoup
import json
import csv
import os
import time
import random
import glob
from urllib.robotparser import RobotFileParser

# 設定 User-Agent 清單（隨機選擇，避免被封鎖）
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/537.36"
]

# 自動讀取所有 `url_*.txt` 檔案
school_files = glob.glob("url_*.txt")
output_folder = "crawl_results"
os.makedirs(output_folder, exist_ok=True)

# 檢查 robots.txt 是否允許爬取
def is_allowed_to_scrape(url):
    base_url = "/".join(url.split("/")[:3])
    robots_url = base_url + "/robots.txt"
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        return rp.can_fetch("*", url)
    except:
        return True  # 如果 robots.txt 無法讀取，預設允許爬取

# 逐個學校處理
for school_file in school_files:
    school_name = school_file.replace("url_", "").replace(".txt", "")  # 取得學校名稱
    school_folder = os.path.join(output_folder, school_name)
    os.makedirs(school_folder, exist_ok=True)

    print(f"\n🔄 開始爬取 {school_name} 的資料...")

    # 讀取該學校的 URL
    with open(school_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]

    all_data = []  # 存放爬取結果

    # 遍歷 URL 進行爬取
    for url in urls:
        print(f"🌍 正在爬取 {url}...")

        # 檢查 robots.txt 是否允許爬取
        if not is_allowed_to_scrape(url):
            print(f"🚫 {url} 被 robots.txt 限制，跳過")
            continue

        headers = {"User-Agent": random.choice(USER_AGENTS)}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # 若 HTTP 回應錯誤 (如 404)，會觸發 Exception
        except requests.exceptions.RequestException as e:
            print(f"❌ 無法爬取 {url}: {e}")
            time.sleep(5)
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        main_content = soup.find("main", id="main-content")

        if main_content:
            # 1️⃣ 提取標題（h1, h2, h3）
            headings = [h.get_text(strip=True) for h in main_content.find_all(["h1", "h2", "h3"])]

            # 2️⃣ 提取段落內容（過濾掉 "Explore"）
            paragraphs = [p.get_text(strip=True) for p in main_content.find_all("p") if "Explore" not in p.get_text()]

            # 3️⃣ 提取所有超連結（去除重複）
            links = list(set(a["href"] for a in main_content.find_all("a", href=True)))

            # 4️⃣ 整理數據
            page_data = {
                "url": url,
                "headings": headings,
                "content": paragraphs,
                "links": links
            }
            all_data.append(page_data)

            print(f"✅ 成功爬取 {url}，標題 {len(headings)}，段落 {len(paragraphs)}，連結 {len(links)}")
        else:
            print(f"⚠️ {url} 沒有主要內容區塊，跳過")

        # **隨機等待 1-3 秒，避免請求過快被封鎖**
        time.sleep(random.uniform(1, 3))

    # 儲存爬取結果
    txt_file = os.path.join(school_folder, f"{school_name}.txt")
    json_file = os.path.join(school_folder, f"{school_name}.json")
    csv_file = os.path.join(school_folder, f"{school_name}.csv")

    # 5️⃣ 存成 TXT 檔案
    with open(txt_file, "w", encoding="utf-8") as txt_out:
        for page in all_data:
            txt_out.write(f"\n===== {page['url']} =====\n")
            txt_out.write("\n".join(page["headings"]) + "\n\n")
            txt_out.write("\n".join(page["content"]) + "\n\n")
            txt_out.write("Links:\n" + "\n".join(page["links"]) + "\n")

    print(f"📂 {school_name} 的 TXT 存入 {txt_file}！")

    # 6️⃣ 存成 JSON 檔案
    with open(json_file, "w", encoding="utf-8") as json_out:
        json.dump(all_data, json_out, ensure_ascii=False, indent=4)

    print(f"📂 {school_name} 的 JSON 存入 {json_file}！")

    # 7️⃣ 存成 CSV 檔案
    with open(csv_file, "w", newline="", encoding="utf-8") as csv_out:
        writer = csv.writer(csv_out)
        writer.writerow(["URL", "Type", "Content"])  # 標題列

        for page in all_data:
            for h in page["headings"]:
                writer.writerow([page["url"], "Heading", h])
            for p in page["content"]:
                writer.writerow([page["url"], "Paragraph", p])
            for l in page["links"]:
                writer.writerow([page["url"], "Link", l])

    print(f"📂 {school_name} 的 CSV 存入 {csv_file}！")

print("🚀 所有學校的爬取工作完成！")
