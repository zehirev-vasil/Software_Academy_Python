def count_primes(num):
    tmp_num = 2

    while tmp_num <= 10:

        count_divisibility = 0

        for i in range(2, num):
            if tmp_num % i == 0:
                count_divisibility += 1
            else:
                continue

        if count_divisibility > 1:
            print(f'The number {tmp_num} is NOT prime!')

        tmp_num += 1


count_primes(10)
