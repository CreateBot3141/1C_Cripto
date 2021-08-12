from flask import Flask
from flask import request
app = Flask(__name__)
from threading import Thread

def xor_cipher(strg, key ):
    encript_str = ''
    while strg != '':
        print ('[+] strg',strg)
        kodansii = int(int(strg[0:4])/3)
        print ('[+] strg',kodansii)
        #sm = chr(int(strg[0:3])/key)
        #for letter in str:
        #    encript_str += chr( ord(letter) ^ key )
        encript_str = encript_str + chr(kodansii)
        strg = strg[4:]        
    print ('[+] encript_str',encript_str)
    return  encript_str   

def ekran (message_in):
    message_in = message_in.replace ("<1>","'")
    message_in = message_in.replace ("<2>",'"')
    message_in = message_in.replace ("<7>","/")
    message_in = message_in.replace ("<8>","?")
    message_in = message_in.replace ("<9>","#")

    message_in = message_in.replace ("**7**","/")
    print ('[+] message_in',message_in)

    if message_in == 'not':
        message_in = ''
    return message_in

def bot_getMe_delete (token,user_id):
    import iz_func
    import json
    db,cursor = iz_func.connect ('main')
    sql = "select id,name,about from bots where token= '"+str(token)+"' "
    cursor.execute(sql)
    results = cursor.fetchall()    
    list = []
    id     = 0
    name   = '' 
    about  = '' 
    for row in results:
        id,name,about = row 
        print ('[+]',id,name,about)
    list.append ([id,name,about]) 
    if name != '':
        answer = "Бот уже зарегестрирован в системе: "+str(name)+", "+str(about)
    else:
        print ('    [+] Регестрируем телеграмм бота') 
        import requests
        url = 'https://api.telegram.org/bot'+str(token)+'/getMe'
        print ('[url]',url)
        page = requests.get(url)
        parsed_string = page.json()
        print ('json_text 1',parsed_string)
        try:
            description = parsed_string['description']
            #if description == 'Not Found':
            answer = "Токен указан неправильно"    
            #else:    
            #answer = "Бот зарегестрирован в системе"                
        except Exception as e: 
            answer = "Зарегестрирован новый бот" 
            username   = ''
            first_name = ''
            username   =  '@'+(parsed_string['result']['username'])
            first_name =  (parsed_string['result']['first_name'])
            sql = "INSERT INTO `bots` (`name`,`about`,`user_id`,`token`) VALUES ('{}','{}','{}','{}')".format (username,first_name,user_id,token)
            print ('[sql]',sql)
            cursor.execute(sql)
            db.commit()
            lastid = cursor.lastrowid
            url = 'https://api.telegram.org/bot'+str(token)+'/setWebhook?url=https://3dot14.ru/bot/bot.php?name='+str(lastid)
            print ('[url]',url)
            page = requests.get(url)
            json_text = page.json()
            print ('json_text 2',json_text)
    return answer

@app.route('/')
def hello_world():
    return 'API'

@app.route('/exchanges_myexchange/<access_code>/')
def exchanges_myexchange (access_code):
    import iz_func
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_myexchange',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    import iz_main
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.exchanges_myexchange ()
    #else:
    # 	answer = "Отказано в доступе ..."
    return answer

@app.route('/exchanges_fetchMarkets/<access_code>/<exchanges>/')
def exchanges_fetchMarkets (access_code,exchanges):
    import iz_func
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_fetchMarkets',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
    	answer = iz_main.exchanges_fetchMarkets (exchanges)
    else:
    	answer = "Отказано в доступе ..."
    return answer

@app.route('/exchanges_load_markets/<access_code>/<exchanges>/')
def exchanges_load_markets (access_code,exchanges):
    import iz_func
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_load_markets',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
    	answer = iz_main.exchanges_load_markets (exchanges)
    else:
    	answer = "Отказано в доступе ..."
    return answer

@app.route('/exchanges_fetchBalance/<access_code>/<exchanges>/<apiKey>/<secret>/')
def exchanges_fetchBalance (access_code,exchanges,apiKey,secret):
    import iz_func
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_fetchBalance',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
    	answer = iz_main.exchanges_fetchBalance (exchanges,apiKey,secret)
    else:
    	answer = "Отказано в доступе ..."
    return answer

