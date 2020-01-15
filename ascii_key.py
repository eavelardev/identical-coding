import readchar

keys = {
    '`': 'grave accent',        '~': 'tilde',               '!': 'exclamation mark',
    '@': 'at sign',             '#': 'number sign',         '$': 'dollar sign',
    '%': 'percent sign',        '^': 'caret',               '&': 'ampersand',
    '*': 'asterisk',            '(': 'open parenthesis',    ')': 'close parenthesis',
    '-': 'hyphen',              '_': 'underscore',          '=': 'equals sign',
    '+': 'plus sign',           '[': 'opening bracket',     ']': 'closing bracket',
    '{': 'opening brace',       '}': 'closing brace',       '|': 'vertical bar',
    ';': 'semicolon',           ':': 'colon',               '"': 'double quotes',
    ',': 'comma',               '.': 'period',              '<': 'less-than sign',
    '>': 'greater-than sign',   '/': 'slash',               '?': 'question mark',
    'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't', 'y': 'y', 'u': 'u',
    'i': 'i', 'o': 'o', 'p': 'p', 'a': 'a', 's': 's', 'd': 'd', 'f': 'f',
    'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l', 'z': 'z', 'x': 'x',
    'c': 'c', 'v': 'v', 'b': 'b', 'n': 'n', 'm': 'm', 
    'Q': 'Q', 'W': 'W', 'E': 'E', 'R': 'R', 'T': 'T', 'Y': 'Y', 'U': 'U',
    'I': 'I', 'O': 'O', 'P': 'P', 'A': 'A', 'S': 'S', 'D': 'D', 'F': 'F',
    'G': 'G', 'H': 'H', 'J': 'J', 'K': 'K', 'L': 'L', 'Z': 'Z', 'X': 'X',
    'C': 'C', 'V': 'V', 'B': 'B', 'N': 'N', 'M': 'M',
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
    '8': '8', '9': '9', '0': '0',
    '\'': 'apostrophe',
    '\\': 'backslash',
    '\r': 'enter',
    '\t': 'tab',
    '\x7f': 'backspace',
    '\x03': 'Copy',
    '\x16': 'Paste',
    '\x18': 'Cut',
    '\x01': 'Select all',
    '\x1a': 'Undo',
    '\x19': 'Redo',
    '\x1bO': 'Rename',
    '\x1b[A': 'Go to previous line',
    '\x1b[B': 'Go to next line',
    '\x1b[C': 'Right',
    '\x1b[D': 'Left',
    '\x1b[F': 'Go to end of line',
    '\x1b[H': 'Go to start line',
    '\x1b[3~': 'Delete'
}

while True:
    key = readchar.readkey()
    print(keys[key])
