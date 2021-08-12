#!/usr/bin/python
# -*- coding: utf-8

def get_account (account):
    import iz_func
    api_key    = ""
    secret_key = ""
    db,cursor = iz_func.connect ()
    sql = "select id,apiKey,secret from cripta_account where name = '"+str(account)+"' limit 1"
    cursor.execute(sql)
    results = cursor.fetchall()   
    for row in results:
        id,api_key,secret_key = row.values()         
    return api_key,secret_key

def test_access_code (access_code):
    import iz_func 
    import time
    unixtime = time.time ()     
    db,cursor = iz_func.connect ()
    sql = "select id,name,begin_key,end_key,user_id from access_code where `key` = '"+str(access_code)+"' and begin_key < "+str(unixtime)+" and end_key > "+str(unixtime)+" limit 1;"
    cursor.execute(sql)
    results = cursor.fetchall()    
    answer = False
    for row in results:
        id,name,begin_key,end_key,user_id = row
        answer = True
    return answer

def get_exchanges (exchanges,apiKey,secret):
    import ccxt
    if 1==1:
        if exchanges == '_1btcxe': 
            client = ccxt._1btcxe ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'acx': 
            client = ccxt.acx ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'allcoin': 
            client = ccxt.allcoin ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'anxpro': 
            client = ccxt.anxpro ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'anybits': 
            client = ccxt.anybits ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bcex': 
            client = ccxt.bcex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bibox': 
            client = ccxt.bibox ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bigone': 
            client = ccxt.bigone ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'binance': 
            client = ccxt.binance ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bit2c': 
            client = ccxt.bit2c ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitbank': 
            client = ccxt.bitbank ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitbay': 
            client = ccxt.bitbay ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitfinex': 
            client = ccxt.bitfinex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitfinex2': 
            client = ccxt.bitfinex2 ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitflyer': 
            client = ccxt.bitflyer ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitforex': 
            client = ccxt.bitforex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bithumb': 
            client = ccxt.bithumb ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitibu': 
            client = ccxt.bitibu ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitkk': 
            client = ccxt.bitkk ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitlish': 
            client = ccxt.bitlish ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitmarket': 
            client = ccxt.bitmarket ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitmex': 
            client = ccxt.bitmex ({'apiKey': apiKey,'secret': secret})

        if exchanges == 'bitmax': 
            client = ccxt.bitmax ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitsane': 
            client = ccxt.bitsane ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitso': 
            client = ccxt.bitso ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitstamp': 
            client = ccxt.bitstamp ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitstamp1': 
            client = ccxt.bitstamp1 ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bittrex': 
            client = ccxt.bittrex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bitz': 
            client = ccxt._1btcxe ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bl3p': 
            client = ccxt.bl3p ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bleutrade': 
            client = ccxt.bleutrade ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'braziliex': 
            client = ccxt.braziliex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'btcalpha': 
            client = ccxt.btcalpha ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'btcbox': 
            client = ccxt.btcbox ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'btcchina': 
            client = ccxt.btcchina ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'btcexchange': 
            client = ccxt.btcexchange ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'btcmarkets': 
            client = ccxt.btcmarkets ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'btctradeim': 
            client = ccxt.btctradeim ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'btctradeua': 
            client = ccxt.btctradeua ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'btcturk': 
            client = ccxt.btcturk ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'buda': 
            client = ccxt.buda ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'bxinth': 
            client = ccxt.bxinth ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'ccex': 
            client = ccxt.ccex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'cex': 
            client = ccxt.cex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'chbtc': 
            client = ccxt.chbtc ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'chilebit': 
            client = ccxt.chilebit ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'cobinhood': 
            client = ccxt.cobinhood ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinbase': 
            client = ccxt.coinbase ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinbaseprime': 
            client = ccxt.coinbaseprime ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinbasepro': 
            client = ccxt.coinbasepro ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coincheck': 
            client = ccxt.coincheck ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinegg': 
            client = ccxt.coinegg ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinex': 
            client = ccxt.coinex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinexchange': 
            client = ccxt.coinexchange ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinfalcon': 
            client = ccxt.coinfalcon ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinfloor': 
            client = ccxt.coinfloor ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coingi': 
            client = ccxt.coingi ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinmarketcap': 
            client = ccxt.coinmarketcap ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinmate': 
            client = ccxt.coinmate ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinnest': 
            client = ccxt.coinnest ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinone': 
            client = ccxt.coinone ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coinspot': 
            client = ccxt.coinspot ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'cointiger': 
            client = ccxt.cointiger ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coolcoin': 
            client = ccxt.coolcoin ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'coss': 
            client = ccxt.coss ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'crex24': 
            client = ccxt.crex24 ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'crypton': 
            client = ccxt.crypton ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'cryptopia': 
            client = ccxt.cryptopia ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'deribit': 
            client = ccxt.deribit ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'dsx': 
            client = ccxt.dsx ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'ethfinex': 
            client = ccxt.ethfinex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'exmo': 
            client = ccxt.exmo ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'exx': 
            client = ccxt.exx ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'fcoin': 
            client = ccxt.fcoin ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'fcoinjp': 
            client = ccxt.fcoinjp ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'flowbtc': 
            client = ccxt.flowbtc ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'foxbit': 
            client = ccxt.foxbit ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'fybse': 
            client = ccxt.fybse ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'fybsg': 
            client = ccxt.fybsg ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'gateio': 
            client = ccxt.gateio ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'gdax': 
            client = ccxt.gdax ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'gemini': 
            client = ccxt.gemini ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'getbtc': 
            client = ccxt.getbtc ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'hadax': 
            client = ccxt.hadax ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'hitbtc': 
            client = ccxt.hitbtc ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'hitbtc2': 
            client = ccxt.hitbtc2 ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'huobipro': 
            client = ccxt.huobipro ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'huobiru': 
            client = ccxt.huobiru ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'ice3x': 
            client = ccxt.ice3x ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'independentreserve': 
            client = ccxt.independentreserve ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'indodax': 
            client = ccxt.indodax ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'itbit': 
            client = ccxt.itbit ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'jubi': 
            client = ccxt.jubi ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'kkex': 
            client = ccxt.kkex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'kraken': 
            client = ccxt.kraken ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'kucoin': 
            client = ccxt.kucoin ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'kuna': 
            client = ccxt.kuna ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'lakebtc': 
            client = ccxt.lakebtc ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'lbank': 
            client = ccxt.lbank ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'liqui': 
            client = ccxt.liqui ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'liquid': 
            client = ccxt.liquid ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'livecoin': 
            client = ccxt.livecoin ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'luno': 
            client = ccxt.luno ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'lykke': 
            client = ccxt.lykke ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'mercado': 
            client = ccxt.mercado ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'mixcoins': 
            client = ccxt.mixcoins ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'negociecoins': 
            client = ccxt.negociecoins ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'nova': 
            client = ccxt.nova ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'okcoincny': 
            client = ccxt.okcoincny ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'okcoinusd': 
            client = ccxt.okcoinusd ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'okex': 
            client = ccxt.okex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'paymium': 
            client = ccxt.paymium ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'poloniex': 
            client = ccxt.poloniex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'quadrigacx': 
            client = ccxt.quadrigacx ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'rightbtc': 
            client = ccxt.rightbtc ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'southxchange': 
            client = ccxt.southxchange ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'stronghold': 
            client = ccxt.stronghold ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'surbitcoin': 
            client = ccxt.surbitcoin ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'theocean': 
            client = ccxt.theocean ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'therock': 
            client = ccxt.therock ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'tidebit': 
            client = ccxt.tidebit ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'tidex': 
            client = ccxt.tidex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'uex': 
            client = ccxt.uex ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'upbit': 
            client = ccxt.upbit ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'urdubit': 
            client = ccxt.urdubit ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'vaultoro': 
            client = ccxt.vaultoro ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'vbtc': 
            client = ccxt.vbtc ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'virwox': 
            client = ccxt.virwox ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'xbtce': 
            client = ccxt.xbtce ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'yobit': 
            client = ccxt.yobit ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'yunbi': 
            client = ccxt.yunbi ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'zaif': 
            client = ccxt.zaif ({'apiKey': apiKey,'secret': secret})
            
        if exchanges == 'zb': 
            client = ccxt.zb ({'apiKey': apiKey,'secret': secret})

    return client