@app.route('/exchanges_fetch_order_book/<access_code>/<exchanges>/<symbol1>/<symbol2>/')
def exchanges_fetch_order_book (access_code,exchanges,symbol1,symbol2):
    import iz_func
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_fetch_order_book',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
    	answer = iz_main.exchanges_fetch_order_book (exchanges,pair)
    else:
    	answer = "Отказано в доступе ..."
    return answer    

@app.route('/exchanges_ask/<access_code>/<exchanges>/<symbol1>/<symbol2>/')
def exchanges_ask (access_code,exchanges,symbol1,symbol2):
    import iz_func
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_ask',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
    	answer = iz_main.exchanges_ask (exchanges,pair)
    else:
    	answer = "Отказано в доступе ..."
    return answer  

@app.route('/exchanges_bid/<access_code>/<exchanges>/<symbol1>/<symbol2>/')
def exchanges_bid (access_code,exchanges,symbol1,symbol2):
    import iz_func
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_bid',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
    	answer = iz_main.exchanges_bid (exchanges,pair)
    else:
    	answer = "Отказано в доступе ..."
    return answer  

@app.route('/exchanges_spread/<access_code>/<exchanges>/<symbol1>/<symbol2>/')
def exchanges_spread (access_code,exchanges,symbol1,symbol2):
    import iz_func
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_spread',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
    	answer = iz_main.exchanges_spread (exchanges,pair)
    else:
    	answer = "Отказано в доступе ..."
    return answer  

@app.route('/exchanges_createLimitBuyOrder/<access_code>/<exchanges>/<apiKey>/<secret>/<symbol1>/<symbol2>/<amount>/<price>/')
def exchanges_createLimitBuyOrder (access_code,exchanges,apiKey,secret,symbol1,symbol2,amount,price):
    import iz_func
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_createLimitBuyOrder',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))
    #print ('[+] {}Объем: {}{}{}'.format(iz_func.c23,iz_func.c4,amount,iz_func.c23))
    #print ('[+] {}Цена: {}{}{}'.format(iz_func.c23,iz_func.c4,price,iz_func.c23))
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
    	answer = iz_main.exchanges_createLimitBuyOrder (exchanges,apiKey,secret,pair,amount,price)
    else:
    	answer = "Отказано в доступе ..."
    return answer  

@app.route('/exchanges_createLimitSellOrder/<access_code>/<exchanges>/<apiKey>/<secret>/<symbol1>/<symbol2>/<amount>/<price>/')
def exchanges_createLimitSellOrder (access_code,exchanges,apiKey,secret,symbol1,symbol2,amount,price):
    import iz_func
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_createLimitSellOrder',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))
    #print ('[+] {}Объем: {}{}{}'.format(iz_func.c23,iz_func.c4,amount,iz_func.c23))
    #print ('[+] {}Цена: {}{}{}'.format(iz_func.c23,iz_func.c4,price,iz_func.c23))
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
        answer = iz_main.exchanges_createLimitSellOrder (exchanges,apiKey,secret,pair,amount,price)
    else:
        answer = "Отказано в доступе ..."
    return answer  

@app.route('/exchanges_cancelOrder/<access_code>/<exchanges>/<apiKey>/<secret>/<symbol1>/<symbol2>/<ID>/')
def exchanges_cancelOrder (access_code,exchanges,apiKey,secret,symbol1,symbol2,ID):
    import iz_func
    answer  = 'TEST'
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_cancelOrder',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))
    #print ('[+] {}ID: {}{}{}'.format(iz_func.c23,iz_func.c4,ID,iz_func.c23))
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
        answer = iz_main.exchanges_cancelOrder (exchanges,apiKey,secret,ID,pair)
    else:
        answer = "Отказано в доступе ..."
    print ('[+] Ответ:')    
    print ('[+]',answer)            
    return answer  

@app.route('/exchanges_fetchOrder/<access_code>/<exchanges>/<apiKey>/<secret>/<symbol1>/<symbol2>/<ID>/')
def exchanges_fetchOrder (access_code,exchanges,apiKey,secret,symbol1,symbol2,ID):
    import iz_func
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_fetchOrder',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))
    #print ('[+] {}ID: {}{}{}'.format(iz_func.c23,iz_func.c4,ID,iz_func.c23))
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
    	answer = iz_main.exchanges_fetchOrder (exchanges,apiKey,secret,pair,ID)
    else:
    	answer = "Отказано в доступе ..."
    print ('[+] Ответ:')    
    print ('[+]',answer)    
    return answer  

