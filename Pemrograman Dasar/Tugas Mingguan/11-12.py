from fastapi import FastAPI

app = FastAPI()

# uvicorn 11-12:app --host 127.0.0.1 --port 8080

flag = ''

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/coba_kirim/{kirim}')
async def set_flag(kirim):
    global flag
    flag = kirim
    return {'flag': flag}

@app.get('/terima')
async def terima():
    return {'flag': flag}

@app.get('/contoh')
async def contoh():
    return {'nim': 152022003,
            'nama': 'Muhammad Daffa Deli Junior Irawan',
            'kelas': 'E',
            'jurusan': 'Informatika',
            'fakultas': 'Fakultas Teknologi Industri',
    }