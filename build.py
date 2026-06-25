import base64, os
SRC="index.src.html"; OUT="index.html"
mime={'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.woff2':'font/woff2'}
tokens={
 '__TEXTURE__':'assets/texture.jpg',
 '__COVER__':'assets/cover.png',
 '__SWORDS__':'assets/swords.png',
 '__HATS__':'assets/hats.png',
 '__FENCERS__':'assets/fencers.png',
 '__DUO__':'assets/duo.png',
 '__FANATIC__':'assets/fanatic.png',
 '__COCKS__':'assets/cocks.png',
 '__WARRIOR__':'assets/warrior.png',
 '__FONT_FELL__':'assets/imfell-english-sc.woff2',
}
def datauri(path):
    ext=os.path.splitext(path)[1].lower()
    b=base64.b64encode(open(path,'rb').read()).decode()
    return f"data:{mime[ext]};base64,{b}"
html=open(SRC,encoding='utf-8').read()
for tok,path in tokens.items():
    if tok in html:
        html=html.replace(tok, datauri(path))
open(OUT,'w',encoding='utf-8').write(html)
print('built', OUT, round(os.path.getsize(OUT)/1024,1),'KB')
