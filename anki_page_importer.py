import argparse
import sys
from pathlib import Path

import requests

ANKI_CONNECT = "http://127.0.0.1:8765"


def invoke(action, **params):
    r = requests.post(
        ANKI_CONNECT,
        json={"action": action, "version": 6, "params": params},
        timeout=30
    )
    r.raise_for_status()
    data = r.json()
    if data.get("error"):
        raise RuntimeError(data["error"])
    return data["result"]


def ensure_deck(deck_name):
    try:
        invoke("createDeck", deck=deck_name)
    except Exception:
        pass


def autodetect_fields(model_name):
    fields = invoke("modelFieldNames", modelName=model_name)
    front = fields[0] if len(fields) > 0 else "Front"
    back = fields[1] if len(fields) > 1 else "Back"
    return front, back, fields


def find_existing_notes(deck_name, front_field, front_text):
    query = f'deck:"{deck_name}" "{front_field}:{front_text}"'
    return invoke("findNotes", query=query)


def get_notes_info(note_ids):
    if not note_ids:
        return []
    return invoke("notesInfo", notes=note_ids)


def update_note(note_id, front_field, back_field, front_text, back_text):
    return invoke(
        "updateNoteFields",
        note={
            "id": note_id,
            "fields": {
                front_field: front_text,
                back_field: back_text
            }
        }
    )


def add_note(deck_name, model_name, front_field, back_field, front_text, back_text, tags=None):
    note = {
        "deckName": deck_name,
        "modelName": model_name,
        "fields": {
            front_field: front_text,
            back_field: back_text
        },
        "options": {
            "allowDuplicate": False,
            "duplicateScope": "deck"
        },
        "tags": tags or []
    }
    return invoke("addNote", note=note)


def parse_cards(txt_path):
    path = Path(txt_path)

    if not path.exists():
        print(f"File not found: {txt_path}", file=sys.stderr)
        sys.exit(1)

    content = path.read_text(encoding="utf-8").strip()
    if not content:
        return []

    blocks = [b.strip() for b in content.split("---") if b.strip()]
    cards = []

    for block in blocks:
        card = {}

        for line in block.splitlines():
            line = line.strip()
            if not line or ":" not in line:
                continue

            key, value = line.split(":", 1)
            key = key.strip().upper()
            value = value.strip()

            card[key] = value

        # minimum required fields
        if "WORD" not in card or "BN" not in card:
            continue

        cards.append(card)

    return cards


def build_back_text(card):
    base = card.get("WORD", "")
    form = card.get("FORM", "")
    synonyms = card.get("SYNONYMS", "")
    present = card.get("PRESENT", "")
    past = card.get("PAST", "")
    future = card.get("FUTURE", "")
    ex_it = card.get("EXAMPLE_IT", "")
    ex_bn = card.get("EXAMPLE_BN", "")

    parts = [f"<b>Base Verb:</b> {base}"]

    if form:
        parts.append(f"<b>Given Form:</b> {form}")

    if synonyms:
        parts.append(f"<b>Synonyms:</b> {synonyms}")

    if present:
        parts.append(f"<b>Present:</b><br>{present}")

    if past:
        parts.append(f"<b>Past:</b><br>{past}")

    if future:
        parts.append(f"<b>Future:</b><br>{future}")

    if ex_it:
        parts.append(f"<b>Example:</b><br>{ex_it}")

    if ex_bn:
        parts.append(f"{ex_bn}")

    return "<br><br>".join(parts)


def main():
    ap = argparse.ArgumentParser(
        description="Import Bangla-front / Italian-back flashcards into Anki from one txt file."
    )
    ap.add_argument("--root-deck", required=True, help="Main/root deck name, e.g. Italian-Flashcards")
    ap.add_argument("--page", required=True, help="Subdeck/page name, e.g. Page-1")
    ap.add_argument("--txt", required=True, help="Text file path, e.g. cards.txt")
    ap.add_argument("--model", default="Basic", help="Anki note type, default: Basic")
    ap.add_argument("--tag", action="append", help="Optional tag; use multiple times if needed")
    args = ap.parse_args()

    full_deck = f"{args.root_deck}::{args.page}"

    try:
        ensure_deck(args.root_deck)
        ensure_deck(full_deck)

        front_field, back_field, fields = autodetect_fields(args.model)

        print(f"Using model: {args.model}")
        print(f"Detected fields: {fields}")
        print(f"Front field: {front_field}")
        print(f"Back field: {back_field}")

        cards = parse_cards(args.txt)
        if not cards:
            print("No valid cards found in file.", file=sys.stderr)
            sys.exit(1)

        added = 0
        updated = 0
        skipped = 0

        for card in cards:
            front_text = card["BN"]  # Bangla on front
            back_text = build_back_text(card)

            existing_ids = find_existing_notes(full_deck, front_field, front_text)

            if existing_ids:
                infos = get_notes_info(existing_ids)
                changed = False

                for info in infos:
                    current_back = info["fields"].get(back_field, {}).get("value", "").strip()

                    if current_back != back_text.strip():
                        update_note(
                            info["noteId"],
                            front_field,
                            back_field,
                            front_text,
                            back_text
                        )
                        updated += 1
                        changed = True
                    else:
                        skipped += 1

                if not changed and infos:
                    pass
            else:
                add_note(
                    deck_name=full_deck,
                    model_name=args.model,
                    front_field=front_field,
                    back_field=back_field,
                    front_text=front_text,
                    back_text=back_text,
                    tags=args.tag
                )
                added += 1

        print()
        print(f"Deck: {full_deck}")
        print(f"From file: {args.txt}")
        print(f"Total blocks read: {len(cards)}")
        print(f"Added: {added} | Updated: {updated} | Skipped: {skipped}")

    except requests.exceptions.ConnectionError:
        print("Could not connect to AnkiConnect. Make sure Anki is open and AnkiConnect is installed.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()