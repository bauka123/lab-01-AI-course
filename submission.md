# Lab 01 — The Price of One Request

## 1. Prediction vs measured value

Before Part 2, I predicted the token ratio using UTF-8 byte size.

| Language | Prediction | Measured |
|---|---:|---:|
| RU / EN | 1.92x | 1.46x |
| KK / EN | 2.13x | 2.15x |

For the Claude Opus 5 reference measurement, the COMPLAINT used:

- English: 92 tokens
- Russian: 134 tokens
- Kazakh: 198 tokens

The Russian prediction was higher than the measured value. The Kazakh prediction was very close. This shows that byte size is only an approximation because tokenization depends on the tokenizer vocabulary.

Note: I used the provided `measurements.example.json` reference run because the classroom API key was not available.

## 2. Annual cost

I chose 5,000 support requests per day because this is a reasonable example volume for a large digital customer support service.

This gives 1,825,000 requests per year.

| Model | English | Russian | Kazakh |
|---|---:|---:|---:|
| Haiku 4.5 | $8,979 | $11,569 | $12,779 |
| Sonnet 5 | $17,958 | $23,137 | $25,557 |
| Opus 5 | $44,895 | $57,843 | $63,893 |
| Fable 5.1 | $89,790 | $115,687 | $127,786 |

For the full request, Kazakh uses 317 input tokens compared with 145 for English. On Opus 5, the total Kazakh bill is about 1.42x the English bill.

## 3. Production choice

For a Kazakh-language support queue, I would use Sonnet 5 as a production candidate.

Its estimated annual cost for Kazakh at 5,000 requests per day is $25,557, compared with $63,893 for Opus 5.

Haiku 4.5 is cheaper at $12,779, but I would not choose a support model only by price. Before production, I would test answer quality in Kazakh, accuracy, instruction following, and whether the model gives a clear next step to the customer.

Sonnet 5 gives a reasonable balance between cost and expected quality for this use case.

## 4. Cost-reduction lever

A cost-reduction lever not used in this lab is prompt caching: the repeated system prompt can be cached instead of paying its full input cost for every request.
