n = 81**18 - ( (( (81**8) - 1 )*( ((8+1)**8)+1 ))/8 ) - 8
s = ''
while n:
    s += str(int(n%3))
    n //= 3
print(s.count('1'))
    