@app.route('/exchanges_fetchTrades/<access_code>/<exchanges>/<symbol1>/<symbol2>/')
def exchanges_fetchTrades (access_code,exchanges,symbol1,symbol2):
    import iz_func
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_fetchTrades',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))    
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
        answer = iz_main.exchanges_fetchTrades (exchanges,pair)
    else:
        answer = "Отказано в доступе ..."
    print ('[+] Ответ:')    
    print ('[+]',answer)    
    return answer  

@app.route('/exchanges_fetchMyTrades/<access_code>/<exchanges>/<apiKey>/<secret>/<symbol1>/<symbol2>/')
def exchanges_fetchMyTrades (access_code,exchanges,apiKey,secret,symbol1,symbol2):
    import iz_func
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_fetchMyTrades',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))    
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
        answer = iz_main.exchanges_fetchMyTrades (exchanges,apiKey,secret,pair)
    else:
        answer = "Отказано в доступе ..."
    print ('[+] Ответ:')    
    print ('[+]',answer)    
    return answer  

@app.route('/exchanges_fetchOpenOrders/<access_code>/<exchanges>/<apiKey>/<secret>/<symbol1>/<symbol2>/')
def exchanges_fetchOpenOrders (access_code,exchanges,apiKey,secret,symbol1,symbol2):
    import iz_func
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_fetchOpenOrders',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))    
    import iz_main
    access = iz_main.test_access_code (access_code)
    if access == True:
        answer = iz_main.exchanges_fetchOpenOrders (exchanges,apiKey,secret,pair)
    else:
        answer = "Отказано в доступе ..."
    print ('[+] Ответ:')    
    print ('[+]',answer)    
    return answer  

############################################################################################################################################

@app.route('/exchanges_add_order/<exchanges>/<account>/<access_code>/<apiKey>/<secret>/<kod_doc>/<symbol1>/<symbol2>/<id_order>/<torg>/<amount_buy>/<amount_sell>/<amount_recom>/<price>/')
def exchanges_add_order (exchanges,account,access_code,apiKey,secret,kod_doc,symbol1,symbol2,id_order,torg,amount_buy,amount_sell,amount_recom,price):
    import iz_func
    pair = symbol1+'/'+symbol2
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'exchanges_add_order',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}Account: {}{}{}'.format(iz_func.c23,iz_func.c3,account,iz_func.c23))
    #print ('[+] {}КриптаБиржа: {}{}{}'.format(iz_func.c23,iz_func.c4,exchanges,iz_func.c23))
    #print ('[+] {}Инструмент: {}{}{}'.format(iz_func.c23,iz_func.c4,pair,iz_func.c23))
    #print ('[+] {}Номер сделки: {}{}{}'.format(iz_func.c23,iz_func.c4,id_order,iz_func.c23))
    #print ('[+] {}Вид сделки: {}{}{}'.format(iz_func.c23,iz_func.c4,torg,iz_func.c23))
    #print ('[+] {}Цена: {}{}{}'.format(iz_func.c23,iz_func.c4,price,iz_func.c23))
    #print ('[+] {}Объем покупки: {}{}{}'.format(iz_func.c23,iz_func.c4,amount_buy,iz_func.c23))
    #print ('[+] {}Объем продажи: {}{}{}'.format(iz_func.c23,iz_func.c4,amount_sell,iz_func.c23))
    #print ('[+] {}Цена рекомендации: {}{}{}'.format(iz_func.c23,iz_func.c4,amount_recom,iz_func.c23))
    import iz_main
    answer = iz_main.exchanges_add_order (exchanges,account,pair,amount_buy,amount_sell,amount_recom,price,access_code,apiKey,secret,kod_doc,id_order,torg)
    #access = iz_main.test_access_code (access_code)
    #if access == True:
        #answer = iz_main.exchanges_fetchOrder (exchanges,apiKey,secret,pair,ID)
    #    pass
    #else:
    #answer = "Отказано в доступе ..."
    print ('[+] Ответ:')    
    print ('[+]',answer)    
    return answer  

