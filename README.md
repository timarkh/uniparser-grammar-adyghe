uniparser-grammar-adyghe
========================

(For English, see below.)

В этом репозитории находится морфологический анализатор для адыгейского языка, основанный на словаре и правилах. Анализатор был создан в рамках проекта по созданию [Корпуса адыгейского языка](http://adyghe.web-corpora.net/) и продолжает развиваться. Доля разобранных словоформ на литературных текстах составляет 83,7%.

Использованные правила сформулированы для адыгейского языка (в частности, мы предполагаем, что часть правил не должна работать для близкородственного кабардино-черкесского языка).

Тем не менее мы заинтересованы в сотрудничестве в связи с созданием корпусом других абхазо-адыгских языков – в первую очередь кабардино-черкесского.

По поводу возможного сотрудничества пишите авторам:
- <yulander@yandex.ru> Юрий Ландер
- <timarkh@gmail.com> Тимофей Архангельский

Анализатор состоит из следующих частей:
- грамматический словарь (``lexemes.txt``), в котором перечислены непроизводные лексемы, их основы, части речи и другие словарные категории, а также переводы на русский язык;
- основное формализованное описание парадигм (``paradigms.txt``);
- формализованное описание парадигм с частеречными переходами (``paradigms_NtoV.txt``) -- для случаев, когда, например, именные основы употребляются с глагольными аффиксами;
- дополнительные лексические правила, присваивающие вторичные леммы и переводы некомпозициональным сочетаниям основ и аффиксов (``lex_rules.txt``);
- набор правил, запрещающих некоторые разборы как невозможные (``bad_analyses.txt``);
- набор скриптов **UniParser** (папка ``UniParser``), которые осуществляют морфологический анализ.

Анализатором можно восользоваться следующими способами:

1. Использовать список размеченных слов (около 400 тысяч уникальных словоформ), встретившихся в текстах Адыгейского корпуса. Пожалуйста, свяжитесь с авторами, если Вы хотите использовать этот список (он слишком велик, чтобы его можно было хранить в репозитории).

2. Запустить анализатор на списке словоформ, составленном по Вашим текстам. Для этого нужно выполнить следующие шаги:
	- В папку ``UniParser`` нужно положить файлы ``lexemes.txt``, ``paradigms.txt``, ``lex_rules.txt`` и ``bad_analyses.txt``.
	- В ту же папку нужно положить частотный список словоформ, которые необходимо проанализировать. Список должен содержать на каждой строке одну словоформу, затем знак табуляции, а затем её частотность. (Частотности необходимы только для подсчёта процента разобранных словоформ; если Вам он не нужен, можно всем словам приписать частотность 1.) Файл со списком должен называться ``wordlist.csv``.
	- Запустить питоновский скрипт ``UniParser/analyze_adyghe.py`` и дождаться завершения его работы. (К сожалению, скрипт работает очень медленно: 50--200 словоформ словоформ в секунду, в зависимости от производительности компьютера.)

3. Вы можете преобразовать словарь в любой другой удобный Вам формат и использовать его таким образом в своей системе.

Все файлы распространяются по лицензии MIT (см. LICENSE.md).

English version
===============

This is a formalized description of literary Adyghe (West Circassian) morphology, which also includes a number of dialectal elements. The description is carried out in the UniParser format and involves following files:

- grammatical dictionary (``lexemes.txt``), which lists lexemes, their stems, POS and other tags, as well as Russian translations;
- main description of the paradigms (``paradigms.txt``);
- description of POS-changing paradigms (``paradigms_NtoV.txt``) intended for cases such as nouns inflected with verbal morphology;
- additional lexical rules that assign secondary lemmata and Russian translations to certain non-compositional combinations of stems and affixes (``lex_rules.txt``);
- rules prohibiting some parses as impossible (``bad_analyses.txt``);
- set of **UniParser** scripts (``UniParser`` directory) with a separate tweak for Adyghe data, which is used to analyze texts.

This description can be used for morphological analysis of Adyghe texts in the following ways:

1. Use a preannotated list of words (about 400 thousand unique forms), based on the West Circassian corpus. Please contact the authors if you would like to use it (it's too large to be stored in a repository).

2. Run the analyzer on a list of words that occur in your texts. Here is what you need to do:
	- Put ``lexemes.txt``, ``paradigms.txt``, ``lex_rules.txt`` and ``bad_analyses.txt`` to ``UniParser``.
	- Put a list of words to be analyzed to the same directory. It should contain one word per line, followed by a tab and the word's frequency. (Frequencies are only used to count the share of analyzed words; if you don't need it, you can just write 1 as each word's frequency.) This file should be named ``wordlist.csv``.
	- Run ``UniParser/analyze_adyghe.py`` with Python 3 and wait until it is done. (Unfortunately, it's rather slow; expect 50-200 words per second.)
	- Join the analyzed word lists from the three stages.
We are currently working of simplifying the pipeline.

3. Finally, you are free to convert/adapt the description to whatever kind of morphological analysis you prefer to use.

This software is distributed under the MIT license (see LICENSE.md).

