import uvicorn
from fastapi import FastAPI

app = FastAPI()

user_cred = {
    'email': 'email',
    'password': 'password',
}

@app.get('/')
async def root():
    return {'message': 'Validasi Email & password'}

@app.post('/kirim/')
async def post_cred(cred: dict):
    global user_cred
    user_cred = cred
    return {'message': 'Berhasil mengirim data'}

@app.get('/terima')
async def terima():
    return {'cred': user_cred}

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)