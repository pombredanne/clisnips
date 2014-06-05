(
    T_EOF,
    T_TEXT,
    T_PARAM,
    T_TYPEHINT,
    T_LBRACE, T_RBRACE,
    T_LBRACK, T_RBRACK,
    T_STRING, T_DIGIT, T_IDENT,
    T_COMMA,
    T_RANGE_SEP,
    T_COLON,
    T_STAR
) = range(15)

__TOKEN_NAMES = {}

for k, v in dict(vars()).iteritems():
    if k.startswith('T_'):
        __TOKEN_NAMES[v] = k


def token_name(token_type):
    """Returns the token name given its type"""
    if isinstance(token_type, Token):
        token_type = token_type.type
    return __TOKEN_NAMES[token_type]


class Token(object):
#{{{
    __slots__ = (
        'type', 'name', 'value', 'startline', 'startcol', 'endline', 'endcol'
    )

    def __init__(self, type, startline, startcol, value=''):
        self.type = type
        self.name = token_name(type)
        self.startline = startline
        self.startcol = startcol
        self.value = value
        self.endline = startline
        self.endcol = startcol

    def __str__(self):
        return '<Token {s.name}@({s.startline},{s.startcol})->({s.endline},{s.endcol}): "{s.value}"'.format(s=self)

#}}}
