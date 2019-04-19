from nltk.tag import tnt
from nltk.corpus import indian
import nltk

def hindi_model():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger

# contentArray = ["राम सीता के लिए फूलों की माला बनाता है।", 
#                 "सभी बच्चे विद्यालय में पढ़ते है।", 
#                 "मैंने उनसे एक सहज प्रश्न पूछा था।", 
#                 "भागता हुआ हिरण गिर गया। ",
#                 "लक्ष्मण राम के साथ वनवास गया।", 
#                 "इस शुभावसर पर राम ने गरीबों को दान दिया।",
#                 "ट्रेन में होने वाले हर अपराध में इस गाँव का कोई शामिल मिल जाएगा।", 
#                 "तुम्हारे सपने है बड़े से।" ]  

text1= "राम सीता के लिए फूलों की माला बनाता है।" 
text2= "सभी बच्चे विद्यालय में पढ़ते है।" 
text3= "मैंने उनसे एक सहज प्रश्न पूछा था।" 
text4= "भागता हुआ हिरण गिर गया। "
text5= "लक्ष्मण राम के साथ वनवास गया।" 
text6= "इस शुभावसर पर राम ने गरीबों को दान दिया।"
text7= "ट्रेन में होने वाले हर अपराध में इस गाँव का कोई शामिल मिल जाएगा।" 
text8= "तुम्हारे सपने है बड़े से।" 

                  
model = hindi_model()
new_tagged1 = (model.tag(nltk.word_tokenize(text1)))
new_tagged2 = (model.tag(nltk.word_tokenize(text2)))
new_tagged3 = (model.tag(nltk.word_tokenize(text3)))
new_tagged4 = (model.tag(nltk.word_tokenize(text4)))
new_tagged5 = (model.tag(nltk.word_tokenize(text5)))
new_tagged6 = (model.tag(nltk.word_tokenize(text6)))
new_tagged7 = (model.tag(nltk.word_tokenize(text7)))
new_tagged8 = (model.tag(nltk.word_tokenize(text8)))

print(new_tagged1)
print(new_tagged2)
print(new_tagged3)
print(new_tagged4)
print(new_tagged5)
print(new_tagged6)
print(new_tagged7)
print(new_tagged8)