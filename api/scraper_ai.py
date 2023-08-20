import requests
import re
from aiohttp import ClientSession

async def gpt35plus(prompt):
  headers = {
    "authority": "chat-gpt.org",
    "accept": "*/*",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://chat-gpt.org",
    "pragma": "no-cache",
    "referer": "https://chat-gpt.org/chat",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
  }
  json_data = {
    "message": prompt,
    "temperature": 1,
    "presence_penalty": 0,
    "top_p": 1,
    "frequency_penalty": 0,
  }
  try:
    async with ClientSession() as session:
      response = requests.post(
        "https://chat-gpt.org/api/text",
        headers=headers,
        json=json_data,
      )
      #response.raise_for_status()
      return response.json()["message"]
  except Exception as err:
    return str(err)

async def gpt4(prompt):
  try:
    async with ClientSession() as session:
      response = requests.get("https://chatgpt.ai/")
      nonce, post_id, _, bot_id = re.findall(
          r'data-nonce="(.*)"\n     data-post-id="(.*)"\n     data-url="(.*)"\n     data-bot-id="(.*)"\n     data-width',
          response.text,
      )[0]
      headers = {
          "authority": "chatgpt.ai",
          "accept": "*/*",
          "accept-language": "en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3",
          "cache-control": "no-cache",
          "origin": "https://chatgpt.ai",
          "pragma": "no-cache",
          "referer": "https://chatgpt.ai/gpt-4/",
          "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": '"Windows"',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
      }
      data = {
          "_wpnonce": nonce,
          "post_id": post_id,
          "url": "https://chatgpt.ai/gpt-4",
          "action": "wpaicg_chat_shortcode_message",
          "message": prompt,
          "bot_id": bot_id,
      }
      response = requests.post(
          "https://chatgpt.ai/wp-admin/admin-ajax.php", headers=headers, data=data
      )
      #response.raise_for_status()
      return response.json()["data"]
  except Exception as err:
    return str(err)

async def gpt35v2(prompt):
  headers = {
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "origin": "https://chat9.yqcloud.top",
  }
  payload = {
    "prompt": prompt,
    "network": True,
    "system": "",
    "withoutContext": False,
    "stream": False,
  }
  url = "https://api.aichatos.cloud/api/generateStream"
  try:
    async with ClientSession() as session:
      response = requests.post(url=url, headers=headers, json=payload)
      #response.raise_for_status()
      return response.text
  except Exception as err:
    return str(err)