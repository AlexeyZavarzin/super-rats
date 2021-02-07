import time

from super_rats import main

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f'\nВремя выполнения программы {duration} секунд')
