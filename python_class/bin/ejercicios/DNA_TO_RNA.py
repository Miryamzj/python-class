#Pedimos al usuario ingresar secuencias 
secuencias = input ("Dame secuencias separadas por comas").split(",")
#Para reemplazar las T por U 
secuencias_arn =[secuencia.replace("T", "U") for secuencia in secuencias]

print (secuencias_arn)