import json
with open("clever_bangla_train_80000_v2.json") as f:
    payload =json.load(f)
    print(len(payload))