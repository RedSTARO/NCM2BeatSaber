import requests

# URL to the API endpoint
url = "https://sss.unmeta.cn/songlist"

# Headers copied from the network request
headers = {
    'authority': 'bing.com',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'content-length': '66',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://bing.com/',
    'referer': 'https://bing.com/',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}


def getSongs(listUrl = "https://music.163.com/#/playlist?id=3219642517"):
    # Data payload copied from the network request
    data = {
        'u': '1',
        'i': '1',
        'url': listUrl
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=data)

    # Print the response
    return response.text

def getSongsFromNCM(id = "3219642517"):
    # api = f"http://ncm.tryagain.fun/playlist/track/all?id={id}&realIP=192.168.1.1"
    api = f"http://192.168.1.19:3000/playlist/track/all?id={id}&realIP=192.168.1.1"
    # print(api)
    response = requests.get(api + id, headers=headers)
    print(api)
    print(response.text)
    return response.text

def getSongsFromJson(file = "t.json"):
    with open(file, encoding="utf-8") as f:
        return f.read()

# getSongsFromNCM()
