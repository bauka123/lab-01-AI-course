"""Parallel test corpus for Lab 01.

The same three items in English, Russian and Kazakh. Parallel meaning is the
point: any difference in token count is a property of the tokenizer, not of
what is being said.

Instructors: the Kazakh and Russian wordings are a starting point. Substitute
your own if you prefer -- but keep the three versions semantically parallel,
otherwise the comparison measures translation length instead of tokenization.
"""

from __future__ import annotations

from typing import Dict

LANGUAGES = ("en", "ru", "kk")

#: One sentence. Short enough to inspect token by token.
SENTENCE: Dict[str, str] = {
    "en": "The bank raised interest rates by two percentage points last quarter.",
    "ru": "Банк повысил процентные ставки на два процентных пункта в прошлом квартале.",
    "kk": "Банк өткен тоқсанда пайыздық мөлшерлемені екі пайыздық тармаққа көтерді.",
}

#: A realistic support request -- the kind of text a production system pays for
#: thousands of times a day.
COMPLAINT: Dict[str, str] = {
    "en": (
        "Good afternoon. I opened a deposit at your branch in March and was told "
        "the rate was fixed for twelve months. In August the rate on my account "
        "dropped without any notice. I have attached the contract and the "
        "statement. Please explain on what basis the rate was changed and "
        "restore the original terms."
    ),
    "ru": (
        "Добрый день. Я открыл депозит в вашем отделении в марте, и мне сказали, "
        "что ставка зафиксирована на двенадцать месяцев. В августе ставка по "
        "моему счёту снизилась без какого-либо уведомления. Прилагаю договор и "
        "выписку. Прошу объяснить, на каком основании была изменена ставка, и "
        "восстановить первоначальные условия."
    ),
    "kk": (
        "Қайырлы күн. Мен наурыз айында сіздің бөлімшеңізде депозит аштым, маған "
        "мөлшерлеме он екі айға бекітілген деп айтылды. Тамыз айында менің "
        "шотымдағы мөлшерлеме ешқандай хабарламасыз төмендеді. Шартты және "
        "үзінді көшірмені қоса тіркеп отырмын. Мөлшерлеме қандай негізде "
        "өзгертілгенін түсіндіріп, бастапқы шарттарды қалпына келтіруіңізді "
        "сұраймын."
    ),
}

#: A system prompt -- the part you resend on every single request.
SYSTEM_PROMPT: Dict[str, str] = {
    "en": (
        "You are a support assistant for a retail bank. Answer only from the "
        "documents provided. If the answer is not in them, say so. Never invent "
        "an account number, a rate or a date."
    ),
    "ru": (
        "Вы — ассистент поддержки розничного банка. Отвечайте только по "
        "предоставленным документам. Если ответа в них нет, так и скажите. "
        "Никогда не выдумывайте номер счёта, ставку или дату."
    ),
    "kk": (
        "Сіз — бөлшек банктің қолдау көрсету ассистентісіз. Тек берілген "
        "құжаттар бойынша жауап беріңіз. Егер жауап оларда болмаса, солай деп "
        "айтыңыз. Шот нөмірін, мөлшерлемені немесе күнді ешқашан ойдан "
        "шығармаңыз."
    ),
}

#: My own support request for Core Task 1.
TRANSFER_NOTICE: Dict[str, str] = {
    "en": (
        "Yesterday I sent money to another bank, but the transfer is still pending. "
        "The amount was deducted from my account. Please check the transfer status "
        "and tell me when the money will arrive."
    ),
    "ru": (
        "Вчера я отправил деньги в другой банк, но перевод всё ещё находится в обработке. "
        "Сумма была списана с моего счёта. Пожалуйста, проверьте статус перевода "
        "и сообщите, когда поступят деньги."
    ),
    "kk": (
        "Кеше мен басқа банкке ақша аудардым, бірақ аударым әлі өңделіп жатыр. "
        "Сома менің шотымнан алынды. Аударымның мәртебесін тексеріп, "
        "ақшаның қашан түсетінін хабарлаңыз."
    ),
}

#: Kazakh sentence using only Cyrillic letters shared with Russian.
KAZAKH_SHARED: Dict[str, str] = {
    "en": (
        "The bank will inform the client about the card, and the operator "
        "will write an answer about the account and status."
    ),
    "ru": (
        "Банк сообщит клиенту о карте, а оператор напишет ответ "
        "о счёте и статусе."
    ),
    "kk": (
        "Банк клиентке карта туралы хабар берер, ал оператор "
        "шот пен статус туралы жауап жазар."
    ),
}

#: Kazakh sentence rich in Kazakh-specific letters.
KAZAKH_SPECIFIC: Dict[str, str] = {
    "en": (
        "The administration checked the processing status of the request today "
        "and explained the change concerning the payment and document."
    ),
    "ru": (
        "Администрация сегодня проверила статус обработки обращения "
        "и объяснила изменение, связанное с платежом и документом."
    ),
    "kk": (
        "Әкімшілік өтініштің өңделу жағдайын бүгін тексеріп, "
        "төлем мен құжат жөніндегі өзгерісті түсіндірді."
    ),
}

#: Complaint represented as JSON instead of prose.
COMPLAINT_JSON: Dict[str, str] = {
    "en": (
        '{"greeting":"Good afternoon.","deposit":"I opened a deposit at your branch in March '
        'and was told the rate was fixed for twelve months.","change":"In August the rate on '
        'my account dropped without any notice.","attachments":"I have attached the contract '
        'and the statement.","request":"Please explain on what basis the rate was changed and '
        'restore the original terms."}'
    ),
    "ru": (
        '{"greeting":"Добрый день.","deposit":"Я открыл депозит в вашем отделении в марте, '
        'и мне сказали, что ставка зафиксирована на двенадцать месяцев.","change":"В августе '
        'ставка по моему счёту снизилась без какого-либо уведомления.","attachments":"Прилагаю '
        'договор и выписку.","request":"Прошу объяснить, на каком основании была изменена '
        'ставка, и восстановить первоначальные условия."}'
    ),
    "kk": (
        '{"greeting":"Қайырлы күн.","deposit":"Мен наурыз айында сіздің бөлімшеңізде депозит '
        'аштым, маған мөлшерлеме он екі айға бекітілген деп айтылды.","change":"Тамыз айында '
        'менің шотымдағы мөлшерлеме ешқандай хабарламасыз төмендеді.","attachments":"Шартты '
        'және үзінді көшірмені қоса тіркеп отырмын.","request":"Мөлшерлеме қандай негізде '
        'өзгертілгенін түсіндіріп, бастапқы шарттарды қалпына келтіруіңізді сұраймын."}'
    ),
}

#: Everything the lab measures, keyed by a short id.
CORPUS: Dict[str, Dict[str, str]] = {
    "sentence": SENTENCE,
    "complaint": COMPLAINT,
    "system_prompt": SYSTEM_PROMPT,
    "transfer_notice": TRANSFER_NOTICE,
    "kazakh_shared": KAZAKH_SHARED,
    "kazakh_specific": KAZAKH_SPECIFIC,
    "complaint_json": COMPLAINT_JSON,
}
