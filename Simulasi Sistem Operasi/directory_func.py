from datasource import CommandNotValidError, console_colors

def show_dir(dir, path=[], indent=0):
    current = dir
    for folder in path:
        if folder in current:
            current = current[folder]
        else:
            print("Path tidak tersedia.")
            return

    for name, content in current.items():
        print("  " * indent + f" {name}")
        show_dir(content, [], indent + 1)

def delete_dir(dir, path=[]):
    current = dir
    for i, folder in enumerate(path):
        if folder in current:
            if i == len(path) - 1:
                del current[folder]
                print("Direktori berhasil dihapus.")
                return
            current = current[folder]
        else:
            print(f"Folder '{folder}' tidak ada di direktori ini.")
            return
    print("Direktori tidak tersedia.")

def make_dir(dir, path, is_file=True):
    curr = dir

    for item in path[:-1]:
        curr = curr.setdefault(item, {})

    last_item = path[-1]

    if last_item in curr:
        if is_file:
            print(f"File {last_item} sudah ada")
        else:
            print(f"Folder {last_item} sudah ada")

    if is_file:
        curr[last_item] = {}
        print(f"File {last_item} sukses dibuat")
    else:
        curr.setdefault(last_item, {})
        print(f"Folder {last_item} sukses dibuat.")

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