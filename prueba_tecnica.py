
import csv
with open('datos_prueba_tecnica.csv', mode='r', encoding='utf-8-sig') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';')
    csvdata = list(csvreader)

    #FUNCTIONS
    #Function to get all values of column with key
    def getColValues(key):
        finalList =[]
        for row in csvdata:
            finalList.append(row[key])
        return finalList

   #Function to count values from a list acording to type
    def countTypes(listing, typeLetter):
        return str(listing.count(typeLetter))

    #Function to sum values of column accodding to  key
    def sumValues(key, value):
        salaryList =[] 
        for row in csvdata:
            if row[key] == value:
                salary = int(row['salario bruto anual'])
                salaryList.append(salary)
        sumSalary = sum(salaryList)
        return sumSalary

    #function to filter some values from a row
    def selectfields(list):
        return 'ID:' + list['id empleado'] + "   Nombre:" + list['nombre'] + '  Apellidos:' + list['apellido1'] + " " + list['apellido2'] + '  Salario bruto anual: ' + list['salario bruto anual'] + '€  Nombre de la empresa:' + list['Nombre empresa']
 

    #function to filter employers according to salary and company
    def selectEmployers(salary, key, value):
        resultado =[] 
        for row in csvdata:
            itemSalary = int(row['salario bruto anual'])
            if row[key] == value and itemSalary > salary : 
                resultado.append(row)
            resultprueba = map(selectfields, resultado)
        return resultprueba


    #Function to iterate and print a list
    def print_list(it):
        for x in it:
            print(x, end='\n')


    #PRINT
    #Employees acording to gender
    memberListing = getColValues("sexo")
    print("1. Hay " + countTypes(memberListing,"H") + " hombres y " + countTypes(memberListing,"M") + " mujeres.")
    print("\n")

    #Annual salary
    empleadosIT = sumValues("ID Empresa", "1")
    empleadosAloe = sumValues("ID Centro trabajo", "CT2")
    print("2. El salario bruto anual total de los empleados de Equilibra IT es de " + str(empleadosIT) + " y el de los del centro Alovera " + str(empleadosAloe))
    print("\n")

    #Employers list
    employersList = selectEmployers(28000, 'ID Empresa','1')
    print('3. Listado de empleados con un salario superior a 28000 euros y que pertenecen a Equilibra RRHH')
    print_list(employersList)
