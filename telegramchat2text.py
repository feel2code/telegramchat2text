import json


FROM_BOT = 'Пожилая чупакабра'

file = open('result.json')
data = json.load(file)

for i in data["messages"]:
    try:
        if i["from"] == FROM_BOT or i["text"] == '' or i["forwarded_from"] is not None or i['text'][0]['type'] != "1":
            pass
        else:
            demo_file = open("demofile.txt", "a")
            text = str(i['text']) + '. '
            demo_file.write(text)
            demo_file.close()
    except:
        try:
            if i["text"] == '' or i["forwarded_from"] is not None or i['text'][0]['type'] != "1":
                pass
            else:
                demo_file = open("demofile.txt", "a")
                text = str(i['text']) + '. '
                demo_file.write(text)
                demo_file.close()
        except:
            try:
                if i["forwarded_from"] is not None or i['text'][0]['type'] != "1":
                    pass
                else:
                    demo_file = open("demofile.txt", "a")
                    text = str(i['text']) + '. '
                    demo_file.write(text)
                    demo_file.close()
            except:
                try:
                    if i['text'][0]['type'] != "1":
                        pass
                    else:
                        demo_file = open("demofile.txt", "a")
                        text = str(i['text']) + '. '
                        demo_file.write(text)
                        demo_file.close()
                except:
                    demo_file = open("demofile.txt", "a")
                    text = str(i['text']) + '. '
                    demo_file.write(text)
                    demo_file.close()
 
file.close()
