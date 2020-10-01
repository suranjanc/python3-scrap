[-1, 2, 2, 2, 2, 2]
a = 3
b = 1
#print(a + b)

import json

with open(__file__, 'r') as f:
    lines = f.read().split('\n')
    val = lines[0]
    list1=json.loads(val)
    print(list1)
    #new_line = 'a = {}'.format(val+1)
    #new_file = '\n'.join([new_line] + lines[1:])
    list1.append(2)
    print(list1)

with open(__file__, 'w') as f:
    #list1.append(2)
    f.write('\n'.join([str(list1)] + lines[1:]))