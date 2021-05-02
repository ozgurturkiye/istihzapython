import zipfile

def main():
    """	Zipfile password cracker using a brute-force dictionary attack"""
    zipfilename = '6c.zip'
    dictionary = 'words.txt'
    sonuc = 0
    password = None
    zip_file = zipfile.ZipFile(zipfilename)
    with open(dictionary, 'r') as f:
        for line in f.readlines():
            password = line.strip('\n')
            print(password)
            try:
                zip_file.extractall(pwd=password)
                sonuc = 'Password found: %s' % password
                break
            except:
                pass
    print(sonuc)

if __name__ == '__main__':
    main()
