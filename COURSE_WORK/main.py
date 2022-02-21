import requests
import time
from progress.bar import Bar
import json

with open('params.txt', 'r') as f:
    def read_line(f): return f.readline().strip().split(' = ')[1]
    TOKEN_VK = read_line(f)
    VK_API_VERSION = read_line(f)
    TOKEN_YANDEX = read_line(f)
    YANDEX_DISK_FOLDER = read_line(f)
    VK_USER_ID = read_line(f)
    PHOTO_COUNT = int(read_line(f))

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_photos(self, user_id, photo_count):
        photos_url = self.url + 'photos.get'
        photos_params = {
            'album_id': 'wall',
            'extended': '1',
            'count': photo_count,
            'user_id': user_id
        }
        response = requests.get(photos_url, params={**self.params, **photos_params}).json()
        return response

    def get_file_name(self, likes_count, date, files):
        file_name = str(likes_count) + '.jpg'
        for file in files:
            if file_name == file['file_name']:
                file_name = str(likes_count) + '_' + str(date) + '.jpg'
        return file_name

    def get_photo_max_size_and_url(self, sizes_info):
        max_size = 0
        for size in sizes_info:
            actual_size = size['height'] * size['width']
            if actual_size > max_size:
                max_size = actual_size
                photo_url = size['url']
        return {'max_size': max_size, 'url': photo_url}

class YandexUploader:
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def create_folder(self, folder_name):
        headers = self.get_headers()
        params = {"path": folder_name}
        response = requests.put(self.url, headers=headers, params=params)
        if response.status_code == 201:
            return True
        else:
            return False

    def upload_file(self, vk_url, file_path):
        headers = self.get_headers()
        params = {"url": vk_url, "path": file_path}
        response = requests.post(self.url + 'upload/', headers=headers, params=params)
        if response.status_code == 202:
            return True
        else:
            return False

vk_user = VkUser(TOKEN_VK, VK_API_VERSION)
yandex_uploader = YandexUploader(TOKEN_YANDEX)
num_of_photos = PHOTO_COUNT

files = []
progress_bar = Bar('Uploading files', max=num_of_photos)

if yandex_uploader.create_folder(YANDEX_DISK_FOLDER):

    for photo in vk_user.get_photos(VK_USER_ID, num_of_photos)['response']['items']:
        photo_max_size_and_url = vk_user.get_photo_max_size_and_url(photo['sizes'])
        file_name = vk_user.get_file_name(photo['likes']['count'], photo['date'], files)
        files.append({'file_name': file_name, 'size': photo_max_size_and_url['max_size']})

        if yandex_uploader.upload_file(photo_max_size_and_url['url'], YANDEX_DISK_FOLDER + '/' + file_name):
            progress_bar.next()
            time.sleep(0.33)
        else:
            print(f'Uploading {file_name} failed')
            continue

    progress_bar.finish()
    print("UPLOAD COMPLETE")
    with open('files.json', 'w') as f:
        f.write(json.dumps(files))

else:
    print(f'Folder {YANDEX_DISK_FOLDER} already exists')