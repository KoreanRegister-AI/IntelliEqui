import datetime

# 현재 시간 구하기
now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# HTML 파일 업데이트
with open("index.html", "w") as f:
    f.write(f"Last updated at {current_time}")
