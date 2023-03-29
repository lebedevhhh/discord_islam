import requests
import json
import random
import os
from dotenv import load_dotenv
from random import random

load_dotenv()
URL_Surah='http://api.alquran.cloud/v1/ayah/'
TOTAL_VERSE=6236
MAX_HADITH=7000
API_KEY=os.getenv('API_KEY')
Default_Pagination=1
dict_author={
    1: "sahih-bukhari",
    2: "sahih-muslim"
}




def make_random_ayah_request(version):
    if (version=="en"):
        random_ayah=int(random() * TOTAL_VERSE)
        new_url=f"{URL_Surah}{random_ayah}/en.asad"
        json_response= json.loads(requests.get(new_url).text)
        return json_response

    elif (version=="ar"):
        random_ayah=random() * TOTAL_VERSE
        new_url=f"{URL_Surah}{random_ayah}"
        json_response= json.loads(requests.get(new_url).text)
        return json_response

def make_random_hadith_request():
    rdm_hadith = int(random() * MAX_HADITH)
    rdm_idx_for_book=int(random() * 2)
    URL_Hadith=f'https://www.hadithapi.com/api/hadiths?apiKey={API_KEY}&hadithNumber={rdm_hadith}&paginate={Default_Pagination}&book={dict_author[1]}'
    content=requests.get(URL_Hadith).text
    json_response=json.loads(content)
    return json_response['hadiths']['data'][0]
