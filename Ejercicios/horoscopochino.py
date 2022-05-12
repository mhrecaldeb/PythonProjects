year = int(input("Introduce un año: "))

horoscopes = ["mono", "gallo", "perro", "cerdo", "rata", "buey", "tigre", "conejo", "dragon", "serpiente", "caballo", "cabra"]

# los anios divisibles exactamente por 12 seran mono, y luego la lista debe respetar 
# el orden siendo el residuo el indice que corresponde en la lista

horoscope = horoscopes[ year % 12]

print(year % 12)
print(year // 12)
print(year - (year // 12)*12)
print(horoscopes[year % 12])

result = (year, horoscope)

print(result)
