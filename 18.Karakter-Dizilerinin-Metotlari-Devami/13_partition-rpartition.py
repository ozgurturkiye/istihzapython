## partition(), rpartition()


## partition() - ornek_1
a = "İstanbul"
print(a.partition("a"))     ## output: ('İst','a','nbul')
print(20*'*')
print(a.partition("an"))    ## output: ('İst','an','bul')
print(20*'*')
print(a.partition("tan"))   ## output: ('İs','tan','bul')
print(20*'*')
print(a.partition("k"))     ## output: ('İstanbul','','')
print(20*'*')
print(20*'*')

## partition() - ornek_2
a = "istihza"
print(a.partition("ist"))   ## output: ('','ist','ihza')
print(20*'*')
print(a.partition("i"))     ## output: ('','i','stihza')
print(20*'*')
print(a.rpartition("i"))    ## output: ('ist','i','hza')
print(20*'*')
print(a.partition("k"))     ## output: ('istihza','','')
print(20*'*')
print(a.rpartition("k"))    ## output: ('','','istihza')
print(20*'*')
