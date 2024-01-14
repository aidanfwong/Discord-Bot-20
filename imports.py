ball_things = ["yes", "no", "absolutely not", "maybe", "ask again", "it is certain"]

for ball in ball_things:
  print(ball_things)

michael_things = ["https://cdn.discordapp.com/attachments/777233411664379917/794252688598237214/michael_carry.png", "https://cdn.discordapp.com/attachments/777233411664379917/794253577497214986/michael_nae_naed.png", "https://imgur.com/a/TC8lVUG", "https://lowkey.gg/v/bf238937-e9be-4c93-b87e-f392db80e8b5", "https://imgur.com/a/D5nN1oM", "https://lowkey.gg/v/3d4dcf4f-7518-459a-8b8b-ab9358736632", "https://lowkey.gg/v/df627f69-f26e-4359-80f8-a5cc649736e3", "https://lowkey.gg/v/fcd9f25a-5974-4421-b06b-065d0d527ebb", "https://lowkey.gg/v/ca375b09-f0bc-48da-8305-db76c8efd068", "https://lowkey.gg/v/f5e9f28a-1fd9-46ee-8c88-f6b050aa3eb5","https://lowkey.gg/v/35fa8c2c-1693-433b-b94d-161f6c5d1f19","https://lowkey.gg/v/2c895f93-cf37-40de-aa6d-e10380e56c5b","https://lowkey.gg/v/689ba823-55f8-4646-8aaf-ab7ed16857bb","https://lowkey.gg/v/f2100703-497b-4076-950b-c64d240490b9"]

for michael in michael_things:
  print(michael_things)



from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "not dead yet"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()