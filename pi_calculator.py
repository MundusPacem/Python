

n     = 1
p     = 0
count = 0

while p <= 3.14:

    i = (1.0/n)-(1.0/(n+2))
    n += 4
    p += i
    count += 1

ans = p*4

print "\n\tPI is %.2f after %d iterations." % (ans, count)
