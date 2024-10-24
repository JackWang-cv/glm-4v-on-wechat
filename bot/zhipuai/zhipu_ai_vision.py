from zhipuai import ZhipuAI
# 词条改一下，变成
def send(text, url):
    client = ZhipuAI(api_key="")
    response = client.chat.completions.create(
        model="glm-4v",  # 填写需要调用的模型名称 4v比4v-plus好
        messages=[
        {
            "role": "user",
            "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url" : url
                }
            },
            {
                "type": "text",
                "text": text
            }
            ]
        }
        ]
    )
    return response.choices[0].message


if __name__ == "__main__":

    # print(send("http://res.cloudinary.com/dsqtyrogq/image/upload/v1721462376/syaz32j6lxq4myplpumq.jpg").content)
    pass
    # print(send(""))