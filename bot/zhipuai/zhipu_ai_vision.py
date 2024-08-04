from zhipuai import ZhipuAI
# 词条改一下，变成
def send(text, url):
    client = ZhipuAI(api_key="")
    response = client.chat.completions.create(
        model="glm-4v",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": text
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": url
                        }
                    }
                ]
            }
        ],
        top_p=0.7,
        temperature=0.2,
        max_tokens=1024,
        stream=False,
    )
    return response.choices[0].message


if __name__ == "__main__":

    # print(send("http://res.cloudinary.com/dsqtyrogq/image/upload/v1721462376/syaz32j6lxq4myplpumq.jpg").content)
    pass
    # print(send(""))