def exchanges_myexchange ():
    import json
    data = []
    if 1==1:
        data.append({'id':0,'name':'_1btcxe','API':'https://1btcxe.com/api-docs.php','URL':'https://1btcxe.com/'})
        data.append({'id':0,'name':'acx','API':'','URL':''})
        data.append({'id':0,'name':'allcoin','API':'','URL':''})
        data.append({'id':0,'name':'anxpro','API':'','URL':''})
        data.append({'id':0,'name':'anybits','API':'','URL':''})
        data.append({'id':0,'name':'bcex','API':'','URL':''})
        data.append({'id':0,'name':'bibox','API':'','URL':''})
        data.append({'id':0,'name':'bigone','API':'','URL':''})
        data.append({'id':1,'name':'binance','API':'','URL':''})
        data.append({'id':0,'name':'bit2c','API':'','URL':''})
        data.append({'id':0,'name':'bitbank','API':'','URL':''})
        data.append({'id':0,'name':'bitbay','API':'','URL':''})
        data.append({'id':0,'name':'bitfinex','API':'','URL':''})
        data.append({'id':4,'name':'bitfinex2','API':'','URL':''})
        data.append({'id':0,'name':'bitflyer','API':'','URL':''})
        data.append({'id':0,'name':'bitforex','API':'','URL':''})
        data.append({'id':0,'name':'bithumb','API':'','URL':''})
        data.append({'id':0,'name':'bitibu','API':'','URL':''})
        data.append({'id':0,'name':'bitkk','API':'','URL':''})
        data.append({'id':0,'name':'bitlish','API':'','URL':''})
        data.append({'id':0,'name':'bitmarket','API':'','URL':''})
        data.append({'id':0,'name':'bitmex','API':'','URL':''})
        data.append({'id':0,'name':'bitsane','API':'','URL':''})
        data.append({'id':0,'name':'bitso','API':'','URL':''})
        data.append({'id':0,'name':'bitstamp','API':'','URL':''})
        data.append({'id':0,'name':'bitstamp1','API':'','URL':''})
        data.append({'id':0,'name':'bittrex','API':'','URL':''})
        data.append({'id':0,'name':'bitz','API':'','URL':''})
        data.append({'id':0,'name':'bl3p','API':'','URL':''})
        data.append({'id':0,'name':'bleutrade','API':'','URL':''})
        data.append({'id':0,'name':'braziliex','API':'','URL':''})
        data.append({'id':0,'name':'btcalpha','API':'','URL':''})
        data.append({'id':0,'name':'btcbox','API':'','URL':''})
        data.append({'id':0,'name':'btcchina','API':'','URL':''})
        data.append({'id':0,'name':'btcexchange','API':'','URL':''})
        data.append({'id':0,'name':'btcmarkets','API':'','URL':''})
        data.append({'id':0,'name':'btctradeim','API':'','URL':''})
        data.append({'id':0,'name':'btctradeua','API':'','URL':''})
        data.append({'id':0,'name':'btcturk','API':'','URL':''})
        data.append({'id':0,'name':'buda','API':'','URL':''})
        data.append({'id':0,'name':'bxinth','API':'','URL':''})
        data.append({'id':0,'name':'ccex','API':'','URL':''})
        data.append({'id':0,'name':'cex','API':'','URL':''})
        data.append({'id':0,'name':'chbtc','API':'','URL':''})
        data.append({'id':0,'name':'chilebit','API':'','URL':''})
        data.append({'id':0,'name':'cobinhood','API':'','URL':''})
        data.append({'id':2,'name':'coinbase','API':'','URL':''})
        data.append({'id':0,'name':'coinbaseprime','API':'','URL':''})
        data.append({'id':0,'name':'coinbasepro','API':'','URL':''})
        data.append({'id':0,'name':'coincheck','API':'','URL':''})
        data.append({'id':0,'name':'coinegg','API':'','URL':''})
        data.append({'id':0,'name':'coinex','API':'','URL':''})
        data.append({'id':0,'name':'coinexchange','API':'','URL':''})
        data.append({'id':6,'name':'coinfalcon','API':'','URL':''})
        data.append({'id':0,'name':'coinfloor','API':'','URL':''})
        data.append({'id':0,'name':'coingi','API':'','URL':''})
        data.append({'id':0,'name':'coinmarketcap','API':'','URL':''})
        data.append({'id':0,'name':'coinmate','API':'','URL':''})
        data.append({'id':0,'name':'coinnest','API':'','URL':''})
        data.append({'id':0,'name':'coinone','API':'','URL':''})
        data.append({'id':0,'name':'coinspot','API':'','URL':''})
        data.append({'id':0,'name':'cointiger','API':'','URL':''})
        data.append({'id':0,'name':'coolcoin','API':'','URL':''})
        data.append({'id':0,'name':'coss','API':'','URL':''})
        data.append({'id':0,'name':'crex24','API':'','URL':''})
        data.append({'id':0,'name':'crypton','API':'','URL':''})
        data.append({'id':0,'name':'cryptopia','API':'','URL':''})
        data.append({'id':0,'name':'deribit','API':'','URL':''})
        data.append({'id':0,'name':'dsx','API':'','URL':''})
        data.append({'id':0,'name':'ethfinex','API':'','URL':''})
        data.append({'id':0,'name':'exmo','API':'','URL':''})
        data.append({'id':0,'name':'exx','API':'','URL':''})
        data.append({'id':0,'name':'fcoin','API':'','URL':''})
        data.append({'id':0,'name':'fcoinjp','API':'','URL':''})
        data.append({'id':0,'name':'flowbtc','API':'','URL':''})
        data.append({'id':0,'name':'foxbit','API':'','URL':''})
        data.append({'id':0,'name':'fybse','API':'','URL':''})
        data.append({'id':0,'name':'fybsg','API':'','URL':''})
        data.append({'id':0,'name':'gateio','API':'','URL':''})
        data.append({'id':0,'name':'gdax','API':'','URL':''})
        data.append({'id':0,'name':'gemini','API':'','URL':''})
        data.append({'id':0,'name':'getbtc','API':'','URL':''})
        data.append({'id':0,'name':'hadax','API':'','URL':''})
        data.append({'id':5,'name':'hitbtc','API':'','URL':''})
        data.append({'id':0,'name':'hitbtc2','API':'','URL':''})
        data.append({'id':0,'name':'huobipro','API':'','URL':''})
        data.append({'id':0,'name':'huobiru','API':'','URL':''})
        data.append({'id':0,'name':'ice3x','API':'','URL':''})
        data.append({'id':0,'name':'independentreserve','API':'','URL':''})
        data.append({'id':0,'name':'indodax','API':'','URL':''})
        data.append({'id':0,'name':'itbit','API':'','URL':''})
        data.append({'id':0,'name':'jubi','API':'','URL':''})
        data.append({'id':0,'name':'kkex','API':'','URL':''})
        data.append({'id':10,'name':'kraken','API':'','URL':''})
        data.append({'id':7,'name':'kucoin','API':'','URL':''})
        data.append({'id':0,'name':'kuna','API':'','URL':''})
        data.append({'id':0,'name':'lakebtc','API':'','URL':''})
        data.append({'id':0,'name':'lbank','API':'','URL':''})
        data.append({'id':0,'name':'liqui','API':'','URL':''})
        data.append({'id':0,'name':'liquid','API':'','URL':''})
        data.append({'id':0,'name':'livecoin','API':'','URL':''})
        data.append({'id':0,'name':'luno','API':'','URL':''})
        data.append({'id':0,'name':'lykke','API':'','URL':''})
        data.append({'id':0,'name':'mercado','API':'','URL':''})
        data.append({'id':0,'name':'mixcoins','API':'','URL':''})
        data.append({'id':0,'name':'negociecoins','API':'','URL':''})
        data.append({'id':0,'name':'nova','API':'','URL':''})
        data.append({'id':0,'name':'okcoincny','API':'','URL':''})
        data.append({'id':0,'name':'okcoinusd','API':'','URL':''})
        data.append({'id':9,'name':'okex','API':'','URL':''})
        data.append({'id':0,'name':'paymium','API':'','URL':''})
        data.append({'id':3,'name':'poloniex','API':'','URL':''})
        data.append({'id':0,'name':'quadrigacx','API':'','URL':''})
        data.append({'id':0,'name':'rightbtc','API':'','URL':''})
        data.append({'id':0,'name':'southxchange','API':'','URL':''})
        data.append({'id':0,'name':'stronghold','API':'','URL':''})
        data.append({'id':0,'name':'surbitcoin','API':'','URL':''})
        data.append({'id':0,'name':'theocean','API':'','URL':''})
        data.append({'id':0,'name':'therock','API':'','URL':''})
        data.append({'id':0,'name':'tidebit','API':'','URL':''})
        data.append({'id':0,'name':'tidex','API':'','URL':''})
        data.append({'id':0,'name':'uex','API':'','URL':''})
        data.append({'id':0,'name':'upbit','API':'','URL':''})
        data.append({'id':0,'name':'urdubit','API':'','URL':''})
        data.append({'id':0,'name':'vaultoro','API':'','URL':''})
        data.append({'id':0,'name':'vbtc','API':'','URL':''})
        data.append({'id':0,'name':'virwox','API':'','URL':''})
        data.append({'id':0,'name':'xbtce','API':'','URL':''})
        data.append({'id':8,'name':'yobit','API':'','URL':''})
        data.append({'id':0,'name':'yunbi','API':'','URL':''})
        data.append({'id':0,'name':'zaif','API':'','URL':''})
        data.append({'id':0,'name':'zb','API':'','URL':''})
        answer = json.dumps(data)
    return answer

