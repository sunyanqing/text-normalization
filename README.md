A text-normalization toolkit for Chinese
================================

Want a text normalizing for Chinese texts? Here it is!

Forked from https://github.com/soshial/text-normalization which is too out of dated.

Typical features of modes:
------------------
- Support Chinese now.
- Replaced old numword with [num2words](https://github.com/savoirfairelinux/num2words), which had better support with more and more languages.
- update `num_base.py` and add `num_zh` to work with new added num2words.
- Remove dependency of regx, nltk and MySQL, you can run `normalization.py` which is much easier to setup

Any problem, feel free to contact me ^_^






The original README is kept just as it was:
------------------

This library is used for normalizing ru/en texts, according to http://en.wikipedia.org/wiki/Text_normalization
Best suites  for Text-to-Speech text normalizing.

The library is licensed under LGPL v3, full text of which can be found at http://www.gnu.org/copyleft/lesser.html
All sql files are licensed under GNU FDL.

Prerequisites:
* python 2.7 + libs: regex, nltk (+ download 'punkt' package), MySQLdb, ConfigParser
* pymorphy (install.sh converts AOT dics, than copy them into /normalization/dics directory)
* upgraded numword library (http://code.google.com/p/numword/, which is based on pynum2word) is already inluded

How to use:
    ./normalization/main.py [language] [in_folder] [out_folder]
    you should specify 2-letter [langugage] and [IN folder] with files to process and [OUT folder] to put the result
    the main script is a loop that processes all files from IN folder, which have .meta duplicates

There also should be ./normalization/normalization.cfg which specifies database detailsand russian AOT paths
    [db]
    host:...
    user:...
    passwd:...
    db:...

    [lms]
    rml_path:~/ling2/rml/
    aot_path:~/ling2/
    dicts:~/text-normalization/dicts/converted/ru/

numword lib (without num wrappers) is quite handy if you need to get text from any float or integer variable.
    There is also an easy way for inflecting numbers in Russian:
        >>> from numword import numword_ru
        >>> numw_class = numword_ru.NumWordRU()
        >>> numw_class.inflection_case = u'вн,мн,жр'
        >>> numw_class.ordinal(325002)
        ТРИСТА ДВАДЦАТЬ ПЯТЬ ТЫСЯЧ ДВЕ
