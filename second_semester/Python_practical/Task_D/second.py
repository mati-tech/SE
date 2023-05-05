# math task D001
import math as m

def calc_x(z, k , a):
    x = (m.sqrt(abs((z**3)+ 0.25 * (k**2))))/ (0.5 + 2 * m.e**(z+4)) + (k**(1/3))/ 4 - a * m.log(27, 3)
    return x

def calc_b(k, z): 
    b = (m.sin(k*z)**2) + (1/2*m.pi) * (m.atan(2*k)**2)
    return b

while True: 
    print ("1_task: enter the required args to solve the given equation: \n")
    z1 = int (input("z: "))
    k1 = int (input("k: "))
    a1 = int (input("a: "))
    print(calc_x(z1, k1, z1))

    print ("2_task: enter the required args to solve the given equation: \n")
    k2 = int (input("k: "))
    z2 = int (input("z: "))
    print(calc_b(k2, z2))
