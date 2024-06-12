import requests

# kirim API

# def kirim_API(kirim):
#     response1 = requests.get('http://localhost:8765/coba_kirim/'+kirim)
#     if response1.status_code != 200:
#         print(f'Gagal mengirim flag {kirim} ke server FastAPI')
#     else:
#         print(f'{kirim} berhasil dikirim')

# kirim_API('Afrizal')

import time
while True:
    # response_get = requests.get('http://localhost:8765/terima')
    response_get = requests.get('https://p43xg0jh-9090.asse.devtunnels.ms/')
    data_get = response_get.json()
    # get_flag = data_get.get('flag')
    get_flag = data_get['message']

    print(get_flag)
    print(data_get)
    time.sleep(3)