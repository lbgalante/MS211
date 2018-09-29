#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
EPSILON = 0.0001

#Iteration counters
i_bissecao = 0
i_fpos = 0
i_newton = 0
i_newton_mr = 0
i_secante = 0


#Function and respective derivative and second derivative
def func(x):
    return 2*x**5 - 20*x**4 + 68*x**3 - 104*x**2 + 74*x - 20

def dfunc(x):
    return 10*x**4 - 80*x**3 + 204*x**2 - 208*x + 74

def ddfunc(x):
    return 40*x**3 -  240*x**2 + 408*x - 208

def section_divider():
    print("-------------------------------")

#Methods for finding roots
def bissecao(a, b):
    global i_bissecao
    i_bissecao += 1
    f_a = func(a)
    f_b = func(b)
    if(f_a*f_b > 0):
        print("Escolha a e b diferentes")
        return
    m = (a+b)/2
    f_m = func(m)
    print('Media: '+str(m)+' F_m: '+str(f_m))
    if(math.fabs(f_m) < EPSILON):
        print("METODO DA BISSECAO")
        print("Achou a raiz: "+str(m))
        print("Numero de iteracoes: "+str(i_bissecao))
        section_divider()
        return
    if(f_a*f_m < 0):
        bissecao(a,m)
    else:
        bissecao(m,b)

def falsaposicao(a,b):
    global i_fpos
    i_fpos += 1
    f_a = func(a)
    f_b = func(b)
    if(f_a*f_b > 0):
            print("Escolha a e b diferentes")
            return
    m = (a*f_b - b*f_a)/(f_b - f_a)
    f_m = func(m)
    print('Media: '+str(m)+' F_m: '+str(f_m))
    if(math.fabs(f_m) < EPSILON):
        print("METODO DA FALSA POSICAO")
        print("Achou a raiz: "+str(m))
        print("Numero de iteracoes: "+str(i_fpos))
        section_divider()
        return
    if(f_a*f_m < 0):
        falsaposicao(a,m)
    else:
        falsaposicao(m,b)

def newton(x):
    global i_newton
    i_newton += 1
    f_x = func(x)
    df_x = dfunc(x)
    if(df_x == 0.0):
        print('DIVISION BY ZERO EXCEPTION: df_x is zero, try another value.')
        exit(1)
    m = x - (f_x/df_x)
    f_m = func(m)
    print('Media: '+str(m)+' F_m: '+str(f_m))
    if(math.fabs(f_m) < EPSILON):
        print("METODO DE NEWTON")
        print("Achou a raiz: "+str(m))
        print("Numero de iteracoes: "+str(i_newton))
        section_divider()
        return
    else:
        newton(m)

def secante(x1,x0):
    global i_secante
    i_secante += 1
    f_x1 = func(x1)
    f_x0 = func(x0)
    m = x1 - f_x1*((x1 - x0)/(f_x1 - f_x0))
    f_m = func(m)
    print('Media: '+str(m)+' F_m: '+str(f_m))
    if(math.fabs(f_m) < EPSILON):
        print("METODO DA SECANTE")
        print("Achou a raiz: "+str(m))
        print("Numero de iteracoes: "+str(i_secante))
        section_divider()
        return
    else:
        secante(m,x1)

#Newton method for square roots
def newton_sqrt(a):
    i = 1 #counter
    x = a #init x
    f_x = 1 #init f_x
    while(math.fabs(f_x) > EPSILON):
        x = (x**2 + a)/(2*x)
        f_x = x**2 - a
        #print('X: '+str(x)+' F_x: '+str(f_x))
        i += 1
    print('THE SQUARE ROOT OF', a ,'IS', x, 'WITH',i,'ITERATIONS')
    section_divider()

#Newton method for 1/a calculations
def divbyA(a):
    i = 1 #counter
    x = 0.1 #init x
    f_x = 1 #init f_x
    while(math.fabs(f_x) > EPSILON):
        x = 2*x - a*x**2
        f_x = (1/x) - a
        print('X: '+str(x)+' F_x: '+str(f_x))
        i += 1
    print('1/A FOR A:', a ,'IS', x, 'WITH',i,'ITERATIONS')
    section_divider()

#Newton method for roots with multiplicity
def newton_mult_root(x):
    global i_newton_mr
    i_newton_mr += 1
    f_x = func(x)
    df_x = dfunc(x)
    ddf_x = ddfunc(x)
    if(df_x == 0.0):
        print('DIVISION BY ZERO EXCEPTION: df_x is zero, try another value.')
        exit(1)
    m = x - (f_x*df_x)/((df_x**2)-f_x*ddf_x)
    f_m = func(m)
    print('Media: '+str(m)+' F_m: '+str(f_m))
    if(math.fabs(f_m) < EPSILON):
        print("METODO DE NEWTON PARA RAIZES MULTIPLAS")
        print("Achou a raiz: "+str(m))
        print("Numero de iteracoes: "+str(i_newton_mr))
        section_divider()
        return
    else:
        newton_mult_root(m)


#Pontos iniciais para os algoritmos

bissecao(0.0,9.0)
secante(0.0,9.0)
newton(0.5)
newton_mult_root(0.5)
