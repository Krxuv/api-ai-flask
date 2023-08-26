from flask import Flask, request, jsonify, render_template, Response
from aiohttp import ClientSession
import freeGPT
import asyncio
import requests
import time
from apscheduler.schedulers.background import BackgroundScheduler
from scraper_ai import gpt35v2, gpt4, gpt35plus
from scraper_ai_img import ai_image

def send_request():
    response = requests.get("https://api.krxuv.repl.co")
    print('Requests send at: ' + time.ctime())

scheduler = BackgroundScheduler()
scheduler.add_job(send_request, 'interval', minutes=5)

database_model_img = {
    "absreal16": "absolutereality_V16.safetensors [37db0fc3]", #Absolute Reality V1.6
    "absreal181": "absolutereality_v181.safetensors [3d9d4d2b]", #Absolute Reality V1.8.1
    "analog10": "analog-diffusion-1.0.ckpt [9ca13f02]", #Analog V1
    "anythingv3": "anythingv3_0-pruned.ckpt [2700c435]", #Anything V3
    "anythingv45": "anything-v4.5-pruned.ckpt [65745d25]", #Anything V4.5
    "anythingv5": "anythingV5_PrtRE.safetensors [893e49b9]", #Anything V5
    "aom3a3": "AOM3A3_orangemixs.safetensors [9600da17]", #AbyssOrangeMix V3
    "deliberatev2": "deliberate_v2.safetensors [10ec4b29]", #Deliberate V2
    "dldiffus1": "dreamlike-diffusion-1.0.safetensors [5c9fd6e0]", #Dreamlike Diffusion V1
    "dlphoto2": "dreamlike-photoreal-2.0.safetensors [fdcf65e7]", #Dreamlike Photoreal V2
    "dshaper6": "dreamshaper_6BakedVae.safetensors [114c8abb]", #Dreamshaper 6 baked vae
    "dshaper7": "dreamshaper_7.safetensors [5cf5ae06]", #Dreamshaper 7
    "dshaper8": "dreamshaper_8.safetensors [9d40847d]", #Dreamshaper 8
    "animediffv1": "EimisAnimeDiffusion_V1.ckpt [4f828a15]", #Eimis Anime Diffusion V1.0
    "vividmix": "elldreths-vivid-mix.safetensors [342d9d26]", #Elldreth's Vivid
    "lyriel16": "lyriel_v16.safetensors [68fceea2]", #Lyriel V1.6
    "mecha10": "mechamix_v10.safetensors [ee685731]", #MechaMix V1.0
    "meinav9": "meinamix_meinaV9.safetensors [2ec66ab0]", #MeinaMix Meina V9
    "meinav11": "meinamix_meinaV11.safetensors [b56ce717]", #MeinaMix Meina V11
    "ojourneyv4": "openjourney_V4.ckpt [ca2f377f]", #Openjourney V4
    "portraitpv1": "portraitplus_V1.0.safetensors [1400e684]", #Portrait+ V1
    "rvisionv14": "Realistic_Vision_V1.4-pruned-fp16.safetensors [8d21810b]", #Realistic Vision V1.4
    "rvisionv2": "Realistic_Vision_V2.0.safetensors [79587710]", #Realistic Vision V2.0
    "rvisionv4": "Realistic_Vision_V4.0.safetensors [29a7afaa]", #Realistic Vision V4.0
    "rvisionv5": "Realistic_Vision_V5.0.safetensors [614d1063]", #Realistic Vision V5.0
    "rsdiffv1": "redshift_diffusion-V10.safetensors [1400e684]", #Redshift Diffusion V1.0
    "revanimv122": "revAnimated_v122.safetensors [3f4fefd9]", #ReV Animated V1.2.2
    "sdv14": "sdv1_4.ckpt [7460a6fa]", #SD V1.4
    "sdv15": "v1-5-pruned-emaonly.safetensors [d7049739]", #SD V1.5
    "shoninsv10": "shoninsBeautiful_v10.safetensors [25d8c546]", #Shonin's Beautiful People V1.0
    "theallys": "theallys-mix-ii-churned.safetensors [5d9225a4]", #TheAlly's Mix II
    "timeless1": "timeless-1.0.ckpt [7c4971d4]" #Timeless V1
}

app = Flask(__name__)

@app.route('/')
def home():
    #result = {'status': 'Api Status Online'}
    #return jsonify(result)
    return render_template('index.html')

@app.route('/model/gpt3')
def gpt3_route():
    text = request.args.get('prompt')
    if text:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(freegpttext(text, 'gpt3'))
        loop.close()
        return result
    else:
        result = {'result': 'Input query prompt='}
        return jsonify(result)

@app.route('/model/gpt3v2')
def gpt3v2_route():
  text = request.args.get('prompt')
  if text:
      loop = asyncio.new_event_loop()
      asyncio.set_event_loop(loop)
      result = loop.run_until_complete(gpt35v2(text))
      loop.close()
      return result
  else:
      result = {'result': 'Input query prompt='}
      return jsonify(result)

@app.route('/model/gpt3turbo')
def gpt3turbo_route():
  text = request.args.get('prompt')
  if text:
      loop = asyncio.new_event_loop()
      asyncio.set_event_loop(loop)
      result = loop.run_until_complete(gpt35plus(text))
      loop.close()
      return result
  else:
      result = {'result': 'Input query prompt='}
      return jsonify(result)

@app.route('/model/gpt4')
def gpt4_route():
    text = request.args.get('prompt')
    if text:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(gpt4(text))
        loop.close()
        return result
    else:
        result = {'result': 'Input query prompt='}
        return jsonify(result)

@app.route('/model/alpaca')
def alpaca_route():
    text = request.args.get('prompt')
    if text:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(freegpttext(text, 'alpaca_7b'))
        loop.close()
        return result
    else:
        result = {'result': 'Input query prompt='}
        return jsonify(result)

@app.route('/model/falcon')
def falcon_route():
    text = request.args.get('prompt')
    if text:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(freegpttext(text, 'falcon_40b'))
        loop.close()
        return result
    else:
        result = {'result': 'Input query prompt='}
        return jsonify(result)

@app.route('/image/model/<string:kode>', methods=['GET'])
def imagemodel(kode):
  route_include = database_model_img.get(kode)
  if route_include:
    #return f"Success: {route_include} and {kode}"
    text = request.args.get('prompt')
    if text:
      loop = asyncio.new_event_loop()
      asyncio.set_event_loop(loop)
      result = loop.run_until_complete(ai_image(route_include, text))
      loop.close()
      headers = {
        'Content-Type': 'image/jpeg',
        'Content-Disposition': 'inline; filename=result.jpg'
      }
      return Response(result, headers=headers)
    else:
      result = {'result': 'Input query prompt='}
      return jsonify(result)
  else:
    return "Page not found"

async def freegpttext(yourprompt, model):
    try:
        async with ClientSession() as session:
            getresponse = await getattr(freeGPT, model).Completion().create(yourprompt)
            return str(getresponse)
    except Exception as e:
        print(e)
        return str(e)

if __name__ == "__main__":
    # Running server
    scheduler.start()
    app.run(host='0.0.0.0',port=8080)