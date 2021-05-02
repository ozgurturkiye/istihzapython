# text
import unittest
from dictionary import add_word


class TestDictionaryAdd(unittest.TestCase):
  def test_add(self):
    """Test adding key value pairs"""
    sozluk = add_word("key", "value")
    self.assertEqual(sozluk["key"], "value")

  def test_key_is_empty(self):
    """Test for empty key or value."""
    self.assertRaises(ValueError, add_word, "", "kedi")

  def test_value_is_empty(self):
    """Test for empty key or value."""
    self.assertRaises(ValueError, add_word, "cat", "")

  def test_key_value_is_empty(self):
    """Test for empty key or value."""
    self.assertRaises(ValueError, add_word, "", "")

  def test_key_with_empty_value(self):
    # check that add_word("", "value") fails when key is empty string
    with self.assertRaises(ValueError):
      add_word("", "value")


# Bro mola çalıştı play station oynamaya gideceğiz


# bro şuan boş ekliyor harbiden :)
# men et bro ekleyemesin pwenk
# Bro şuan ekler testi geçemiyor ama kodu düzelteceğiz işte

# Bro assertEqual(a, b) a ve b eşit olmalı diyor.
# testten geçti
# ne yazıyorduk shell e python -m unittest
# tmm testten geçiyorda yani neye göre eşit
# sozluk["key"]  bize "value" değerini dondurur
# sozluk["key"] == "value" true vermeli diyor
# tam bir bilinmezliğin ortasındayım :)
# şimdi hatırladın işte :)
# şimdi boş olmamalı onu test edelim eğer key veya value "" ise testi geçemesin
# yaz bro izliorm :) ok



# https://docs.python.org/3/library/unittest.html
# Yukarıda genel test durumlarını vermiş
