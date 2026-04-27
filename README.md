# CSharpForge  
### AI‑Assisted C# Code Generation & Deep Analysis  
Created By: **David Kistner (Unconditional Love)**  
GlyphicMind Solutions LLC

CSharpForge is a standalone Forge‑series tool designed to generate, refactor, analyze, and enhance **C# code** using local LLMs (.gguf models via llama.cpp).  
It mirrors the architecture of PythonForge and JavaScriptForge, providing a unified workflow across all languages in the Forge ecosystem.

---

---

## 🚀 Features

### 🔹 Local‑Only LLM Execution  
Runs entirely on your machine using **llama‑cpp‑python** and `.gguf` models defined in `models/manifest.yaml`.

### 🔹 Tabbed IDE‑Style GUI  
Built with PyQt5, featuring:
- Topic / Corrections  
- Raw LLM Output  
- Extracted Code (append‑only)  
- Master Code (primary workspace)  
- Deep Analysis Log  

### 🔹 Deep Analysis v2 (C#‑Aware)  
Understands:
- namespaces  
- classes  
- methods  
- inheritance  
- logic flow  
- architectural relationships  

### 🔹 Multi‑Model Support  
Switch between models instantly using the model selector.

### 🔹 Pending / Saved Workflow  
- **Forge → Pending** writes branded `.cs` files into `storage/pending`  
- **Save File** writes curated code into `storage/saved`  

### 🔹 Brand Tag Injection  
Every generated file includes:

```csharp
//--- Created with GlyphicMind Solutions: CSharpForge ---//

```

---


### 📦 Project Structure

```
CSharpForge/
    csharpforge.py
    engine/
        llm_engine.py
        deep_analysis.py
        forge_writer.py
    gui/
        csharpforge_window.py
    prompt/
        prompt_builder.py
    models/
        manifest.yaml
    storage/
        logs/
        pending/
        saved/
    config/
        settings.json

```
---

### ▶️ Running CSharpForge

- From inside the project directory:

```
python csharpforge.py

```

- Make sure your virtual environment includes:

```
PyQt5
llama-cpp-python
PyYAML

```
(See requirements.txt.)

---

### 🧠 Part of the Forge Suite

- CSharpForge is one tool in the expanding Forge ecosystem:

-   -PythonForge

-   -JavaScriptForge

-   -CSharpForge

-   -CppForge (coming)

-   -RustForge (coming)

-   -GoForge (coming)

-   -HTML/CSS Forge (coming)

-   -SQLForge (coming)


