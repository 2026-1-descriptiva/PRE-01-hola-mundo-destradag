"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Retorne el string "Hola mundo cruel!".

    Rta/
    Hola mundo cruel!

    """
    a="Hola"
    b="mundo"
    c="cruel!"
    
    word=" ".join([a,b,c])


    return  word


if __name__ == "__main__":
    print(pregunta_01())
