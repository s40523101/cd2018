with open("2a.txt") as fh:
    lines = fh.readlines()
e_list = list()
for i in range(len(lines)):
    a = lines[i].split()
    for g in range(0,len(a),3):
        c = a[g:g+3]
        e_list.append(c)
        print('第'+str(len(e_list))+'組'+str(c))

    
    
