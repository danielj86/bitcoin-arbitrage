import logging
import httplib
import urllib
import config
from .observer import Observer


class Logger(Observer):
    def opportunity(self, profit, volume, buyprice, kask, sellprice, kbid, perc,
                    weighted_buyprice, weighted_sellprice):
        params = {'message': message}
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("jany.co.il:80")
        conn.request("POST", "/contact", params, headers)
        response = conn.getresponse()
        data = response.read()
        logging.warn("data")
        logging.warn(data)
        conn.close()			
        logging.info("profit: %f USD with volume: %f BTC - buy at %.4f (%s) sell at %.4f (%s) ~%.2f%%" % (profit, volume, buyprice, kask, sellprice, kbid, perc))
