from __future__ import print_function, unicode_literals
from whaaaaat import style_from_dict, Token, prompt, print_json, Separator


style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})

# Separator()
questions = [
    {
        'type': 'rawlist',
        'name': 'theme',
        'message': 'What is 1 + 1?',
        'choices': ['7','2','12','4']
    },
    # {
    #     'type': 'rawlist',
    #     'name': 'size',
    #     'message': 'What size do you need',
    #     'choices': ['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
    #     'filter': lambda val: val.lower()
    # }
]

answers = prompt(questions, style=style)
if answers == '2':
    print("correct")
else:
    print("wrong")
# print_json(answers)