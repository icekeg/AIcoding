#from krita import *
#Krita.instance().action("ten_brushes").trigger()
#Krita.instance().action("ten_scripts").trigger()
#Krita.instance().action("color_space").trigger()
#Krita.instance().action("python_scripter").trigger()
#doc = Krita.instance().createDocument(100, 100, "Doc1", "RGBA", "U8", "", 120.0)
#Krita.instance().activeWindow().addView(doc)
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import  QtNetwork
from PyQt5.QtCore import QCoreApplication, QUrl, QByteArray
import sys
import json
import uuid

prompt_text = """
{
    "3": {
        "class_type": "KSampler",
        "inputs": {
            "cfg": 8,
            "denoise": 1,
            "latent_image": [
                "5",
                0
            ],
            "model": [
                "4",
                0
            ],
            "negative": [
                "7",
                0
            ],
            "positive": [
                "6",
                0
            ],
            "sampler_name": "euler",
            "scheduler": "normal",
            "seed": 8566257,
            "steps": 20
        }
    },
    "4": {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {
            "ckpt_name": "realisticVisionV51_v51VAE.safetensors"
        }
    },
    "5": {
        "class_type": "EmptyLatentImage",
        "inputs": {
            "batch_size": 1,
            "height": 512,
            "width": 512
        }
    },
    "6": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "4",
                1
            ],
            "text": "masterpiece best quality girl"
        }
    },
    "7": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "4",
                1
            ],
            "text": "bad hands"
        }
    },
    "8": {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": [
                "3",
                0
            ],
            "vae": [
                "4",
                2
            ]
        }
    },
    "9": {
        "class_type": "SaveImage",
        "inputs": {
            "filename_prefix": "ComfyUI",
            "images": [
                "8",
                0
            ]
        }
    }
}
"""

prompt_text2 = """
{
    "1": {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {
            "ckpt_name": "realisticVisionV51_v51VAE.safetensors"
        }
    },
    "2": {
        "class_type": "CLIPSetLastLayer",
        "inputs": {
            "clip": [
                "1",
                1
            ],
            "stop_at_clip_layer": -1
        }
    },
    "3": {
        "class_type": "EmptyLatentImage",
        "inputs": {
            "width": 568,
            "height": 752,
            "batch_size": 4
        }
    },
    "4": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "2",
                0
            ],
            "text": "cinematic film still "
        }
    },
    "5": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "2",
                0
            ],
            "text": "anime, cartoon, graphic, text, painting, crayon, graphite, abstract"
        }
    },
    "6": {
        "class_type": "KSamplerAdvanced",
        "inputs": {
            "noise_seed": 13254948372015727120,
            "sampler_name": "dpmpp_2m",
            "scheduler": "karras",
            "model": [
                "1",
                0
            ],
            "positive": [
                "4",
                0
            ],
            "negative": [
                "5",
                0
            ],
            "latent_image": [
                "3",
                0
            ],
            "steps": 20,
            "start_at_step": 0,
            "end_at_step": 20,
            "cfg": 6.0,
            "add_noise": "enable",
            "return_with_leftover_noise": "disable"
        }
    },
    "7": {
        "class_type": "VAEDecode",
        "inputs": {
            "vae": [
                "1",
                2
            ],
            "samples": [
                "6",
                0
            ]
        }
    },
    "8": {
        "class_type": "ImageScale",
        "inputs": {
            "image": [
                "7",
                0
            ],
            "width": 563,
            "height": 751,
            "upscale_method": "bilinear",
            "crop": "disabled"
        }
    },
    "9": {
        "class_type": "ETN_SendImageWebSocket",
        "inputs": {
            "images": [
                "8",
                0
            ]
        }
    }
}
"""
            
class Example:
    client_id = str(uuid.uuid4())
 
    def __init__(self, prompt):    
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.doRequest(prompt)
        
        
    def doRequest(self, prompt):   
        p = {"prompt": prompt, "client_id": self.client_id}
        #data = json.dumps(p).encode('utf-8')
        #req =  urllib.request.Request("http://{}/prompt".format(server_address), data=data)
        #return json.loads(urllib.request.urlopen(req).read())
    
        url = "http://127.0.0.1:8188/prompt"
        req = QtNetwork.QNetworkRequest(QUrl(url))
        req.setRawHeader(b"ngrok-skip-browser-warning", b"69420")

        with open('C:/Users/Alfred/AppData/Roaming/krita/pykrita/ai_diffusion/data01.json', 'w') as file:
            json.dump(p, file, indent=4)

        data_bytes = QByteArray(json.dumps(p).encode("utf-8"))
        req.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, "application/json")
        req.setHeader(QtNetwork.QNetworkRequest.ContentLengthHeader, data_bytes.size())
        
        self.nam.post(req, data_bytes)
        #self.nam.get(req)
             
      
    def handleResponse(self, reply):

        er = reply.error()
        
        if er == QtNetwork.QNetworkReply.NoError:
    
            bytes_string = reply.readAll()
            print("ooo")
            print(str(bytes_string, 'utf-8'))
            
        else:
            print("Error occured: ", er)
            print(reply.errorString())
            
        QCoreApplication.quit()    

prompt = json.loads(prompt_text2)
#prompt["6"]["inputs"]["text"] = "masterpiece best quality man"

#set the seed for our KSampler node
#prompt["3"]["inputs"]["seed"] = 5

app = QCoreApplication([])
ex = Example(prompt)
sys.exit(app.exec_())
