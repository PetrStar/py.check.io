def backward_string_by_word(text: str) -> str: #my first code
    res = ''
    start = -1
    end = -1
    for i, c in enumerate(text):
        if c.isalpha() and start == -1:
            start = i
        if not c.isalpha():
            if start != -1:
                word = text[start:i]
                res += word[::-1]
                start = -1
            res += c
    if start != -1:
        word = text[start:]
        res += word[::-1]
    return res     
    
def backward_string_by_word(text: str) -> str: #result
    return ' '.join([word[::-1] for word in text.split(' ')])
