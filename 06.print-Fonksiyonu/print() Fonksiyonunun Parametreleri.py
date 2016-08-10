#Print fonksiyonun print() Fonksiyonunun Parametreleri
# sep
# end
# file
# flush
# Yıldızlı parametreler

print("Tahir olmak da ayıp değil", "Zühre olmak da", sep=" ", end="\n", file=sys.stdout, flush=True)

print(*"Linux", sep=".")    # output: L.i.n.u.x
print(*"Beşiktaş")          # output: B e ş i k t a ş
print(*"Beşiktaş", sep="-") # output: B-e-ş-i-k-t-a-ş

#ASCII karakter tablosunu yazdıran program örneği

for i in range(128):
    if i % 4 == 0:
        print("\n")

    print("{:<3}{:>8}\t".format(i, repr(chr(i))), sep="", end="")
