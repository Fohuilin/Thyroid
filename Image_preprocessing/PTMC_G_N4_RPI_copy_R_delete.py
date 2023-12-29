import os
import shutil
# import ants
import traceback
import SimpleITK as sitk

dir_path = r'E:\Pystudy\Thyroid_P_N\data\PTMC'

def Delete(dir_path):

    for paths,dirs,files in os.walk(dir_path):
        if len(dirs) == 0 and 'Label' not in paths:
            # print('paths:',paths)
            # print('dirs:',dirs)
            # print('files:',files)
            for file in files:
                delete_file_path = os.path.join(paths, file)
                # print('files:', delete_file_path)
                os.remove(delete_file_path)

Delete(dir_path)



