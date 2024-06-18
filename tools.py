import requests
import zipfile
import io

def downloader(url):
    """
    从指定URL下载ZIP文件并返回字节流
    """
    response = requests.get(url)
    if response.status_code == 200:
        return io.BytesIO(response.content)
    else:
        raise Exception(f"下载失败，状态码：{response.status_code}")

def extracter(file_bytes, extract_to='.'):
    """
    解压字节流中的ZIP文件到指定目录
    """
    with zipfile.ZipFile(file_bytes, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("文件解压成功")

# # 示例使用
# url = 'http://example.com/file.zip'
# try:
#     zip_file_bytes = download_zip(url)
#     extract_zip(zip_file_bytes, extract_to='your_target_directory')
# except Exception as e:
#     print(e)
