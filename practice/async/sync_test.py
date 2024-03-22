import time

def write():
    print("Hey")
    time.sleep(1)
    print("there")

def main():
    for _ in range(3):
        write()

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"File executed in {elapsed:0.2f} seconds")