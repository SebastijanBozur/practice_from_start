
hololive_member = {'firstname': 'Fubuki', 'lastname':'Shirakami', 'gen':['1','gamers']}

print(hololive_member['gen'])
print(hololive_member.get('year', 'Not Found'))

for key, value in hololive_member.items():
    print(key.capitalize(), value)

hololive_member['year'] = 2018

print(hololive_member.get('year'))

print(hololive_member)

hololive_member.update({'firstname': 'Akai', 'lastname':'Haato', 'gen':1})

print(hololive_member)

del hololive_member['year']

print(hololive_member)