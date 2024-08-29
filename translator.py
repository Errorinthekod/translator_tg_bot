from deep_translator import GoogleTranslator as G

def translator(text):
    translation = G(source = 'ru', target = 'en').translate(text)
    translation1 = G(source = 'en', target = 'ru').translate(text)
    a = translation + " - " + translation1
    return a 

# def translator_kz(text):
#     translation_kz = G(source = 'ru', target = 'kk').translate(text)
#     translation_kz1 = G(source = 'kk', target = 'ru').translate(text)
#     kz = translation_kz + " - " + translation_kz1
#     return kz

print(translator('Bot activated'))
# print(translator_kz('Бот істеп бастады'))
