# 비동기로 웹페이지 가져오기
# ayncio를 사용하여 비동기로 웹페이지를 가져와보자

# 1. asyncio를 사용하지 않고 웹페이지를 순차적으로 가져와보자
# 2. urllib.request의 urlopen으로 웹페이지를 가져온뒤 웹페이지의 길이를 출력해본다.

from time import time
from urllib.request import Request, urlopen

urls = ['https://www.google.co.kr/search?q=' +i 
        for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry'] ]

begin = time()
result = []
for url in urls:
    request = Request(url, headers={'User-Agent':'Mozilla/5.0'})  # UA가 없으면 에러 403발생
    response = urlopen(request)
    page = response.read()
    result.append(len(page))

print(result)
end =time()
print('실행시간 : {0:.3f}초'.format(end - begin))