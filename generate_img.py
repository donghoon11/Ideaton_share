import keras_cv
from translate import  Translator
import matplotlib.pyplot as plt

model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)
translator = Translator(from_lang='ko', to_lang='en')

def generate_img(text:str, cnt:int) -> list:
    text = translator.translate(text)
    images = model.text_to_image(text, batch_size=cnt)
    return images

def plot_image(images) -> None:
    plt.figure(figsize=(20,20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i+1)
        plt.imshow(images[i])
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(f'text.png')

# if __name__ == '__main__':
#     images = generate_img('노란 풍선', 1)
#     plot_image(images)