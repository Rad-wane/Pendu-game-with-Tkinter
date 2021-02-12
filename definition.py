import re
from urllib.request import urlopen
def find(x):
    srch=str(x)
    word = x
    url = "http://dictionary.reference.com/browse/"+srch+"?s=t"
    x=urlopen(url)
    x=x.read()
    
    items=re.findall(b'<meta name="description" content="'+b".*$",x,re.MULTILINE)
    for x in items:
        y=x.replace(b'<meta name="description" content="',b'')
        z=y.replace(b' See more."/>',b'')
        m=re.findall(b'at Dictionary.com, a free online dictionary with pronunciation, synonyms and translation. Look it up now! "/>',z)
        if m==[]:
            if z.startswith(b"Get your reference question answered by Ask.com"):
                return False
            else:
                remo1 = len(word) + len(' definition, ') 
                remo2 = -len(' See more."/>')

                return (z[remo1:remo2].decode("utf-8") )
    else:
            return False
