# pip install aksharamukha indic-transliteration epitran pandas

import pandas as pd
import epitran

# Method 1: Aksharamukha
from aksharamukha import transliterate as akshara_trans

# Method 2: indic-transliteration
from indic_transliteration.sanscript import transliterate as indic_trans
from indic_transliteration.sanscript import HK, DEVANAGARI

# IPA converter
epi = epitran.Epitran('hin-Deva')


# ---------- Transliteration Functions ----------

def aksharamukha_deva(word):
    try:
        return akshara_trans.process("ISO", "Devanagari", word)
    except:
        return "ERROR"

def indic_deva(word):
    try:
        return indic_trans(word, HK, DEVANAGARI)
    except:
        return "ERROR"

def to_ipa(deva_word):
    try:
        return epi.transliterate(deva_word)
    except:
        return "ERROR"


# ---------- Your word list ----------
animals = [
    "kutta",
    "billi",
    "gai",
    "ghoda",
    "bakri",
    "sher",
    "hathi",
    "bandar",
    "machli",
    "oont",
    "gadha",
    "lomdi",
    "bhalu",
    "murga",
    "tota",
    "chuha",
    "mendak",
    "saanp",
    "mor",
    "kabootar"
]



# ---------- Build comparison table ----------
rows = []

for w in animals:
    deva_ak = aksharamukha_deva(w)
    deva_ind = indic_deva(w)

    ipa_ak = to_ipa(deva_ak) if deva_ak != "ERROR" else "ERROR"
    ipa_ind = to_ipa(deva_ind) if deva_ind != "ERROR" else "ERROR"

    rows.append([w, deva_ak, ipa_ak, deva_ind, ipa_ind])

df = pd.DataFrame(
    rows,
    columns=[
        "Roman Input",
        "Aksharamukha Devanagari",
        "Aksharamukha IPA",
        "Indic-Translit Devanagari",
        "Indic-Translit IPA",
    ]
)

print(df)
