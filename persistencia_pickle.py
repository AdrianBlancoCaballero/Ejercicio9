import pickle

def store(data, filename):
    pickle.dump(data, open(filename, "wb"))

def retrieve(filename):
    try:
        f_o = open(filename, "rb")
    except:
        print("Error al abrir el archivo", filename)
        return None
    contenido = pickle.load(f_o)
    f_o.close()
    return contenido