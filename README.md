# Italian (Language) Anki Flashcard Generator (Python Automation Tool)

This is a simple Python project I built to improve my Italian learning process in a more structured and efficient way.

---

## 💡 Why I built this

While learning Italian, I realized that just reading words is not enough.

I needed a better system to:

* Understand the **actual base verb (infinitive)**
* Learn meanings in **Bangla**
* See **synonyms**
* Practice **present, past, and future tense**
* Learn through **real example sentences**

So I built this Python tool to automatically create and update Anki flashcards.

---

## ⚙️ What this project does

This script:

* Reads structured data from text files
* Creates or updates flashcards in Anki using **AnkiConnect**

Each card includes:

* **FORM** → word as found in the book
* **WORD** → base verb (infinitive)
* **Bangla meaning**
* **Italian synonyms**
* **Present / Past / Future tense**
* **Example sentence (Italian + Bangla)**

---

## 📘 Book Source

I am learning from the book:

**"FACILE - Libro di Italiano per Studenti Stranieri"**
by **Paolo Cassaiani and Laura Mattioli**

For each page:

1. I collect vocabulary
2. Convert them into structured flashcards
3. Practice them using Anki

---

## 📁 Project Structure

```
italian-anki-flashcard-generator/
├── anki_page_importer.py
├── requirements.txt
└── pages/
    ├── page_1.txt
    ├── page_2.txt
    ├── page_3.txt
    └── page_4.txt
```

---

## 📄 Example Input and Output

```
FORM: nata
WORD: nascere
BN: জন্মগ্রহণ করা
SYNONYMS: venire al mondo
PRESENT: nasco, nasci, nasce, nasciamo, nascete, nascono
PAST: sono nato/a, sei nato/a, è nato/a, siamo nati/e, siete nati/e, sono nati/e
FUTURE: nascerò, nascerai, nascerà, nasceremo, nascerete, nasceranno
EXAMPLE_IT: Sono nata a Roma.
EXAMPLE_BN: আমি রোমে জন্মেছি।
---
```

---

## 🎯 Goal

My goal is to build a consistent learning system using:

* Python
* Anki
* Structured repetition

I will continue updating this repository as I learn more.

👉 This method can be used by anyone to learn any language in a structured way.

---

## 🔧 Requirements

* Python
* requests
* Anki
* AnkiConnect add-on

---

## ⭐

This is a personal learning project.
I will keep improving it as I continue my Italian learning journey.



## 🚀 How to Run (Step-by-Step)

Follow these steps to run the project on your own machine:

### 1. Install Python Requirements

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

---

### 2. Install Anki and AnkiConnect

1. Install **Anki Desktop**
2. Open Anki
3. Go to:
   `Tools → Add-ons → Get Add-ons`
4. Enter this code:

```
2055492159
```

5. Click OK and restart Anki

👉 Important: Keep Anki open while running the script

---

### 3. Prepare Your Input File

Go to the `pages/` folder and create a file like:

```bash
pages/page_1.txt
```

Add content like this:

```
FORM: nata
WORD: nascere
BN: জন্মগ্রহণ করা
SYNONYMS: venire al mondo
PRESENT: nasco, nasci, nasce, nasciamo, nascete, nascono
PAST: sono nato/a, sei nato/a, è nato/a, siamo nati/e, siete nati/e, sono nati/e
FUTURE: nascerò, nascerai, nascerà, nasceremo, nascerete, nasceranno
EXAMPLE_IT: Sono nata a Roma.
EXAMPLE_BN: আমি রোমে জন্মেছি।
---
```

---

### 4. Run the Script

Open Command Prompt and run:

```bash
python anki_page_importer.py --root-deck "Italian-Flashcards" --page "Page-1" --txt "pages/page_1.txt"
```

---

### 5. Check Anki

* Open Anki
* You will see a new deck:
  `Italian-Flashcards → Page-1`
* Your flashcards will be created automatically

---

### 🔁 Add More Pages

For a new page:

1. Create a new file:

```
pages/page_2.txt
```

2. Run:

```bash
python anki_page_importer.py --root-deck "Italian-Flashcards" --page "Page-2" --txt "pages/page_2.txt"
```

---

### ⚠️ Notes

* File name and page name should match (page_1 → Page-1)
* Each card must end with `---`
* Keep Anki open while running the script

