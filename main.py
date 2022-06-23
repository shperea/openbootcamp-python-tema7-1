import operaciones as op

def main():

	suma = op.suma(int(input("Valor x: ")), int(input("Valor y: ")))
	print("El valor de la suma es", suma)

	resta = op.resta(int(input("Valor x: ")), int(input("Valor y: ")))
	print("El valor de la resta es", resta)

	multiplicacion = op.multiplicacion(int(input("Valor x: ")), int(input("Valor y: ")))
	print("El valor de la multiplicacion es", multiplicacion)

	division = op.division(int(input("Valor x: ")), int(input("Valor y: ")))
	print("El valor de la division es", division)

if __name__ == '__main__':
	main()