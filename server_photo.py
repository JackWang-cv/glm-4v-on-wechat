# 不行
from flask import Flask, send_file
import os

app = Flask(__name__)

# 设置本地图片的路径
IMAGE_PATH = 'tmp/240721-180036.png'

@app.route('/image')
def serve_image():
    # 检查文件是否存在
    if not os.path.exists(IMAGE_PATH):
        return "Image not found", 404

    # 使用 send_file 返回图像
    return send_file(IMAGE_PATH, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