def exchanges_fetchMarkets (exchanges):
    import json
    client = get_exchanges (exchanges,'','')
    data = client.fetchMarkets()
    answer = json.dumps(data)
    return answer 

def exchanges_load_markets (exchanges):
    import json
    client = get_exchanges (exchanges,'','')
    data = client.load_markets()
    answer = json.dumps(data)
    return answer 

def exchanges_fetchBalance (exchanges,apiKey,secret):
    import json
    client = get_exchanges (exchanges,apiKey,secret)
    data = client.fetchBalance()
    answer = json.dumps(data)
    return answer 

def exchanges_fetch_order_book (exchanges,pair):
    import json
    client = get_exchanges (exchanges,'','')
    data = client.fetch_order_book(pair)
    answer = json.dumps(data)
    return answer 

def exchanges_ask (exchanges,pair):
    import json
    client = get_exchanges (exchanges,'','')
    orderbook = client.fetch_order_book (pair)
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
    data = ask
    answer = json.dumps(data)
    return answer 

def exchanges_bid (exchanges,pair): 
    import json
    client = get_exchanges (exchanges,'','')
    orderbook = client.fetch_order_book (pair)                                         ###
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None       
    data = bid
    answer = json.dumps(data)
    return answer 

def exchanges_spread  (exchanges,pair):
    import json
    client = get_exchanges (exchanges,'','')
    orderbook = client.fetch_order_book (pair)                                                ###
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None                    ###
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None                    ###
    spread = (ask - bid) if (bid and ask) else None    
    data = {'ask':ask,'bid':bid,'spread':spread}
    answer = json.dumps(data)   
    return answer      

