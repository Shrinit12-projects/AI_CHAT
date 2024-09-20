import google.generativeai as genai
import os
import gradio as gr
import PIL.Image
import numpy as np


genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

def chatbot(prompt, img):
    print(prompt)
    print(img)
    if img is not None:
        organ = PIL.Image.fromarray(np.uint8(img))
        response = model.generate_content([prompt, organ])
    else:
        response = model.generate_content(prompt)
    return response.text

inputs=[]
inputs.append(gr.Textbox(lines=7, label="Chat with AI"))
inputs.append(gr.Image(label="Image here"))
print(inputs)
outputs = gr.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="default").launch(share=True)