@app.route('/exchanges_fetchPositions/<access_code>/<account>/')   ### 
def exchanges_fetchPositions (access_code,account):   ### 
    import iz_func    
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main    
    #from binance.client import Client
    #api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    #secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    #client = Client(api_key, secret_key)
    #order = client.create_order(symbol='BTCUSDT',side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=0.001,price='52585.60000000')
    #answer = str(order)
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.exchanges_fetchPositions (account)
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer      

############################################################################################################################################

@app.route('/exchanges_pipy/<access_code>/<torg>/<symbol1>/<symbol2>/<amount>/<price>/')
def exchanges_pipy (access_code,torg,symbol1,symbol2,amount,price):
    pair = symbol1+'/'+symbol2
    import iz_main
    import iz_func
    import json
    import requests
    print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'Выставление моментального ордера',iz_func.c23))
    print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))  
    print ('[+] {}torg: {}{}{}'.format(iz_func.c23,iz_func.c3,torg,iz_func.c23)) 
    print ('[+] {}pair: {}{}{}'.format(iz_func.c23,iz_func.c3,pair,iz_func.c23)) 
    print ('[+] {}amount: {}{}{}'.format(iz_func.c23,iz_func.c3,amount,iz_func.c23)) 
    print ('[+] {}price: {}{}{}'.format(iz_func.c23,iz_func.c3,price,iz_func.c23)) 
    
    if 1==1:
        if 1==1:
            if torg == 'sell':
                print ('    [+] Процедура продажи')
                access_code = '1111-2222-1111-3333-5555'
                exchanges   = 'binace'
                symbol      = pair
                apiKey      = 'rGp4XQOVaDNH1TUhc5HYA7BOJCSavhARtlI2riUuF5vHMBX66fs1uKmcAcbSr9CZ'
                secret      = 'UMfCVcR3VcDdGvpdN5lAyTawn14oihliuj7li3FQYXNi1Tf5Q07jjHqYONrAaTdR'
                ##apiKey      = 'NhmiJYAF3kyGWweW7psotM9z7Bm5p0Vz'
                ##secret      = 'MQbZqYeBgCLazVyzQPYDNiimxyiNcRyQFnpLBsZsjo5dItH3Eo3T2Kekntbw9AUR'
                amount      = amount
                price       = price
                url = "http://192.168.0.85:5000/exchanges_createLimitSellOrder/"+str(access_code)+"/"+exchanges+"/"+str(apiKey)+"/"+str(secret)+"/"+symbol+"/{}/{}/".format(amount,price)
                print ('    [+]',url)
                #response = requests.get(url = url)
                #print (response.text)
                #sql = "UPDATE openorder SET answer = '"+response.text+"' WHERE `id` = '"+str(id)+"'"
                #cursor.execute(sql)
                #db.commit()

            if torg == 'buy':    
                print ('    [+] Процедура покупки')
                access_code = '1111-2222-1111-3333-5555'
                exchanges   = exchange
                symbol      = pair
                apiKey      = 'rGp4XQOVaDNH1TUhc5HYA7BOJCSavhARtlI2riUuF5vHMBX66fs1uKmcAcbSr9CZ'
                secret      = 'UMfCVcR3VcDdGvpdN5lAyTawn14oihliuj7li3FQYXNi1Tf5Q07jjHqYONrAaTdR'                
                ##apiKey      = 'NhmiJYAF3kyGWweW7psotM9z7Bm5p0Vz'
                ##secret      = 'MQbZqYeBgCLazVyzQPYDNiimxyiNcRyQFnpLBsZsjo5dItH3Eo3T2Kekntbw9AUR'
                amount      = amount
                price       = price
                url = "http://192.168.0.85:5000/exchanges_createLimitBuyOrder/"+str(access_code)+"/"+exchanges+"/"+str(apiKey)+"/"+str(secret)+"/"+symbol+"/{}/{}/".format(amount_buy,price)
                print ('    [+]',url)
                #response = requests.get(url = url)
                #print (response.text)
                #sql = "UPDATE openorder SET answer = '"+response.text+"' WHERE `id` = '"+str(id)+"'"
                #cursor.execute(sql)
                #db.commit()

    answer = "Выставлен ордер"
    return answer    

############################################################################################################################################


