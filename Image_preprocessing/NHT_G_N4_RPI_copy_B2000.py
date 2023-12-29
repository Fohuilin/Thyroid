import os
import shutil
import traceback
import SimpleITK as sitk

dir_path = r'E:\Pystudy\Thyroid_P_N\data\NHT'
# all_list = os.listdir(dir_path)
# print('all_list',all_list)

def Copy(dir_path):
    for path, dirs, files in os.walk(dir_path):
        # print('path:',path)
        # print('dirs:',dirs)
        # print('files:',files)

        # Create a new directory (Label) to facilitate the copying of two registered files (the move file and the move_label file) from B2000.
        if 1 < len(dirs) < 10:
            new_file_path = path+'\\'+'Label'
            # print('new_file_path:', new_file_path)
            # os.makedirs(new_file_path) 

        for file in files:
            # print('path:', path)
            # print('dirs:', dirs)
            # print('files:', files)
            if file == 'B2000_label.nii.gz':
                move_path = os.path.join(path, 'B2000_blur_N4_RPI.nii.gz')
                move_path_new = new_file_path+'\\'+'B2000_blur_N4_RPI.nii.gz'
                # print('move_path:', move_path, '\n')
                # print('move_path_new:', move_path_new, '\n')


                shutil.copyfile(move_path, move_path_new)


    print('done')

Copy(dir_path)





