from concurrent.futures import ThreadPoolExecutor
import time


def study(fname, lname):
    for i in range(10):
        print(f'{fname} {lname} is Studying {i}')
        time.sleep(1)


'''
description: 
param {*} fname
param {*} lname
return {*}
'''
def listen_to_music(fname, lname):
    for i in range(10):
        print(f'{fname} {lname} is Listening to music {i}')
        time.sleep(1)


if __name__ == '__main__':
    arguments = ['A', 'B']
    arguments2 = [['A', 'B'], ['C', 'D']]
    with ThreadPoolExecutor(max_workers=2) as executor:
        # executor.submit(study, *arguments)
        # executor.submit(listen_to_music, 'A', 'B')
        # executor.map(study, arguments, arguments)
        executor.map(listen_to_music, *arguments2)


