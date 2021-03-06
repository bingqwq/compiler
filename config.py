WENFA_DICT = {
    'startVn': '<源程序>',
    'vn': {
        '<标识符>',
        '<源程序>',
        '<形参列表>',
        '<形参列表_后续>',
        '<参数列表后续>',
        '<语句列表>',
        '<输出语句>',
        '<逻辑表达式>',
        '<赋值语句>',
        '<else语句>',
        '<变量列表>',
        '<逻辑运算符>',
        '<运算表达式>',
        '<项>',
        '<因子>',
        '<运算对象>',
        '<参数列表>',
        '<是否定义多维数组>',
        '<是否多维数组>',
    },
    'chanshenshi': {
        '<源程序>': [
            ['#', 'include', '<', ('<标识符>', (11,)), '>', '<源程序>'],
            [('<类型>', (1,10)), ('<标识符>', (4,8,'T')), ('(', (3,)), '<形参列表>', (')', (9,)), '{', '<语句列表>', ('}', (5,'P')), '<源程序>'],
            [('<类型>', (1,10)), ('<标识符>', (2,8,'Q','K')), '<变量列表>', ';', '<源程序>'],
            [('<类型>', (1,10)), ('<标识符>', (2,8,'Q')), '=', ('<运算表达式>', ('R',)), '<变量列表>', ';', '<源程序>'],
            [('<类型>', (1,10)), ('<标识符>', (6,8)), '[', ('<常数>', (12,)), ']', ('<是否定义多维数组>', (13,'Q','K')), ';', '<源程序>'],
            [],
        ],

        '<是否定义多维数组>': [
            ['[', ('<常数>', (12,)), ']', '<是否定义多维数组>'],
            [],
        ],

        '<标识符>':[
            [('<函数标识符>', ('A',))],
            [('<非函数标识符>', ('A',))],
            [('<未定义标识符>', ('A',))],
            [('<数组标识符>', ('A',))],
        ],

        '<形参列表>':[
            [('<类型>', (7,10)), ('<标识符>', (8,'K')), '<形参列表_后续>'],
            [],
        ],

        '<形参列表_后续>':[
            [',', ('<类型>', (7,10)), ('<标识符>', (8,'K')), '<形参列表_后续>'],
            [],
        ],

        '<语句列表>':[
            ['<输出语句>', '<语句列表>'],
            [('<函数标识符>', ('A',14)), '(', '<参数列表>', (')', ('B',)), ';', '<语句列表>'],
            [('<非函数标识符>', ('A',)), '<赋值语句>', '<语句列表>'],
            [('<数组标识符>', ('A',)), '[', '<运算表达式>', ']', ('<是否多维数组>', ('I',)), '<赋值语句>', '<语句列表>'],
            ['return', ('<运算表达式>', ('C',)), ';', '<语句列表>'],
            [('<类型>', (1,10)), ('<标识符>', (2,8,'Q','K')), '<变量列表>', ';', '<语句列表>'],
            [('<类型>', (1,10)), ('<标识符>', (2,8,'Q')), '=', ('<运算表达式>', ('R',)), '<变量列表>', ';', '<语句列表>'],
            [('<类型>', (1,10)), ('<标识符>', (6,8)), '[', ('<常数>', (12,)), ']', ('<是否定义多维数组>', (13,'Q','K')), ';', '<语句列表>'],
            ['if', '(', '<逻辑表达式>', (')', ('F',)),  ('{', (3,)), '<语句列表>', ('}', (5,)), ('<else语句>', ('D',)), '<语句列表>'],
            [('while', ('G',)), '(', ('<逻辑表达式>', ('M',)), ')', ('{', (3,)), '<语句列表>', ('}', (5,'N')), '<语句列表>'],
            [],
        ],

        '<输出语句>': [
           [ 'print', '(', ('<运算表达式>', ('J',)), ')', ';'],
        ],

        '<参数列表>':[
            [('<运算表达式>', ('L',)), '<参数列表后续>'],
            [],
        ],

        '<参数列表后续>':[
            [',', ('<运算表达式>', ('L',)), '<参数列表后续>'],
            [],
        ],

        '<逻辑表达式>':[
            ['<运算表达式>', '<逻辑运算符>', ('<运算表达式>', ('H',))],
        ],

        '<逻辑运算符>':[
            [('>', ('A',))], [('<', ('A',))], [('>=', ('A',))], [('<=', ('A',))], [('==', ('A',))],
        ],

        '<赋值语句>':[
            ['=', '<运算表达式>', (';', ('R',))],
            [(';', ('K',))],
        ],

        '<else语句>':[
            [('else', ('E',)), ('{', (3,)), '<语句列表>', ('}', (5,))],
            [],
        ],

        '<变量列表>':[
            [(',', (10,)), ('<标识符>', (2,8,'Q')), '=', ('<运算表达式>', ('R',)), '<变量列表>'],
            [(',', (10,)), ('<标识符>', (2,8,'Q','K')), '<变量列表>'],
            [],
        ],

        '<运算表达式>':[
            ['<项>'],
            ['<运算表达式>', ('<+->', ('A',)), ('<项>', ('H',))],
        ],

        '<项>':[
            ['<因子>'],
            ['<项>', ('<*/>', ('A',)), ('<因子>', ('H',))],       
        ],

        '<因子>':[
            ['<运算对象>'],
            ['(', '<运算表达式>', ')'],        
        ],

        '<运算对象>':[
            [('<函数标识符>', ('A',14)), '(', '<参数列表>', (')', ('B',))],
            [('<非函数标识符>', ('A',))],
            [('<常数>', ('A',))],       
            [('<数组标识符>', ('A',)), '[', '<运算表达式>', ']', ('<是否多维数组>', ('I',))],
        ],

        '<是否多维数组>':[
            ['[', '<运算表达式>', ']', '<是否多维数组>'],
            [],
        ]
    },
}

