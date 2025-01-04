# 使用本项目说明文档

## Introduction
利用GLM4V图生文模型进行图识别分析,并通过wechat聊天方式进行使用

## Run
1. 添加/glm4v-on-wechat/bot/zhipuai/zhipu_ai_vision.py中第4行的API-KEY（从智谱平台获取）
2. 添加/tencent_cos.py的12-15和39行key,secert信息(从腾讯云存储桶获取信息)
3. 运行以下命令，若后台运行使用Nohup
```bash 
python app.py
```

## Acknowledgments
This project is built upon the open-source project [chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat) and retains its original license..

Thanks to the original authors for their work!