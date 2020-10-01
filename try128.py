a = 21
b = 1
print(a + b)

with open(__file__, 'r') as f:
    lines = f.read().split('\n')
    val = int(lines[0].split(' = ')[-1])
    new_line = 'a = {}'.format(val+1)
    print('new line 1: ', new_line)
    #new_file = '\n'.join([new_line] + lines[1:])
    #print('new line 2: ', new_file)

with open(__file__, 'w') as f:
    f.write('\n'.join([new_line] + lines[1:]))