




import json 

with open("CLEVR_train_questions.json") as j:
    payload = json.load(j)
    payload["questions"] = payload["questions"][0:1000]

    with open("clevr_bn_train","w") as f:
        json.dump(payload,f)