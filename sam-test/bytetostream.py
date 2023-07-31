
import base64
import requests
from PIL import Image
from io import BytesIO
from tencent_cos import OssDef

def filename_to_base64(filename):
    with open(filename, "rb") as fh:
        return base64.b64encode(fh.read())

img_filename = "new1.jpg"


""" payload = {
    "input_image": filename_to_base64(img_filename).decode(),
    "sam_positive_points":[[732.2916666666667,231.64166666666668],[715.625,367.05833333333334],[694.7916666666667,194.140625],[644.7916666666667,160.80729166666669]],
    "sam_negative_points":[],
    "dino_enabled": False,
    "dino_model_name":"GroundingDINO_SwinT_OGC (694MB)",
    "dino_text_prompt": "",
    "dino_box_threshold":0.3,
    "dino_preview_checkbox": False,
    "dino_preview_boxes_selection":None,
} """

url = "http://1.14.15.140:7860/sam/sam-predict"
payload = {
    "input_image": filename_to_base64(img_filename).decode(),
    "sam_positive_points":[[465.37815126050424,478.4873949579832],[687.2268907563025,533.9495798319327],[475.46218487394964,695.2941176470588],[697.3109243697479,720.5042016806723]],
    "dino_enabled": False,
    "dino_text_prompt": "",
    "dino_preview_checkbox": False,
}
response = requests.post(url, json=payload)
reply = response.json()
#print("---return-----",reply)

first_String=reply["blended_images"][0]
#print("----blengd imag-------",first_String)

imagebyte=BytesIO(base64.b64decode(first_String)).read()

#with open('D:/py-workspace/stable-diffusion-webui/sam-test/aaa.jpg', 'wb') as wf:
#    wf.write(imagebyte)


#
ossdef = OssDef()
key_of_file="/sam/lxiaodao/2023-7-27/8866unippppp.jpg"
returns=ossdef.upload(imagebyte, key_of_file)
print(1,returns)


""" grid = Image.new('RGBA', (3 * 512, 3 * 512))
def paste(img, row):
    for idx, img in enumerate(img):
        img_pil = Image.open(BytesIO(base64.b64decode(img))).resize((512, 512)).
        grid.paste(img_pil, (idx * 512, row * 512)) """
#paste(reply["blended_images"], 0)
#paste(reply["masks"], 1)
#paste(reply["masked_images"], 2)
#grid.show()