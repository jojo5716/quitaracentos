# Còmo quitar acentos con python

```python
# -*- coding: utf-8 -*-
from unicodedata import normalize

def quitarAcentos(texto):
    return normalize('NFKD', texto.decode("utf-8")).encode('ASCII','ignore')

[1] print quitarAcentos("Avión")
# Avion
[2] print quitarAcentos("Niño") 
# Nino
```




