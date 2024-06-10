data = open('main.txt', 'r', encoding='UTF-8').read()

# Cucumber Alpha 1.0.4

print('Cucumber Alpha 1.0.4\nMade by watakak | https://github.com/watakak/Cucumber\n\n'
      ' Select the convert type:\n'
      '  1. Convert to Cucumber\n'
      '  2. Convert to Python')
convertType = input(' Input: ')

repl = {
    # keywords
    'print(': 'ā',
    'input(': 'ā',

    # another keywords
    'def ': 'Å',
    'func': 'Á',
    'var': 'È',
    'import ': 'Ñ',
    ' as ': 'Ó',
    'from ': 'Ô',

    # special characters
    "('": 'ä',
    "')": 'ë',
    '("': 'Ä',
    '")': 'Ë',
    "(f'": 'Ê',
    '(f"': 'Ë',
    "):": 'É',
    "}ë": 'Í',
    "Æ{": 'Ù',
    '\\n': 'Ï',
    '(': 'Â',
    ')': 'Ã',
    ' = ': 'Ī',
    ': ': 'Æ',
    ', ': 'Ð',

    # tabs, spaces
    '\n\n\n\n': 'Ό',
    '\n\n\n': 'Ή',
    '\n\n': 'Έ',
    '\n': 'Ά',
    '    ': 'ø',

    # numbers
    '000000': 'ဖ',
    '00000': 'ပ',
    '0000': 'ဎ',
    '000': 'ခ',
    '00': 'ဒ',

    # letters
    'ta': 'Ꭻ',
    'te': 'Ꭺ',
    'ti': 'Ꭹ',
    'to': 'Ꭸ',
    'tu': 'Ꭷ',
    'ty': 'Ꭶ',
    'tw': 'Ꭵ',
    'st': 'Ꭴ',
    'put': 'Ꭰ',
    'In': 'Ꭱ',
    'Out': 'Ꭲ',
    'said': 'Ꭼ',
    'You ': 'ค',
    'on': 'Ç',
    'int': '½',
    'rand': 'ɲ',
    'om': 'ȅ',
    'number': 'ฃ',
    'll': 'ฆ',
    'He': 'ง',
    'World': 'ฉ',

    # combinations
    'øāÂ': 'Ա',
    'øāÊ': 'Բ'
}

if convertType == '1':
    for key, value in repl.items():
        data = data.replace(key, value)
elif convertType == '2':
    for key, value in repl.items():
        data = data.replace(value, key)
else:
    print('Incorrect action!')

print(f'\n Output:\n{data}')
