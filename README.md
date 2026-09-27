# SmartKey – NLP-Based Keyword Extraction

## 📌 Project Overview

**SmartKey** is a simple Natural Language Processing (NLP) project that automatically extracts the most important keywords from a given paragraph.

The project uses the **RAKE (Rapid Automatic Keyword Extraction)** algorithm to identify important words and phrases from text.

No dataset or model training is required.

---

## 🎯 Objective

The main objective of this project is to demonstrate how NLP techniques can be used to identify important keywords from unstructured text.

---

## ⚙️ Technologies Used

| Technology | Purpose                             |
| ---------- | ----------------------------------- |
| Python     | Programming Language                |
| NLP        | Text Processing                     |
| RAKE-NLTK  | Keyword Extraction                  |
| NLTK       | Natural Language Processing Library |

---

## ✨ Features

* Accepts text directly from the user
* Extracts important keywords and phrases
* Displays keyword scores
* No dataset required
* No machine learning model training required
* Simple and beginner-friendly

---

## 📂 Project Structure

```text
SmartKey/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🔄 Working Process

```text
User Input
    ↓
Text Processing
    ↓
RAKE Algorithm
    ↓
Keyword Scoring
    ↓
Important Keywords
```

---

## 🛠️ Installation

### 1. Install Python

Make sure Python is installed on your computer.

Check using:

```bash
python --version
```

### 2. Install Required Library

Open the terminal inside the project folder and run:

```bash
pip install rake-nltk
```

---

## ▶️ How to Run

Run the following command:

```bash
python main.py
```

Enter a paragraph when prompted.

### Example Input

```text
Artificial intelligence is transforming healthcare through
machine learning, medical diagnosis, and intelligent systems.
```

### Example Output

```text
Important Keywords:

- artificial intelligence
- intelligent systems
- machine learning
- medical diagnosis
- healthcare
```

---

## 🧠 NLP Technique

### RAKE

RAKE stands for **Rapid Automatic Keyword Extraction**.

It identifies important words and phrases from a document by analyzing word frequency and relationships between words.

The extracted keywords are then ranked according to their scores.

---

## 📊 Advantages

* Easy to implement
* Does not require a dataset
* Fast execution
* Simple to understand
* Useful for text analysis

---

## 🔮 Future Scope

The project can be extended to:

* Build a graphical user interface
* Process uploaded text files
* Extract keywords from PDF documents
* Add multilingual keyword extraction
* Display keywords using charts or word clouds

---

## 👩‍💻 Author

**Kavya Balsaraf**

**Department:** Electronics and Telecommunication Engineering

**Project:** SmartKey – NLP-Based Keyword Extraction

---

## 📜 License

This project is created for **educational and academic purposes**.
