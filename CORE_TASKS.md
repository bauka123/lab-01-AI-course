# Lab 01 — Core Tasks

## Core Task 1 — My own corpus item

I added a new banking support request called `transfer_notice` in English, Russian and Kazakh.

### Token ratios

| Tokenizer | RU / EN | KK / EN |
|---|---:|---:|
| o200k_base | 1.35x | 1.59x |
| cl100k_base | 2.27x | 3.43x |

The offline measurements showed:

- EN bytes/char: 1.00
- RU bytes/char: 1.82
- KK bytes/char: 1.84

Kazakh required more tokens than English, especially with `cl100k_base`.

## Core Task 2 — Kazakh premium

I compared two Kazakh sentences: one mainly using letters shared with Russian and another containing more Kazakh-specific letters.

| Text | o200k_base KK tokens | cl100k_base KK tokens | KK bytes/char |
|---|---:|---:|---:|
| Kazakh shared | 21 | 43 | 1.83 |
| Kazakh specific | 31 | 91 | 1.87 |

The byte-per-character values are almost the same, but the token counts are very different.

This shows that the extra token cost is caused mainly by tokenizer vocabulary and merge rules, not simply by UTF-8 byte size. The difference is especially large with `cl100k_base`.

## Core Task 3 — Prose vs JSON

Before measuring, I expected JSON to require more tokens because it adds braces, quotation marks, field names, colons and commas.

### Token counts

| Tokenizer | Format | EN | RU | KK |
|---|---|---:|---:|---:|
| o200k_base | Prose | 59 | 80 | 118 |
| o200k_base | JSON | 72 | 93 | 131 |
| o200k_base | Extra | +13 | +13 | +13 |
| cl100k_base | Prose | 59 | 146 | 265 |
| cl100k_base | JSON | 72 | 158 | 278 |
| cl100k_base | Extra | +13 | +12 | +13 |

JSON added approximately the same absolute overhead in all three languages. The punctuation and English field names are mostly language-independent, so the extra token count stays close to constant.
