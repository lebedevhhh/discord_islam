from calls import make_random_ayah_request, make_random_hadith_request

class Test:
    def test(self):
        print(make_random_ayah_request("en"))
        # print(make_random_ayah_request("ar"))
        # print(get_hadith())
    
if __name__=="__main__":
    t=Test()
    t.test()