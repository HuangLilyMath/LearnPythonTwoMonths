text = '{} {} {} {}'

print(text.format(1,2,3,4))
print(text.format('one','two','three','four'))
print(text.format(True,False,False,True))
print(text.format(text,text,text,text))
print(text.format(
    'Try your',
    'Own text here',
    'Maybe a poem',
    'Or a song about fear'
    ))