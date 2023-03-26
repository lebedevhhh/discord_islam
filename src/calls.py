import requests
import json
import random
from random import random

URL=' http://api.alquran.cloud/v1/ayah/'
TOTAL_VERSE=6236

class Test:
    def test(self):
        print(make_random_ayah_request("en"))
        print(make_random_ayah_request("ar"))
        


def make_random_ayah_request(version):
    if (version=="en"):
        print("english version")
        random_ayah=random() * TOTAL_VERSE
        new_url=f"{URL}{random_ayah}/en.asad"
        json_response= json.loads(requests.get(new_url).text)
        return json_response

    elif (version=="ar"):
        print("arabic version")
        random_ayah=random() * TOTAL_VERSE
        new_url=f"{URL}{random_ayah}"
        json_response= json.loads(requests.get(new_url).text)
        return json_response


if __name__=="__main__":
    t=Test()
    t.test()