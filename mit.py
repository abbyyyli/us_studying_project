import requests
from bs4 import BeautifulSoup
import json

# MIT 網頁
url = "https://www.mit.edu/about"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}

# 發送 GET 請求
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 1️⃣ 提取主要內容段落（找所有 <p>）
paragraphs = soup.find_all("p")

# 2️⃣ 過濾內容並處理超連結
content = []
for p in paragraphs:
    text_parts = []
    for element in p.contents:
        if element.name == "a":
            text_parts.append(f"{element.get_text(strip=True)} ({element['href']})")  # 處理超連結
        elif isinstance(element, str):  # 確保是字串
            text_parts.append(element.strip())

    full_text = " ".join(text_parts).strip()
    if full_text:  # 避免加入空行
        content.append(full_text)

# 3️⃣ 輸出 MIT 內容
print("\n🔍 MIT 頁面內容：")
for text in content:
    print(text)

# 4️⃣ 存成 JSON 檔案
mit_content = {"content": content}

with open("mit_about_content.json", "w", encoding="utf-8") as json_file:
    json.dump(mit_content, json_file, ensure_ascii=False, indent=4)

# 5️⃣ 存成 TXT 檔案
with open("mit_about_content.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write("\n".join(content))

print("✅ MIT 內容已成功提取並存入 mit_about_content.json 和 mit_about_content.txt！")
