from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import logging
import sys
import os

# 日志设置
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 配置信息 modify

secret_id = ''        # 替换为你的SecretId
secret_key = ''      # 替换为你的SecretKey
region = ''             # 替换为你Bucket所在的地域
bucket = '' # 替换为你的存储桶名称

# 初始化配置
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

def upload_image_to_cos(local_file_path):
    """
    上传图片到腾讯云COS

    :param local_file_path: 本地图片的路径
    :return: 上传结果
    """
    key = os.path.basename(local_file_path)  # 使用文件名作为存储桶中的文件名
    try:
        response = client.upload_file(
            Bucket=bucket,
            LocalFilePath=local_file_path,
            Key=key,
            PartSize=1,
            MAXThread=10,
            EnableMD5=False
        )
        logging.info(f"Upload file {local_file_path} success: {response}")
        return 'https://zhipuai-on-wechat-1319111495.cos.ap-guangzhou.myqcloud.com/' + key  # 需更换
    except Exception as e:
        logging.error(f"Upload file {local_file_path} failed: {str(e)}")
        return None

if __name__ == "__main__":
    # 示例调用
    local_path = 'tmp/240721-180036.png'  # 替换为你要上传的文件路径
    print(upload_image_to_cos(local_path))
