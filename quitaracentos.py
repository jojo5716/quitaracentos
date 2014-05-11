# -*- coding: utf-8 -*-
from unicodedata import normalize

def quitarAcentos(texto):
    return normalize('NFKD', texto.decode("utf-8")).encode('ASCII','ignore')

print quitarAcentos("Avión")
print quitarAcentos("Niño")
