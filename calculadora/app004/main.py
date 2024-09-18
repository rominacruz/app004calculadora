import flet as ft

def cal_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value"Error Ingresa valores correctos"
        

def calc_resta(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1-num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value"Error Ingresa valores correctos"
        
    

def calc_mult(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1*num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value"Error Ingresa valores correctos"
        
    
def cal_div(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1/num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value"Error Ingresa valores correctos"

#funciones de manejo de manejo de eventos 
def on_calc_suma(e):
    calc_suma(txtNum1, txtNum2, lblResultado)
    page.update()

def on_calc_resta(e):
    calc_resta(txtNum1, txtNum2, lblResultado)
    page.update()

def on_calc_mult(e):
    calc_mult(txtNum1, txtNum2, lblResultado)
    page.update()

def on_calc_div(e):
    calc_div(txtNum1, txtNum2, lblResultado)
    page.update() 
    
def limpiar(e):
    txtNum1.value = ""
    txtNum2.value = ""
    lblResultado.value = "Resuslado:"
    pagex.update()






ft.app(main) 
