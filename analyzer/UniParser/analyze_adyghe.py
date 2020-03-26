from analyze import analyze
from postprocessor import finalize, split_o_wordlist

if __name__ == '__main__':
    lexFile = '../lexemes.txt'
    lexRulesFile = '../lex_rules.txt'
    derivFile = '../derivations.txt'
    conversionFile = '../stem_conversions.txt'
    cliticFile = '../clitics.txt'
    delAnaFile = '../bad_analyses.txt'
    freqListSeparator = '\t'
    parserVerbosity = 0
    parsingMethod = 'fst'
    errorFile = None
    parsedFile = None
    unparsedFile = None
    xmlOutput = True
    analyze('../wordlist_full.csv', '../paradigms.txt', lexFile, lexRulesFile, derivFile, conversionFile,
            cliticFile, delAnaFile, '../wordlist.csv-parsed-main.txt', '../wordlist.csv-unparsed-main.txt',
            errorFile, xmlOutput, False, parserVerbosity, freqListSeparator, parsingMethod=parsingMethod)
    split_o_wordlist('../wordlist_full.csv', '../wordlist.csv-unparsed-main.txt')
    analyze('../wordlist-unparsed-all.csv', '../paradigms-NtoV.txt', lexFile, lexRulesFile, derivFile, conversionFile,
            cliticFile, delAnaFile, '../wordlist.csv-parsed-NtoV.txt', '../wordlist.csv-unparsed-NtoV.txt',
            errorFile, xmlOutput, False, parserVerbosity, freqListSeparator, parsingMethod=parsingMethod)
    analyze('../wordlist-o.csv', '../paradigms.txt', lexFile, lexRulesFile, derivFile, conversionFile,
            cliticFile, delAnaFile, '../wordlist.csv-parsed-o.txt', '../wordlist.csv-unparsed-o.txt',
            errorFile, xmlOutput, False, parserVerbosity, freqListSeparator, parsingMethod=parsingMethod)
    finalize()
