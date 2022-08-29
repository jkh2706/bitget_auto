# 웹소켓 공부
import asyncio  # 비동기 작업 처리 모듈

async def make_Americano():
    print("Americano Starts!")
    await asyncio.sleep(3)  # CPU를 점유하지 않고 3초를 기다린다.
    print("Americano Ends!")
    return "Americano"

async def make_latte():
    print("Latte Starts!")
    await asyncio.sleep(5)  # asyncio.sleep()도 코루틴이고 코루틴 안에서 코루틴을 사용하려면 await 를 붙인다.
    print("Latte Ends!")
    return "Latte"

async def main(): # 두 코루틴을 동시에 실행하는 코루틴을 만든다. 비동기방식에서의 함수를 코루틴이라 부른다.
    col_1 = make_Americano()  # 첫번째 코루틴 객체를 생성한다.
    col_2 = make_latte()  # 두번째 코루틴 객체를 생성한다.

    # 두개의 코루틴을 합친다.
    result = await asyncio.gather(
        col_1,
        col_2
    )
    print(result)

# 이벤트 루프 생성 및 실행 후 루프를  종료한다.
print("Main Starts!")
print("\n")
asyncio.run(main())  # run()함수는 이벤트루프를 생성 및 실행 종료까지 한번에 해준다.
print("\n")
print("Main Ends!")