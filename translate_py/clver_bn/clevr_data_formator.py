

#python3 clevr_data_formator.py -i CLEVR_train_questions.json -o bn_test.json -l 5

from argparse import ArgumentParser
import json 


def concat_dataset(input_path , output_path,ques_length):
    with open(input_path) as j:
        payload = json.load(j)
        payload["questions"] = payload["questions"][0:int(ques_length)]

        with open(output_path,"w") as f:
            json.dump(payload,f)

def main(args):
    concat_dataset(args.input_path,args.output_path,args.len)



if __name__ == '__main__':
    parser = ArgumentParser("Take path and legnth as input to optimise the dataset")
    parser.add_argument("-i","--input_path",help="provide the path of input file")
    parser.add_argument("-o","--output_path",help="provide the path of output file")
    parser.add_argument("-l","--len",help="length of the dataset")
    args = parser.parse_args()
    main(args)
