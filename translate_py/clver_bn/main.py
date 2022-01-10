
from json.decoder import JSONDecoder
from googletrans import Translator




# st="ভাল"
# f=open('test.json','w')
# f.write(str(st))
# f.close()



def translate_to_bn(text):
    translator = Translator()

    translated = translator.translate(text, src='en', dest='bn').text
    
    print(translated)
    return translated

import json 
with open('test.json') as j:
    payload=json.load(j)
    ques = payload["question"]

    ques_in_bn = translate_to_bn(ques)
    payload["question"] = str(ques_in_bn)
    

    with open('test.json','w',encoding='utf8') as f:
        json.dump(payload,f,ensure_ascii=False)
      

with open('test.json') as j:
    payload=json.load(j)
    ques = payload["question"]
    print(str(ques))
