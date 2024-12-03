import json

PREFIX = 'COCO_train2014_'
with open(r'C:\Users\Administrator\Desktop\minimind-v\dataset\LLaVA-Instruct\pokemon_data.json', 'rb') as f:
    temp = json.load(f)
    print(temp)
    with open('train.txt', 'wb') as fw:
        for t in temp:
            name = (t['conversations'][1]['value'].split('是')[1][:-1])
            fw.write((PREFIX + t['image'] + ' ' + name + '\n').encode())