def exchanges_fetchStatus (exchanges):
    import json
    client = get_exchanges (exchanges,'','')
    data = client.fetchStatus()
    answer = json.dumps(data)
    return answer 

def exchanges_fetchL2OrderBook (exchanges,pair):
    import json
    client = get_exchanges (exchanges,'','')
    data = client.fetchL2OrderBook (pair)
    answer = json.dumps(data)
    return answer 

def exchanges_fetchTrades (exchanges,pair):
    import json
    client = get_exchanges (exchanges,'','')
    data = client.fetchTrades (pair)
    answer = json.dumps(data)
    return answer 

def exchanges_fetchTicker (exchanges,pair):
    import json
    client = get_exchanges (exchanges,'','')
    data = client.fetchTicker (pair)
    answer = json.dumps(data)
    return answer 

def exchanges_createOrder (exchanges):
    import json
    client = get_exchanges (exchanges,'','')
    data = client.createOrder ()
    answer = json.dumps(data)
    return answer 

def exchanges_createLimitBuyOrder (exchanges,apiKey,secret,pair,amount,price):
    import json
    client = get_exchanges (exchanges,apiKey,secret)
    try:
        data = client.createLimitBuyOrder (pair,float(amount),float(price))
        answer = json.dumps(data)
    except Exception as e:                
        print ('    [+]',str(e)) 
        data = {'error':str(e)}  
        answer = json.dumps(data)    
    return answer 

def exchanges_createLimitSellOrder (exchanges,apiKey,secret,pair,amount,price):
    import json
    client = get_exchanges (exchanges,apiKey,secret) 
    try:   
        data = client.createLimitSellOrder(pair,float(amount),float(price))
        answer = json.dumps(data)
    except Exception as e:                
        print ('    [+]',str(e)) 
        data = {'error':str(e)}  
        answer = json.dumps(data)            
    return answer 

def exchanges_createMarketBuyOrder (exchanges,apiKey,secret):
    import json
    client = get_exchanges (exchanges,apiKey,secret)        
    data = client.createMarketBuyOrder()
    answer = json.dumps(data)
    return answer 

def exchanges_createMarketSellOrder (exchanges,apiKey,secret):
    import json
    client = get_exchanges (exchanges,apiKey,secret)            
    data = client.createMarketSellOrder()
    answer = json.dumps(data)
    return answer 

def exchanges_cancelOrder (exchanges,apiKey,secret,ID,pair):
    import json
    client = get_exchanges (exchanges,apiKey,secret)
    try: 
        data = client.cancelOrder(int(ID),pair)
        answer = json.dumps(data)
    except Exception as e:                
        print ('    [+]',str(e)) 
        data = {'error':str(e)}  
        answer = json.dumps(data)            
    return answer 
        
