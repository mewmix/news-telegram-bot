import requests
import json
import time

from gnews import GNews

import os
search1 = 'Ukraine'

search2 = 'Russia'

google_news = GNews(language='en', country='US', period='1h', max_results=5, exclude_websites=['yahoo.com', 'cnn.com'])
news1 = google_news.get_news(search1)
news2 =  google_news.get_news(search2)


pretty_bn = json.dumps(news1, indent = 4)

pretty_gn = json.dumps(news2, indent = 4)

gn_len = len(pretty_gn)

int_gn = int(gn_len)


i = 5
i1 = int_gn


bn_len = len(pretty_bn)

int_bn = int(bn_len)

j = int_gn

print(int_gn)

json_dict1 = json.loads(pretty_gn)
json_dict2 = json.loads(pretty_bn)



while True:


  def send_msg(text):
     token = ""
     chat_id = ""
     url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
     results = requests.get(url_req)
     print(results.json())

  send_msg(f"Here are the top 5 results for {search1}!")   

  for i in json_dict1:


         send_msg(f"{i}")
         time.sleep(5)    

  send_msg(f"Here are the top 5 results for {search2}!")

  for i in json_dict2:

   slp = 1 
   send_msg(f"{i}")
   time.sleep(5)

  break
send_msg(f"Sleeping for {slp} hours")
time.sleep(60 * 60 * slp)

