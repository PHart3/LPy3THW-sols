class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, mod1, subject, verb, mod2, obj):
        if mod1 != None:
            self.mod1 = mod1[1]
        else:
            self.mod1 = None
        self.subject = subject[1]
        self.verb = verb[1]
        if mod2 != None:
            self.mod2 = mod2[1]
        else:
            self.mod2 = None
        self.object = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_number(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'number':
        return match(word_list, 'number')
    else:
        return None

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    numb1 = parse_number(word_list)
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    numb2 = parse_number(word_list)
    obj = parse_object(word_list)

    return Sentence(numb1, subj, verb, numb2, obj)
