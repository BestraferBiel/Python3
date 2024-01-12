#!/usr/bin/env python3

import datetime

# Obtenemos la fecha actual 
fecha_actual = datetime.datetime.now()
anno = fecha_actual.year
hora = fecha_actual.hour,fecha_actual.minute


print(fecha_actual)
print(anno)
print(f"{fecha_actual.hour}:{fecha_actual.minute}")