file_ = open('poem.txt', encoding='utf-8')
content = file_.read()
file_.close()

print(content)

# context manager
with open('poem.txt', encoding='utf-8') as file_:
    content2 = file_.read()

with open('poem.txt', mode='a', encoding='utf-8') as file_:
    print(' vecer', file=file_)
    file_.write('dobroou noc')

print('I heard a poem: ')
print()
with open('poem.txt', encoding='utf-8') as file_:
    for line in file_:
        line = line.rstrip()  # remove white space
        print('   ' + line)

print()
print('Do you like it?')
