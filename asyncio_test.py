# 덧셈함수 비동기처리
# await 로 코루틴 실행하기
# await 는 코루틴 안에서만 실행한다.

import asyncio 

async def add(a, b):
    print("add: {0} + {1}". format(a, b))
    await asyncio.sleep(1)  # 1초 대기 asyncio.sleep()도 코루틴
    return a + b  # 더한 결과를 반환한다.

async def print_add(a, b):
    result = await add(a, b)  # await 로 다른 코루틴을 실행하고 반환값을 변수 result 에 저장
    print('print_add: {0} + {1} = {2}'.format(a, b, result))

loop = asyncio.get_event_loop()  # 이벤트 루프를 얻음
loop.run_until_complete(print_add(1, 2))  # print_add()가 끝날 때 까지 이벤트루프를 실행
loop.close()  # 이벤트루프를 닫음