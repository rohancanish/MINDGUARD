---
license: mit
language:
  - en
base_model:
  - unsloth/llama-3.2-3b-instruct-unsloth-bnb-4bit

title: 🧠 MindGuard - Mental Health AI Chatbot
emoji: 🧘‍♂️
colorFrom: pink
colorTo: purple
sdk: docker
sdk_version: "1.0"
app_file: app.py
pinned: false
models:
  - unsloth/llama-3.2-3b-instruct-unsloth-bnb-4bit
  - mthabet00/serenity-AI_Therapist
tags:
  - mental-health
  - chatbot
  - ai-therapist
  - gradio
  - peft
  - lora
  - transformers
  - unsloth
gpu: true
---

# 🧠 MindGuard: Mental Health Chatbot

MindGuard is an empathetic, AI-powered mental health companion built using large language models. It is designed to offer supportive, non-judgmental conversations for users who are feeling emotionally overwhelmed, stressed, or in need of someone to talk to.

---

## 💡 What It Does

- Provides comforting, human-like responses using an LLM fine-tuned for therapeutic dialogue.
- Retains context to maintain natural conversations.
- Designed with compassion, emotional sensitivity, and mental well-being in mind.

---

# How It Works
---

MindGuard uses:

- **Base Model:** `unsloth/llama-3.2-3b-instruct-unsloth-bnb-4bit`  
- **PEFT Fine-Tuned Model:** `mthabet00/serenity-AI_Therapist`  
  (Using PEFT for efficient, low-resource fine-tuning)

The chatbot is deployed using **Gradio**, offering a simple and safe UI for users to type their thoughts and receive emotionally aware replies.

# 🚀 Running the Project
---

This Space automatically runs:

- `app.py`

# 🛡️ Disclaimer
---

MindGuard is **not a substitute for professional mental health care**.  
If you are in crisis or need help, please reach out to certified professionals or hotlines in your region.

# 📜 License
---

MIT License

# 🙌 Acknowledgements
---

- [Unsloth](https://huggingface.co/unsloth)  
- [Serenity AI Therapist](https://huggingface.co/mthabet00/serenity-AI_Therapist)  
- Hugging Face 🤗
