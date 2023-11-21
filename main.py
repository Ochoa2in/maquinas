import pyromat as pm

pm.config["unit_pressure"] = "kPa"
pm.config["def_p"] = 100

mp_water = pm.get("mp.H2O")

def calcular_presion_de_bomba(p1):
    T1 = mp_water.Ts(p=p1)[0]
    s1 = mp_water.ss(p=p1)[0]
    return T1, s1
def obtener_trabajo_bomba(p1,p2):
    v = 1/mp_water.ds(p=p1)[0]
    w_p = v*(p2-p1)
    return w_p
def obtener_entalpia_de_salida_y_temp_out(p1,p2,w_p):
    h1 = mp_water.hs(p=p1)[0]
    h2 = h1+w_p
    T2 = mp_water.T_h(p=p2,h=h2)
    print (h2)
    return h2,T2
def datos_turbina_alta_presion(p3):
    p3 = p2
    h3,s3,d3 = mp_water.hsd(T=T3,p=p3)
    return T3,h3,s3 
def isentropico_turbina_alta_presion(s4):
    for x in range(10,100,10):
        p4=x
    if x4<1:
        T4, x4 = mp_water.T_s(s=s4,p=p4, quality=True)
        h4 = mp_water.h(p=p4,x=x4)

    elif x4>1:
        T4 = mp_water.T_h(p=p4,h=h4)
        h4 = mp_water.h(p=p4,s=s4)
    else: 
    #no es vapor
        pass 
    return x4
def salida_de_turbina_AP(p5):
    h5,s5,d5 = mp_water.hsd(T=T5,p=p5)
    return h5,s5
def salida_de_turbina_BP(p6,s6):
    if x6<1:
        T6, x6 = mp_water.T_s(s=s6,p=p6, quality=True)
        h6 = mp_water.h(p=p6,x=x6)

    elif x6>1:
        T6 = mp_water.T_h(p=p6,h=h6)
        h6 = mp_water.h(p=p6,s=s6)
    else: 
    #no es vapor
        pass 
    return h6,x6
def calor_entrada_salida(h1,h2,h3,h4,h5,h6):
    q_ent = (h3 - h2) + (h5 - h4)     #print(f"calor de entrada: {round(float(q_ent),2)} kJ/kg")
    q_sal = h1 - h6                   #print(f"calor rechazado por condensador: {round(float(q_sal),2)} kJ/kg")
    return q_ent,q_sal
def calor_neto(q_ent,q_sal):          
    q_neto = q_ent - q_sal
    return q_neto                      #print(f"calor neto: {round(float(q_neto),2)} kJ/kg")
def tasa_flujo_masico(W_dot_neto,h3,h4,h5,h6,w_p):
    m = W_dot_neto/(abs(h4-h3)+abs(h6-h5)-abs(w_p))
    return m                              #La tasa de flujo másico del vapor en el ciclo se determina como sigue
def tasa_elim_entra_calor(m,q_ent,q_sal):
    Q_ENT = m*q_ent
    Q_SAL = m*q_sal
    return Q_ENT,Q_SAL
def eficiencia_termica_ciclo(W_dot_neto,)Q_ENT:
    n_ter=W_dot_neto/Q_ENT
    return n_ter
    
print(f"eficiencia = {round(float(n_ter),3)} ")



W_dot_neto = 5000
p1=68.9
T3 = 315.56+273.15
T5 = 315.56+273.15
p6 = 68.9

T3_Lsat = mp_water.Ts(p=p3)
s3_Lsat = mp_water.ss(p=p3)[1]

T3_Vsat = mp_water.Ts(p=p3)[0]
s3_Vsat = mp_water.ss(p=p3)[0]