ENDCHAR = '$'

# 界符
p_LIST = [
    '<=', '==', '=', '>', '<', '+', '-', '*', '/', '{', '}', ',', ';', '(',
    ')', '[', ']'
]
# 关键字
k_LIST = ['int', 'void', 'if', 'else', 'char', 'float', 'while', 'return', 'print', 'include']

# 整体自动机调用数字自动机状态名
MATH_CONDITION = 'MFA'
# 注释返回名
COMMENT_CONDITION = 'comment'

# 整体自动机
ALL_STARTSTATUS = 1

ALL_STATUS = [
    1, 2, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
    24, 25, 26, 27, 28, 29, 33, 34, 35
]

ALL_ENDSTATUS = [
    2, 4, 5, 6, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
    29, 33, 35
]

# l -> letter, d -> 数字, n -> 空格回车
ALL_DERVEDICT = {
    1: {
        'n': 1,
        'l': 2,
        'd': MATH_CONDITION,
        '\'': 9,
        '"': 11,
        '>': 4,
        '<': 5,
        '=': 6,
        '+': 18,
        '-': 19,
        '*': 20,
        '/': 21,
        '{': 22,
        '}': 23,
        ',': 24,
        ';': 25,
        '(': 26,
        ')': 27,
        '[': 28,
        ']': 29,
        '#': 33,
        ENDCHAR: 35,
    },
    2: {
        'l': 2,
        'd': 2,
    },
    4: {
        '=': 13,
    },
    5: {
        '=': 14,
    },
    6: {
        '=': 15,
    },
    9: {
        'l': 10
    },
    10: {
        '\'': 16,
    },
    11: {
        'l': 12,
    },
    12: {
        'l': 12,
        '"': 17,
    },
    21: {
        '/': COMMENT_CONDITION,
    },
}

# 规约到哪个表
GUIYUE_LIST = {
    2: 'i',
    7: 'c',
    3: 'c',
    16: 'C',
    17: 'S',
    13: 'p',
    14: 'p',
    15: 'p',
    18: 'p',
    19: 'p',
    20: 'p',
    21: 'p',
    22: 'p',
    23: 'p',
    24: 'p',
    25: 'p',
    26: 'p',
    27: 'p',
    28: 'p',
    29: 'p',
    4: 'p',
    5: 'p',
    6: 'p',
    30: 'c',
    31: 'c',
    32: 'c',
    33: 'p',
    35: 'end',
}

# math automachine
MATH_STARTSTATUS = 1
MATH_STATUS = [1, 3, 7, 8, 30, 31, 32]
MATH_ENDSTATUS = [3, 7, 31, 32]
MATH_DERVEDICT = {
    1: {
        'd': 3,
    },
    3: {
        'd': 3,
        '.': 8,
        'e': 30,
    },
    7: {
        'd': 7,
        'e': 30,
    },
    8: {
        'd': 7,
    },
    30: {
        'd': 31,
        '-': 32,
    },
    31: {
        'd': 31,
    },
    32: {
        'd': 32,
    },
}
