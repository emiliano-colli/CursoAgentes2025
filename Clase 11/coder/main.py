#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from coder.crew import Coder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Crea el directorio de salida si no existe
os.makedirs('output', exist_ok=True)

#assignment = 'Escribe un programa Python para calcular los primeros 10,000 términos \
#    de esta serie, multiplicando el total por 4: 1 - 1/3 + 1/5 - 1/7 + ...'

assignment = 'Escribe un programa en Python que le pida al usuario \
    ingresar un número entero positivo y luego imprima la tabla de multiplicar \
    de ese número desde 1 hasta 10.'
    
def run():
    """
    Ejecuta la Crew.
    """
    inputs = {
        'assignment': assignment,
    }
    
    result = Coder().crew().kickoff(inputs=inputs)
    print(result.raw)