SUPPORTED_LENGUAGES = {
    "pl": "pol",
    "en": "eng",
}


class LangAdapt:
    @staticmethod
    def map(lang_code: str):
        return SUPPORTED_LENGUAGES.get(lang_code, )


'''
lang_detect_support = """
af als am an ar arz as ast av az azb ba bar bcl be bg bh bn bo bpy br bs bxr
ca cbk ce ceb ckb co cs cv cy da de diq dsb dty dv el eml en eo es et eu fa
fi fr frr fy ga gd gl gn gom gu gv he hi hif hr hsb ht hu hy ia id ie ilo
io is it ja jbo jv ka kk km kn ko krc ku kv kw ky la lb lez li lmo lo lrc lt
lv mai mg mhr min mk ml mn mr mrj ms mt mwl my myv mzn nah nap nds ne new nl
nn no oc or os pa pam pfl pl pms pnb ps pt qu rm ro ru rue sa sah sc scn sco
sd sh si sk sl so sq sr su sv sw ta te tg th tk tl tr tt tyv ug uk ur uz vec
vep vi vls vo wa war wuu xal xmf yi yo yue zh"""

# ISO-639 set 3
tesseract_support = """afr	Afrikaans	x	x	x	x	x	x
amh	Amharic	 	x	x	x	x	x
ara	Arabic	x	x	x	x	x	x
asm	Assamese	 	x	x	x	x	x
aze	Azerbaijani	 	x	x	x	x	x
aze_cyrl	Azerbaijani - Cyrilic	x	x	x	x	x	x
bel	Belarusian	x	x	x	x	x	x
ben	Bengali	x	x	x	x	x	x
bod	Tibetan	 	x	x	x	x	x
bos	Bosnian	 	x	x	x	x	x
bre	Breton	 	 	x	x	x	x
bul	Bulgarian	x	x	x	x	x	x
cat	Catalan; Valencian	x	x	x	x	x	x
ceb	Cebuano	 	x	x	x	x	x
ces	Czech	x	x	x	x	x	x
chi_sim	Chinese - Simplified	x	x	x	x	x	x
chi_tra	Chinese - Traditional	x	x	x	x	x	x
chr	Cherokee	x	x	x	x	x	x
cos	Corsican	 	 	 	x	x	x
cym	Welsh	 	x	x	x	x	x
dan	Danish	x	x	x	x	x	x
dan_frak	Danish - Fraktur (contrib)	x	x	 	 	 	 
deu	German	x	x	x	x	x	x
deu_frak	German - Fraktur (contrib)	x	x	 	 	 	 
deu_latf	German (Fraktur Latin)	 	 	x	x	x	x
dzo	Dzongkha	 	x	x	x	x	x
ell	Greek, Modern (1453-)	x	x	x	x	x	x
eng	English	x	x	x	x	x	x
enm	English, Middle (1100-1500)	x	x	x	x	x	x
epo	Esperanto	x	x	x	x	x	x
equ	Math / equation detection module	x	x	 	x	x	x
est	Estonian	x	x	x	x	x	x
eus	Basque	x	x	x	x	x	x
fao	Faroese	 	 	 	x	x	x
fas	Persian	 	x	x	x	x	x
fil	Filipino (old - Tagalog)	 	 	 	x	x	x
fin	Finnish	x	x	x	x	x	x
fra	French	x	x	x	x	x	x
frk	German - Fraktur (now deu_latf)	x	x	x	x	x	x
frm	French, Middle (ca.1400-1600)	x	x	x	x	x	x
fry	Western Frisian	 	 	 	x	x	x
gla	Scottish Gaelic	 	 	 	x	x	x
gle	Irish	 	x	x	x	x	x
glg	Galician	x	x	x	x	x	x
grc	Greek, Ancient (to 1453) (contrib)	x	x	x	x	x	x
guj	Gujarati	 	x	x	x	x	x
hat	Haitian; Haitian Creole	 	x	x	x	x	x
heb	Hebrew	x	x	x	x	x	x
hin	Hindi	x	x	x	x	x	x
hrv	Croatian	x	x	x	x	x	x
hun	Hungarian	x	x	x	x	x	x
hye	Armenian	 	 	 	x	x	x
iku	Inuktitut	 	x	x	x	x	x
ind	Indonesian	x	x	x	x	x	x
isl	Icelandic	x	x	x	x	x	x
ita	Italian	x	x	x	x	x	x
ita_old	Italian - Old	x	x	x	x	x	x
jav	Javanese	 	x	x	x	x	x
jpn	Japanese	x	x	x	x	x	x
kan	Kannada	x	x	x	x	x	x
kat	Georgian	 	x	x	x	x	x
kat_old	Georgian - Old	 	x	x	x	x	x
kaz	Kazakh	 	x	x	x	x	x
khm	Central Khmer	 	x	x	x	x	x
kir	Kirghiz; Kyrgyz	 	x	x	x	x	x
kmr	Kurmanji (Kurdish - Latin Script)	 	 	x	x	x	x
kor	Korean	x	x	x	x	x	x
kor_vert	Korean (vertical)	 	 	x	x	x	x
kur	Kurdish (Arabic Script)	 	x	 	 	 	 
lao	Lao	 	x	x	x	x	x
lat	Latin	 	x	x	x	x	x
lav	Latvian	x	x	x	x	x	x
lit	Lithuanian	x	x	x	x	x	x
ltz	Luxembourgish	 	 	x	x	x	x
mal	Malayalam	x	x	x	x	x	x
mar	Marathi	 	x	x	x	x	x
mkd	Macedonian	x	x	x	x	x	x
mlt	Maltese	x	x	x	x	x	x
mon	Mongolian	 	 	x	x	x	x
mri	Maori	 	 	x	x	x	x
msa	Malay	x	x	x	x	x	x
mya	Burmese	 	x	x	x	x	x
nep	Nepali	 	x	x	x	x	x
nld	Dutch; Flemish	x	x	x	x	x	x
nor	Norwegian	x	 	x	x	x	x
oci	Occitan (post 1500)	 	x	x	x	x	x
ori	Oriya	 	x	x	x	x	x
osd	Orientation and script detection module	x	x	x	x	x	x
pan	Panjabi; Punjabi	 	x	x	x	x	x
pol	Polish	x	x	x	x	x	x
por	Portuguese	x	x	x	x	x	x
pus	Pushto; Pashto	 	x	x	x	x	x
que	Quechua	 	 	x	x	x	x
ron	Romanian; Moldavian; Moldovan	x	x	x	x	x	x
rus	Russian	x	x	x	x	x	x
san	Sanskrit	 	x	x	x	x	x
sin	Sinhala; Sinhalese	 	x	x	x	x	x
slk	Slovak	x	x	x	x	x	x
slk_frak	Slovak - Fraktur (contrib)	x	x	 	 	 	 
slv	Slovenian	x	x	x	x	x	x
snd	Sindhi	 	 	x	x	x	x
spa	Spanish; Castilian	x	x	x	x	x	x
spa_old	Spanish; Castilian - Old	x	x	x	x	x	x
sqi	Albanian	x	x	x	x	x	x
srp	Serbian	x	x	x	x	x	x
srp_latn	Serbian - Latin	 	x	x	x	x	x
sun	Sundanese	 	 	x	x	x	x
swa	Swahili	x	x	x	x	x	x
swe	Swedish	x	x	x	x	x	x
syr	Syriac	 	x	x	x	x	x
tam	Tamil	x	x	x	x	x	x
tat	Tatar	 	 	x	x	x	x
tel	Telugu	x	x	x	x	x	x
tgk	Tajik	 	x	x	x	x	x
tgl	Tagalog (new - Filipino)	x	x	x	 	 	 
tha	Thai	x	x	x	x	x	x
tir	Tigrinya	 	x	x	x	x	x
ton	Tonga	 	 	x	x	x	x
tur	Turkish	x	x	x	x	x	x
uig	Uighur; Uyghur	 	x	x	x	x	x
ukr	Ukrainian	x	x	x	x	x	x
urd	Urdu	 	x	x	x	x	x
uzb	Uzbek	 	x	x	x	x	x
uzb_cyrl	Uzbek - Cyrilic	 	x	x	x	x	x
vie	Vietnamese	x	x	x	x	x	x
yid	Yiddish	 	x	x	x	x	x
yor	Yoruba	 	 	x	x	x	x"""'''