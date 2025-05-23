from tkinter import *
import math

def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    result = str(math.cot(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def sign_change():
    global calc_operator
    if calc_operator[0] == '-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)

def percent():
    global calc_operator
    temp = str(eval(calc_operator + '/100'))
    calc_operator = temp
    text_input.set(temp)

def button_equal():
    global calc_operator
    result = ""
    if(calc_operator!= " "):
        try:
            temp_op = str(eval(calc_operator))
        except:
            temp_op = "Can't Divide By Zero"
    text_input.set(temp_op)
    calc_operator = temp_op

sin = math.sin
cos = math.cos
tan = math.tan
e = math.exp
p = math.pi
E = '*10**'

tk_calc = Tk()
tk_calc.configure(bg = "#293C4A",bd = 10)
tk_calc.title("Scientific Calculator")

calc_operator = ""
text_input = StringVar()
text_display = Entry(tk_calc,font=('sans-serif',20,'bold'),textvariable = text_input,
                     bd=5,insertwidth=5,bg='#BBB',justify='right').grid(columnspan=5,padx=10,pady=15)

button_params = {'bd':5,'fg':'#BBB','bg':'#3C3636','font':('sans-serif',20,'bold')}
button_params_main = {'bd':5,'fg':'#000','bg':'#BBB','font':('sans-serif',20,'bold')}

sine = Button(tk_calc,button_params,text='sin',command=trig_sin).grid(row=1,column=0,sticky="nsew")
cosine = Button(tk_calc,button_params,text='cos',command=trig_cos).grid(row=1,column=1,sticky="nsew")

tangent = Button(tk_calc,button_params,text='tan',command=trig_tan).grid(row=1,column=2,sticky="nsew")
cotangent = Button(tk_calc,button_params,text='cot',command=trig_cot).grid(row=1,column=3,sticky="nsew")

pi_num = Button(tk_calc,button_params,text='pi',command=lambda:button_click(str(math.pi))).grid(row=1,column=4,sticky="nsew")
second_power = Button(tk_calc,button_params,text='x\u00B2',command=lambda:button_click('**2')).grid(row=2,column=0,sticky="nsew")
third_power = Button(tk_calc,button_params,text='x\u00B3',command=lambda:button_click('**3')).grid(row=2,column=1,sticky="nsew")

nth_power = Button(tk_calc,button_params,text='x^n',command=lambda:button_click('**')).grid(row=2,column=2,sticky="nsew")
inv_power = Button(tk_calc,button_params,text='x\u207b\xb9',command=lambda:button_click('**(-1)')).grid(row=2,column=3,sticky="nsew")

tens_powers = Button(tk_calc,button_params,text='10^x',font=('sans-serif',15,'bold'),command=lambda:button_click('10**')).grid(row=2,column=4,sticky="nsew")
left_par = Button(tk_calc,button_params,text='(',command=lambda:button_click('(')).grid(row=3,column=0,sticky="nsew")
right_par = Button(tk_calc,button_params,text=')',command=lambda:button_click(')')).grid(row=3,column=1,sticky="nsew")

signs = Button(tk_calc,button_params,text='\u00B1',command=sign_change).grid(row=3,column=2,sticky="nsew")
percentage = Button(tk_calc,button_params,text='%',command=percent).grid(row=3,column=3,sticky="nsew")
ex = Button(tk_calc,button_params,text='e^x',command=lambda:button_click('e(')).grid(row=3,column=4,sticky="nsew")

button_7 = Button(tk_calc,button_params_main,text='7',command=lambda:button_click('7')).grid(row=4,column=0,sticky="nsew")
button_8 = Button(tk_calc,button_params_main,text='8',command=lambda:button_click('8')).grid(row=4,column=1,sticky="nsew")
button_9 = Button(tk_calc,button_params_main,text='9',command=lambda:button_click('9')).grid(row=4,column=2,sticky="nsew")

delete_one = Button(tk_calc,bd=5,fg='#000',font=('sans-serif',20,'bold'),text='DEL',command=button_delete,bg='#db701f').grid(row=4,column=3,sticky="nsew")
delete_all = Button(tk_calc,bd=5,fg='#000',font=('sans-serif',20,'bold'),text='AC',command=button_clear_all,bg='#db701f').grid(row=4,column=4,sticky="nsew")

button_4 = Button(tk_calc,button_params_main,text='4',command=lambda:button_click('4')).grid(row=5,column=0,sticky="nsew")
button_5 = Button(tk_calc,button_params_main,text='5',command=lambda:button_click('5')).grid(row=5,column=1,sticky="nsew")
button_6 = Button(tk_calc,button_params_main,text='6',command=lambda:button_click('6')).grid(row=5,column=2,sticky="nsew")

mul = Button(tk_calc,button_params_main,text='*',command=lambda:button_click('*')).grid(row=5,column=3,sticky="nsew")
div = Button(tk_calc,button_params_main,text='/',command=lambda:button_click('/')).grid(row=5,column=4,sticky="nsew")

button_1 = Button(tk_calc,button_params_main,text='1',command=lambda:button_click('1')).grid(row=6,column=0,sticky="nsew")
button_2 = Button(tk_calc,button_params_main,text='2',command=lambda:button_click('2')).grid(row=6,column=1,sticky="nsew")
button_3 = Button(tk_calc,button_params_main,text='3',command=lambda:button_click('3')).grid(row=6,column=2,sticky="nsew")

add = Button(tk_calc,button_params_main,text='+',command=lambda:button_click('+')).grid(row=6,column=3,sticky="nsew")
sub = Button(tk_calc,button_params_main,text='-',command=lambda:button_click('-')).grid(row=6,column=4,sticky="nsew")

button_0 = Button(tk_calc,button_params_main,text='0',command=lambda:button_click('0')).grid(row=7,column=0,sticky="nsew")
point = Button(tk_calc,button_params_main,text='.',command=lambda:button_click('.')).grid(row=7,column=1,sticky="nsew")

exp = Button(tk_calc,button_params_main,text='EXP',font=('sans-serif',16,'bold'),command=lambda:button_click('E')).grid(row=7,column=2,sticky="nsew")
equal = Button(tk_calc,button_params_main,text='=',command=button_equal).grid(row=7,columnspan=2,column=3,sticky="nsew")

tk_calc.mainloop()
