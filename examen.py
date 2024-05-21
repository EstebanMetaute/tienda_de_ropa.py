import os
os.system('cls')

var_totalFlt = 0
cons_camisaD = 50000
cons_pantalonD = 85000
cons_interiorD = 15000

cons_camisaC = 60000
cons_pantalonC = 90000
cons_interiorC = 12000

cons_camisaN = 55000 
cons_pantalonN = 87000 
cons_interiorN = 14500 



var_controlBln = True
while var_controlBln == True:
    os.system('cls')
    print('<<<<< welcome to clothes shops MATYW >>>>>')
    var_opcion = int(input('<<<< choose category >>>> \n\n1. Women\n2. Men\n3. Children\n4. EXIT\n ->'))
    if var_opcion >= 1 and var_opcion <= 5:
        os.system('cls')
        if var_opcion == 1:
            var_ferreStr = int(input('<<< Agrega a la canasta >>> \n\n1. camisas\n2. pantalon\n3. ropa interior\n4. EXIT\n ->'))
            if var_ferreStr >= 1 and var_ferreStr <= 6:
                var_cantidadInt = int(input('cantidad ->'))
            if var_ferreStr == 1:
                var_totalFlt += (var_cantidadInt * cons_camisaD)
            if var_ferreStr == 2:
                var_totalFlt += (var_cantidadInt * cons_pantalonD)
            if var_ferreStr == 3:
                var_totalFlt += (var_cantidadInt * cons_interiorD)
            if var_ferreStr == 4:
                var_totalFlt += (var_cantidadInt * cons_llave)

        os.system('cls')
        if var_opcion == 2:
            var_aseoStr = int(input('<<< Agrega a la canasta >>> \n\n1. camisas\n2. pantalon\n3. ropa interior\n4. EXIT\n ->'))
            if var_aseoStr >= 1 and var_aseoStr <= 5:
                var_cantidadInt = int(input('cantidad ->'))
            if var_aseoStr == 1:
                var_totalFlt += (var_cantidadInt * cons_camisaC)
            if var_aseoStr == 2:
                var_totalFlt += (var_cantidadInt * cons_pantalonC)
            if var_aseoStr == 1:
                var_totalFlt += (var_cantidadInt * cons_interiorC)
            if var_aseoStr == 1:
                var_totalFlt += (var_cantidadInt * cons_dete)

        os.system('cls')
        if var_opcion == 3:
            var_seguridadStr = int(input('<<< agrega a la canasta >>> \n\n1. camisas\n2. pantalon\n3. ropa inetrior\n4. EXIT\n ->'))
            if var_seguridadStr >= 1 and var_aseoStr <= 3:
                var_cantidadInt = int(input('cantidad ->'))
            if var_seguridadStr == 1:
                var_totalFlt += (var_cantidadInt * cons_camisaN)
            if var_seguridadStr == 2:
                var_totalFlt += (var_cantidadInt * cons_pantalonN)
            if var_seguridadStr == 3:
                var_totalFlt += (var_cantidadInt * cons_interiorN)
        os.system('cls')
  
        
    if var_opcion == 4:
        print('el total a pagar:______________________________________________$', var_totalFlt)
        var_controlBln = False