def exchanges_fetchOrder (exchanges,apiKey,secret,pair,ID):
    import json
    client = get_exchanges (exchanges,apiKey,secret)            
    try:
        data = client.fetchOrder(int(ID),pair)
        answer = json.dumps(data)
    except Exception as e:                
        print (str(e)) 
        data = {'error':str(e)}  
        answer = json.dumps(data)      
    return answer 

def exchanges_fetchOrders (exchanges,pair):
    import json
    client = get_exchanges (exchanges,"","")            
    data = client.fetchOrders (pair)
    answer = json.dumps(data)   
    return answer 

def exchanges_fetchOpenOrders (exchanges,apiKey,secret,pair):
    import json
    client = get_exchanges (exchanges,apiKey,secret)            
    data = client.fetchOpenOrders (pair)
    answer = json.dumps(data)
    return answer 

def exchanges_fetchClosedOrders (exchanges,pair):
    import json
    client = get_exchanges (exchanges,"","")            
    data = client.fetchClosedOrders(pair)
    answer = json.dumps(data)
    return answer 

def exchanges_fetchMyTrades (exchanges,apiKey,secret,pair):
    import json
    client = get_exchanges (exchanges,apiKey,secret)            
    data = client.fetchMyTrades (pair)
    answer = json.dumps(data)
    return answer 

def exchanges_fetchOHLCV (exchanges,pair,timeframes):
    import json
    client = get_exchanges (exchanges,"","")            
    data = client.fetchOHLCV (pair,timeframes)
    answer = json.dumps(data)
    return answer 

def exchanges_fetchTransactions (exchanges,apiKey,secret):
    import json
    client = get_exchanges (exchanges,apiKey,secret)            
    data = client.fetchTransactions()
    answer = json.dumps(data)
    return answer 

def exchanges_fetchDeposits (exchanges,apiKey,secret):
    import json
    client = get_exchanges (exchanges,apiKey,secret)            
    data    = client.fetchDeposits()
    answer  = json.dumps(data)
    return answer 

def exchanges_fetchWithdrawals (exchanges,apiKey,secret):
    import json
    client = get_exchanges (exchanges,apiKey,secret)            
    data   = client.fetchWithdrawals ()
    answer = json.dumps(data)                                                                                                                                     
    return answer 

def exchanges_add_order (exchanges,account,symbol,amount_buy,amount_sell,amount_recom,price,access_code,apiKey,secret,kod_doc,id_order,torg):
    import iz_func    
    namebot = ''
    db,cursor = iz_func.connect (namebot)  
    id_order       =  '' 
    dateofbirth    =  0
    status         =  '' 
    answer         =  '' 
    sql = "INSERT INTO openorder (`account`,`exchanges`,`id_order`,`dateofbirth`,`status`,`answer`,`amount_buy`,`amount_sell`,`amount_recom`,`price`,`symbol`,`access_code`,`apiKey`,`secret`,`kod_doc`,`torg`) VALUES ('{}','{}','{}',{},'{}','{}',{},{},{},{},'{}','{}','{}','{}','{}','{}')".format (account,exchanges,id_order,dateofbirth,status,answer,amount_buy,amount_sell,amount_recom,price,symbol,access_code,apiKey,secret,kod_doc,torg)  ## amount_buy,amount_sell,amount_recom
    print ('[+]',sql)
    cursor.execute(sql)
    db.commit()
    answer = "Добавлен" 
    return answer 

def exchanges_fetchPositions (account):  
    import iz_func  
    import json   
    import ccxt
    answer = 'Нет данных'
    from binance.client import Client
    import iz_func
    api_key    = ""
    secret_key = ""
    db,cursor = iz_func.connect ()
    sql = "select id,apiKey,secret  from cripta_account where name = '"+str(account)+"' limit 1"
    cursor.execute(sql)
    results = cursor.fetchall()   
    for row in results:
        id,api_key,secret_key = row.values()         
    print ('[+] api_key:',api_key)
    print ('[+] secret_key:',secret_key)

    client = ccxt.binance({'apiKey': api_key,'secret': secret_key,'enableRateLimit': True,'options': {'defaultType': 'future', },})
    answer = client.fetchPositions()
    answer = str(answer) 
    answer = answer.replace("True","'True'")
    answer = answer.replace("False","'False'")
        
    return answer

#########################################   BINANCE   ############################################

def binance_account (access_code,name_account,apiKey,secret,exchange,comment,kod_1C):  
    import iz_func  
    import json   
    answer = 'Нет данных'
    db,cursor = iz_func.connect ()   
    sql = "select id,name from cripta_account where kod_1C = '"+str(kod_1C)+"' "
    cursor.execute(sql)
    results = cursor.fetchall()    
    id = 0
    for row in results:
        id,name = row.values() 

    if id == 0:
        sql = "INSERT INTO cripta_account (`name`,`apiKey`,`secret`,`exchange`,`comment`,user_id,kod_1C,access_code) VALUES ('{}','{}','{}','{}','{}','','{}','{}')".format (name_account,apiKey,secret,exchange,comment,kod_1C,access_code)
        cursor.execute(sql)
        db.commit()
    else:   
        sql = "UPDATE cripta_account SET name = '"+name_account+"' WHERE `kod_1C` = '"+str(kod_1C)+"'"
        cursor.execute(sql)
        db.commit()        
        sql = "UPDATE cripta_account SET apiKey = '"+apiKey+"' WHERE `kod_1C` = '"+str(kod_1C)+"'"
        cursor.execute(sql)
        db.commit()        
        sql = "UPDATE cripta_account SET secret = '"+secret+"' WHERE `kod_1C` = '"+str(kod_1C)+"'"
        cursor.execute(sql)
        db.commit()        
    answer = str(results)
    db.close()
    return answer

