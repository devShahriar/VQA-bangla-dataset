
from json.decoder import JSONDecoder
from googletrans import Translator




# st="ভাল"
# f=open('test.json','w')
# f.write(str(st))
# f.close()



def translate_to_bn(text):
    translator = Translator()

    translated = translator.translate(text, src='en', dest='bn').text
    
    # print(translated)
    return translated

import json
import time  
with open('clevr_bn_train.json') as j:
    payload=json.load(j)
    i = 1
    length = len(payload["questions"])
    print(length)
    questions = payload["questions"][0:4]
    for data in questions:
        print(i)
        i+=1
        ques = data["question"]
        print(ques)
        answer = data["answer"]
        print(answer)
        ques_in_bn = translate_to_bn(ques)
        data["question"] = str(ques_in_bn)
        time.sleep(1)
        ans_in_bn = translate_to_bn(answer)
        data["answer"] = str(ans_in_bn)
    
        print("remaining")
        print(length-i)

    payload["questions"] = questions
  


    with open('bn.json','w',encoding='utf8') as f:
        print(payload)
        json.dump(payload,f,ensure_ascii=False)
      


