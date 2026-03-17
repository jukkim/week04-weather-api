# kma_weather.py
import requests
from datetime import datetime

SERVICE_KEY = "MT7c9rQ0XN8AJrWxI1PU4fKyZ1qv8CK+9UKGUSgiiSOT47KosoQme5Th4W5RuvttNNBKQ9v2aNyeNSZSL2IRMA=="

url = ("http://apis.data.go.kr/1360000/"
       "VilageFcstInfoService_2.0/getUltraSrtNcst")

# 오늘 날짜와 시각 자동 계산
now       = datetime.now()
base_date = now.strftime("%Y%m%d")
base_time = now.strftime("%H00")

params = {
    "serviceKey": SERVICE_KEY,
    "pageNo":     1,
    "numOfRows":  10,
    "dataType":   "JSON",
    "base_date":  base_date,
    "base_time":  base_time,
    "nx":         60,   # 서울
    "ny":         127,
}

res = requests.get(url, params=params)
print(f"상태 코드: {res.status_code}")

if res.status_code == 200:
    data  = res.json()
    items = data["response"]["body"]["items"]["item"]

    code_map = {
        "T1H": "기온(°C)",
        "RN1": "1시간 강수량(mm)",
        "REH": "습도(%)",
        "WSD": "풍속(m/s)",
        "VEC": "풍향(deg)",
    }

    print("=== 서울 현재 날씨 ===")
    for item in items:
        cat  = item["category"]
        val  = item["obsrValue"]
        name = code_map.get(cat, cat)
        print(f"{name}: {val}")
else:
    print(f"오류: {res.status_code}")
    print(res.text[:200])
