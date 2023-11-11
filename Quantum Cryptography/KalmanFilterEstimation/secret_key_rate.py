#New Method for secret key rate calculation
import math as math
import matplotlib.pyplot as matplot

rate = []

dist_km = []

rate_2 = []
rate_3 = []

def function_dist ( km ):

    error_phase = 0.000178    #Add phase noise here

    dist_km.append(km)

    Va = 2.5 # Enter Va here

    V = Va + 1 

    V_drift = 0.001

    error_phase = error_phase + V_drift

    e_phase = 2*Va*(1-math.exp(((-1)*(error_phase))/2))


   # e_phase = V_drift + e_phase

    att = 0.2

    #km = 20

    r_eff = 0.5

    vele = 0.1

    atte = att * km

    T = 10 ** (((-1)*atte)/10)

    print ( T )

    x_line = ( 1/T ) - 1 + e_phase

    print ("x_line", x_line)

    x_ohm = ( 1 - r_eff + vele )/r_eff

    x_tot = x_line + (x_ohm)/T

    a = V

    b = T* ( V+ x_line)

    c = math.sqrt( T*( V**2 -1 ))

    A = a**2 + b**2 - ( 2 * c**2 )

    B = ( (a*b) - c**2 )**2

    print ( a, b, c)

    print( A, B)

    C_cal = ( ( A * x_ohm ) + ( a * math.sqrt(B)) + b) / ( b + x_ohm )


    D = math.sqrt(B)* (   ( a + ( math.sqrt(B)*x_ohm) )/ (b+x_ohm) )

    print ("C" ,C_cal, D)

    #print ( A**2 - ( 4*B))

    lambda_1 = math.sqrt ( 1/2 * ( A + math.sqrt ((A**2 - ( 4*B)))))

    lambda_2 =math.sqrt( 1/2 * ( A - math.sqrt ( A**2 - ( 4*B))))

    lambda_3 = math.sqrt(1/2*( C_cal + math.sqrt ( C_cal**2 - ( 4 * D ))))

    lambda_4 = math.sqrt(1/2*( C_cal - math.sqrt ( C_cal**2 - ( 4 * D ))))

    lambda_5 = 1

    print ( lambda_1, lambda_2, lambda_3, lambda_4)

    def function_g ( x ):

        result = ( ( x + 1 )*math.log2(x+1) ) - ( x * math.log2(x) )

        return result

    g_1 = function_g ( (lambda_1-1)/2)
    g_2 = function_g ( (lambda_2-1)/2)
    g_3 = function_g ( ( lambda_3-1)/2)
    g_4 = function_g ( abs(( lambda_4-1)/2))
    #g_5 = function_g(0.5*(lambda_5-1))

    print ( g_1, g_2, g_3, g_4)

    g = g_1 +g_2 - g_3 - g_4 

    calc_temp = (V+x_tot)/(1+x_tot)

    print(calc_temp)

    I_AB = 0.5*math.log2(abs(calc_temp))

    betta = 0.95

    K = (betta*I_AB) - g

    rate.append(K)

def function_dist_2 ( km ):

    error_phase = 0.000183   #Add phase noise here

    #dist_km.append(km)

    Va = 2.5 # Enter Va here

    V = Va + 1 

    e_phase = 2*Va*(1-math.exp(((-1)*(error_phase))/2))

    V_drift = 0.1

    e_phase = V_drift + e_phase

    att = 0.2

    #km = 20

    r_eff = 0.5

    vele = 0.1

    atte = att * km

    T = 10 ** (((-1)*atte)/10)

    print ( T )

    x_line = ( 1/T ) - 1 + e_phase

    print ("x_line", x_line)

    x_ohm = ( 1 - r_eff + vele )/r_eff

    x_tot = x_line + (x_ohm)/T

    a = V

    b = T* ( V+ x_line)

    c = math.sqrt( T*( V**2 -1 ))

    A = a**2 + b**2 - ( 2 * c**2 )

    B = ( (a*b) - c**2 )**2

    print ( a, b, c)

    print( A, B)

    C_cal = ( ( A * x_ohm ) + ( a * math.sqrt(B)) + b) / ( b + x_ohm )


    D = math.sqrt(B)* (   ( a + ( math.sqrt(B)*x_ohm) )/ (b+x_ohm) )

    print ("C" ,C_cal, D)

    #print ( A**2 - ( 4*B))

    lambda_1 = math.sqrt ( 1/2 * ( A + math.sqrt ((A**2 - ( 4*B)))))

    lambda_2 =math.sqrt( 1/2 * ( A - math.sqrt ( A**2 - ( 4*B))))

    lambda_3 = math.sqrt(1/2*( C_cal + math.sqrt ( C_cal**2 - ( 4 * D ))))

    lambda_4 = math.sqrt(1/2*( C_cal - math.sqrt ( C_cal**2 - ( 4 * D ))))

    lambda_5 = 1

    print ( lambda_1, lambda_2, lambda_3, lambda_4)

    def function_g ( x ):

        result = ( ( x + 1 )*math.log2(x+1) ) - ( x * math.log2(x) )

        return result

    g_1 = function_g ( (lambda_1-1)/2)
    g_2 = function_g ( (lambda_2-1)/2)
    g_3 = function_g ( ( lambda_3-1)/2)
    g_4 = function_g ( abs(( lambda_4-1)/2))
    #g_5 = function_g(0.5*(lambda_5-1))

    print ( g_1, g_2, g_3, g_4)

    g = g_1 +g_2 - g_3 - g_4 

    calc_temp = (V+x_tot)/(1+x_tot)

    print(calc_temp)

    I_AB = 0.5*math.log2(abs(calc_temp))

    betta = 0.95

    K = (betta*I_AB) - g

    rate_2.append(K)

