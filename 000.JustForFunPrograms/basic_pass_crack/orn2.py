import zipfile

def main():
    """ Sayisal sirali denemesi"""
    zipfilename = '6c.zip'

    sonuc = 0
    password = None
    zip_file = zipfile.ZipFile(zipfilename)

    for i in range(5000000):
        password = str(i)
        print(i)
        try:
            zip_file.extractall(pwd=password)
            sonuc = 'Parola Bulundu: %s' % password
            break
        except:
            pass
    print(sonuc)

if __name__ == '__main__':
    main()
