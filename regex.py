import re

url = 'https://helion.pl/ksiazki/testowanie-kodu-z-react-testing-library-jak-tworzyc-testy-ktore-beda-proste-w-utrzymaniu-i-modyfik-scottie-crump,bibrea.htm#format/d'
ejnoo = re.findall(r'[^,]+,([^\.]+)\.htm',url)

print(ejnoo[0])