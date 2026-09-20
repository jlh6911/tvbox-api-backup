import json
import os

BASE_URL = "https://jlh6911.github.io/tvbox-api-backup/tvbox/"
LIST_FILE = "list.txt"
OUTPUT_FILE = "duocang.json"

urls = []

if os.path.exists(LIST_FILE):
    with open(LIST_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("|")
            if len(parts) >= 1:
                filename = parts[0].strip()
                name = filename.replace(".json", "")
                url = BASE_URL + filename
                urls.append({
                    "url": url,
                    "name": name
                })

# 去重
seen = set()
unique_urls = []
for item in urls:
    if item["url"] not in seen:
        seen.add(item["url"])
        unique_urls.append(item)

data = {"urls": unique_urls}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"已生成 {OUTPUT_FILE}，共 {len(unique_urls)} 个接口")
