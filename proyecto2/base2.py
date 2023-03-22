import os
import sys
import getopt
from math import log2
import csv
file_full_path = ""
file_split_path = [];
def myfunc(argv):
    global file_full_path, file_split_path
    arg_output = ""
    arg_user = ""
    arg_help = "{0} -i <input>".format(argv[0])
    
    try:
        opts, args = getopt.getopt(argv[1:], "hi:", ["help", "input="])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  
            sys.exit(2)
        elif opt in ("-i", "--input"):
            file_full_path = arg
            file_split_path = os.path.normpath(file_full_path)
            file_split_path = os.path.split(file_split_path)
if __name__ == "__main__":
    myfunc(sys.argv)
file_huffman_comprimido = file_full_path+".huffman.bin"
ruta_diccionario = file_full_path+".diccionario.csv"
recovered_path = os.path.join(file_split_path[0], "recovered_"+file_split_path[1]);
string=[];
with open(file_full_path, "rb") as f:
    while (byte := f.read(1)):
        int_val = int.from_bytes(byte, "big")
        string.append(int_val)
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def children(self):
        return (self.left, self.right)
    def nodes(self):
        return (self.left, self.right)
    def __str__(self):
        return '%s_%s' % (self.left, self.right)
def insert_in_tree(raiz, ruta, valor):
    if(len(ruta)==1):
        if(ruta=='0'):
            raiz.left = valor;
        else:
            raiz.right = valor;
    else:
        if(ruta[0]=='0'):
            #if type(raiz.left) is int:
            if(raiz.left==None):
                raiz.left = NodeTree(None,None);
            ruta = ruta[1:];
            insert_in_tree(raiz.left,ruta,valor);
        else:
            #if type(raiz.right) is int:
            if(raiz.right==None):
                raiz.right = NodeTree(None,None);
            ruta = ruta[1:];
            insert_in_tree(raiz.right,ruta,valor);
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is int:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d
prob_unit = 1/len(string)
freq = {}
stringmem = sys.getsizeof(string)
for c in string:
    if c in freq:
        freq[c] += prob_unit
    else:
        freq[c] = prob_unit
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = freq
while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
huffmanCode = huffman_code_tree(nodes[0][0])
print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))

entropy = 0
for (char, frequency) in freq:
    entropy += frequency * log2(1/frequency)
print("Entropía de la fuente: ", entropy)

avg_length = 0
for (char, frequency) in freq:
    huffman_length = len(huffmanCode[char])
    avg_length += frequency * huffman_length
print("Longitud media del código de Huffman: ", avg_length)

#Calculando la varianza del código de Huffman generado
variance = 0
for (char, frequency) in freq:
    huffman_length = len(huffmanCode[char])
    variance += frequency * (huffman_length - avg_length)**2
print("Varianza del código de Huffman: ", variance)

#Eficiencia de la codificación original de la fuente
original_efficiency = entropy/8
print("Eficiencia de la codificación original de la fuente: ", original_efficiency)

#Eficiencia del nuevo código generado
new_efficiency = avg_length/8
print("Eficiencia del nuevo código de Huffman: ", new_efficiency)

#Se crea una lista vacía para guardar el string binario
binary_string = [];
#Se itera sobre el código y se agrega abinary_string cada código de los códigos de Huffman
for c in string :
    binary_string += huffmanCode [ c ]
#Se calcula el largo de los códigos comprimidos
compressed_length_bit = len(binary_string)
if (compressed_length_bit %8 >0):  # se calculan los bytes de el código comprimido
    for i in range(8 - len(binary_string) % 8>0):
        binary_string += '0'
#se agrega a byte_string cada caracter en binary_string
byte_string = " " . join ([ str ( i ) for i in binary_string ]) 
byte_string =[ byte_string [ i : i +8] for i in range (0 , len ( byte_string ), 8) ];

for i in range(len(byte_string)):
    byte_string[i] = byte_string[i].encode()

membytestring = sys.getsizeof(byte_string)

print("Memoria original: ", stringmem, "  Memoria de comprimido: ", membytestring)
with open(file_huffman_comprimido, "wb") as f: # write the byte variable to the file 
    for binary_num in byte_string:
        f.write(binary_num)
    f.close()

csvfile = open(ruta_diccionario, 'w')
writer = csv.writer(csvfile)
writer.writerow([str(compressed_length_bit),"bits"])

for entrada in huffmanCode:
    writer.writerow([str(entrada),huffmanCode[entrada]])
csvfile.close()

# ------------------------------------------------------------------------

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
        

x = 0
incoherencias = 0
while x < 786572:
    if data_estimated[x] != string[x]:
    	incoherencias += 1
    x += 1

print("Incoherencias: ", incoherencias)
            
	


