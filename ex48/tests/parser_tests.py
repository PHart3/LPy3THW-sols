from nose.tools import *
from ex48 import lexicon, parser



def test_subject():
    sentence = parser.Sentence(None, ('noun', 'princess'), ('verb', 'kill'),('number', 5), ('noun', 'cabinet'))
    assert_equal(sentence.subject, 'princess')
    assert_equal(sentence.mod1, None)
    assert_equal(sentence.verb, 'kill')
    assert_equal(sentence.mod2, 5)
    assert_equal(sentence.object, 'cabinet')

def test_peek():
    word_list = []
    assert None == parser.peek(word_list)

    word_list = lexicon.scan("princess kill bear")
    assert "noun" == parser.peek(word_list)

def test_match():
    word_list = lexicon.scan("bear eat princess")
    assert_equal(('noun', 'bear'), parser.match(word_list, 'noun'))
    assert_equal(None, parser.match(word_list, 'noun'))

def tests_skip():
    word_list = lexicon.scan("the bear eat princess")
    assert parser.skip(word_list, 'stop') == None

def test_parse_verb():
    word_list = lexicon.scan("eat the bear")
    assert parser.parse_verb(word_list) == ('verb', 'eat')
    
    word_list = lexicon.scan("the bear eat the cabinet")
    assert_raises(parser.ParserError, parser.parse_verb, word_list)

def test_parse_subject():
    word_list = lexicon.scan("the bear eat the cabinet")
    assert parser.parse_subject(word_list) == ('noun', 'bear')

    word_list = lexicon.scan("eat the bear")
    assert parser.parse_subject(word_list) == ('noun', 'player')

    word_list = lexicon.scan('the the bear')
    print(parser.parse_subject(word_list))

def test_parse_sentence():
    word_list = lexicon.scan("the 10  bear eat the princess")
    x = parser.parse_sentence(word_list)
    assert x.subject == "bear"
    assert x.mod1 == 10
    assert x.verb == "eat"
    assert x.mod2 == None
    assert x.object == "princess"
