import logging
import http.client
import config
import json
from .observer import Observer

class httpPoster(Observer):
    def opportunity(self, profit, volume, buyprice, kask, sellprice, kbid, perc,
                    weighted_buyprice, weighted_sellprice):
        params = {'profit': profit, 'volume': volume, 'buyprice' : buyprice, 'kask' : kask, 'sellprice' : sellprice, 'kbid' : kbid, 'perc' : perc, 'weighted_buyprice' : weighted_buyprice, 'weighted_sellprice' : weighted_sellprice  }
        json_dump = json.dumps(params)
        headers = {"Content-type": "application/json","Accept": "application/json"}
        conn = http.client.HTTPConnection(config.posterhost)
        conn.request("POST", config.posterurl, json_dump, headers)
        response = conn.getresponse()
        data = response.read().decode()
        logging.warn("[HTTP Observer] - posted data to %s" % config.posterhost)
        logging.warn(data)
        conn.close()			
        

		
		