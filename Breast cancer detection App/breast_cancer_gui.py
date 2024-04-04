from tkinter import *
from CVD_breast_cancer_model import *

def main():

    def button():
        result_str = ""
        bc_prediction_text.delete("1.0","end")


        #Gets Mean
        radiusMean =radius_m.get()
        textureMean = texture_m.get()
        perimeterMean = perimeter_m.get()
        areaMean= area_m.get()
        smoothnessMean = smoothness_m.get()
        compactnessMean = compactness_m.get()
        concavityMean = concavity_m.get()
        concaveMean = concave_m.get()
        symmetryMean =symmetry_m.get()
        fractalMean = frac_dim_m.get()

        #Gets standard Error
        radiusSE =radius_se.get()
        textureSE = texture_se.get()
        perimeterSE = perimeter_se.get()
        areaSE= area_se.get()
        smoothnessSE = smoothness_se.get()
        compactnessSE = compactness_se.get()
        concavitySE = concavity_se.get()
        concaveSE = concave_point_se.get()
        symmetrySE =symmetry_se.get()
        fractalSE = frac_dim_se.get()

        #Gets worst Mean
        radiusWorst =radius_worst.get()
        textureWorst = texture_worst.get()
        perimeterWorst = perimeter_worst.get()
        areaWorst= area_worst.get()
        smoothnessWorst = smoothness_worst.get()
        compactnessWorst = compactness_worst.get()
        concavityWorst = concavity_worst.get()
        concaveWorst = concave_point_worst.get()
        symmetryWorst =symmetry_worst.get()
        fractalWorst = frac_dim_worst.get()

        #creating result
        result_str +='----Patient Result----'
        patient_data = (radiusMean,textureMean,perimeterMean,areaMean,smoothnessMean,compactnessMean,
                        concavityMean,concaveMean,symmetryMean,fractalMean, radiusSE,textureSE,perimeterSE,
                        areaSE,smoothnessSE,compactnessSE,concavitySE,concaveSE,symmetrySE,fractalSE,
                        radiusWorst,textureWorst,perimeterWorst,areaWorst,smoothnessWorst,compactnessWorst,
                        concavityWorst,concaveWorst,symmetryWorst,fractalWorst)

        bc_prediction = best_model.predict([patient_data])
        accuracy_string = str("This prediction has an accuracy of: "+str(model_accuracy))

        #Model predicted 1 as "Benign" and 0 as "Malignant" so result had to be swapped around
        if(bc_prediction == [1]):
            result_str = str(accuracy_string +'\n'+'Benign - You have a low chance of having breast cancer')
        else:
            result_str = str(accuracy_string+ '\n'+ 'Malignant - You have a high chance of you having of breast cancer')
        bc_prediction_text.insert('1.0',result_str)
    window = Tk()

    #mean column
    Label(window,text="Mean").grid(row=0,column=0,columnspan=2)

    Label(window,text="Radius Mean").grid(row=1,column=0)
    Label(window,text= "Texture Mean").grid(row = 2,column=0)
    Label(window,text="Perimeter Mean").grid(row=3,column=0)
    Label(window,text="Area Mean").grid(row=4,column=0)
    Label(window,text="Smoothness Mean").grid(row=5,column=0)
    Label(window,text="Compactness Mean").grid(row=6,column=0)
    Label(window,text= "Concavity Mean").grid(row = 7,column=0)
    Label(window,text="Concave Points Mean").grid(row=8,column=0)
    Label(window,text="Symmetry Mean").grid(row=9,column=0)
    Label(window,text="Fractal Dimension Mean").grid(row=10,column=0)

    radius_m = IntVar()
    texture_m= IntVar()
    perimeter_m = IntVar()
    area_m = IntVar()
    smoothness_m = IntVar()
    compactness_m = IntVar()
    concavity_m = IntVar()
    concave_m = IntVar()
    symmetry_m = IntVar()
    frac_dim_m = IntVar()

    Entry(window,textvariable=radius_m).grid(row=1,column=1)
    Entry(window,textvariable=texture_m).grid(row=2,column=1)
    Entry(window,textvariable=perimeter_m).grid(row=3,column=1)
    Entry(window,textvariable=area_m).grid(row=4,column=1)
    Entry(window,textvariable=smoothness_m).grid(row=5,column=1)
    Entry(window,textvariable=compactness_m).grid(row=6,column=1)
    Entry(window,textvariable=concavity_m).grid(row=7,column=1)
    Entry(window,textvariable=concave_m).grid(row=8,column=1)
    Entry(window,textvariable=symmetry_m).grid(row=9,column=1)
    Entry(window,textvariable=frac_dim_m).grid(row=10,column=1)


    #Standard error column(se)

    Label(window,text="Mean").grid(row=0,column=1,columnspan=2)

    Label(window,text="Radius Standard Error").grid(row=1,column=2)
    Label(window,text= "Texture Standard Error").grid(row = 2,column=2)
    Label(window,text="Perimeter Standard Error").grid(row=3,column=2)
    Label(window,text="Area Standard Error").grid(row=4,column=2)
    Label(window,text="Smoothness Standard Error").grid(row=5,column=2)
    Label(window,text="Compactness Standard Error").grid(row=6,column=2)
    Label(window,text= "Concavity Standard Error").grid(row =7,column=2)
    Label(window,text="Concave Points Standard Error").grid(row=8,column=2)
    Label(window,text="Symmetry Standard Error").grid(row=9,column=2)
    Label(window,text="Fractal Dimension Standard Error").grid(row=10,column=2)

    radius_se = IntVar()
    texture_se= IntVar()
    perimeter_se = IntVar()
    area_se = IntVar()
    smoothness_se = IntVar()
    compactness_se = IntVar()
    concavity_se = IntVar()
    concave_point_se = IntVar()
    symmetry_se = IntVar()
    frac_dim_se = IntVar()

    Entry(window,textvariable=radius_se).grid(row=1,column=3)
    Entry(window,textvariable=texture_se).grid(row=2,column=3)
    Entry(window,textvariable=perimeter_se).grid(row=3,column=3)
    Entry(window,textvariable=area_se).grid(row=4,column=3)
    Entry(window,textvariable=smoothness_se).grid(row=5,column=3)
    Entry(window,textvariable=compactness_se).grid(row=6,column=3)
    Entry(window,textvariable=concavity_se).grid(row=7,column=3)
    Entry(window,textvariable=concave_point_se).grid(row=8,column=3)
    Entry(window,textvariable=symmetry_se).grid(row=9,column=3)
    Entry(window,textvariable=frac_dim_se).grid(row=10,column=3)

    #Worst(Largest Mean Value
    Label(window,text="Worst").grid(row=0,column=2,columnspan=2)

    Label(window,text="Radius Worst").grid(row=1,column=4)
    Label(window,text= "Texture Worst").grid(row = 2,column=4)
    Label(window,text="Perimeter Worst").grid(row=3,column=4)
    Label(window,text="Area Worst").grid(row=4,column=4)
    Label(window,text="Smoothness Worst").grid(row=5,column=4)
    Label(window,text="Compactness Worst").grid(row=6,column=4)
    Label(window,text= "Concavity Worst").grid(row = 7,column=4)
    Label(window,text="Concave Points Worst").grid(row=8,column=4)
    Label(window,text="Symmetry Worst").grid(row=9,column=4)
    Label(window,text="Fractal Dimensions Worst").grid(row=10,column=4)

    radius_worst = IntVar()
    texture_worst= IntVar()
    perimeter_worst = IntVar()
    area_worst = IntVar()
    smoothness_worst = IntVar()
    compactness_worst = IntVar()
    concavity_worst = IntVar()
    concave_point_worst = IntVar()
    symmetry_worst = IntVar()
    frac_dim_worst = IntVar()

    Entry(window,textvariable=radius_worst).grid(row=1,column=5)
    Entry(window,textvariable=texture_worst).grid(row=2,column=5)
    Entry(window,textvariable=perimeter_worst).grid(row=3,column=5)
    Entry(window,textvariable=area_worst).grid(row=4,column=5)
    Entry(window,textvariable=smoothness_worst).grid(row=5,column=5)
    Entry(window,textvariable=compactness_worst).grid(row=6,column=5)
    Entry(window,textvariable=concavity_worst).grid(row=7,column=5)
    Entry(window,textvariable=concave_point_worst).grid(row=8,column=5)
    Entry(window,textvariable=symmetry_worst).grid(row=9,column=5)
    Entry(window,textvariable=frac_dim_worst).grid(row=10,column=5)

    #button for result
    Button(window,command=button,text='Predict').grid(row=11,column=0,columnspan=5)

    #Prediction
    Label(window,text="Result:").grid(row=12,column=0,columnspan=2)
    bc_prediction_text =Text(window,bg='light blue')
    bc_prediction_text.grid(row=13,column=0,columnspan=2)

    window.mainloop()
if __name__ == '__main__':
    main()
#Reference
#Author: Unknown
#Date: Trimester 1 2023
#Title: Program called Heart Disease Predictor Capstone Project
#Version 1
#Source Code
#Template used from https://uclearn.canberra.edu.au/courses/14056/pages/week-10-project-assignment-workshop?module_item_id=1064187
