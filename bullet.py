  
import requests

class Bullet:
       
 def __init__(self,string_to_send):

    token = "insert your token"
    chat_id = "insert your chat id"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text="+string_to_send 
    #url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=bau bau" 
    results = requests.get(url_req)
    print(results.json())

