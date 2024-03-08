import re

def tokenize(query):
    token_specification = [
        ('SELECT',  r'select'),               
        ('FROM',    r'from'),                 
        ('WHERE',   r'where'),                
        ('ID',      r'[a-zA-Z_]\w*'),         
        ('NUM',     r'\d+'),                  
        ('COMMA',   r','),                    
        ('GREATER_EQ', r'>='),                
        ('WHITESPACE', r'\s+'),               
        ('ERROR',   r'.'),                    
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []
    for mo in re.finditer(tok_regex, query):
        dic = mo.groupdict()
        for key, value in dic.items():
            if value:
                tokens.append((key, value))
                break
    return tokens

query = "select id, nome, salary from empregados where salary >= 820"
tokens = tokenize(query)
for token in tokens:
    print(token)
