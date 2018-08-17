#vill fråga efter en siffra i fib-talföljd och finna platsen den finns på

#fibtal = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

n = int(input("Which fibonacci number do you want to find? "))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

ber_fib = fib(n)

print(ber_fib)

