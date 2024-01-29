import tkinter

window = tkinter.Tk()
window.geometry("400x250")
window.title("BMI CALCULATOR")

label_weight = tkinter.Label(text="Enter your weight (kg)",pady=10)
label_weight.pack()
weight_input = tkinter.Entry(bg="White",fg="Black",width=20)
weight_input.pack()

label_height = tkinter.Label(text="Enter your height (cm)",pady=10)
label_height.pack()
height_input = tkinter.Entry(bg="White",fg="Black",width=20)
height_input.pack()


label_bmi = tkinter.Label()
label_bmi.pack()

def button_click():
    if str(weight_input.get()) =="":
        label_bmi.config(text="Please enter both values")
    else:

        if str(height_input.get()) =="":
            label_bmi.config(text="Please enter both values")
        else:
            try:
                bmi = int(weight_input.get())/((int(height_input.get())*int(height_input.get()))/10000)
                bmi = round(bmi,2)
                if bmi <= 18.5:
                    label_bmi.config(text=f"Your BMI Is: {str(bmi)}. You are Underweight")
                elif bmi <= 24.9:
                    label_bmi.config(text=f"Your BMI Is: {str(bmi)}. You are Normal weight")
                elif bmi <= 29.9:
                    label_bmi.config(text=f"Your BMI Is: {str(bmi)}. You are Overweight")
                else:
                    label_bmi.config(text=f"Your BMI Is: {str(bmi)}. You are Obese")
            except:
                label_bmi.config(text="Please enter integer")


button = tkinter.Button(text="Calculate",command=button_click)
button.pack()


window.mainloop()