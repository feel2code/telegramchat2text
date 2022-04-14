import json


f = open('result.json')
data = json.load(f)

for i in data["messages"]:
    try:
        if i["from"] == "Пожилая чупакабра" or i["text"] == '' or i["forwarded_from"] is not None or i['text'][0]['type'] != "1":
            pass
        else:
            d = open("demofile.txt", "a")
            text = str(i['text']) + '. '
            d.write(text)
            d.close()
    except:
        try:
            if i["text"] == '' or i["forwarded_from"] is not None or i['text'][0]['type'] != "1":
                pass
            else:
                d = open("demofile.txt", "a")
                text = str(i['text']) + '. '
                d.write(text)
                d.close()
        except:
            try:
                if i["forwarded_from"] is not None or i['text'][0]['type'] != "1":
                    pass
                else:
                    d = open("demofile.txt", "a")
                    text = str(i['text']) + '. '
                    d.write(text)
                    d.close()
            except:
                try:
                    if i['text'][0]['type'] != "1":
                        pass
                    else:
                        d = open("demofile.txt", "a")
                        text = str(i['text']) + '. '
                        d.write(text)
                        d.close()
                except:
                    d = open("demofile.txt", "a")
                    text = str(i['text']) + '. '
                    d.write(text)
                    d.close()
 
f.close()
