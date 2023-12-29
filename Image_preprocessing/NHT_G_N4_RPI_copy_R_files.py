import os
import shutil
# import ants
import traceback
import SimpleITK as sitk

dir_path = r'E:\Pystudy\Thyroid_P_N\data\NHT'

def copyfiles(dir_path):
    for paths,dirs,filenames in os.walk(dir_path):
        if 'Label' in paths:
            # print('paths:',paths)
            # print('dirs:',dirs)
            # print('files:',filenames)
            for file in filenames:
                if 'ADC' in file:
                    old_file = os.path.join(paths, file)
                    print('old_file:', old_file)

                    new_path = os.path.split(old_file)[0]
                    new_path = os.path.split(new_path)[0]
                    new_path = new_path + '\\' + 'ADC'
                    print('new_path:', new_path, '\n')

                    shutil.copy(old_file, new_path)

                if 'B0' in file:
                    old_file = os.path.join(paths, file)
                    print('old_file:', old_file)

                    new_path = os.path.split(old_file)[0]
                    new_path = os.path.split(new_path)[0]
                    new_path = new_path + '\\' + 'B0'
                    print('new_path:', new_path, '\n')

                    shutil.copy(old_file, new_path)

                if 'B800' in file:
                    old_file = os.path.join(paths, file)
                    print('old_file:', old_file)

                    new_path = os.path.split(old_file)[0]
                    new_path = os.path.split(new_path)[0]
                    new_path = new_path + '\\' + 'B800'
                    print('new_path:', new_path, '\n')

                    shutil.copy(old_file, new_path)

                if 'B2000' in file:
                    old_file = os.path.join(paths, file)
                    print('old_file:', old_file)

                    new_path = os.path.split(old_file)[0]
                    new_path = os.path.split(new_path)[0]
                    new_path = new_path + '\\' + 'B2000'
                    print('new_path:', new_path, '\n')

                    shutil.copy(old_file, new_path)

                if 'T1' in file and 'T1_C' not in file:
                    old_file = os.path.join(paths, file)
                    print('old_file:', old_file)

                    new_path = os.path.split(old_file)[0]
                    new_path = os.path.split(new_path)[0]
                    new_path = new_path + '\\' + 'T1'
                    print('new_path:', new_path, '\n')

                    shutil.copy(old_file, new_path)

                if 'T1_C' in file:
                    old_file = os.path.join(paths, file)
                    print('old_file:', old_file)

                    new_path = os.path.split(old_file)[0]
                    new_path = os.path.split(new_path)[0]
                    new_path = new_path + '\\' + 'T1_C'
                    print('new_path:', new_path, '\n')

                    shutil.copy(old_file, new_path)

                if 'T2' in file:
                    old_file = os.path.join(paths, file)
                    print('old_file:', old_file)

                    new_path = os.path.split(old_file)[0]
                    new_path = os.path.split(new_path)[0]
                    new_path = new_path + '\\' + 'T2'
                    print('new_path:', new_path, '\n')

                    shutil.copy(old_file, new_path)


    print('Done')

copyfiles(dir_path)



