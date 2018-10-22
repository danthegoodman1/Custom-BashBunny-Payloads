import subprocess

a = subprocess.check_output("ps -ae | grep Applications | awk '{print $4}' | sort -u", shell=True) 

a = a.decode('utf-8').split('\n')
a.remove('grep')
a.remove('')

b = []

for i in a:
    i = str(i)
    if 'Applications' not in i:
        a.remove(i)
    else:
        i = i.split('Applications/')[1]
        if '.app' in i:
            i = i.split('.app')[0]
        elif '/' in i:
            i = i.split('/')[0]
        b.append(i)

# def stringify(e):
#     e = str(e)
#     return e.split('Applications/')[0]

# b = map(stringify, a)

print b
