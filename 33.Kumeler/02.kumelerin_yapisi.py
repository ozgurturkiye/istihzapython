## Kümelerin Yapısı

meyveler_listesi = ["elma", "armut", "kiraz", "üzüm",
                    "kiraz", "üzüm", "armut", "kiraz",
                    "kiraz", "üzüm", "armut", "erik",
                    "şeftali", "kayısı", "çilek", "üzüm",
                    "kavun", "karpuz", "şeftali", "kayısı"]

meyveler_kumesi = set(meyveler_listesi)
print(meyveler_kumesi)

for i in set(meyveler_listesi):
    print("{} listede {} kez geçiyor".format(i, meyveler_listesi.count(i)))
