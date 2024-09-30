import json
import requests
from datetime import datetime


def load_file(name):
    try:
        with open('%s.json' % name) as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def save_file(name):
    with open('%s.json' % name, 'w') as file:
        json.dump(file_data, file, indent=4)


def getCurseforgeData(id):
    return requests.get('https://api.curseforge.com/v1/mods/%s' % id, headers=cfheaders).json()


def getModrinthData(id):
    return requests.get('https://api.modrinth.com/v2/project/%s' % id).json()


def getDownloads():
    profile = 0
    for i in mods:
        ids = i.split('-')
        cfdl = 0
        if ids[0] != 'n/a':
            cfdl = getCurseforgeData(ids[0])['data']['downloadCount']
        mrdl = 0
        if ids[1] != 'n/a':
            mrdl = getModrinthData(ids[1])['downloads']
        profile += cfdl + mrdl
        # print(profile)
    print('{:,}'.format(profile))
    print(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    date = datetime.today().strftime('%Y-%m-%d')
    time = datetime.today().strftime('%H:%M:%S')
    downloads = '{:,}'.format(profile)
    if not file_data['downloads'].get(date):
        file_data['downloads'][date] = {}
    file_data['downloads'][date][time] = downloads


cfheaders = {
    'Accept': 'application/json',
    'x-api-key': load_file("key/key")["key"]
}

mods = [
    "858032-HKKqmr2p",
    "932715-7jzrCiK0",
    "913586-C5hwIsg1",
    "550532-X4XNSWNM",
    "997888-twjW6Ggd",
    "1002272-aFKTqsnr",
    "n/a-46RgF8H2",
    "917744-oyJUwUv3",
    "581903-jCEmfHBM",
    "714218-GbO1YeS0",
    "915346-meHEWmih",
    "575963-n/a",
    "852342-Y7CHzqj5"
]

print(cfheaders)

file_name = 'data'
file_data = load_file(file_name)
save_file('data-backup')
getDownloads()
save_file('data')
