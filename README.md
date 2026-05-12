# 🤖 NorverGPT: The Next-Gen Multimodal AI Assistant

![NorverGPT Banner](https://shields.io)
![Status](https://shields.io)
![Platform](https://shields.io)

**NorverGPT** is a high-performance, intelligent AI platform that merges visual understanding with real-time global web research. Built for speed, memory retention, and accuracy, NorverGPT is designed to behave like a personal "Reasoning Engine" that can see, hear, and research the world just for you.

---

## 🚀 Key Features

### 👁️ Advanced Vision Engine
Equipped with the **Moondream2** local vision model, NorverGPT can analyze any image uploaded. It doesn't just label objects; it understands context. Ask it to describe a room, explain a complex diagram, or even write code based on a screenshot of a website.

### 🌐 Live Web Intelligence (Tavily Integration)
Unlike static AI models that are stuck in the past, NorverGPT has "Internet Eyes." Using the **Tavily Search API**, it browses the live web to find current news, prices, and facts, synthesizing them into a single, cohesive paragraph of truth.

### 🧠 Persistent Context Memory
NorverGPT features a **Gemini-style memory loop**. It remembers past instructions and the context of the conversation. If a secret is shared in the first message, it will remember it later.

### 💻 Developer-Ready (The NGPTS Library)
NorverGPT isn't just a website; it's a tool for builders. Using the `pip install NGPTS` command, developers can integrate the NorverGPT "Brain" directly into their own Python projects, apps, and robots.

---

## 🛠️ Technical Architecture

NorverGPT is built using a "Best-of-Breed" stack:
*   **Frontend:** [Streamlit](https://streamlit.io) for a clean, responsive, and dark-themed UI.
*   **Model Hosting:** [Hugging Face Spaces](https://huggingface.co) for 24/7 cloud availability.
*   **Vision Brain:** [Moondream2](https://huggingface.co) (Auto-Regressive Vision-Language Model).
*   **Search Engine:** [Tavily AI](https://tavily.com) for LLM-optimized web scraping.
*   **Language:** Python 3.11 with [PyTorch](https://pytorch.org) and [Transformers](https://huggingface.co).

---

## 🔧 Installation & Usage

### For Users:
Access the live version at **[norvergpt.com](https://norvergpt.com)**. No installation is required.

### For Developers (Local Run):
1.  **Clone the Repo:**
    ```bash
    git clone https://github.com
    cd Norver-GPT
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Launch the AI:**
    ```bash
    streamlit run app.py
    ```

---

## 🗺️ Roadmap
-   [x] Multimodal Image Support
-   [x] Live Web Search Integration
-   [x] Conversation History & Memory
-   [ ] Voice Input & Speech Synthesis (Coming Soon)
-   [ ] Mobile App (iOS/Android)
-   [ ] PDF & Document Analysis

---

## 📄 License & Credits
Developed by **Narjistudio**.
Special thanks to the Hugging Face community and the Tavily AI team for providing the infrastructure that powers NorverGPT.

---

© 2026 NorverGPT. All Rights Reserved.