####  BINANCE ##############

@app.route('/binance_account/<access_code>/<name>/<apiKey>/<secret>/<exchange>/<comment>/<kod_1C>/')   ### 
def binance_account (access_code,name,apiKey,secret,exchange,comment,kod_1C):   ### 
    import iz_func
    print ('[+]',name)
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_account (access_code,name,apiKey,secret,exchange,comment,kod_1C)
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer  

@app.route('/binance_currency/<access_code>/<key>/')   ### 
def binance_currency (access_code,key):   ### 
    import iz_func
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_currency (key)    
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer  

@app.route('/binance_pire/<access_code>/<key>/')   ### 
def binance_pire (access_code,key):   ### 
    import iz_func
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_pire (key)    
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer  

@app.route('/binance_get_servertime/<access_code>/')   ### 
def binance_get_servertime (access_code):   ### 
    import iz_func
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_get_servertime ()    
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer  

#####################  СПОТОВАЯ ТОРГОВЛЯ #####################

@app.route('/binance_balance/<access_code>/<currency>/<account>/')   ### 
def binance_balance (access_code,currency,account):   ### 
    import iz_func
    print ('[+]',account)
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_balance (currency,account)    
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer  

@app.route('/binance_orderbook/<access_code>/')   ### 
def binance_orderbook (access_code):   ### 
    import iz_func
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_orderbook ()    
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer  

@app.route('/binance_create_order/<access_code>/')   ### 
def binance_create_order (access_code):   ### 
    #from binance.enums import *    
    import iz_func    
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main    
    #from binance.client import Client
    #api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    #secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    #client = Client(api_key, secret_key)
    #order = client.create_order(symbol='BTCUSDT',side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=0.001,price='52585.60000000')
    #answer = str(order)
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_create_order ()
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer  

@app.route('/binance_get_open_orders/<access_code>/')   ### 
def binance_get_open_orders (access_code):   ### 
    #from binance.enums import *    
    import iz_func    
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main    
    #from binance.client import Client
    #api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    #secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    #client = Client(api_key, secret_key)
    #order = client.create_order(symbol='BTCUSDT',side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=0.001,price='52585.60000000')
    #answer = str(order)
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_get_open_orders ()
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer      

@app.route('/binance_get_order/<access_code>/')   ### 
def binance_get_order (access_code):   ### 
    #from binance.enums import *    
    import iz_func    
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main    
    #from binance.client import Client
    #api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    #secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    #client = Client(api_key, secret_key)
    #order = client.create_order(symbol='BTCUSDT',side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=0.001,price='52585.60000000')
    #answer = str(order)
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_get_order ()
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer      

@app.route('/binance_cancel_order/<access_code>/<orderId>/')   ### 
def binance_cancel_order (access_code,orderId):   ### 
    #from binance.enums import *    
    import iz_func    
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main    
    #from binance.client import Client
    #api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    #secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    #client = Client(api_key, secret_key)
    #order = client.create_order(symbol='BTCUSDT',side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=0.001,price='52585.60000000')
    #answer = str(order)
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_cancel_order (orderId)
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer      

#################  margin  #########################

@app.route('/binance_get_margin_price_index/<access_code>/<account>/<pire>/')   ### 
def binance_get_margin_price_index (access_code,account,pire):   ### 
    #from binance.enums import *    
    import iz_func    
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main    
    #from binance.client import Client
    #api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    #secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    #client = Client(api_key, secret_key)
    #order = client.create_order(symbol='BTCUSDT',side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=0.001,price='52585.60000000')
    #answer = str(order)
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    account = ''
    answer = iz_main.binance_get_margin_price_index (account,pire)
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer      

@app.route('/binance_get_open_margin_orders/<access_code>/')   ### 
def binance_get_open_margin_orders (access_code):   ### 
    #from binance.enums import *    
    import iz_func    
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main    
    #from binance.client import Client
    #api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    #secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    #client = Client(api_key, secret_key)
    #order = client.create_order(symbol='BTCUSDT',side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=0.001,price='52585.60000000')
    #answer = str(order)
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_get_open_margin_orders ()
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer      

