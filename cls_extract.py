# -*- coding: utf-8 -*-

__author__ = 'Hugo E. Rodríguez C., Jhonny S. Rosero C.'
__maintainer__ = "Big Data - Universidad Central"
__copyright__ = "Copyright 2021 - Asignatura Big Data"
__version__ = "1.0"

try:
    import glob
    import os
    import filecmp
    from pathlib import Path as p
    from pathlib import PurePath

except Exception as exc:
    print('Module(s) {} are missing.:'.format(str(exc)))
    
#%%
class extract(object):
    '''
    Clase para extraer y validar los archivos pdf de la biblioteca virtual
    '''

    def __init__(self, path=None):
        self.listFileNew = []
        self.path = path
        self.lst_files = None

    def check_path(self,path_check):
        '''
        Valida que exista el path

        Returns
        -------
        None.

        '''
        try:
            self.dir_exist = os.path.exists(path_check)
        except Exception as exc:
            self.show_error(exc)

    def get_lst_files(self, path_data, tipo):
        '''
        Lista los archivo de un directorio segun el tipo de solicitado.

        Parameters
        ----------
        path_data : string
            Ruta del directorio que contiene los archivos.
        tipo : string
            Extensión o tipo de archivo.

        Returns
        -------
        None.

        '''
        print('path get_lst_files ' + str(path_data))
        print('tipo get_lst_files ' + str(tipo))

        try:
            # self.lst_files = [f for f in glob.glob(str(path_data), recursive=True)]
            self.lst_files = [f for f in glob.glob(str(path_data)+'/**/*.'+ tipo.lower(), recursive=True)]
            print('files : -----------------> ' + str(self.lst_files))
            
        except Exception as exc:
            self.show_error(exc)

    def show_files(self):
        '''
        Imprime en pantalla cada uno de los elementos contenidos en lst_files

        Returns
        -------
        None.

        '''
        try:
            # print('list: ' + self.lst_files)
            for f in self.lst_files:
                print('---------- show files: ' + f)
                child = os.path.splitext(os.path.basename(f))[0]
                print('************* show_files: ' + child)
                
        except Exception as exc:
            self.show_error(exc)

    def compare_files_dir(self, dir1, dir2):
        '''
        Compara todos los archivos en común que se encuentren en dos directorios

        Parameters
        ----------
        dir1 : string - path
            Ruta del directorio inicial.
        dir2 : string - path
            Ruta del directorio final.

        Returns
        -------
        Retorna la salida en 5 archivos de texto con el resultado de la comparación.

        '''
        try:
            # Determine the items that exist in both directories
            d1_contents = set(os.listdir(dir1))
            print("----" + str(d1_contents))
            d2_contents = set(os.listdir(dir2))
            print("----" + str(d2_contents))
            self.diff1 = list(d1_contents - d2_contents)
            if len(self.diff1) > 0:
                print('Los siguientes archivos no están en ', dir2, self.diff1)
            self.diff2 = list(d2_contents - d1_contents)
            if len(self.diff2) > 0:
                print('Los siguientes archivos no están en ', dir1, self.diff2)
            common = list(d1_contents & d2_contents)
            common_files = [
                f
                for f in common
                if os.path.isfile(os.path.join(dir1, f))
            ]
            #print('Common files:', common_files)
            
            # Compare the directories
            self.match, self.mismatch, self.errors = filecmp.cmpfiles(
                dir1,
                dir2,
                common_files,
                shallow = False
            )
            #print('Match       :', self.match)
            #print('Mismatch    :', self.mismatch)
            #print('Errors      :', self.errors)
            
            name_list = ['match.txt', 'mismatch.txt', 'errors.txt', 'diff1vsdiff2.txt', 'diff2vsdiff1.txt']
            list1 = [self.match, self.mismatch, self.errors, self.diff1, self.diff2]
            for k in range(len(name_list)):
                with open((str(p(self.path) / 'files' / 'result' / str(name_list[k]))), '+w') as f:
                    for name in list1[k]:
                        f.write(name)
                        f.write('\n')
            for i in range(len(self.mismatch)):    
                if len(self.mismatch) > 0:
                    print('\n','*'*30)
                    print('Archivo: ', PurePath(self.mismatch[i]).name, '\n')
                    self.compare_file(str(p(dir1) / self.mismatch[i]), str(p(dir2) / self.mismatch[i]))
                
        except Exception as exc:
            self.show_error(exc)
            
    def compare_file(self, file1, file2):
        '''
        Compara dos archivos, se debe ingresar la ruta completa.

        Parameters
        ----------
        file1 : string - path
            Ruta completa del nombre del archivo.
        file2 : string - path
            Ruta completa del nombre del archivo.

        Returns
        -------
        None.

        '''
        try:
            # reading files
            f1 = open(file1, "r")  
            f2 = open(file2, "r")
    
            i = 0
              
            for line1 in f1:
                i += 1
                  
                for line2 in f2:
                      
                    # matching line1 from both files
                    if line1 == line2:  
                        # print IDENTICAL if similar
                        break
                        #print("Line ", i, ": IDENTICAL")       
                    else:
                        print("Line ", i, ":")
                        # else print that line from both files
                        print("\tFile 1:", line1, end='')
                        print("\tFile 2:", line2, end='')
                    break
            
        except Exception as exc:
            self.show_error(exc)
            
    def show_error(self,ex):
        '''
        Captura el tipo de error, su description y localización.

        Parameters
        ----------
        ex : Object
            Exception generada por el sistema.

        Returns
        -------
        None.

        '''
        trace = []
        tb = ex.__traceback__
        while tb is not None:
            trace.append({
                          "filename": tb.tb_frame.f_code.co_filename,
                          "name": tb.tb_frame.f_code.co_name,
                          "lineno": tb.tb_lineno
                          })
            
            tb = tb.tb_next
            
        print('{}Something went wrong:'.format(os.linesep))
        print('---type:{}'.format(str(type(ex).__name__)))
        print('---message:{}'.format(str(type(ex))))
        print('---trace:{}'.format(str(trace)))