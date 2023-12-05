from datasource import CommandNotValidError, console_colors

def show_dir(dir, path=[], indent=0):
    current = dir
    for directory in path:
        if 'FD-'+directory in current:
            current = current['FD-'+directory]
        elif 'F-'+directory in current:
            print('Path mengandung direktori bertipe file')
            return
        else:
            print("Path tidak tersedia.")
            return

    for name, content in current.items():
        if 'FD-' in name:
            name = name.replace('FD-', '', 1)
        elif 'F-' in name:
            name = name.replace('F-', '', 1)
        print("  " * indent + f" {name}")
        show_dir(content, [], indent + 1)

def delete_dir(dir, path=[]):
    current = dir
    for i, directory in enumerate(path):
        if 'FD-'+directory in current.keys(): 
            if i == len(path) - 1:
                del current['FD-'+directory]
                print("Direktori berhasil dihapus.")
                return
            current = current['FD-'+directory]
        elif 'F-'+directory in current.keys():
            if i == len(path) - 1:
                del current['F-'+directory]
                print("Direktori berhasil dihapus.")
                return
            print('Direktori ini berisi file')
        else:
            print(f"Folder '{directory}' tidak ada di direktori ini.")
            return
    print("Direktori tidak tersedia.")

def make_dir(dir, path, is_file=True):
    current = dir

    for directory in path[:-1]:
        if 'FD-'+directory in current:
            current = current['FD-'+directory]
        elif 'F-'+directory in current:
            print('Path mengandung direktori bertipe file')
            return
        else:
            print("Path tidak tersedia.")
            return
    
    if is_file:
        last_item = 'F-'+path[-1].replace('/', '')
    else:
        last_item = 'FD-'+path[-1].replace('/', '')
    
    if last_item in current:
        if is_file:
            print(f"File {last_item.replace('F-', '')} sudah ada")
            return
        else:
            print(f"Folder {last_item.replace('FD-', '')} sudah ada")
            return

    if is_file:
        current[last_item] = {}
        print(f"File {last_item.replace('F-', '')} sukses dibuat")
    else:
        current.setdefault(last_item, {})
        print(f"Folder {last_item.replace('FD-', '')} sukses dibuat.")

def get_type_make_dir(DIRECTORY, dir_type):
    CURDIR = input("Masukkan path direktori gunakan '/': ")
    CURDIR = CURDIR.split('/')
    if len(CURDIR[0]) < 1:
        CURDIR = ['root']
    else:
        CURDIR.insert(0, 'root')
    input_dir = input(f'Nama {dir_type} : ').strip()
    if len(input_dir) < 1:
        raise CommandNotValidError(f'{console_colors.FAIL}Nama tidak boleh kosong!{console_colors.ENDC}')
    CURDIR.append(input_dir.replace(' ', '-'))
    make_dir(DIRECTORY, CURDIR, True if dir_type == 'file' else False)