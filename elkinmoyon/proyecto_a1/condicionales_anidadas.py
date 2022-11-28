#Listado de Becarios
#Academicas, promedio 95 a 100 , >= 90 de asistencia, deuda actual 0
#bajo, medio bajo, medio, medio alto, alto
def beca_academica(estudiantes):
    for i in estudiantes:
        cumplea= False
        cumplep = False
        cumpled = False
        if i['promedio']>= 95 and i['promedio']<= 100:
            cumplep = True

        if i['asistencia'] >= 90 and i['asistencia'] <= 100:
            cumplea = True

        if i['deuda'] == 0:
            cumpled = True

        if cumplep == True and cumplea == True and cumpled == True:
            i['beca'] = True

    for i in estudiantes:
        if i['beca'] == True:
            print(f"Beca academica {i['nombre']} {i['beca']}")

def beca_socioeconomica(estudiantes):
    pass



def run():
    estudiantes = [
        {'nombre' : 'Elkin' , 'carrera' :  'Software' , 'sexo' : 'H' , 'estado' : 'bajo' , 'promedio' : 95 , 'asistencia' : 100,'beca': False, 'deuda' : 0},
        {'nombre' : 'Kevin' , 'carrera' :  'Software' , 'sexo' : 'H' , 'estado' : 'bajo' , 'promedio' : 90 , 'asistencia' : 90 ,'beca': False, 'deuda' : 0},
        {'nombre' : 'Kristhel' , 'carrera' :  'Software' , 'sexo' : 'M' , 'estado' : 'medio bajo' , 'promedio' : 79 , 'asistencia' : 95 ,'beca': False, 'deuda' : 12},
        {'nombre' : 'Mariela' , 'carrera' :  'Biotecnologia' , 'sexo' : 'M' , 'estado' : 'alto' , 'promedio' : 100 , 'asistencia' : 80 ,'beca': False, 'deuda' : 0},
        {'nombre' : 'Sofia' , 'carrera' :  'Biotecnologia' , 'sexo' : 'M' , 'estado' : 'alto' , 'promedio' : 100 , 'asistencia' : 98 ,'beca': False, 'deuda' : 10},
        {'nombre' : 'Williams' , 'carrera' :  'Biotecnologia' , 'sexo' : 'H' , 'estado' : 'alto' , 'promedio' : 94 , 'asistencia' : 100,'beca': False, 'deuda' : 0},
        {'nombre' : 'Miguel' , 'carrera' :  'Industrial' , 'sexo' : 'H' , 'estado' : 'medio alto' , 'promedio' : 90 , 'asistencia' : 98,'beca': False, 'deuda' : 67},
        {'nombre' : 'Carmen' , 'carrera' :  'Industrial' , 'sexo' : 'M' , 'estado' : 'alto' , 'promedio' : 95 , 'asistencia' : 90,'beca': False, 'deuda' : 0},
        {'nombre' : 'Cristopher' , 'carrera' :  'Industrial' , 'sexo' : 'H' , 'estado' : 'medio alto' , 'promedio' : 70 , 'asistencia' : 96,'beca': False, 'deuda' : 13},
        {'nombre' : 'Edison' , 'carrera' :  'Industrial' , 'sexo' : 'H' , 'estado' : 'medio alto' , 'promedio' : 80 , 'asistencia' : 97,'beca': False, 'deuda' : 0}
                   ]
    beca_academica(estudiantes)
    beca_socioeconamica




if __name__ == "__main__":
   run();
