import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Завдання 1
def subcreatedir(p):
    q = 1
    while q == 1: 
        q = int(input(f'Створити субдиректорію у директорії {p}? Введіть 1, щоб створити, будь-який інший символ, щоб відмовитись. '))
        if q == 1: 
            d = input('Введіть назву субдиректорії - папки: ')
            n = os.path.join(p, d) 
            os.mkdir(n)
            filecreate(n)
        else: 
            break
def filecreate(p): 
    q = 1
    while q == 1: 
        q = int(input(f'Створити файл у директорії {p}? Введіть 1, щоб створити, будь-який інший символ, щоб відмовитись. '))
        if q == 1: 
            f = input('Введіть назву файлу: ')
            n = os.path.join(p, f) 
            newf = open(n, "w+")
            newf.close()
        else: 
            break
def m(): 
    dir = input('Введіть назву директорії - папки: ')
    os.mkdir(dir)
    p = os.path.abspath(dir)  
    filecreate(p)
    subcreatedir(p)

# Завдання 2 
print('Завдання 2. Виведення інформації про файли і папки голової директорії')
dir = 'my_directory'
p = os.path.abspath(dir) 
print('Застосування os.listdir')
print(f'Папки та файли директорії {dir}: {os.listdir(dir)}')
print(f'Папки та файли директорії {dir} (рядкове подання): ')
l = os.listdir(dir)
for i in range(0, len(l)): 
    print(l[i])
print('Застосування os.scandir')
print(f'Папки та файли директорії {dir} (рядкове подання): ')
with os.scandir(p) as entries: 
    for entry in entries: 
        print(entry.name)

# Завдання 3
print('Завдання 3. Виведення інформації про файли головної директорї ')
print('Застосування listdir')
for i in range(0, len(l)): 
    if os.path.isfile(os.path.join(p, l[i])): 
        print(l[i])
# або: 
onlyfiles = [print(f) for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
print('Застосування scandir')
with os.scandir(p) as entries: 
    for entry in entries: 
        if entry.is_file(): 
            print(entry.name)

# Завдання 4
n = 0
find = '.txt'
for f_name in l: 
    if f_name.endswith(find): 
        n += 1
        print(f_name)
if n==0: 
    print(f'{find} не знайдено')

# Завдання 5 
print('Завдання 5. Виведення інформації про вміст головної директорії та всіх папок у ній ')
def w(p): 
    for root, directories, files in os.walk(p): 
        print(f'Знайдена директорія: {os.path.split(root)[-1]} (налічує каталогів - {len(directories)}, файлів - {len(files)})')
        for file in files: 
            print(file)
        for dir in directories: 
            w(os.path.join(p, dir))

# Завдання 6
e = '.py'
n = '.csv'
p = os.path.abspath(dir) 
print(f'Завдання 6. Виведення .py файлів із директорії {dir} та її підкаталогів')
for root, dirs, files in os.walk(p): 
    for file in files: 
        if file.endswith(e): 
            nfile = file[0:-len(e)] + n 
            os.rename(os.path.join(root, file), os.path.join(root, nfile))
print('Структура директорії: ')
w(p)

# Завдання 7 
def d(dir): 
    p = os.path.abspath(dir) 
    print(f'Видалення всіх каталогів і файлів {dir}')
    for root, dirs, files in os.walk(p, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
        os.rmdir(root)
    print('Директорія видалена')
dir = 'my_directory'
d(dir)