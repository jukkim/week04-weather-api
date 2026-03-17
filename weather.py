# weather.py
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude":        37.5665,   # 서울 위도
    "longitude":       126.9780,  # 서울 경도
    "current":         "temperature_2m,wind_speed_10m,relative_humidity_2m",
    "timezone":        "Asia/Seoul",
    "wind_speed_unit": "kmh"
}

res = requests.get(url, params=params)

if res.status_code == 200:
    data = res.json()
    c    = data["current"]
    print("=== 서울 현재 날씨 ===")
    print(f"기온:  {c['temperature_2m']}°C")
    print(f"풍속:  {c['wind_speed_10m']} km/h")
    print(f"습도:  {c['relative_humidity_2m']}%")
else:
    print(f"오류: {res.status_code}")
