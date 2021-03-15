import requests
import re, time, sys

def gRab():
    xx = open("dir.txt").read().splitlines()
    for xs in xx:
        for page in range(1,101):
            headers = {
                'authority': 'www.aihitdata.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '^\\^Google',
                'sec-ch-ua-mobile': '?0',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://www.aihitdata.com/directory/companies',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8',
                'cookie': 'gadsTest=test; _ga=GA1.2.337006503.1615004085; __gads=ID=2d205cdca8deaf65-2261bfa844c600d6:T=1615004084:RT=1615004084:S=ALNI_MbefgVsIcFoLXesOZSBZfVQwRj83A; cookieconsent_dismissed=yes; _gid=GA1.2.629638151.1615776435; gadsTest=test; remember_token=120003^|3a50c91e9d54a60b3b4a8064ee1bd18c8f9251bd479c2a6fa428c22f734a74a7ce564c05815e5e09becb2baa14e64fa467559c981280f7d3585e74d240f0bd1b; _gat_gtag_UA_10576731_7=1; session=.eJx9kE-LwjAQxb9KydlDEi1CwYNLWqkwKZXUMr3I_qm2E6vQKtWI332D7O5xD29gmN97MO_Bdvu-HhoWXfprPWG79otFDxZ8sIih0Q2UOGZlHEKXu8xs2kwlpCnlWm1afxPYbVtt_C5TWan4Xq1irl1CoA4SzJbQFA6pGGG1teCKqS69ulwApRJUztEdnDaF1GV19N4Qu7UFpb0Siw5HpPRWdRtb0VunKZ5lprFaxiOUxUy73GlCDnRYsOeEfQ79fnc52_r094KWFYEsOLi3Y6bsDQnvKJMGTCq8fQomFrpcW5Q-jpaeqyhbLl5xw08VfjI4nyaBCAN47wPJpQi4jMIwkvNgBeYFX4b_4Xkk-C98Her-VTQTknM-Zc9vTzZ2gw.EzBehg.jat7SGPx7HhUuEwo4zjZzAOaJEQ',
            }

            params = (
                ('i', xs),
                ('p', page)
            )

            response = requests.get('https://www.aihitdata.com/search/companies', headers=headers, params=params)
            if 'text-success' in response.text:
                sites = re.findall(r'<span class="text-success">(.*?)</span>', response.text)
                for x in sites:
                    print ("\033[1;32;40m[DONE] \033[0m\033[1;31;40m"+ x +"\033[0m")
                    save = open('domengrab.txt', 'a')
                    save.write(str(x)+'\n')
                    save.close()     


gRab()
