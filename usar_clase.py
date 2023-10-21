# -*- coding: utf-8 -*-

__author__ = 'Hugo E. Rodríguez C., Jhonny S. Rosero C.'
__maintainer__ = "Big Data - Universidad Central"
__copyright__ = "Copyright 2021 - Asignatura Big Data"
__version__ = "1.0"

try:
    from pathlib import Path as p
    import sys
    import os
    import warnings
    warnings.filterwarnings("ignore")
    

except Exception as exc:
            print('Module(s) {} are missing.:'.format(str(exc)))

dir_root = p(__file__).parents[1]
print('-----------------dir_root ' + str(dir_root))
path_code = str(p(dir_root) /'source')
sys.path.append(str(p(path_code).joinpath('classes')))

from cls_extract import extract as extract

#%%
''' Crear una instancia de la clase extract'''

e = extract(path=dir_root)
print('-----------------extract ' + str(e))

#%%
''' Existe el directorio origen '''
e.check_path(e.path)
print(e.dir_exist)

#%%
'''Existen los directorios'''
path_files_old = str(p(e.path) / 'files' / 'old')
path_files_new = str(p(e.path) / 'files' / 'new')

e.check_path(path_files_old)
print(e.dir_exist)

e.check_path(path_files_new)
print(e.dir_exist)

#%%
''' Listar archivos según el tipo'''

e.get_lst_files(path_files_old,'csv')
print('{}Instancia Dataset:'.format(os.linesep))

print('-----------------extract ' + str(e.get_lst_files(path_files_old,'csv')))

e.show_files()
print('Cantidad de archivos:', len(e.lst_files))

e.get_lst_files(path_files_new,'csv')
print('{}Instancia Dataset:'.format(os.linesep))
e.show_files()
print('Cantidad de archivos:', len(e.lst_files))

#%%
e.compare_files_dir(path_files_old, path_files_new)

#%%
file1 = str(p(path_files_old) / 'prueba.csv')
file2 = str(p(path_files_new) / 'prueba.csv')

e.compare_file(file1, file2)





