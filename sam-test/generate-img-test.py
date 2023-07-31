
import base64
import requests
from PIL import Image
from io import BytesIO

def filename_to_base64(filename):
    with open(filename, "rb") as fh:
        return base64.b64encode(fh.read())

img_filename = "shirt-another.jpg"


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
#/sdapi/v1/img2img
url = "http://1.14.15.140:7800/sdapi/v1/img2img"
payload = {
  "init_images": [
    "string"
  ],
  "resize_mode": 0,    # 0: just resize, 1: crop and resize, 2: resize and fill  3：just resize（潜空间放大）
  "denoising_strength": 0.75,
  "image_cfg_scale": 0,
  "mask": "string",
  "mask_blur": 0,
  "mask_blur_x": 4,
  "mask_blur_y": 4,
  "inpainting_fill": 0,
  "inpaint_full_res": true,
  "inpaint_full_res_padding": 0,
  "inpainting_mask_invert": 0,
  "initial_noise_multiplier": 0,
  "prompt": "",
  "styles": [
    "string"
  ],
  "seed": -1,
  "subseed": -1,
  "subseed_strength": 0,
  "seed_resize_from_h": -1,
  "seed_resize_from_w": -1,
  "sampler_name": "string",
  "batch_size": 1,
  "n_iter": 1,
  "steps": 50,
  "cfg_scale": 7,
  "width": 512,
  "height": 512,
  "restore_faces": false,
  "tiling": false,
  "do_not_save_samples": false,
  "do_not_save_grid": false,
  "negative_prompt": "string",
  "eta": 0,
  "s_min_uncond": 0,
  "s_churn": 0,
  "s_tmax": 0,
  "s_tmin": 0,
  "s_noise": 1,
  "override_settings": {},
  "override_settings_restore_afterwards": true,
  "script_args": [],
  "sampler_index": "Euler",
  "include_init_images": false,
  "script_name": "string",
  "send_images": true,
  "save_images": false,
  "alwayson_scripts": {}
}
response = requests.post(url, json=payload)
reply = response.json()
#print("---return-----",reply)

grid = Image.new('RGBA', (3 * 512, 3 * 512))
def paste(img, row):
    for idx, img in enumerate(img):
        img_pil = Image.open(BytesIO(base64.b64decode(img))).resize((512, 512))
        grid.paste(img_pil, (idx * 512, row * 512))
paste(reply["blended_images"], 0)
paste(reply["masks"], 1)
paste(reply["masked_images"], 2)
grid.show()



