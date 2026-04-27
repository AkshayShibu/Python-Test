a={1,2,34,7}
b={42,12,7,18}

# union- 2 ways 
print(a|b)
print(a.union(b))

# inytersection 2 ways
print(a&b)
print(a.intersection(b))

# diffrence
print(a-b)
print(a.difference(b))
print(b-a)
print(b.difference(a))

#symentric diff
print(a^b)
print(a.symmetric_difference(b))