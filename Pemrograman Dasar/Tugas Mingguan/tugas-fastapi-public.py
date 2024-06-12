from fastapi import FastAPI

app = FastAPI()

# uvicorn 11-12:app --host 127.0.0.1 --port 8080

flag = ''

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/kirim/{kirim}')
async def set_flag(kirim):
    global flag
    flag = kirim
    return {'flag': flag}

@app.get('/terima')
async def terima():
    return {'flag': flag}

# import requests

# url_public = 'https://dd86b3cae28ef4.lhr.life/'

# requests.get(url_public + str('kirim/fastapi-pemdas'))
# response_get = requests.get(url_public + str('terima'))
# data_get = response_get.json()
# get_flag = data_get['flag']

# print(get_flag)