def binance_pire (key):  
    import iz_func  
    import json   
    answer = 'Нет данных'
    db,cursor = iz_func.connect ()   
    sql = "select id,name,base,quote,status,price_min,amount_min,exchange from cripta_instrument where exchange = '"+str(key)+"' "
    cursor.execute(sql)
    results = cursor.fetchall()    
    answer = str(results)
    db.close()
    return answer

def binance_currency (key):  
    import iz_func  
    import json   
    list = []
    answer = 'Нет данных'
    db,cursor = iz_func.connect ()   
    sql = "select id,name,exchange from cripta_currency where exchange = '"+str(key)+"'"
    print ('[+] sql',sql)
    cursor.execute(sql)
    results = cursor.fetchall()    
    for row in results:
        id,name,exchange = row.values() 
        list.append ([id,name,exchange])
    answer = str(list)
    #print ('[+] answer:',answer)
    db.close()
    return answer

def binance_get_servertime ():
    from binance_f import RequestClient

    account = 'Администратор'
    api_key,secret_key = get_account (account)
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)

    result = request_client.get_servertime()
    answer = str(result)
    return  answer

def binance_balance (currency,account):  
    from binance.client import Client
    import iz_func  
    import json       
    import iz_func
    answer = 'Нет данных'
    #api_key    = ""
    #secret_key = ""
    #db,cursor = iz_func.connect ()
    #sql = "select id,apiKey,secret from cripta_account where name = '"+str(account)+"' limit 1"
    #cursor.execute(sql)
    #results = cursor.fetchall()   
    #for row in results:
    #    id,api_key,secret_key = row.values()         
    api_key,secret_key = get_account (account)
    client = Client(api_key, secret_key)
    balance = client.get_asset_balance(asset=currency)
    answer = balance
    return answer

def binance_orderbook ():
    #import iz_func  
    import json   
    answer = 'Нет данных'
    from binance.client import Client
    import iz_func
    #print(ccxt.__version__)
    api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    #wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG
    #uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc
    client = Client(api_key, secret_key)
    tickers = client.get_orderbook_tickers()
    answer = str(tickers)
    return answer

def binance_create_order ():
    answer = 'Нет данных'
    import json    
    from binance.client import Client
    api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    client = Client(api_key, secret_key)
    order = client.order_limit_buy(symbol='BTCUSDT',quantity=0.001,price='52585.60000000')
    #order = client.create_order(symbol='BTCUSDT',side='SIDE_BUY',type='ORDER_TYPE_LIMIT',timeInForce='TIME_IN_FORCE_GTC',quantity=0.001,price='52585.60000000')
    answer = str(order)
    return answer

def binance_get_open_orders ():
    answer = 'Нет данных'
    import json    
    from binance.client import Client
    api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    client = Client(api_key, secret_key)
    orders = client.get_open_orders(symbol='BTCUSDT')
    #order = client.order_limit_buy(symbol='BTCUSDT',quantity=0.001,price='52585.60000000')
    #order = client.create_order(symbol='BTCUSDT',side='SIDE_BUY',type='ORDER_TYPE_LIMIT',timeInForce='TIME_IN_FORCE_GTC',quantity=0.001,price='52585.60000000')
    answer = str(orders)
    answer = answer.replace("True","'True'") 
    return answer

def binance_get_order ():
    answer = 'Нет данных'
    import json    
    from binance.client import Client
    api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    client = Client(api_key, secret_key)
    orders = client.get_order(symbol='BTCUSDT',orderId='5321731787')
    #order = client.order_limit_buy(symbol='BTCUSDT',quantity=0.001,price='52585.60000000')
    #order = client.create_order(symbol='BTCUSDT',side='SIDE_BUY',type='ORDER_TYPE_LIMIT',timeInForce='TIME_IN_FORCE_GTC',quantity=0.001,price='52585.60000000')
    answer = str(orders)
    answer = answer.replace("True","'True'") 
    return answer

def binance_cancel_order (orderId):
    answer = 'Нет данных'
    import json    
    from binance.client import Client
    api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    client = Client(api_key, secret_key)
    result = client.cancel_order(symbol='BTCUSDT', orderId=orderId)
    #order = client.order_limit_buy(symbol='BTCUSDT',quantity=0.001,price='52585.60000000')
    #order = client.create_order(symbol='BTCUSDT',side='SIDE_BUY',type='ORDER_TYPE_LIMIT',timeInForce='TIME_IN_FORCE_GTC',quantity=0.001,price='52585.60000000')
    answer = str(result)
    answer = answer.replace("True","'True'") 
    return answer

def binance_get_open_margin_orders ():
    answer = 'Нет данных'
    import json    
    from binance.client import Client
    api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    client = Client(api_key, secret_key)
    #orders = client.get_open_orders(symbol='BTCUSDT')
    #order = client.order_limit_buy(symbol='BTCUSDT',quantity=0.001,price='52585.60000000')
    #order = client.create_order(symbol='BTCUSDT',side='SIDE_BUY',type='ORDER_TYPE_LIMIT',timeInForce='TIME_IN_FORCE_GTC',quantity=0.001,price='52585.60000000')
    orders = client.get_open_margin_orders(symbol='BNBBTC')
    answer = str(orders)
    answer = answer.replace("True","'True'") 
    return answer

