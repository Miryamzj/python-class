import sys

if len(sys.argv)==3: 
    
    num1= float(sys.argv[1])
    num2= float(sys.argv[2])
    suma = num1 + num2

    print (f"la suma es {suma}")        
    
else:
    print(f"Necesitas escribir 2 números")
