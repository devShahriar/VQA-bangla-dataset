
from json.decoder import JSONDecoder
from googletrans import Translator
from argparse import ArgumentParser
import json
import time  


# st="ভাল"
# f=open('test.json','w')
# f.write(str(st))
# f.close()



def translate_to_bn(text):
    time.sleep(1)
    translator = Translator(service_urls=[
      'translate.google.co.kr',
    ])

    translated = translator.translate(text, src='en', dest='bn').text
    
    # print(translated)
    return translated

def translator_exec(input_path,output_path):
    dump_data = []
    with open(input_path) as j:

        payload=json.load(j)
        i = 0
        length = len(payload["questions"])
        print(length)
        questions = payload["questions"]
        for data in questions:
            print(i)
            
            ques = data["question"]
            print(ques)
            answer = data["answer"]
            print(answer)
            ques_in_bn = translate_to_bn(ques)
            data["question"] = str(ques_in_bn)
           # time.sleep(1)
            ans_in_bn = translate_to_bn(answer)
            data["answer"] = str(ans_in_bn)
            dump_data.append(data)
            print("remaining")
            print(length-i)
            if i%100==0 and i!=0:
                save_batch(dump_data,output_path)
            i+=1
  

def save_batch(data,output_path):

    with open(output_path,'w',encoding='utf8') as f:
        json.dump(data,f,ensure_ascii=False)
      

def main(args):
   translator_exec(args.input_path,args.output_path)



if __name__ == '__main__':
    parser = ArgumentParser("Translator script")
    parser.add_argument("-i","--input_path",help="provide the path of input file")
    parser.add_argument("-o","--output_path",help="provide the path of output file")
    args = parser.parse_args()
    main(args)



