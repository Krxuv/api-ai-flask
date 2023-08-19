from flask import Flask, request, jsonify, render_template
from aiohttp import ClientSession
import freeGPT
import asyncio

app = Flask(__name__)

@app.route('/')
def home():
    #result = {'status': 'Api Status Online'}
    #return jsonify(result)
    return render_template('index.html')

@app.route('/model/gpt3')
def gpt3():
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

@app.route('/model/gpt4')
def gpt4():
    text = request.args.get('prompt')
    if text:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(freegpttext(text, 'gpt4'))
        loop.close()
        return result
    else:
        result = {'result': 'Input query prompt='}
        return jsonify(result)

@app.route('/model/alpaca')
def alpaca():
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
def falcon():
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
    app.run(host='0.0.0.0',port=8080)
