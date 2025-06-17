import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import gradio as gr

model_name = "unsloth/llama-3.2-3b-instruct-unsloth-bnb-4bit"
peft_model_name = "mthabet00/serenity-AI_Therapist"

base_model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = PeftModel.from_pretrained(base_model, peft_model_name)

def generate_response(user_input, history):
    if history is None:
        history = ""
    prompt = f"""The following is a conversation between a user and a compassionate mental health assistant named MindGuard. Be empathetic, concise, and supportive.

{history}
User: {user_input}
MindGuard:"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=80,  # Reduced to prevent rambling
        temperature=0.7,
        do_sample=True,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )
    response_raw = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    response = response_raw.split("User:")[0].strip()

    updated_history = history + f"\nUser: {user_input}\nMindGuard: {response}"
    return response, updated_history

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Column(elem_id="main-col"):
        gr.Markdown("### 🧠 MindGuard: Your Mental Health Companion\nWelcome. Let’s talk. This is a safe space.")
        chatbot = gr.Chatbot(label="MindGuard Chat")
        state = gr.State("")
        with gr.Row():
            txt = gr.Textbox(
                placeholder="Type how you’re feeling...",
                label="Your Message",
                show_label=False,
                scale=4
            )
            send_btn = gr.Button("Send", scale=1)

        def user_message(user_input, history):
            response, new_history = generate_response(user_input, history)
            return [(user_input, response)], new_history, ""

        txt.submit(user_message, [txt, state], [chatbot, state, txt])
        send_btn.click(user_message, [txt, state], [chatbot, state, txt])

demo.launch()
