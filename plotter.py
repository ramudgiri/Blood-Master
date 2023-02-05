import matplotlib.pyplot as plt
import pandas as pd
d = 0.02
A = ((22 / 7) / 4) * d ** 2
I = 0.2 # Am
V = 5 # Volt
P = (I * V) / 1000 # Kw
N = pd.read_csv('Book1.csv')
T = ((P * 60) / (2 * (22 / 7) * N)) * 1000
V1=((22/7)*d*N)/60
F1 = 2 * (T / d)
F2 = 2 * F1
Fb = 0.981 # Weight of wooden block
Ft = F2 + Fb
 
Page 46 of 74
Pr = (Ft / A) / 6
d1 = 0.015 # m
d2 = 0.002 # m
L=0.080
z1 = 0.425 # m
z2 = 0.400 # m
A1 = ((22 / 7) / 4) * (d1 * d1) # m2
A2 = ((22 / 7) / 4) * (d2 * d2) # m2
g = 9.81 # m/s
rho = 1.224
myu = 0.0055
Q = A1 * V1 # m3 / s
v2 = Q / A2
Re = (rho * d2 * v2) / myu
f = 0.316 / (Re ** 0.25)
h=((32*myu*v2*L)/(rho*g*d**2))
dp = (f * rho * v2 ** 2 * 60) / (2 * 2)
p2 = Pr - dp
#plt.plot(N, V1)
#plt.xlabel('RPM')
#plt.ylabel('Velocity')
#plt.plot(N, T)

#plt.xlabel('RPM')
#plt.ylabel('Torque(N.m)')
#plt.plot(N, Pr)
#plt.xlabel('RPM')
#plt.ylabel('Pressure (Pa)')
#plt.plot(V1, Q)
#plt.xlabel('Velocity(m/s)')
#plt.ylabel('Discharge(m3/s)')
#plt.plot(V1, Re)
#plt.xlabel('Velocity(m/s)')
#plt.ylabel("Reynold's No.")
#plt.plot(V1, Pr)
#plt.xlabel('Velocity(m/s)')
#plt.ylabel('Pressure(pa)')
#plt.plot(V1, p2)
#plt.xlabel('Velocity(m/s)')
#plt.ylabel('Pressure(pa)')
#plt.plot(V1, h)
#plt.xlabel('Velocity(m/s)')
#plt.ylabel('Frictional head loss')
plt.grid()
plt.show()
