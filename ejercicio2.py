# Formula usada: FOIL Gain = p * (log2(p / (p + n)) - log2(P / (P + N)))

'''
A) Desarrollar un programa en Python que obtenga el cálculo del FOIL Gain para la condición
nivel_educativo == 'terciario'
'''

import math

# mismos datos que en el ejercicio anterior
datos = [
{"edad": 22, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
{"edad": 24, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": True},
{"edad": 21, "departamento": "RRHH", "nivel_educativo": "terciario", "en_formacion": True},
{"edad": 35, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": False},
{"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría", "en_formacion": False},
{"edad": 29, "departamento": "RRHH", "nivel_educativo": "universitario", "en_formacion": False},
{"edad": 23, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
{"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False}
]

# separo los que estan en formacion de los que no
positivos = [p for p in datos if p["en_formacion"]]
negativos = [p for p in datos if not p["en_formacion"]]

# totales sin aplicar ninguna condicion
P = len(positivos)
N = len(negativos)

condicion = "nivel_educativo == 'terciario'"

# cuento cuantos cumplen la condicion en cada grupo
p = len([x for x in positivos if x["nivel_educativo"] == "terciario"])
n = len([x for x in negativos if x["nivel_educativo"] == "terciario"])

# calculo (si da 0 evito dividir por cero o hacer log de 0)
ratio_p = p / (p + n) if (p + n) > 0 else 0
ratio_P = P / (P + N)
log_p = math.log2(ratio_p) if ratio_p > 0 else 0
log_P = math.log2(ratio_P) if ratio_P > 0 else 0
foil_gain = p * (log_p - log_P)

# muestro los resultados
print(f"\nCondición: {condicion}")
print(f"P (positivos antes) = {P}")
print(f"N (negativos antes) = {N}")
print(f"p (positivos después) = {p}")
print(f"n (negativos después) = {n}")
print(f"p / (p + n) = {ratio_p:.3f}")
print(f"P / (P + N) = {ratio_P:.3f}")
print(f"log2(p / (p + n)) = {log_p:.3f}")
print(f"log2(P / (P + N)) = {log_P:.3f}")
print(f"FOIL Gain = {foil_gain:.3f}")

'''
B) Calculo manual del FOIL Gain para verificar el resultado del programa.

Condicion: nivel_educativo == 'terciario'

Valores:

Término                |      Valor
----------------------------------------------
P (positivos antes)    |        4
N (negativos antes)    |        4
p (positivos después)  |        3
n (negativos después)  |        0
----------------------------------------------

1. Proporcion despues de la condicion:
p / (p + n) = 3 / (3 + 0) = 3 / 3 = 1

2. Proporcion antes de la condicion:
P / (P + N) = 4 / (4 + 4) = 4 / 8 = 0.5

3. Logaritmos:
log₂(1) = 0
log₂(0.5) = -1

4. FOIL Gain:
p x (log₂(p/(p+n)) - log₂(P/(P+N)))
3 x (0 - (-1))
3 x 1
= 3

Da 3, igual que en el programa.

5. Interpretacion:
Con la condicion "nivel_educativo == 'terciario'" quedan 3 positivos y 0 negativos,
o sea que todos los que tienen nivel terciario estan en formacion. La ganancia es 3,
asi que es una buena condicion para la regla.
'''

'''
C) Programa en Python que calcula el FOIL Gain para la condicion edad <= 23
'''

import math

# mismos datos
datos = [
{"edad": 22, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
{"edad": 24, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": True},
{"edad": 21, "departamento": "RRHH", "nivel_educativo": "terciario", "en_formacion": True},
{"edad": 35, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": False},
{"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría", "en_formacion": False},
{"edad": 29, "departamento": "RRHH", "nivel_educativo": "universitario", "en_formacion": False},
{"edad": 23, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
{"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False}
]

positivos = [p for p in datos if p["en_formacion"]]
negativos = [p for p in datos if not p["en_formacion"]]

# filtro por edad
positivos_edad = [p for p in positivos if p["edad"] <= 23]
negativos_edad = [p for p in negativos if p["edad"] <= 23]

# totales sin condicion
P = len(positivos)
N = len(negativos)

condicion = "edad <= 23"

# los que cumplen la condicion
p = len(positivos_edad)
n = len(negativos_edad)

# calculo
ratio_p = p / (p + n) if (p + n) > 0 else 0
ratio_P = P / (P + N)
log_p = math.log2(ratio_p) if ratio_p > 0 else 0
log_P = math.log2(ratio_P) if ratio_P > 0 else 0
foil_gain = p * (log_p - log_P)

# resultados
print(f"\nCondición: {condicion}")
print(f"P (positivos antes) = {P}")
print(f"N (negativos antes) = {N}")
print(f"p (positivos después) = {p}")
print(f"n (negativos después) = {n}")
print(f"p / (p + n) = {ratio_p:.3f}")
print(f"P / (P + N) = {ratio_P:.3f}")
print(f"log2(p / (p + n)) = {log_p:.3f}")
print(f"log2(P / (P + N)) = {log_P:.3f}")
print(f"FOIL Gain = {foil_gain:.3f}")

'''
D) Calculo manual del FOIL Gain para verificar el resultado del programa.

Condicion: edad <= 23

Término                |      Valor
----------------------------------------------
P (positivos antes)    |        4
N (negativos antes)    |        4
p (positivos después)  |        3
n (negativos después)  |        0
----------------------------------------------

1. Proporcion despues de la condicion:
p / (p + n) = 3 / (3 + 0) = 3 / 3 = 1

2. Proporcion antes de la condicion:
P / (P + N) = 4 / (4 + 4) = 4 / 8 = 0.5

3. Logaritmos:
log₂(1) = 0
log₂(0.5) = -1

4. FOIL Gain:
3 x (0 - (-1)) = 3 x 1 = 3

Tambien da 3, coincide con el programa.

5. Interpretacion:
Con "edad <= 23" pasa lo mismo que con la condicion anterior: entran 3 positivos y
ningun negativo. En estos datos todos los que tienen 23 años o menos estan en formacion,
por lo que la condicion sirve para separar a los que estan en formacion.
Las dos condiciones dan la misma ganancia (3) y agarran a las mismas 3 personas.
'''