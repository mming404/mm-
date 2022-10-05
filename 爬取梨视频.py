import requests


url = '	https://www.pearvideo.com/videoStatus.jsp?contId=1035919&mrd=0.5299589978419361'
#'https://video.pearvideo.com/mp4/short/20170219/1663292814997-10210285-hd.mp4'
#'https://image1.pearvideo.com/cont/20170219/cont-1035919-10144900.png'

Referer = 'https://www.pearvideo.com/video_1035919'
id = Referer.split('_')[1]
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Referer':Referer
}

response = requests.get(url, headers=headers)
data = response.json()
systemTime = data['systemTime']
s_url = data['videoInfo']['videos']['srcUrl']
v_url = s_url.replace(systemTime, f'cont-{id}')
re = requests.get(v_url)
with open('梨视频.mp4', 'wb') as f:
    f.write(re.content)

