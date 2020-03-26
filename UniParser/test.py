import grammar
import morph_parser
import time
import json


def load_test_data(fname):
    testData = {}
    fTest = open(fname, 'r', encoding='utf-8-sig')
    lines = [line.strip() for line in fTest.readlines() if '\t' in line]
    for line in lines:
        wf, analyses = line.split('\t')
        analyses = json.loads(analyses)
        testData[wf] = analyses
    fTest.close()
    print('Test data loaded.')
    return testData


def test_wf(parser, wf, analyses):
    """
    Test whether a single wordform is analyzed by the parser
    in the way described by the list of analyses. Each element of the
    analyses list is a dictionary where keys represent properties
    of the Wordform objects. If an actual analysis has more non-empty
    fields than specified in the dictionary, these are not taken
    into account.
    Return a report string.
    """
    if type(analyses) != list:
        return 'Wrong test data: list of analyses expected.'
    realAnalyses = parser.parse(wf)
    if len(realAnalyses) != len(analyses):
        return 'FAILED: ' + str(len(analyses)) + ' expected, ' +\
               str(len(realAnalyses)) + ' given.'
    correctAna = [False] * len(realAnalyses)
    for ana in analyses:
        for iRealAna in range(len(realAnalyses)):
            bAnalysisConforms = True
            for k, v in ana.items():
                try:
                    realValue = realAnalyses[iRealAna].__dict__[k]
                    if realValue != v:
                        bAnalysisConforms = False
                        break
                except KeyError:
                    if any(d[0] == k and d[1] == v
                           for d in realAnalyses[iRealAna].otherData):
                        continue
                    bAnalysisConforms = False
                    break
            if bAnalysisConforms:
                correctAna[iRealAna] = True
    if all(correctAna):
        return 'OK'
    return 'FAILED'


def perform_tests(parser, testData):
    """
    Check if the wordforms in the testData dictionary
    are analyzed correctly by the parser.
    Return a report string.
    """
    if parser is None:
        return 'The parser is not initialized, exiting tests.'
    t1 = time.clock()
    report = ''
    for wf in sorted(testData, key=lambda w: (len(w), w)):
        report += wf + ': ' + test_wf(parser, wf, testData[wf]) + '\n'
    print(time.clock() - t1, ' seconds for performing the tests.')
    return report


t1 = time.clock()
g = grammar.Grammar(verbose=True)
print(g.load_paradigms('test/paradigms_simple.txt', compileParadigms=True), 'simple paradigms loaded.')
print(g.load_paradigms('test/paradigms_polysynth.txt', compileParadigms=True), 'polysynthetic paradigms loaded.')
print(g.load_paradigms('test/paradigms_agglutinative.txt', compileParadigms=True), 'right-branching agglutinative paradigms loaded.')
print(g.load_derivations('test/derivations.txt'), 'derivations loaded.')
print(g.load_lexemes('test/lexemes.txt'), 'lexemes loaded.')
print(g.load_lex_rules('test/lex_rules.txt'), 'lexical rules loaded.')
print(g.load_clitics('test/clitics.txt'), 'clitics loaded.')
print(g.load_bad_analyses('test/bad_analyses.txt'), 'wrong analyses loaded.')

g.compile_all()
print(time.clock() - t1, ' seconds for loading and compiling paradigms.')

print('\n\n**** Starting parser... ****\n')
m = morph_parser.Parser(verbose=0)
# m.parsingMethod = 'hash'
m.fill_stems()
m.fill_affixes()

testData = load_test_data('test/test_wordforms.txt')
report = perform_tests(m, testData)
print(report)
# print(m.parse('кӏогъ'))
