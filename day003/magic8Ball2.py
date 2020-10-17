import random

messages = ['たしかにそうだ',
    '間違いなくそうだ',
    'はい',
    'なんとも。もう一度やってみて',
    '後でもう一度きいてみて',
    '集中してもう一度きいてみて',
    '私の答えはノーです',
    '見通しはそれほどよくない',
    'とても疑わしい']

print(messages[random.randint(0, len(messages) - 1)])