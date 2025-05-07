from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def DEVANAGARI_to_SLP1(text):
    return transliterate(text, sanscript.DEVANAGARI, sanscript.SLP1)

def ITRANS_to_DEVANAGARI(text):
    return transliterate(text, sanscript.ITRANS, sanscript.DEVANAGARI)