def binance_get_all_margin_orders ():
    answer = 'Нет данных'
    import json    
    from binance.client import Client
    api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    client = Client(api_key, secret_key)
    #orders = client.get_open_orders(symbol='BTCUSDT')
    #order = client.order_limit_buy(symbol='BTCUSDT',quantity=0.001,price='52585.60000000')
    #order = client.create_order(symbol='BTCUSDT',side='SIDE_BUY',type='ORDER_TYPE_LIMIT',timeInForce='TIME_IN_FORCE_GTC',quantity=0.001,price='52585.60000000')
    orders = client.get_all_margin_orders(symbol='BNBBTC')
    answer = str(orders)
    answer = answer.replace("True","'True'") 
    return answer

def binance_get_isolated_margin_account (account):
    answer = 'Нет данных'
    import json    
    from binance.client import Client
    api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    client = Client(api_key, secret_key)
    #orders = client.get_open_orders(symbol='BTCUSDT')
    #order = client.order_limit_buy(symbol='BTCUSDT',quantity=0.001,price='52585.60000000')
    #order = client.create_order(symbol='BTCUSDT',side='SIDE_BUY',type='ORDER_TYPE_LIMIT',timeInForce='TIME_IN_FORCE_GTC',quantity=0.001,price='52585.60000000')
    info = client.get_isolated_margin_account()    
    answer = str(info)
    answer = answer.replace("True","'True'") 
    return answer

def binance_get_margin_price_index (account,pire):
    answer = 'Нет данных'
    import json    
    from binance.client import Client
    api_key    = "wAZOmPMC4CK2UvEhy2JzgpmQVFEP0Bzni8Dzy1WG0lfcty6WovNsBaxT38dYdXGG"
    secret_key = "uLdojYftkpJTN1Uj8FMsyWJu9cEiFFjw4wGG2AxvB0PvCAO9mdvJUy1Z1fAR4glc"
    client = Client(api_key, secret_key)
    #info = client.get_isolated_margin_account()    
    info = client.get_margin_price_index(symbol=pire)
    answer = str(info)
    answer = answer.replace("True","'True'") 
    return answer

#########################################   futures   ############################################

def binance_futures_get_position (account):
    from binance_f import RequestClient
    import json            
    answer = 'Нет данных'
    api_key,secret_key = get_account (account)
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)
    result = request_client.get_position()
    list = []
    for line in result:
        symbol      = str(line.symbol)
        leverage    = str(line.leverage)
        markPrice   = str(line.markPrice)
        positionAmt = str(line.positionAmt)
        unrealizedProfit = str(line.unrealizedProfit)
        list.append ([symbol,leverage,markPrice,positionAmt,unrealizedProfit]) 
    answer = str(list)
    answer = answer.replace("True","'True'") 
    return answer

def binance_futures_get_balance (account):
    from binance_f import RequestClient    
    import json    
    answer = 'Нет данных'
    api_key,secret_key = get_account (account)
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)
    result = request_client.get_balance()
    list = []
    for line in result:
        asset   = line.asset
        balance = line.balance    
        list.append ([asset,balance])         
    answer = str(list)
    answer = answer.replace("True","'True'") 
    return answer

def binance_futures_get_symbol_orderbook_ticker (account,symbol):
    answer = 'Нет данных'
    import json    
    from binance_f import RequestClient
    #api_key    = "ib3oiVLZhbsq2NwphEshEK3MRWuf8ImojIFdUUHe7VJxIXfZYJYLlCDtt2uiWTXO"
    #secret_key = "2HhyK5M1w0IhnHzHwxAgTNiaUqWiggNlIap6NUeQmQu57F1E8RRTC0WGUKHY3lD4"
    api_key,secret_key = get_account (account)
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)
    result = request_client.get_symbol_orderbook_ticker(symbol)
    list = []
    for line in result:
        print ('[+] line: {:10} {:10} {:10}'.format(line.symbol,line.bidPrice,line.askPrice))        
        symbol   = line.symbol
        bidPrice = line.bidPrice
        askPrice = line.askPrice
        list.append ([symbol,askPrice,bidPrice])         
    answer = str(list)
    answer = answer.replace("True","'True'") 
    return answer

def binance_futures_post_order (account,symbol,amount,price,side):
    from binance_f import RequestClient
    import json        
    answer = 'Нет данных'
    api_key,secret_key = get_account (account)
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)
    result = request_client.post_order(symbol=symbol, side=side, ordertype="LIMIT", quantity = amount,price=price,timeInForce='GTC')
    orderId  = result.orderId
    symbol   = result.symbol
    status   = result.status
    price   = result.price
    side    = result.side
    answer = str([symbol,orderId,status,price,side])
    answer = answer.replace("True","'True'") 
    return answer

def binance_futures_post_order_buy (account,symbol,amount,price,side):
    from binance_f import RequestClient
    import json
    try:        
        answer = 'Нет данных'
        api_key,secret_key = get_account (account)
        request_client = RequestClient(api_key=api_key, secret_key=secret_key)
        result = request_client.post_order(symbol=symbol, side=side, ordertype="LIMIT", quantity = amount,price=price,timeInForce='GTC')
        orderId  = result.orderId
        symbol   = result.symbol
        status   = result.status
        price   = result.price
        side    = result.side
        answer = str([symbol,orderId,status,price,side])
        answer = answer.replace("True","'True'") 
    except Exception as e: 
        print ('    [+] Вывод ошибки в ответ:',e)
        answer = [e]
    return answer

