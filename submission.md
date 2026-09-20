# Lab 01 — The Price of One Request

## Part 1 — Prediction

Before running Part 2, I predicted the token ratios for the COMPLAINT:

- RU / EN = 1.92x
- KK / EN = 2.13x

I based my prediction on UTF-8 bytes.

Russian complaint:
576 / 300 = 1.92x

Kazakh complaint:
640 / 300 = 2.13x

I chose bytes because tokenizers process encoded text and byte size can be a useful rough indicator. However, the real token count also depends on the tokenizer vocabulary and its tokenization rules, so the measured ratios may be different.
