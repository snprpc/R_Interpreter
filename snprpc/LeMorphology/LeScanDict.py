__author__ = '1'

illegalChars = '@#$~'
keywords = ('funtion','if','else','for','while','switch','in','print','true','TRUE','false','FALSE','NULL','next','break','vector','c','list','matrix','array','factor','return','repeat','pie')

LeScanDict = {
        # 'abc' or "abc"
        'STRING' : 0,
        # abc
        'VARIABLE' : 1,
        # 12 12.122
        'DIGIT' : 2,
        # '
        'SQUOTEMARK' : 3,
        # "
        'DQUOTEMARK' : 4,
        # ,
        'COMMA' : 5,
        # (
        'LPARENTEHESE;' : 6,
        # )
        'RPARENTEHESE' : 7,
        # {
        'LBRACE' : 8,
        # }
        'RBRACE' : 9,
        # ;
        'SEMICOLON' : 10,
        # +
        'PLUS' : 11,
        # -
        'MINUS' : 12,
        # *
        'MULT' : 13,
        # /
        'DIV' : 14,
        # %%
        'VECTORREMAINDER' : 15,
        # %/%
        'VECTORDIV' : 16,
        # ^
        'VECTORPOWER' : 17,
        # >
        'GREATER' : 18,
        # <
        'LESS' : 19,
        # ==
        'ISEQUAL' : 20,
        # >=
        'GREATEREQUAL' : 21,
        # <=
        'LESSEQUAL' : 22,
        # !=
        'NOTEQUAL' : 23,
        # &
        'ELEMENTAND' : 24,
        # |
        'ELEMENTOR' : 25,
        # !
        'ELEMENTNOT' : 26,
        # &&
        'AND' : 27,
        # ||
        'OR' : 28,
        # <- or = or <<-
        'LEFTDISTRIBUTE' : 29,
        # -> or ->>
        'RIGHTDISTRIBUTE' : 30,
        # :
        'COLON' : 31,
        # %in%
        'ISVECTOR' : 32,
        # %*%
        'TRANSPOSEMINUS' : 33,
        # 12.1
        'FRACTION' : 34,
        # if
        'IF' : 35,
        # else
        'ELSE' : 36,
        # for
        'FOR' : 37,
        # while
        'WHILE' : 38,
        # switch
        'SWITCH' : 39,
        # in
        'IN' : 40,
        #print
        'PRINT' : 41,
        # .
        'POINT' : 42,
        # true
        'TRUE' : 43,
        # false
        'FALSE' : 44,
        # NULL
        'NULL' : 45,
        # next
        'NEXT' : 46,
        # break
        'BREAK' : 47,
        # vector
        'VECTOR' : 48,
        # c
        'C' : 49,
        # list
        'LIST' : 50,
        # matrix
        'MATRIX' : 51,
        # array
        'ARRAY' : 52,
        # factor
        'FACTOR' : 53,
        # return
        'RETURN' : 54,
        # <-function
        'FUNCTIONCLAIM' : 55,
        # repeat
        'REPEAT' : 56,
        # <-c
        'DEFINEC' : 57,
        'PIE': 58
    }
