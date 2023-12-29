import numpy as np
import pandas as pd
import openpyxl
from openpyxl import load_workbook
import os
from radiomics import featureextractor

dir_path = r'E:\Pystudy\Thyroid_P_N\data\NHT'

def FA(dir_path):

    para_path = r'E:\Pystudy\Thyroid_P_N\Feature_extract\Para_thyroid.yaml'
    result_path = r'E:\Pystudy\Thyroid_P_N\data\results\NHT_results.xlsx'
    extractor = featureextractor.RadiomicsFeatureExtractor(para_path)

    if os.path.exists(result_path):
        writer = pd.ExcelWriter(result_path, engine='openpyxl', mode='w')

    df1_ADC = pd.DataFrame()
    df2_BO = pd.DataFrame()
    df3_B800 = pd.DataFrame()
    df4_B2000 = pd.DataFrame()
    df5_T1 = pd.DataFrame()
    df6_T1_C = pd.DataFrame()
    df7_T2 = pd.DataFrame()

    for paths,dirs,filenames in os.walk(dir_path):
        # print('paths:',paths)
        # print('dirs:',dirs)
        # print('files:',filenames, '\n')

        if 'ADC' in paths:
            sheet_name = 'ADC'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)
            image_path = os.path.join(paths, filenames[0])
            label_path = os.path.join(paths, filenames[1])
            print('image_path:', image_path)
            print('label_path:', label_path,'\n')

            featureVector = extractor.execute(image_path, label_path)
            fe_ADC = pd.DataFrame.from_dict(featureVector.values()).T
            fe_ADC.columns = featureVector.keys()
            df1_ADC = pd.concat([df1_ADC,fe_ADC])
            # print('df1_ADC:', df1_ADC)
            df1_ADC.to_excel(writer, sheet_name=sh,index=False, header=True)
            writer.save()
        elif len(filenames) == 0 and os.path.split(paths)[1] != 'Data_NHT' and 'ADC' not in dirs:
            sheet_name = 'ADC'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)
            fe_ADC_nan = pd.DataFrame([np.nan])
            df1_ADC = pd.concat([df1_ADC, fe_ADC_nan])
            # print('df1_ADC:', df1_ADC)
            df1_ADC.to_excel(writer, sheet_name=sh, index=False, header=True)
            df1_ADC.to_excel(writer, sheet_name=sh, index=False, header=True)

        if 'B0' in paths:

            sheet_name = 'B0'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)
            image_path = os.path.join(paths, filenames[0])
            label_path = os.path.join(paths, filenames[1])
            print('image_path:', image_path)
            print('label_path:', label_path,'\n')

            featureVector = extractor.execute(image_path, label_path)
            fe_B0 = pd.DataFrame.from_dict(featureVector.values()).T
            fe_B0.columns = featureVector.keys()
            df2_BO = pd.concat([df2_BO, fe_B0])
            # print('df2_B0:', df2_B0)
            df2_BO.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()
        elif len(filenames) == 0 and os.path.split(paths)[1] != 'Data_NHT' and 'B0' not in dirs:
            sheet_name = 'B0'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)

            fe_B0_nan = pd.DataFrame([np.nan])
            df2_BO = pd.concat([df2_BO, fe_B0_nan])
            # print('df2_B0:', df2_BO)
            df2_BO.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()

        if 'B800' in paths:

            sheet_name = 'B800'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)
            image_path = os.path.join(paths, filenames[0])
            label_path = os.path.join(paths, filenames[1])
            print('image_path:', image_path)
            print('label_path:', label_path,'\n')

            featureVector = extractor.execute(image_path, label_path)
            fe_B800 = pd.DataFrame.from_dict(featureVector.values()).T
            fe_B800.columns = featureVector.keys()
            df3_B800 = pd.concat([df3_B800, fe_B800])
            # print('df3_B800:', df3_B800)
            df3_B800.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()
        elif len(filenames) == 0 and os.path.split(paths)[1] != 'Data_NHT' and 'B800' not in dirs:
            sheet_name = 'B800'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)

            fe_B800_nan = pd.DataFrame([np.nan])
            df3_B800 = pd.concat([df3_B800, fe_B800_nan])
            # print('df3_B800:', df3_B800)
            df3_B800.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()

        if 'B2000' in paths:

            sheet_name = 'B2000'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)
            image_path = os.path.join(paths, filenames[0])
            label_path = os.path.join(paths, filenames[1])
            print('image_path:', image_path)
            print('label_path:', label_path,'\n')

            featureVector = extractor.execute(image_path, label_path)
            fe_B2000 = pd.DataFrame.from_dict(featureVector.values()).T
            fe_B2000.columns = featureVector.keys()
            df4_B2000 = pd.concat([df4_B2000, fe_B2000])
            # print('df4_B2000:', df4_B2000)
            df4_B2000.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()
        elif len(filenames) == 0 and os.path.split(paths)[1] != 'Data_NHT' and 'B2000' not in dirs:
            sheet_name = 'B2000'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)

            fe_B2000_nan = pd.DataFrame([np.nan])
            df4_B2000 = pd.concat([df4_B2000, fe_B2000_nan])
            # print('df4_T1:', df4_B2000)
            df4_B2000.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()

        if 'T1' in paths and 'T1_C' not in paths:

            sheet_name = 'T1'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)
            image_path = os.path.join(paths, filenames[0])
            label_path = os.path.join(paths, filenames[1])
            print('image_path:', image_path)
            print('label_path:', label_path,'\n')

            featureVector = extractor.execute(image_path, label_path)
            fe_T1 = pd.DataFrame.from_dict(featureVector.values()).T
            fe_T1.columns = featureVector.keys()
            df5_T1 = pd.concat([df5_T1, fe_T1])
            # print('df5_T1:', df5_T1)
            df5_T1.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()
        elif len(filenames) == 0 and os.path.split(paths)[1] != 'Data_NHT' and 'T1' not in dirs:
            sheet_name = 'T1'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)

            fe_T1_nan = pd.DataFrame([np.nan])
            df5_T1 = pd.concat([df5_T1, fe_T1_nan])
            # print('df5_T1_nan:', df5_T1)
            df5_T1.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()

        if 'T1_C' in paths:
            sheet_name = 'T1_C'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)
            image_path = os.path.join(paths, filenames[0])
            label_path = os.path.join(paths, filenames[1])
            print('image_path:', image_path)
            print('label_path:', label_path,'\n')

            featureVector = extractor.execute(image_path, label_path)
            fe_T1_C = pd.DataFrame.from_dict(featureVector.values()).T
            fe_T1_C.columns = featureVector.keys()
            df6_T1_C = pd.concat([df6_T1_C, fe_T1_C])
            # print('df6_T1_C:', df6_T1_C)
            df6_T1_C.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()
        elif len(filenames) == 0 and os.path.split(paths)[1] != 'Data_NHT' and 'T1_C' not in dirs:
            sheet_name = 'T1_C'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)

            fe_T1_C_nan = pd.DataFrame([np.nan])
            df6_T1_C = pd.concat([df6_T1_C, fe_T1_C_nan])
            # print('df6_T1_C:', df6_T1_C)
            df6_T1_C.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()


        if 'T2' in paths:

            sheet_name = 'T2'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)
            image_path = os.path.join(paths, filenames[0])
            label_path = os.path.join(paths, filenames[1])
            print('image_path:', image_path)
            print('label_path:', label_path,'\n')

            featureVector = extractor.execute(image_path, label_path)
            fe_T2 = pd.DataFrame.from_dict(featureVector.values()).T
            fe_T2.columns = featureVector.keys()
            df7_T2 = pd.concat([df7_T2,fe_T2])
            # print('df7_T2:', df7_T2)
            df7_T2.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()
        elif len(filenames) == 0 and os.path.split(paths)[1] != 'Data_NHT' and 'T2' not in dirs:
            sheet_name = 'T2'
            sh = '{}'.format(sheet_name)
            # print('sheet_name:', sh)

            fe_T2_nan = pd.DataFrame([np.nan])
            df7_T2 = pd.concat([df7_T2, fe_T2_nan])
            # print('df7_T2:', df7_T2)
            df7_T2.to_excel(writer, sheet_name=sh, index=False, header=True)
            writer.save()


    writer.close()
    print('Done')


FA(dir_path)


