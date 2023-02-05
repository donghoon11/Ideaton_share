import gradio as gr

def greet(name:str):
    return "Hello" + name

demo = gr.Interface(fn=greet, inputs='text',
                    outputs='text')
demo.launch()
# 잘 안되는 구만...
# pip install 상에서의 문제인듯...