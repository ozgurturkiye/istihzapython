#Sözlük içinde sözlük tanımlama

kişiler = {"Ahmet Özkoparan": {"Memleket": "İstanbul",
                               "Meslek"  : "Öğretmen",
                               "Yaş"     : 34},

           "Mehmet Yağız"   : {"Memleket": "Adana",
                               "Meslek"  : "Mühendis",
                               "Yaş"     : 40},

           "Seda Bayrak"    : {"Memleket": "İskenderun",
                               "Meslek"  : "Doktor",
                               "Yaş"     : 30}}
                               

okul =  {"Kadı Mehmet": {
          "6a": {
            "mehmet": {
              "Fen": {
                "1. Yazılı": "85"
              }
            }
          }
        },
        "Cezayirli": {},
        "Piri Paşa":{},
}

print(okul["Kadı Mehmet"]["6a"]["mehmet"]["Fen"]["1. Yazılı"])
print(okul["Kadı Mehmet"]["6a"]["mehmet"]["Fen"])
print(okul["Kadı Mehmet"]["6a"]["mehmet"])
print(okul["Kadı Mehmet"]["6a"])
print(okul["Kadı Mehmet"])
print(okul)
