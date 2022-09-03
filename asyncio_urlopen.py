# 비동기로 웹페이지 가져오기 
# asyncio를 이용해서 비동기로 웹페이지를 가져온다.

from time import time 
from urllib.request import Request, urlopen 
import asyncio

urls = ['https://www.google.co.kr/search?q=' +i 
        for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry'] ]

async def fetch(url):
    request = Request(url, headers={'User-Agent':'Mozilla/5.0'})  # UA가 없으면 에러 403발생
    response = await loop.run_in_executor(None, urlopen, request)
    page = await loop.run_in_executor(None, response.read)
    return len(page)

async def main():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]  # 태스크(퓨처)객체를 리스트로 만듬
    result = await asyncio.gather(*futures)  # 결과를 한꺼번에 가져옴
    print(result)

begin = time()
loop = asyncio.get_event_loop()  # 이벤트루프를 얻음
loop.run_until_complete(main())  # main이 끝날때까지 기다림
loop.close()  # 이벤트 루프를 닫음
end = time()

print('실행시간: {0:.3f}'.format(end - begin))
