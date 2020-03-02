https://www.spoj.com/problems/PRIME1/

sieve = [True] * (int(1000000000**.5) + 7)
sieve[0] = False
sieve[1] = False
for i, is_prime in enumerate(sieve):
    if is_prime:
        sieve[i*i::i] = [False] * len(xrange(i*i, len(sieve), i))
primes = [i for i, is_prime in enumerate(sieve) if is_prime]

for _ in xrange(int(raw_input())):
    a, b = map(int, raw_input().split())
    if a < 2:
        a = 2
    local_sieve = [True] * (b - a + 7)
    for p in primes:
        start = max(p*p, p*int(math.ceil((a * 1.0)/p)))
        local_sieve[start - a::p] = [False] * len(xrange(start, len(local_sieve) + a, p))
    for i, is_prime in enumerate(local_sieve):
        if is_prime and a + i <= b:
            print a + i
    print
