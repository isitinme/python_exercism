QUESTION_CHAR = '?'
ANSWER_TO_YELL_QUESTION = 'Calm down, I know what I\'m doing!'
ANSWER_TO_QUESTION = 'Sure.'
ANSWER_TO_SILENCE = 'Fine. Be that way!'
ANSWER_TO_YELL = 'Whoa, chill out!'
DEFAUL_ANSWER = 'Whatever.'

def response(hey_bob):
    s = hey_bob.strip()
    if s.endswith(QUESTION_CHAR):
        return ANSWER_TO_YELL_QUESTION if s.isupper() else ANSWER_TO_QUESTION
    elif len(s) == 0:   
        return ANSWER_TO_SILENCE
    elif s.isupper():
        return ANSWER_TO_YELL
    else:
        return DEFAUL_ANSWER