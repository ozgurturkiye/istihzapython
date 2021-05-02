# This is dictionary dict module to add eng-tur word


sozluk = {} # This is main dictionary
sozluk["example"] = "Örnek"
def add_word(eng, tur):
  # weng: word english , ktur: kelime Türkçe
  """Add key value pair to dictionary key is eng, value is tur."""
  if eng == "" or tur == "":
    raise ValueError("key and value can not be empty")
  if not eng:
    raise ValueError("key can not be empty")
  if not tur:
    raise ValueError("value can not be empty")

  sozluk[eng] = tur
  return sozluk


# bro ayrı ayrı yazdım testleri kolay olsun diye
# test_key_is_empty

# geçti bro testler
# nası 1 failure 3 error yazıyor bende
