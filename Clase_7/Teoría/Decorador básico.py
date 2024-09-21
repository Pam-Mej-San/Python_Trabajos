# Decorador basico
def mi_decorador (func):
    def wrapper (*args, **kwargs):
        print("Antes de ejecutar la funcion")
        resultado = func(*args, **kwargs)
        print("Despues de ejecutar la funcion")
        return resultado
    return wrapper

# Usamos el decorador en una función
@mi_decorador
def saludar (nombre) :
    print(f"Hola, {nombre}!")

# LLamamos La funcion decorada
print("=== Decorador en una funcion ===")
saludar ("Ana")


def repetir_veces(veces):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(veces):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir_veces(3)
def decir_hola():
    print("Hola!")

print("\n=== Decorador con parámetros ===")
decir_hola()
