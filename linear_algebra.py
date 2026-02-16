def addvectors(a,b):
    assert len(a)==len(b)
    return[a[i]+b[i] for i in range (len(a))]

a=[1,3,4]
b=[2,6,3]

print(addvectors(a,b))