import asyncio

async def write():
    print("Hey")
    await asyncio.sleep(1)
    print("there")

async def main():
    await asyncio.gather(write(), write(), write())

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"File executed in {elapsed:0.2f} seconds")