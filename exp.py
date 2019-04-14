import nltk
#nltk.download('popular')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 

contentArray = ['There were once a man and a woman who had long, in vain, wished for a child.',
                'At length it appeared that God was about to grant their desire.',
                'These people had a little window at the back of their house from which a splendid garden could be seen.',
                'The garden was full of the most beautiful flowers and herbs.',
                'It was, however, surrounded by a high wall, and no one dared to go into it because it belonged to an enchantress.',
                'She had great power and was dreaded by all the world. ',
                'One day the woman was standing by this window and looking down into the garden. ',
                'She saw a bed which was planted with the most beautiful rampion, and she longed for it.',
                'Her husband was alarmed, and asked "What ails you, dear wife?" ',
                '\'Ah,\' she replied, \'if I cannot eat some of the rampion, which is in the garden behind our house, I shall die.\' ']  
                    
def processContent():
    try:
        for item in contentArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            

            print(tagged)
            # chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>}"""
            # chunkParser = nltk.RegexpParser(chunkGram)

            # chunked = chunkParser.parse(tagged)
            # print(chunked)
            #chunked.draw()
            
    except Exception as e:
        print(str(e))
    


processContent()