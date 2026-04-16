# Italian Anki Flashcard Generator

This is a simple Python project I built to improve my Italian learning process.

## Why I built this

While learning Italian, I realized that only reading words is not enough.  
I wanted a better way to learn:

- the actual base verb
- the meaning in Bangla
- synonyms
- present, past, and future tense
- example sentences

So I built this small Python tool to create and update Anki flashcards automatically.

## What this project does

This script reads structured data from text files and creates or updates Anki flashcards using AnkiConnect.

Each card can include:

- FORM (the word form found in the book)
- WORD (the actual base word / infinitive)
- Bangla meaning
- Italian synonyms
- Present / Past / Future forms
- Italian example sentence
- Bangla meaning of the example sentence

## Book source

I am learning from the book:

**FACILE - Libro di Italiano per Studenti Stranieri**  
by **Paolo Cassaiani and Laura Mattioli**

I collect words page by page from this book and turn them into flashcards for repeated practice.

## Project structure

```text
italian-anki-flashcard-generator/
├── anki_page_importer.py
├── requirements.txt
├── cards.txt
└── pages/
    ├── page_1.txt
    ├── page_2.txt
    ├── page_3.txt
    └── page_4.txt

Eample:
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
How to Run:
1. Go to CMD
2. Go to folder through CMD
3. Then run : python anki_page_importer.py --root-deck "Italian-Flashcards" --page "Page-1" --txt "pages/page_1.txt"
