import tkinter as tk
from tkinter import filedialog

def selectDir():
    root = tk.Tk()
    root.withdraw()

    directory_path = filedialog.askdirectory()
    return directory_path


import requests
import os

def downloader(url, path):
    try:
        # 发送 HTTP 请求获取文件数据
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功

        # 确保目录存在
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # 打开文件并写入数据
        with open(path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                
        return True

    except requests.exceptions.RequestException as e:
        return "E2"

import zipfile
import os
def unzip(filePath):
    try:
        parent_dir = os.path.dirname(filePath)

        with zipfile.ZipFile(filePath, 'r') as zip_ref:
            zip_ref.extractall(parent_dir)
    except:
        return "E3"
