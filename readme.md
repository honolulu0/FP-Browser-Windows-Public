## 联系我

![wechat](https://github.com/tyua07/FP-Browser-Detect/raw/master/docs/wechat.jpg)

## exe 下载

我们提供了免费公开的 Windows 端指纹浏览器，注入参数有限，详细项目说明请参考 [FP-Browser-Public](https://github.com/tyua07/FP-Browser-Public) 。 下载地址：
* [chrome.7z](https://n7uax7j29h.feishu.cn/file/boxcnuRRMtuvkr5oiD5N7sq6ojw?from=from_copylink) 

## 相关开源项目
* [FP-Browser-Public 浏览器底层动态注入](https://github.com/tyua07/FP-Browser-Public) 
* [FP-Browser-Detect 浏览器属性检测](https://github.com/tyua07/FP-Browser-Detect)
* [FP-Browser-SDK 浏览器属性注入参数 SDK](https://github.com/tyua07/FP-Browser-SDK)
* [FP-Browser-Test 指纹浏览器（For Android）全部选项的测试用例](https://github.com/tyua07/FP-Browser-Test)
* [FP-Browser-Windows-Test 指纹浏览器（For Windows）全部选项的测试用例](https://github.com/tyua07/FP-Browser-Windows-Test)
* [FP-Browser-Windows-Public 指纹浏览器（For Windows）免费公开项目](https://github.com/tyua07/FP-Browser-Windows-Public)

## 示例代码
>注意：下载好 chrome.7z 文件后解压到当前目录的 chrome 文件夹下
```python
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

```