@app.route('/binance_get_all_margin_orders/<access_code>/')   ### 
def binance_get_all_margin_orders (access_code):   ### 
    #from binance.enums import *    
    import iz_func    
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main    
    #from binance.client import Client
    #api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    #secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    #client = Client(api_key, secret_key)
    #order = client.create_order(symbol='BTCUSDT',side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=0.001,price='52585.60000000')
    #answer = str(order)
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_get_all_margin_orders ()
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer      

@app.route('/binance_get_isolated_margin_account/<access_code>/<account>/')   ### 
def binance_get_isolated_margin_account (access_code,account):   ### 
    import iz_func    
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main    
    #from binance.client import Client
    #api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    #secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    #client = Client(api_key, secret_key)
    #order = client.create_order(symbol='BTCUSDT',side=SIDE_BUY,type=ORDER_TYPE_LIMIT,timeInForce=TIME_IN_FORCE_GTC,quantity=0.001,price='52585.60000000')
    #answer = str(order)
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_get_isolated_margin_account (account)
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer    

#################  futures  #########################

@app.route('/binance_futures_get_position/<access_code>/<account>/')   ### 
def binance_futures_get_position (access_code,account):   ### 
    import iz_func    
    import iz_main    
    answer = iz_main.binance_futures_get_position (account)
    print ('[+] Ответ:',answer)
    return answer    

@app.route('/binance_futures_get_balance/<access_code>/<account>/')   ### 
def binance_futures_get_balance (access_code,account):   ### 
    import iz_func    
    import iz_main    
    answer = iz_main.binance_futures_get_balance (account)
    print ('[+] Ответ:',answer)
    return answer    

@app.route('/binance_futures_get_symbol_orderbook_ticker/<access_code>/<account>/<symbol>/')   ### 
def binance_futures_get_symbol_orderbook_ticker (access_code,account,symbol):   ### 
    import iz_func    
    import iz_main    
    answer = iz_main.binance_futures_get_symbol_orderbook_ticker (account,symbol)
    print ('[+] Ответ:',answer)
    return answer    

@app.route('/binance_futures_post_order/<access_code>/<account>/<symbol>/<amount>/<price>/<side>/')   ### 
def binance_futures_post_order (access_code,account,symbol,amount,price,side):   ### 
    #### Выставить ордер согласно позиции
    import iz_func    
    import iz_main        
    #side = 'SELL'
    result = iz_main.binance_futures_post_order(account,symbol,amount,price,side)
    answer = str(result)
    print ('[+] Ответ:',answer)
    return answer  

@app.route('/binance_futures_stop_order/<access_code>/<account>/<symbol>/<side>/')   ### 
def binance_futures_stop_order (access_code,account,symbol,side):   ### 
    #### Выставить ордер согласно позиции
    import iz_func    
    import iz_main        
    #side = 'SELL'
    result = iz_main.binance_futures_stop_order(account,symbol,side)
    answer = str(result)
    print ('[+] Ответ:',answer)
    return answer  

@app.route('/binance_futures_post_order_buy/<access_code>/<account>/<symbol>/<amount>/<price>/')   ### 
def binance_futures_post_order_buy (access_code,account,symbol,amount,price):   ### 
    #### Выставить ордер согласно позиции
    print ('[+] symbol:',symbol)
    import iz_func    
    import iz_main        
    side = 'BUY'
    result = iz_main.binance_futures_post_order_buy(account,symbol,amount,price,side)
    answer = str(result)
    print ('[+] Ответ:',answer)
    return answer  

@app.route('/binance_futures_post_order_sell/<access_code>/<account>/<symbol>/<amount>/<price>/')   ### 
def binance_futures_post_order_sell (access_code,account,symbol,amount,price):   ### 
    #### Выставить ордер согласно позиции
    import iz_func    
    import iz_main        
    side = 'SELL'
    result = iz_main.binance_futures_post_order_sell(account,symbol,amount,price,side)
    answer = str(result)
    print ('[+] Ответ:',answer)
    return answer  

@app.route('/binance_futures_get_open_orders/<access_code>/<account>/<symbol>/')   ### 
def binance_futures_get_open_orders (access_code,account,symbol):   ### 
    import iz_func  
    import iz_main    
    result = iz_main.binance_futures_get_open_orders(account,symbol)    
    answer = str(result)
    print ('[+] Ответ:',answer)
    return answer    

