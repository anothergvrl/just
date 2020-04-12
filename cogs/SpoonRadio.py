from discord.ext import commands
import requests,json,sys,random,threading,time,pickle,os
from time import sleep
from threading import *
from multiprocessing import Process
from time import sleep
API_BASE_URL = "https://id-api.spooncast.net"
API_LIVES = '/lives/'
API_JOIN = '/join/'
API_LEAVE = '/leave/'
API_LIKE = '/like/'
user_token = ('token.txt')
UAInput = open('UALIST.txt','r').read().splitlines()
paramex = {'cv':'heimdallr'}
headerbasic = {'content-type':'application/json','connection':'keep-alive','user-agent':str(UAInput)}

class SpoonRadio(commands.Cog):
    def _init_(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(help='Tools Untuk Ganti ID Akun Spoon Radio')
    async def neng_gantiin(ctx):
      embed = discord.Embed(
        title = 'Klik Link Dibawah',
        description = '[############](https://GID.sepun.repl.run)',
        colour = discord.Colour.blue()
      )

      await ctx.send(embed=embed, delete_after=5)
    #############END SPOON TOOLS
    @commands.command(help='Fast uproom Spoon Radio')
    async def neng_anu(self, ctx, *, message):
        await ctx.send('Oke otw anu', delete_after=1)
        sleep(1)
        linklive = message
        respone = requests.get(linklive)
        url = respone.url
        shortlink = url[34:-59]
        r = requests.get(API_BASE_URL+API_LIVES+shortlink)
        respone_livex = r.json()
        for i in respone_livex['results']:
                livetitle = i['title']
                livenick = i['author']['nickname']
                jedabot = 0
                print (
                '\x1b[1;31;40m' + ' Nama Room :' + '\x1b[0m'+' '+livetitle,
                '\n','\x1b[1;32;40m'+'Penyiar : '+'\x1b[0m'+livenick)
                def love():
                    class lv1(Thread):
                        def run(self):
                            for i in range(0, 33):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                    class lv2(Thread):
                        def run(self):
                            for i in range(33, 66):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv3(Thread):
                        def run(self):
                            for i in range(66, 99):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION 
                    class lv4(Thread):
                        def run(self):
                            for i in range(99, 132):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv5(Thread):
                        def run(self):
                            for i in range(132, 165):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv6(Thread):
                        def run(self):
                            for i in range(165, 198):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv7(Thread):
                        def run(self):
                            for i in range(198, 231):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv8(Thread):
                        def run(self):
                            for i in range(231, 264):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv9(Thread):
                        def run(self):
                            for i in range(264, 297):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv10(Thread):
                        def run(self):
                            for i in range(297, 330):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                  
                    class lv11(Thread):
                        def run(self):
                            for i in range(330, 363):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                    class lv12(Thread):
                        def run(self):
                            for i in range(363, 396):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv13(Thread):
                        def run(self):
                            for i in range(396, 429):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION 
                    class lv14(Thread):
                        def run(self):
                            for i in range(429, 462):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv15(Thread):
                        def run(self):
                            for i in range(462, 495):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv16(Thread):
                        def run(self):
                            for i in range(495, 528):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv17(Thread):
                        def run(self):
                            for i in range(528, 561):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv18(Thread):
                        def run(self):
                            for i in range(561, 594):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv19(Thread):
                        def run(self):
                            for i in range(594, 627):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)
                ##ENDLINE FUNCTION HERE
                    class lv20(Thread):
                        def run(self):
                            for i in range(627, 661):
                                with open(user_token) as f:
                                    lst = f.read().splitlines()
                                    paramex = {'cv':'heimdallr'}
                                    headers = {'Authorization': 'Token ' + str(lst[i]),
                                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                    'content-type':'application/json',
                                    'user-agent':str(UAInput[i])}
                                    with requests.Session() as c:
                                      r = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
                                      r2 = c.post(API_BASE_URL+API_LIVES+shortlink+API_LIKE, headers=headers,params=paramex)
                                      print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                      sleep(jedabot)

                    t1 = lv1()
                    t2 = lv2()
                    t3 = lv3()
                    t4 = lv4()
                    t5 = lv5()
                    t6 = lv6()
                    t7 = lv7()
                    t8 = lv8()
                    t9 = lv9()
                    t10 = lv10()
                    t11 = lv11()
                    t12 = lv12()
                    t13 = lv13()
                    t14 = lv14()
                    t15 = lv15()
                    t16 = lv16()
                    t17 = lv17()
                    t18 = lv18()
                    t19 = lv19()
                    t20 = lv20()

                    t1.start()
                    t2.start()
                    t3.start()
                    t4.start()
                    t5.start()
                    t6.start()
                    t7.start()
                    t8.start()
                    t9.start()
                    t10.start()
                    t11.start()
                    t12.start()
                    t13.start()
                    t14.start()
                    t15.start()
                    t16.start()
                    t17.start()
                    t18.start()
                    t19.start()
                    t20.start()

                    t1.join()
                    t2.join()
                    t3.join()
                    t4.join()
                    t5.join()
                    t6.join()
                    t7.join()
                    t8.join()
                    t9.join()
                    t10.join()
                    t11.join()
                    t12.join()
                    t13.join()
                    t14.join()
                    t15.join()
                    t16.join()
                    t17.join()
                    t18.join()
                    t19.join()
                    t20.join()

                p=Process(target=love())
                p.start()
        else :
            await ctx.send('Ughh capek', delete_after=3)
            os.system('clear')
    ##ENDLINE FUNCTION HERE
    @commands.command(help='Fast Bot Leave')
    async def neng_keluarin(self, ctx, *, message):
        await ctx.send('Oke eneng bantu keluarin', delete_after=3)
        linklive = message
        respone = requests.get(linklive)
        url = respone.url
        shortlink = url[34:-59]
        r = requests.get(API_BASE_URL+API_LIVES+shortlink)
        respone_livex = r.json()
        for i in respone_livex['results']:
            livetitle = i['title']
            livenick = i['author']['nickname']
            jedabot = 0
            print (
            '\x1b[1;31;40m' + ' Nama Room :' + '\x1b[0m'+' '+livetitle,
            '\n','\x1b[1;32;40m'+'Penyiar : '+'\x1b[0m'+livenick)
            def love():
                class lv1(Thread):
                    def run(self):
                        for i in range(0, 33):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
                class lv2(Thread):
                    def run(self):
                        for i in range(33, 66):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
            ##ENDLINE FUNCTION HERE
                class lv3(Thread):
                    def run(self):
                        for i in range(66, 99):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
            ##ENDLINE FUNCTION 
                class lv4(Thread):
                    def run(self):
                        for i in range(99, 132):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
            ##ENDLINE FUNCTION HERE
                class lv5(Thread):
                    def run(self):
                        for i in range(132, 165):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
            ##ENDLINE FUNCTION HERE
                class lv6(Thread):
                    def run(self):
                        for i in range(165, 198):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
            ##ENDLINE FUNCTION HERE
                class lv7(Thread):
                    def run(self):
                        for i in range(198, 231):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
            ##ENDLINE FUNCTION HERE
                class lv8(Thread):
                    def run(self):
                        for i in range(231, 264):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
            ##ENDLINE FUNCTION HERE
                class lv9(Thread):
                    def run(self):
                        for i in range(264, 297):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
            ##ENDLINE FUNCTION HERE
                class lv10(Thread):
                    def run(self):
                        for i in range(297, 330):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
              
                class lv11(Thread):
                    def run(self):
                        for i in range(330, 363):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
                class lv12(Thread):
                    def run(self):
                        for i in range(363, 396):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
            ##ENDLINE FUNCTION HERE
                class lv13(Thread):
                    def run(self):
                        for i in range(396, 429):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)
            ##ENDLINE FUNCTION 
                class lv14(Thread):
                    def run(self):
                        for i in range(429, 462):
                            with open(user_token) as f:
                                lst = f.read().splitlines()
                                paramex = {'cv':'heimdallr'}
                                headers = {'Authorization': 'Token ' + str(lst[i]),
                                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                'content-type':'application/json',
                                'user-agent':str(UAInput[i])}
                                with requests.Session() as c:
                                  r = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
                                  print('Jajang Ke',i+1,'sudah nganu di room.','| Status Server :',r.status_code)
                                  sleep(jedabot)

                t1 = lv1()
                t2 = lv2()
                t3 = lv3()
                t4 = lv4()
                t5 = lv5()
                t6 = lv6()
                t7 = lv7()
                t8 = lv8()
                t9 = lv9()
                t10 = lv10()
                t11 = lv11()
                t12 = lv12()
                t13 = lv13()
                t14 = lv14()

                t1.start()
                t2.start()
                t3.start()
                t4.start()
                t5.start()
                t6.start()
                t7.start()
                t8.start()
                t9.start()
                t10.start()
                t11.start()
                t12.start()
                t13.start()
                t14.start()

                t1.join()
                t2.join()
                t3.join()
                t4.join()
                t5.join()
                t6.join()
                t7.join()
                t8.join()
                t9.join()
                t10.join()
                t11.join()
                t12.join()
                t13.join()
                t14.join()

            p=Process(target=love())
            p.start()
        else:
            await ctx.send('Ughhh Capek', delete_after=5)
            os.system('clear')
def setup(bot):
    bot.add_cog(SpoonRadio(bot))
