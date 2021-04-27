def shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print('Too few.')

    elif num_cycles > 4:
        print('Too many.')
    else:
        N = 1;
        for N in range(N, num_cycles+1):
            print(N , ": Lather and rinse.")
        print('Done.')
user_cycles = int(input())
shampoo_instructions(user_cycles)
