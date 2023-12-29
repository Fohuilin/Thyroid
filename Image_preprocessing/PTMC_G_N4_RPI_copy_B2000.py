import os
import shutil
import traceback
import SimpleITK as sitk

dir_path = r'E:\Pystudy\Thyroid_P_N\data\PTMC'

def Copy(dir_path):
    for path, dirs, files in os.walk(dir_path):
        # print('path:',path)
        # print('dirs:',dirs)
        # print('files:',files)

        # Create a new directory (Label) to facilitate the copying of two registered files (the move file and the move_label file) from B2000.
        # if 1 < len(dirs) < 10:
        #     new_file_path = path+'\\'+'Label'
        #     print('new_file_path:', new_file_path)
        #     os.makedirs(new_file_path) (OK)

        if 'B2000' in path:
            move_path_1 = os.path.join(path, files[3])
            new_path_1 = os.path.split(move_path_1)[0]
            new_path_1 = os.path.split(new_path_1)[0]
            new_path_1 = new_path_1 + '\\' + 'Label'
            new_path_1 = os.path.join(new_path_1, files[3])
            # print('new_path_1:', new_path_1)
            shutil.copyfile(move_path_1, new_path_1)

            move_path_2 = os.path.join(path, files[4])
            new_path_2 = os.path.split(move_path_2)[0]
            new_path_2 = os.path.split(new_path_2)[0]
            new_path_2 = new_path_2 + '\\' + 'Label'
            new_path_2 = os.path.join(new_path_2, files[4])
            # print('new_path_2:', new_path_2)
            shutil.copyfile(move_path_2, new_path_2)



    print('done')

Copy(dir_path)





