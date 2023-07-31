import requests
import json
from PIL import Image


url = "https://u179511-aba7-786fea81.westb.seetacloud.com:8443/sam/sam-predict"

payload = {
    "input_image": 'https://stable-1305002912.cos.ap-nanjing.myqcloud.com/sam/lxiaodao/2023-7-26/union777abc9999.jpg',
    "sam_positive_points":[[732.2916666666667,231.64166666666668],[715.625,367.05833333333334],[694.7916666666667,194.140625],[644.7916666666667,160.80729166666669]],
    "sam_negative_points":[],
    "dino_enabled": False,
    "dino_model_name":"GroundingDINO_SwinT_OGC (694MB)",
    "dino_text_prompt": "",
    "dino_box_threshold":0.3,
    "dino_preview_checkbox": False,
    "dino_preview_boxes_selection":None,
}

back = requests.post(url, json=payload)
# print(back.success)
# print(back.code)
# print(back.message)
# print(back.content)
print(back.json())
# reply = response.json()
# print(reply)
# jsonstr = json.dumps(back.__dict__)
# print(jsonstr)