import concurrent.futures
import time

def sleep_for_a_bit(seconds):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return 'Done sleeping'


with concurrent.futures.ProcessPoolExecutor() as executor:
    if __name__ == '__main__':
        f1 = executor.submit(sleep_for_a_bit, 1)
        f2 = executor.submit(sleep_for_a_bit, 1)
        print(f1.result())
        print(f2.result())


        
finish = time.perf_counter()
print('Finished in time: ', finish)
