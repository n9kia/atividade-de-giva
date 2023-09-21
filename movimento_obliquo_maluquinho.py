import math
m=0.5
g=10
t=[]
y0=0
x0=0

x=float(input("me diga a cordenada de x"))
y=float(input("me diga a cordenada de y"))

f=float(input("me diga, em newtons, a força"))

zero=float(input("insira pelo amor de Deus um ângulo"))
 
angulo_rad=math.radians(zero)
angulocos=math.cos(angulo_rad)
angulosin= math.sin(angulo_rad)

#velocidade inicial 
def velo_inicial(f,m):
    v0= f*1/m
    return v0
#velocidade inicial de x e y
def velo_inicial_x(angulocos,v0):
    vx=v0*angulocos
    return vx

def velo_ini_y(v0,angulosin):
    vy=v0*angulosin
    return vy

#velocidade de y
def velo_y (vy,g,t):
    vely=vy - g*t
    return vely

# tempo do voo
def tempo_maximo(vy,g):
    tx= 2*vy/g
    return tx
# altura maxima
def y_maximo(vy,t,g,tx,y0,):
    t=tx/2
    yx=y0+vy*t-g*t**2/2
    return yx
# local da queda
def xmax(x0,vx,tx):
    xm=x0+vx*tx
    return xm

print(f"a velocidade inicial é:{velo_inicial(f,m)}")