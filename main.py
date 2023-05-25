import requests
import openai


# input the city name
# city = input("Please input the city name: (input pinyin, lowercased, like: beijing)\n")

city = "beijing"

citycode = {
    "beijing": "110000",
    "tianjin": "120000",
    "shanghai": "310000",
    "guangzhou": "440100"
}

city = citycode[city]
# 构造API请求URL
url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={city}&key=b9e0879f68ab4242d913f5a85cb3fc5a"

# 发送API请求
response = requests.get(url)

data = response.json()

# 打印返回结果
if(data["status"] != "1"):
    print("error to get the weather")

info = data["lives"][0]


# 设置API Key
openai.api_key = "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"

# 构造请求参数
prompt = "province:" + info["province"] + "\n" + \
"city:" + info["city"] + "\n" + \
"adcode:" + info["adcode"] + "\n" + \
"weather:" + info["weather"] + "\n" + \
"temperature:" + info["temperature"] + "\n" + \
"winddirection:" + info["winddirection"] + "\n" + \
"windpower:" + info["windpower"] + "\n" + \
"humidity:" + info["humidity"] + "\n" + \
"reporttime:" + info["reporttime"] + "\n" + \
"请你为播音员写一段文字稿，播报上述天气状况，注意包含所有信息\n" 


model = "text-davinci-002"
params = {
    "prompt": prompt,
    "model": model,
    "temperature": 0.8,
    "max_tokens": 3500,
}

# 发送API请求
response = openai.Completion.create(**params)



# 解析响应结果
if response["choices"]:
    print()
    print("the prompt is:")
    print()
    print(prompt)
    print()

    answer = response["choices"][0]["text"]
    print("the answer is:")
    print(answer)
    print()
else:
    print(f"error to get answer from openai")