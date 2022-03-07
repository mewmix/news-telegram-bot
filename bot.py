import requests
import json
import time

from gnews import GNews

search1 = "Ukraine"

search2 = "Hack" 

while True:

 google_news = GNews(language='en', country='US', period='1h', max_results=5, exclude_websites=['yahoo.com', 'cnn.com'])
 news1 = google_news.get_news(search1)
 news2 =  google_news.get_news(search2)
 token = "" 
 chat_id = ""
 

 pretty_bn = json.dumps(news1, indent = 4)

 pretty_gn = json.dumps(news2, indent = 4)

 json_dict1 = json.loads(pretty_bn)
 json_dict2 = json.loads(pretty_gn)





 def send_msg(text):
    token 
    chat_id 
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())

 send_msg(f"Here are the top 5 results for {search1}!")   

 for i in json_dict1:


        send_msg(f"{i}")
        time.sleep(5)    

 send_msg(f"Here are the top 5 results for {search2}!")

 for i in json_dict2:

  slp = 2
  hour = 1
  send_msg(f"{i}")
  time.sleep(5)

  
 if slp > hour:
  send_msg(f"Sleeping for {slp} hours")
  time.sleep(60 * 60 * slp)
 else:
  send_msg(f"Sleeping for {slp} hour")
  time.sleep(60 * 60 * slp)