@app.route('/binance_futures_cancel_order/<access_code>/<account>/<symbol>/<orderId>/')   ### 
def binance_futures_cancel_order (access_code,account,symbol,orderId):   ### 
    import iz_func    
    import iz_main        
    answer = iz_main.binance_futures_cancel_order (account,symbol,orderId)
    print ('[+] Ответ:',answer)
    return answer    

@app.route('/binance_futures_post_stoploss_order/<access_code>/<account>/<symbol>/<price>/<side>/')   ### 
def binance_futures_post_stoploss_order (access_code,account,symbol,price,side):   ### 
    #### Выставить ордер согласно позиции
    import iz_func    
    import iz_main        
    try:
        result = iz_main.binance_futures_post_stoploss_order(account,symbol,price,side)    
        answer = str(['ok',str(result)])
        print ('[+] Ответ:',answer)
        return answer    
    except Exception as e:
        print ('[+] str(e)'),str(e)
        answer = str(['error',str(e)])
        return answer    
        
    
    ## http://3dot14.ru:5000/binance_futures_get_candlestick_data/3141/Дима Клиент/BTCUSDT/3/30min/

@app.route('/binance_futures_get_candlestick_data/<access_code>/<account>/<symbol>/<koll>/<timeF>/')   ### 
def binance_futures_get_candlestick_data (access_code,account,symbol,koll,timeF):   ### 
    #### Выставить ордер согласно позиции
    import iz_func    
    import iz_main        
    result = iz_main.binance_futures_get_candlestick_data(account,symbol,koll,timeF)
    answer = str(result)
    print ('[+] Ответ:',answer)
    return answer    

@app.route('/binance_futures_change_initial_leverage/<access_code>/<account>/<symbol>/<koll>/')   ### 
def binance_futures_change_initial_leverage (access_code,account,symbol,koll):   ### 
    #### Выставить ордер согласно позиции
    import iz_func    
    import iz_main  
    try:      
        result = iz_main.binance_futures_change_initial_leverage(account,symbol,koll)
        answer = str(['ok',str(result)])
        print ('[+] Ответ:',answer)
        return answer    
    except Exception as e:
        print ('[+] str(e)'),str(e)
        answer = str(['error',str(e)])
        return answer    

@app.route('/binance_futures_get_order/<access_code>/<account>/<symbol>/<orderId>/')   ### 
def binance_futures_get_order (access_code,account,symbol,orderId):   ### 
    #### Выставить ордер согласно позиции
    import iz_func    
    import iz_main        
    result = iz_main.binance_futures_get_order(account,symbol,orderId)
    answer = str(result)
    print ('[+] Ответ:',answer)
    return answer    

@app.route('/binance_futures_get_recent_trades_list/<access_code>/<symbol>/<limit>/')   ### 
def binance_futures_get_recent_trades_list (access_code,symbol,limit):   ### 
    import iz_func
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_futures_get_recent_trades_list (symbol,limit)    
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer  

@app.route('/binance_futures_get_aggregate_trades_list/<access_code>/<symbol>/<limit>/')   ### 
def binance_futures_get_aggregate_trades_list (access_code,symbol,limit):   ### 
    import iz_func
    #print ('[+] {}Запуск процедуры: {}{}{}'.format(iz_func.c23,iz_func.c2,'SQL',iz_func.c23))
    #print ('[+] {}Access_code: {}{}{}'.format(iz_func.c23,iz_func.c3,access_code,iz_func.c23))
    #print ('[+] {}key: {}{}{}'.format(iz_func.c23,iz_func.c4,key,iz_func.c23))
    import iz_main
    #access = iz_main.test_access_code (access_code)
    #if access == True:
    answer = iz_main.binance_futures_get_aggregate_trades_list (symbol,limit)    
    print ('[+] Ответ:',answer)
    #else:
    #    answer = "Отказано в доступе ..."
    #print ('[+] Ответ при выполнении запроса:',answer) 
    #sql = request.form['sql']
    #form = RegisterForm(request.form)
    #print('[+]: ',sql)
    #answer = 'Ответ'
    return answer  

@app.route('/nmap/<access_code>/<site>/')
def nmap (access_code,site):
    print ('[+]')
    import os
    myCmd = os.popen('nmap 127.0.0.1').read()
    print(myCmd)    
    return myCmd

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)