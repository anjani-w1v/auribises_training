import json
order = {
    'oid': 1

}

import requests
import json
api_key=''
newsapi_url='' 
response=requests.get(newsapi_url)
news_json=response.text
news_dictionary=json.loads(news_json)
