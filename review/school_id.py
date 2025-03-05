import requests
import json
import time
import random

# 🔗 Niche API URL
search_url = "https://www.niche.com/api/entity-reviews/"

# 🎓 List of schools
school_names = [
    "Massachusetts Institute of Technology", "Yale University", "Stanford University",
    "Columbia University", "Brown University", "Duke University", "Washington University in St. Louis",
    "Georgetown University", "University of Florida", "University of Notre Dame", "Princeton University",
    "Harvard University", "Dartmouth College", "Rice University", "Boston University",
    "University of Pennsylvania", "Vanderbilt University", "Carnegie Mellon University",
    "California Institute of Technology", "Tulane University", "University of Chicago",
    "University of California - Berkeley", "University of Southern California",
    "University of North Carolina at Chapel Hill", "Washington and Lee University",
    "Harvey Mudd College", "Wellesley College", "Northwestern University",
    "University of Michigan - Ann Arbor", "Johns Hopkins University", "Cornell University",
    "University of California - Los Angeles", "Claremont McKenna College", "New York University",
    "University of Virginia", "Emory University", "Georgia Institute of Technology",
    "Amherst College", "Grinnell College", "Wake Forest University", "Middlebury College",
    "Bowdoin College", "University of Illinois Urbana-Champaign", "Texas A&M University",
    "University of Texas - Austin", "University of Georgia", "New Mexico Tech",
    "Virginia Tech", "Florida State University", "University of Miami", "Michigan State University",
    "Barnard College", "Boston College", "Swarthmore College", "Williams College",
    "Pomona College", "Davidson College", "Tufts University", "Northeastern University",
]

# 🛠 Multiple User-Agents (to avoid detection)
user_agents = [
    
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36",
]

# 🏫 Dictionary to store school IDs
school_ids = {}

# 🔄 Start requests
for school in school_names:
    params = {"query": school, "context": "college", "page": 1, "limit": 1}
    headers = {"User-Agent": random.choice(user_agents)}
    
    retries = 3  # Maximum retries
    while retries > 0:
        response = requests.get(search_url, params=params, headers=headers)

        if response.status_code == 200:
            results = response.json()
            if "items" in results and results["items"]:
                school_id = results["items"][0]["entity"]["uuid"]
                school_ids[school] = school_id
                print(f"✅ {school} 的 School ID：{school_id}")
            else:
                print(f"❌ 未找到 {school} 的 ID")
            break  # Exit retry loop

        elif response.status_code == 403:
            print(f"🚫 403 Forbidden - {school} 被封鎖，等待 30 秒後重試...")
            time.sleep(30)  # Wait before retrying
            retries -= 1

        elif response.status_code == 404:
            print(f"❌ 404 Not Found - {school} 的 ID 無法找到")
            break  # No need to retry

        else:
            print(f"❌ {school} 請求失敗，狀態碼：{response.status_code}")
            retries -= 1
            time.sleep(5)  # Short delay before retry

    time.sleep(random.uniform(5, 15))  # Add random delay

# 📝 Save results
with open("school_ids.json", "w", encoding="utf-8") as f:
    json.dump(school_ids, f, indent=4)

print("🎉 所有學校 ID 已獲取並存入 school_ids.json")
