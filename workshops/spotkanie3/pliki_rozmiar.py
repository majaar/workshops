import os
import os.path

files_dict = {}

def przegladanie_rozmiar(root):
    file_list = os.listdir(root)
    dir_list = []
    for item in file_list:
        if os.path.isfile(os.path.join(root, item)):
            full_name = os.path.join(root, item)
            file_size = os.path.getsize(full_name)
            if file_size in files_dict:
                files_list = files_dict[file_size]
                files_list.append(full_name)
                files_dict[file_size] = files_list
            else:
                files_dict[file_size] = [full_name]
        if os.path.isdir(os.path.join(root, item)):
            dir_list.append(item)
    for dirname in dir_list:
        przegladanie_rozmiar(os.path.join(root, dirname))
    return files_dict


files_dict = przegladanie_rozmiar('.')
print(files_dict)

