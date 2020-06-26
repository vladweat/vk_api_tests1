import vk_api
from vk_api import audio
import requests
from time import time
import os

"""Does not work since 02/15/2020"""

REQUEST_STATUS_CODE = 200
name_dir = ''
path = r'D:\\' + name_dir
login = ''
password = ''
my_id = ''

if not os.path.exists(path):
    os.makedirs(path)

vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()

vk_audio = audio.VkAudio(vk_session)

os.chdir(path)

time_start = time()
for i in vk_audio.get(owner_id=my_id):
    try:
        r = requests.get(i["url"])
        if r.status_code == REQUEST_STATUS_CODE:
            with open(i["artist"] + '_' + i["title"] + '.mp3', 'wb') as output_file:
                output_file.write(r.content)
    except OSError:
        print(i["artist"] + '_' + i["title"])
time_finish = time()
print("Time seconds:", time_finish - time_start)