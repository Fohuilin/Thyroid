import os
import SimpleITK as sitk

dir_path = r'E:\Pystudy\Thyroid_P_N\data\PTMC'

def N4(dir_path):
    if not os.path.exists(dir_path):
        print('path dose not exist')
    else:

        for path,dirs,files in os.walk(dir_path):
            if len(dirs) == 0 & len(files): # Determine if it is a subfolder (directly containing .nii files), rather than a parent folder.
                imagePath = os.path.join(path,files[1])
                input_image = sitk.ReadImage(imagePath)
                mask_image = sitk.OtsuThreshold(input_image, 0, 1, 200)
                input_image = sitk.Cast(input_image, sitk.sitkFloat32)
                corrector = sitk.N4BiasFieldCorrectionImageFilter()
                output_image = corrector.Execute(input_image, mask_image)
                output_image = sitk.Cast(output_image, sitk.sitkInt16)
                sitk.WriteImage(output_image, os.path.join(path,files[1]).split('.')[0]+'_N4.nii.gz')

    print('done')

N4(dir_path)


