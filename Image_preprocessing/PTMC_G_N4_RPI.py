import os
import SimpleITK as sitk

dir_path = r'E:\Pystudy\Thyroid_P_N\data\PTMC'

def RPI(dir_path):
    if not os.path.exists(dir_path):
        print('path dose not exist')
    else:

        for path,dirs,files in os.walk(dir_path):
            if len(dirs) == 0 & len(files): # Determine if it is a subfolder (directly containing .nii files), rather than a parent folder.
                imagePath = os.path.join(path,files[2])
                input_image = sitk.ReadImage(imagePath)
                input_image.SetDirection((1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0))  
                sitk.WriteImage(input_image, os.path.join(path,files[2]).split('.')[0]+'_RPI.nii.gz')

    print('done')

RPI(dir_path)


