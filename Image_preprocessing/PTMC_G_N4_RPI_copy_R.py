import os
import shutil
import ants
import traceback
import SimpleITK as sitk

dir_path = r'/media/wqj/0A9AD66165F33762/Pystudy/Thyroid_P_N/data/PTMC'

def Reg(dir_path):

    for paths,dirs,filenames in os.walk(dir_path):

        if 'Label' in paths:
            # print('paths:',paths)
            # print('dirs:',dirs)
            # print('files:',filenames)
            move_file = os.path.join(paths, 'B2000_blur_N4_RPI.nii.gz')
            # print('move_file:', move_file)
            move_img = ants.image_read(move_file)

            move_label_file = os.path.join(paths, 'B2000_label.nii.gz')
            # print('move_label_file:', move_label_file)
            move_label_img = ants.image_read(move_label_file)

            for file in filenames:
                if file !='B2000_blur_N4_RPI.nii.gz' and file !='B2000_label.nii.gz':

                    fix_file = paths+'/'+file
                    # print('fix_path:', fix_file, '\n')
                    fix_img = ants.image_read(fix_file)

                    # registration
                    outs = ants.registration(fix_img, move_img, type_of_transforme='ElasticSyN')

                    # Acquire the transformation matrix from move to fix; apply it to move_label; select nearest neighbor interpolation as the interpolation method. At this time, correspondingly transform the label to the registered move image
                    reg_label_img = ants.apply_transforms(fix_img, move_label_img, transformlist=outs['fwdtransforms'], interpolator='nearestNeighbor')

                    # Save the registered label to its respective directory
                    reg_label_img_save = os.path.splitext(fix_file)[0]
                    reg_label_img_save = os.path.splitext(reg_label_img_save)[0]
                    # print('reg_label_img_save:',reg_label_img_save)
                    ants.image_write(reg_label_img, reg_label_img_save + '_label.nii.gz')

    print('done')

Reg(dir_path)



