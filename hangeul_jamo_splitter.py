import re
def split_syllable(syllable):
    #19개 초성
    onsets = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    #21개 중성
    nuclears = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

    #28개 종성
    codas = ['_', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    jamos = []
    # 한글 자모인 경우
    if '가'<=syllable<='힣':
        syllable_number = ord(syllable) - ord('가') #해당 음절의 유니코드 번호
        # 588개 마다 초성이 바뀜. 중성(21개) * 종성(28개) = 588
        cho = (syllable_number)//588
        
        # 28개 마다 중성이 바뀐다. (종성의 수=28), 중성 x 종성의 콤비네이션만 얻기 위해 초성 값을 제외해준다. 
        jung = ((syllable_number) - (588*cho)) // 28 # syllable_number % (21*28) // 28, 21*28 = 588

        # 종성의 콤비네이션만 얻기 위해 초성, 중성 값을 제외해준다.
        jong = (syllable_number) - (588*cho) - 28*jung # syllable_number % 28
        jamos = ([onsets[cho], nuclears[jung], codas[jong]])
    else: #그 외 한글 자모, 알파벳 혹은 숫자 혹은 다른 글자인 경우
        jamos = ([syllable])
    return jamos

## 음절 결합
def concat_syllable(cho, jung, jong):
    #19개
    onsets = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    #21개
    nuclears = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

    #28개
    codas = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    ## 리스트의 인덱스 번호
    cho_n = onsets.index(cho)
    jung_n = nuclears.index(jung)
    jong_n = codas.index(jong)

    ## 앞서 자모 splitter의 역함수
    syllable_number = cho_n * 588 + jung_n * 28 + jong_n
    syllable = chr(syllable_number + ord('가'))
    return syllable

##regex converter
def jamo_regex(regex):
    onsets = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    #21개
    nuclears = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

    #28개
    codas = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    
    res = regex
    jamos = re.findall('<[ㄱ-ㅎㅏ-ㅣ#xX]{3}>', regex)
    jamo_ls = list(map(lambda x: list(x)[1:4] ,jamos))
    converted_ls = []

    for jm in jamo_ls:
        temp = ''
        if jm == ['#', '#', '#']:
            temp = '가-힣'
        else:
            if jm[0] == '#':
                ons_ls = onsets
            else:
                ons_ls = [jm[0]]

            if jm[1] == '#':
                nuc_ls = nuclears
            else:
                nuc_ls = [jm[1]]

            if jm[2] == '#':
                cod_ls = codas
            elif jm[2] == 'x' or jm[2] == 'X':
                cod_ls = [codas[0]]
            else:
                cod_ls = [jm[2]]
            for o in ons_ls:
                for n in nuc_ls:
                    for c in cod_ls:
                        temp += concat_syllable(o, n, c)
        temp = '[' + temp + ']'
        converted_ls.append(temp)
    for i, jamo in enumerate(jamos):
        res = re.sub(jamo, converted_ls[i], res)
    
    if res == regex:
        print('no jamo_regex applied')

    return res


    

def get_cho(syllable):
    onsets = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    syllable_number = ord(syllable) - ord('가')
    return onsets[syllable_number // 588]


def get_jong(syllable):
    codas = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    syllable_number = ord(syllable) - ord('가')
    return codas[syllable_number % 28]

def get_jung(syllable):
    nuclears = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    syllable_number = ord(syllable) - ord('가')
    return nuclears[syllable_number % 588 //28]

def decompose_chojung_jong(syllable):
    codas = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    syllable_number = ord(syllable) - ord('가')
    jong = codas[syllable_number % 28]
    syllable_number -= syllable_number % 28
    return chr(syllable_number + ord('가')), jong

def get_rhyme(syllable):
    return(get_jung(syllable), get_jong(syllable))