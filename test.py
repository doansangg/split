from plate_line_recognition import plate_line_recognition
import pandas as pd
import cv2
import os
file=open('train.txt','w+')
file1=open('val.txt','w+')
path='dataplate.csv'
df=pd.read_csv(path)
list_img=df['filename\tlabel'].tolist()
ann=[img.split("\t") for img in list_img]
annotations=[]
for x in ann:
    if x[1] in not ['Error']:
        t=x.split('/')
        try:
            os.mkdir(t[2])
        except OSError:
            pass
        img=cv2.imread(x[0])
        if img is not None:
            splited_index, line1_img, line2_img = plate_line_recognition(img)
            if splited_index == -1:
                cv2.imwrite(t[2]+'/'+t[3],img)
                str_1=t[2]+'/'+t[3]+'\t'+x[1]+'\n'
                annotations.append(str_1)
            else :
                l=x[1].split("/")
                cv2.imwrite(t[2]+'_1'+'/'+t[3],line1_img)
                cv2.imwrite(t[2]+'_2'+'/'+t[3],line2_img)
                str_2=t[2]+'_1'+'/'+t[3]+'\t'+l[0]+'\n'
                str_3=t[2]+'_2'+'/'+t[3]+'\t'+l[1]+'\n'
                annotations.append(str_2)
                annotations.append(str_3)
lenght=len(annotations)
k=int(lenght*0.2)
for i in range(0,k):
    file1.write(annotations[i])
for i in range(k,lenght):
    file.write(annotations[i])
file1.close()
file.close()