def binance_futures_post_order_sell (account,symbol,amount,price,side):
    from binance_f import RequestClient
    import json  
    try:        
        answer = 'Нет данных'
        api_key,secret_key = get_account (account)
        request_client = RequestClient(api_key=api_key, secret_key=secret_key)
        result = request_client.post_order(symbol=symbol, side=side, ordertype="LIMIT", quantity = amount,price=price,timeInForce='GTC')
        orderId  = result.orderId
        symbol   = result.symbol
        status   = result.status
        price   = result.price
        side    = result.side
        answer = str([symbol,orderId,status,price,side])
        answer = answer.replace("True","'True'") 
    except Exception as e: 
        print ('    [+] Вывод ошибки в ответ:',e)
        answer = [e]        
    return answer    

def binance_futures_post_order (account,symbol,amount,price,side):
    from binance_f import RequestClient
    import json        
    answer = 'Нет данных'
    api_key,secret_key = get_account (account)
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)
    result = request_client.post_order(symbol=symbol, side=side, ordertype="LIMIT", quantity = amount,price=price,timeInForce='GTC')
    orderId  = result.orderId
    symbol   = result.symbol
    status   = result.status
    price   = result.price
    side    = result.side
    answer = str([symbol,orderId,status,price,side])
    answer = answer.replace("True","'True'") 
    return answer    

def binance_futures_post_stoploss_order (account,symbol,price,side):
    answer = 'Нет данных'
    import json    
    from binance_f import RequestClient
    api_key,secret_key = get_account (account)
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)
    result = request_client.post_order(symbol=symbol, side=side, ordertype='STOP_MARKET', stopPrice=price, closePosition=True)

    orderId  = result.orderId
    symbol   = result.symbol
    status   = result.status
    price    = result.price
    side     = result.side
    answer   = str([symbol,orderId,status,price,side])
    answer   = answer.replace("True","'True'") 
    return answer

def binance_futures_get_open_orders (account,symbol):
    from binance_f import RequestClient    
    import json    
    answer = 'Нет данных'
    api_key,secret_key = get_account (account)    
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)
    result = request_client.get_open_orders(symbol=symbol)
    list = []
    for line in result:
         symbol  = line.symbol
         orderId = line.orderId
         status  = line.status
         price   = line.price
         side    = line.side
         list.append ([symbol,orderId,status,price,side]) 
    answer = str(list)
    answer = answer.replace("True","'True'") 
    return answer

def binance_futures_cancel_order (account,symbol,orderId):
    from binance_f import RequestClient    
    import json    
    answer = 'Нет данных'
    api_key,secret_key = get_account (account)  
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)
    result = request_client.cancel_order(symbol=symbol, orderId=orderId)
    orderId  = result.orderId
    symbol   = result.symbol
    status   = result.status
    price   = result.price
    side    = result.side
    answer = str([symbol,orderId,status,price,side])
    answer = answer.replace("True","'True'") 
    return answer

def binance_futures_get_candlestick_data (account,symbol,koll,timeF):
    from binance_f import RequestClient    
    import json    
    answer = 'Нет данных'
    api_key,secret_key = get_account (account)  
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)
    #timeF  = '30m'  
    symbol = symbol
    result = request_client.get_candlestick_data(symbol=symbol, interval=timeF,startTime=None, endTime=None, limit=koll)
    candels = []
    for line in result:                
        open  = line.open
        high  = line.high
        low   = line.low
        close = line.close
        closeTime = line.closeTime
        candel = [open,high,low,close,closeTime]
        candels.append(candel)    
    answer = candels
    return answer

def binance_futures_change_initial_leverage (account,symbol,leverage1):
    from binance_f import RequestClient    
    import json    
    answer = 'Нет данных'
    api_key,secret_key = get_account (account)  
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)
    result = request_client.change_initial_leverage(symbol=symbol, leverage=leverage1)
    symbol    = result.symbol
    leverage  = result.leverage
    answer = [symbol,leverage]
    return answer

def binance_futures_get_order (account,symbol,orderId):
    from binance_f import RequestClient    
    import json    
    answer = 'Нет данных'
    api_key,secret_key = get_account (account)  
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)
    list = []
    #timeF  = '30m'  
    #symbol = symbol
    #result = request_client.get_candlestick_data(symbol=symbol, interval=timeF,startTime=None, endTime=None, limit=koll)
    result = request_client.get_order(symbol=symbol, orderId=orderId)    
    status  = result.status
    price   = result.price
    order = [status,price]
    list.append(order)
    answer = str(list)
    print ('[+] answer:',answer)
    return answer

def binance_futures_get_recent_trades_list (symbol,limit):
    from binance_f import RequestClient

    account = 'Администратор'
    api_key,secret_key = get_account (account)
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)

    result = request_client.get_recent_trades_list(symbol=symbol, limit=limit)

    list = []
    for line in result:
        price = line.price
        isBuyerMaker = str(line.isBuyerMaker)
        time = line.time
        list.append([price,isBuyerMaker,time])

    answer = str(list)
    return  answer

def binance_futures_get_aggregate_trades_list (symbol,limit):
    from binance_f import RequestClient

    account = 'Администратор'
    api_key,secret_key = get_account (account)
    request_client = RequestClient(api_key=api_key, secret_key=secret_key)

    result = request_client.get_aggregate_trades_list(symbol=symbol, limit=limit)

    list = []
    for line in result:
        price = line.price
        isBuyerMaker = str(line.isBuyerMaker)
        time = line.time
        list.append([price,isBuyerMaker,time])

    answer = str(list)
    return  answer

