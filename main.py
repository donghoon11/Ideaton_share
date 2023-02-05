import gradio as gr
from generate_img import generate_img
# import pytesseract      # textocr
import cv2      # textocr
from PIL import Image   
# from google.colab.patches import cv2_imshow
# import os
# from textOCR import img2text

def inference_ocr(img_path):
    sentence = img2text(img_path)
    image = generate_img(sentence, 1).squeeze()
    return image, str(sentence)

def inference(sentence:str):
    image = generate_img(sentence, 1).squeeze()
    return image

demo = gr.Interface(
    fn=inference,
    inputs='text',
    outputs='image',
    show_api=True)

# demo = gr.Interface(
#     fn=inference_ocr,
#     inputs=gr.Image(shape=(200,200)),
#     outputs=['image','text'])
demo.launch()