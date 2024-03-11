#This is an example that uses the websockets api to know when a prompt execution is done
#Once the prompt execution is done it downloads the images using the /history endpoint

import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid
import json
import urllib.request
import urllib.parse

server_address = "127.0.0.1:8188"
client_id = str(uuid.uuid4())

def queue_prompt(prompt):
    p = {"prompt": prompt, "client_id": client_id}
    with open('C:/Users/Alfred/AppData/Roaming/krita/pykrita/ai_diffusion/data02.json', 'w') as file:
        json.dump(p, file, indent=4)
    data = json.dumps(p).encode('utf-8')
    req =  urllib.request.Request("http://{}/prompt".format(server_address), data=data)
    return json.loads(urllib.request.urlopen(req).read())

def get_image(filename, subfolder, folder_type):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    with urllib.request.urlopen("http://{}/view?{}".format(server_address, url_values)) as response:
        return response.read()

def get_history(prompt_id):
    with urllib.request.urlopen("http://{}/history/{}".format(server_address, prompt_id)) as response:
        return json.loads(response.read())

def get_images(ws, prompt):
    prompt_id = queue_prompt(prompt)['prompt_id']
    output_images = {}
    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message['type'] == 'executing':
                data = message['data']
                if data['node'] is None and data['prompt_id'] == prompt_id:
                    break #Execution is done
        else:
            continue #previews are binary data

    history = get_history(prompt_id)[prompt_id]
    for o in history['outputs']:
        for node_id in history['outputs']:
            node_output = history['outputs'][node_id]
            if 'images' in node_output:
                images_output = []
                for image in node_output['images']:
                    image_data = get_image(image['filename'], image['subfolder'], image['type'])
                    images_output.append(image_data)
            output_images[node_id] = images_output

    return output_images

prompt_text = """
{
  "3": {
    "inputs": {
      "seed": 793849426877181,
      "steps": 20,
      "cfg": 4,
      "sampler_name": "euler_ancestral",
      "scheduler": "simple",
      "denoise": 1,
      "model": [
        "49",
        0
      ],
      "positive": [
        "53",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "latent_image": [
        "34",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "6": {
    "inputs": {
      "text": "evening sunset scenery blue sky nature,a portrait of one girl,stand, full body",
      "clip": [
        "49",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Positive Prompt)"
    }
  },
  "7": {
    "inputs": {
      "text": "text, watermark,low quality",
      "clip": [
        "49",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Negative Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "33",
        0
      ],
      "vae": [
        "42",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "9": {
    "inputs": {
      "filename_prefix": "ComfyUI",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  },
  "33": {
    "inputs": {
      "seed": 59968871002298,
      "steps": 10,
      "cfg": 1.1,
      "sampler_name": "euler_ancestral",
      "scheduler": "simple",
      "denoise": 1,
      "model": [
        "42",
        0
      ],
      "positive": [
        "36",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "latent_image": [
        "34",
        1
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "34": {
    "inputs": {
      "width": 2048,
      "height": 2048,
      "compression": 42,
      "batch_size": 1
    },
    "class_type": "StableCascade_EmptyLatentImage",
    "_meta": {
      "title": "StableCascade_EmptyLatentImage"
    }
  },
  "36": {
    "inputs": {
      "conditioning": [
        "6",
        0
      ],
      "stage_c": [
        "3",
        0
      ]
    },
    "class_type": "StableCascade_StageB_Conditioning",
    "_meta": {
      "title": "StableCascade_StageB_Conditioning"
    }
  },
  "42": {
    "inputs": {
      "ckpt_name": "cascade/stable_cascade_stage_b.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "48": {
    "inputs": {
      "image": "sunset03.png",
      "upload": "image"
    },
    "class_type": "LoadImage",
    "_meta": {
      "title": "Load Image"
    }
  },
  "49": {
    "inputs": {
      "ckpt_name": "cascade/stable_cascade_stage_c.safetensors"
    },
    "class_type": "unCLIPCheckpointLoader",
    "_meta": {
      "title": "unCLIPCheckpointLoader"
    }
  },
  "50": {
    "inputs": {
      "clip_vision": [
        "49",
        3
      ],
      "image": [
        "48",
        0
      ]
    },
    "class_type": "CLIPVisionEncode",
    "_meta": {
      "title": "CLIP Vision Encode"
    }
  },
  "51": {
    "inputs": {
      "strength": 1,
      "noise_augmentation": 0,
      "conditioning": [
        "6",
        0
      ],
      "clip_vision_output": [
        "50",
        0
      ]
    },
    "class_type": "unCLIPConditioning",
    "_meta": {
      "title": "unCLIPConditioning"
    }
  },
  "52": {
    "inputs": {
      "image": "bb (1).jpg",
      "upload": "image"
    },
    "class_type": "LoadImage",
    "_meta": {
      "title": "Load Image"
    }
  },
  "53": {
    "inputs": {
      "strength": 1,
      "noise_augmentation": 0,
      "conditioning": [
        "51",
        0
      ],
      "clip_vision_output": [
        "54",
        0
      ]
    },
    "class_type": "unCLIPConditioning",
    "_meta": {
      "title": "unCLIPConditioning"
    }
  },
  "54": {
    "inputs": {
      "clip_vision": [
        "49",
        3
      ],
      "image": [
        "52",
        0
      ]
    },
    "class_type": "CLIPVisionEncode",
    "_meta": {
      "title": "CLIP Vision Encode"
    }
  }
}
"""

prompt = json.loads(prompt_text)
#set the text prompt for our positive CLIPTextEncode
prompt["6"]["inputs"]["text"] = "masterpiece best quality man"

#set the seed for our KSampler node
prompt["3"]["inputs"]["seed"] = 7

ws = websocket.WebSocket()
ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
images = get_images(ws, prompt)

#Commented out code to display the output images:

# for node_id in images:
#     for image_data in images[node_id]:
#         from PIL import Image
#         import io
#         image = Image.open(io.BytesIO(image_data))
#         image.show()

