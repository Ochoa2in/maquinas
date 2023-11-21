import pyromat as pm

pm.config["unit_pressure"] = "kPa"
pm.config["def_p"] = 100

mp_water = pm.get("mp.H2O")

def calcular_presion_de_bomba(p1):
    T1 = mp_water.Ts(p=p1)[0]
    s1 = mp_water.ss(p=p1)[0]
    return T1, s1