def function_dist_3 ( km ):

    error_phase = 0.000273    #Add phase noise here

    #dist_km.append(km)

    Va = 2.5 # Enter Va here

    V = Va + 1 

    e_phase = 2*Va*(1-math.exp(((-1)*(error_phase))/2))

    V_drift = 0.1

    e_phase = V_drift + e_phase

    att = 0.2

    #km = 20

    r_eff = 0.5

    vele = 0.1

    atte = att * km

    T = 10 ** (((-1)*atte)/10)

    #print ( T )

    x_line = ( 1/T ) - 1 + e_phase

    #print ("x_line", x_line)

    x_ohm = ( 1 - r_eff + vele )/r_eff

    x_tot = x_line + (x_ohm)/T

    a = V

    b = T* ( V+ x_line)

    c = math.sqrt( T*( V**2 -1 ))

    A = a**2 + b**2 - ( 2 * c**2 )

    B = ( (a*b) - c**2 )**2

    #print ( a, b, c)

    #print( A, B)

    C_cal = ( ( A * x_ohm ) + ( a * math.sqrt(B)) + b) / ( b + x_ohm )


    D = math.sqrt(B)* (   ( a + ( math.sqrt(B)*x_ohm) )/ (b+x_ohm) )

    #print ("C" ,C_cal, D)

    #print ( A**2 - ( 4*B))

    lambda_1 = math.sqrt ( 1/2 * ( A + math.sqrt ((A**2 - ( 4*B)))))

    lambda_2 =math.sqrt( 1/2 * ( A - math.sqrt ( A**2 - ( 4*B))))

    lambda_3 = math.sqrt(1/2*( C_cal + math.sqrt ( C_cal**2 - ( 4 * D ))))

    lambda_4 = math.sqrt(1/2*( C_cal - math.sqrt ( C_cal**2 - ( 4 * D ))))

    lambda_5 = 1

    #print ( lambda_1, lambda_2, lambda_3, lambda_4)

    def function_g ( x ):

        result = ( ( x + 1 )*math.log2(x+1) ) - ( x * math.log2(x) )

        return result

    g_1 = function_g ( (lambda_1-1)/2)
    g_2 = function_g ( (lambda_2-1)/2)
    g_3 = function_g ( ( lambda_3-1)/2)
    g_4 = function_g ( abs(( lambda_4-1)/2))
    #g_5 = function_g(0.5*(lambda_5-1))

    #print ( g_1, g_2, g_3, g_4)

    g = g_1 +g_2 - g_3 - g_4 

    calc_temp = (V+x_tot)/(1+x_tot)

    #print(calc_temp)

    I_AB = 0.5*math.log2(abs(calc_temp))

    betta = 0.95

    K = (betta*I_AB) - g

    rate_3.append(K)

n = 1
dist=5
while ( n != 20 ):

  function_dist (dist)
  function_dist_2 (dist)
  function_dist_3(dist)

  n = n + 1
  dist = dist + 5 


print ( len (dist_km))
print ( len ( rate))

#matplot.figure(figsize=(10,10))



matplot.semilogy( dist_km, rate )
matplot.title ( '$V_{drift}$ = 0.001')
matplot.xlabel ('Distance [kms]')
matplot.ylabel ('Secret key rate [bits/pulse]')



matplot.show