import requests
from bs4 import BeautifulSoup

# MIT 網頁
url = "https://www.mit.edu/about"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}

# 發送 GET 請求
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 1️⃣ 提取標題
title_tag = soup.find("h2")
title = title_tag.get_text(strip=True) if title_tag else "❌ 找不到標題"
print(f"MIT Page Title: {title}")

# 2️⃣ 列出所有 H2
all_h2 = [h.get_text(strip=True) for h in soup.find_all("h2")]
print("MIT 所有 H2 標題:", all_h2)

# 3️⃣ 提取主要內容段落（找所有 <p>）
paragraphs = soup.find_all("p")

print("\n🔍 MIT 頁面內容：")
for p in paragraphs:
    text_parts = []
    for element in p.contents:
        if element.name == "a":
            text_parts.append(f"{element.get_text(strip=True)} ({element['href']})")  # 處理超連結
        

    full_text = " ".join(text_parts)
    print(full_text)
