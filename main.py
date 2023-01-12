import os
import base64


def base64_encode(string):
    return base64.b64encode(string.encode()).decode()


setting_json = {
    "webgl.vendor": "Qualcomm",
    "webgl.renderer": "Adreno (TM) 640",
    "navigator.user-agent": "Mozilla/5.0 (Linux; Android 11; ASUS_I005DA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
    "navigator.webdriver-status": "0",
    "navigator.platform": "Linux armv8l",
    "navigator.max-touch-points": "5",
    "navigator.hardware-concurrency": "8",
    "navigator.device-memory": "4",
    "navigator.languages": "zh-CN,en-US",
    "battery-manager.charging": "0",
    "battery-manager.level": "0.76",
    "connection.effective-type": "4g",
    "connection.type": "wifi",
    "fingerprint.canvas-rand-value": "0.001"
}

# 默认打开的 url
url = "https://browserleaks.com/javascript"

cmd = r".\chrome\chrome.exe --incognito --app={} ".format(url)

for (key, item) in setting_json.items():
    cmd += "--{}={} ".format(key, base64_encode(item))

print(cmd)
os.system(cmd)
