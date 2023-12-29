import os
import SimpleITK as sitk


dir_path = r'E:\Pystudy\Thyroid_P_N\data\NHT'

def BlurImage(dir_path):
    if not os.path.exists(dir_path):
        print('path dose not exist')
    else:

        for path,dirs,files in os.walk(dir_path):
            if len(dirs) == 0 & len(files): 
                imagePath = os.path.join(path,files[0])
                input_image = sitk.ReadImage(imagePath)  
                sitk_gassuian = sitk.SmoothingRecursiveGaussianImageFilter()  
                sitk_gassuian.SetSigma(1.0)
                sitk_gassuian.NormalizeAcrossScaleOff()
                sitk_gassuian = sitk_gassuian.Execute(input_image)
                sitk.WriteImage(sitk_gassuian, os.path.join(path,files[0]).split('.')[0]+'_blur.nii.gz')

    print('done')

BlurImage(dir_path)