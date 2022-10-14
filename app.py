
import tkinter as tk

window = tk.Tk()
window.geometry("600x400")
window.title('Heart Failed Prediction')

#label
age_label = tk.Label(window,
                text='age : ',
                font=('Arial',16))
age_label.place(x=40,y=40)

anaemia_label = tk.Label(window,
                text='anaemia : ',
                font=('Arial',16))
anaemia_label.place(x=40,y=80)

CPK_label = tk.Label(window,
                text='CPK : ',
                font=('Arial',16))
CPK_label.place(x=40,y=120)

diabetes_label = tk.Label(window,
                text='diabetes : ',
                font=('Arial',16))
diabetes_label.place(x=40,y=160)

EF_label = tk.Label(window,
                text='EF : ',
                font=('Arial',16))
EF_label.place(x=40,y=200)

BP_label = tk.Label(window,
                text='BP : ',
                font=('Arial',16))
BP_label.place(x=40,y=240)

platelets_label = tk.Label(window,
                text='platelets : ',
                font=('Arial',16))
platelets_label.place(x=300,y=40)

serum_creatinine_label = tk.Label(window,
                text='serum_creatinine : ',
                font=('Arial',16))
serum_creatinine_label.place(x=300,y=80)

serum_sodium_label = tk.Label(window,
                text='serum_sodium : ',
                font=('Arial',16))
serum_sodium_label.place(x=300,y=120)

sex_label = tk.Label(window,
                text='sex : ',
                font=('Arial',16))
sex_label.place(x=300,y=160)

smoking_label = tk.Label(window,
                text='smoking : ',
                font=('Arial',16))
smoking_label.place(x=300,y=200)

time_label = tk.Label(window,
                text='time : ',
                font=('Arial',16))
time_label.place(x=300,y=240)

prob_label = tk.Label(window,
                text=' Predicted : ',
                font=('Arial',16))
prob_label.place(x=40,y=300)



#entry
age_entry = tk.Entry(window,
                font=('Arial',16),
                width=5)
age_entry.place(x=100,y=40)

anaemia_entry = tk.Entry(window,
                font=('Arial',16),
                width=5)
anaemia_entry.place(x=145,y=80)

CPK_entry = tk.Entry(window,
                font=('Arial',16),
                width=5)
CPK_entry.place(x=100,y=120)

diabetes_entry = tk.Entry(window,
                font=('Arial',16),
                width=5)
diabetes_entry.place(x=145,y=160)

EF_entry = tk.Entry(window,
                font=('Arial',16),
                width=5)
EF_entry.place(x=100,y=200)

BP_entry = tk.Entry(window,
                font=('Arial',16),
                width=5)
BP_entry.place(x=100,y=240)

platelets_entry = tk.Entry(window,
                font=('Arial',16),
                width=10)
platelets_entry.place(x=400,y=40)

serum_creatinine_entry = tk.Entry(window,
                font=('Arial',16),
                width=5)
serum_creatinine_entry.place(x=490,y=80)

serum_sodium_entry = tk.Entry(window,
                font=('Arial',16),
                width=5)
serum_sodium_entry.place(x=460,y=120)

sex_entry = tk.Entry(window,
                font=('Arial',16),
                width=5)
sex_entry.place(x=360,y=160)

smoking_entry = tk.Entry(window,
                font=('Arial',16),
                width=5)
smoking_entry.place(x=400,y=200)

time_entry = tk.Entry(window,
                font=('Arial',16),
                width=5)
time_entry.place(x=360,y=240)

#button
def click():
    inp=[]
    inp.append(int(age_entry.get()))
    inp.append(int(anaemia_entry.get()))
    inp.append(float(CPK_entry.get()))
    inp.append(float(diabetes_entry.get()))
    inp.append(float(EF_entry.get()))
    inp.append(float(BP_entry.get()))
    inp.append(float(platelets_entry.get()))
    inp.append(float(serum_creatinine_entry.get()))
    inp.append(float(serum_sodium_entry.get()))
    inp.append(float(sex_entry.get()))
    inp.append(float(smoking_entry.get()))
    inp.append(float(time_entry.get()))
    # 
    prob_label.config(text='Predicted : prob')



    inp =[]

button = tk.Button(window,
                    text='Predict!!',
                    font=('Arial',16),
                    command=click)

button.place(x=400,y=300)

window.mainloop()