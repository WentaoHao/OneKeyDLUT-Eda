import requests 

try: 
    requests.get('https://www.baidu.com/', timeout = 0.5)
except requests.exceptions.ConnectTimeout:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }

    data = {
        'action': 'login',
        'ac_id' : '3',
        'username': '此处填入学号',
        'password': '此处填入密码',
        'save_me' : '1'
        }

    url = 'http://172.20.20.1:801/srun_portal_pc.php?ac_id=3&' 

    session = requests.Session()

    session.post(url, headers=headers, data=data)

    try:
        requests.get('https://www.baidu.com/', timeout = 0.5)
    except requests.exceptions.ConnectTimeout:
        print('Connect to the Internet failed !!!')
    else:
        print('Connect to the Internet successful !!!')
else:
    print('You has already connected to the Internet !!!')
