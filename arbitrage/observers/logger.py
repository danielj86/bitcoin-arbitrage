import logging
import http.client
import config
import json
from .observer import Observer

class Logger(Observer):
    def opportunity(self, profit, volume, buyprice, kask, sellprice, kbid, perc,
                    weighted_buyprice, weighted_sellprice):
        params = {'profit': profit, 'volume': volume, 'buyprice' : buyprice, 'kask' : kask, 'sellprice' : sellprice, 'kbid' : kbid, 'perc' : perc  }
        json_dump = json.dumps(params)
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection(config.posterhost)
        conn.request("POST", config.posterurl, json_dump, headers)
        response = conn.getresponse()
        data = response.read().decode()
        logging.warn("data")
        logging.warn(data)
        conn.close()			
        logging.info("profit: %f USD with volume: %f BTC - buy at %.4f (%s) sell at %.4f (%s) ~%.2f%%" % (profit, volume, buyprice, kask, sellprice, kbid, perc))

		
		