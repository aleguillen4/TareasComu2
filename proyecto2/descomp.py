csvfile = open(ruta_diccionario, 'r')
reader = csv.reader(csvfile)
bits_a_leer = None
diccionario = dict()


for row in reader:

    if bits_a_leer == None:
        bits_a_leer = int(row[0])
    else:
        diccionario.update({int(row[0]):row[1]})

Decoding = NodeTree(None, None)
for entrada in diccionario:
    insert_in_tree(Decoding, diccionario[entrada], entrada)


nodo = Decoding
data_estimated = []
for i in range(compressed_length_bit):
    (l,r) = nodo.children()
    #print([i, binary_string[i]])

    if (binary_string[i]=='1'):
        nodo = r
    else:
        nodo = l

    if type(nodo) is int:
        data_estimated.append(nodo)
        #print([i, nodo])
        nodo = Decoding
