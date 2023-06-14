""" 
la mejor manera de manejar excepciones es con try/except
- Se maneja cualquier excepcion con "Exception"
- algunos otros tipos de excepcion
-- ValueError
-- TypeError
-- NameError

estructura:
try:
    codigo...
except:
    codigo... 
finally: (opcional)
    codigo...    
"""

try:
    n1 = int('daniel')
except NameError as e:
    print(f"Ocurrio un error: {e}")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    print(f'se ejecuta siempre')    
