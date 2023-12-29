import os
import shutil
# import ants
import traceback
import SimpleITK as sitk

dir_path = r'E:\Pystudy\Thyroid_P_N\data\NHT'

def Newfile(dir_path):
    for paths,dirs,filenames in os.walk(dir_path):
        for index in range(len(filenames)):
            # print('paths:',paths)
            # print('dirs:',dirs)
            # print('files:',filenames)
            if index==3 and 'B2000' not in paths and 'Label' not in paths:
                # print('paths:',paths)
                # print('dirs:',dirs)
                # print('files:',filenames)
                old_file = os.path.join(paths, filenames[index])
                # print('old_file:', old_file)

                new_file_path = os.path.split(old_file)[0]
                new_file_path = os.path.split(new_file_path)[0]
                new_file_path = new_file_path + '\\' + 'Label'

                new_file = os.path.join(new_file_path,filenames[index])
                # print('new_files:', new_file, '\n')
                shutil.copyfile(old_file, new_file)

    print('Done')

Newfile(dir_path)



