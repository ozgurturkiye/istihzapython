## Kümelerin Metotları

## union() - birleşim -

k1 = set([1, 2, 3, 4])
k2 = set([1, 3, 5, 7])
print(k1.union(k2))         ## output: {1, 2, 3, 4, 5, 7}
print(k1|k2)                ## output: {1, 2, 3, 4, 5, 7}

print("----------------")
## update()

kume_1   = set([1, 3, 6, 8])
meyveler = ["elma","armut","üzüm"]

kume_1.update(meyveler)
print(kume_1)

print("----------------")
## symmetric_difference()

a = set([1, 2, 5])
b = set([1, 4, 5])

print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))

print("----------------")
## pop() - rastgele öğe siler.

k3 = (k1|k2)

print(k3)
k3.pop()
print(k3)
k3.pop()
print(k3)
