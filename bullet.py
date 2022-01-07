  
import requests

class Bullet:
       
 def __init__(self,string_to_send):

    token = "2054727581:AAH_RVxNd7F2fxCpxGbS7gw6CPp23ED-9YE"
    chat_id = "1761157621"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text="+string_to_send 
    #url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=bau bau" 
    results = requests.get(url_req)
    print(results.json())

