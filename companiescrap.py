import requests
import re, time, sys

def gRab():
    xx = open("dir.txt").read().splitlines()
    for xs in xx:
        for page in range(1,101):
            

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
