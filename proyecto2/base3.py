import os
import sys
import getopt
from math import log2
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
file_huffman_comprimido = file_full_path+".huffman"
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
        self.char = None

def huffman_code_tree(tree, prefix="", code={}):
    if isinstance(tree, NodeTree):
        huffman_code_tree(tree.left, prefix + "0", code)
        huffman_code_tree(tree.right, prefix + "1", code)
    else:
        code[tree] = prefix
    return code

def huffman_decode(file_full_path):
    # Definir los nombres de los archivos de entrada y salida
    file_huffman_comprimido = file_full_path + ".huffman"
    ruta_diccionario = file_full_path + ".diccionario.csv"
    recovered_path = os.path.join(file_dir, "recovered_" + file_name)

    # Leer el diccionario de Huffman desde el archivo CSV
    huffmanCode = {}
    with open(ruta_diccionario, "r") as f:
        for line in f:
            line = line.strip()
            char, code = line.split(",")
            huffmanCode[code] = int(char)

    # Decodificar el archivo comprimido y guardar el resultado en el archivo descomprimido
    with open(file_huffman_comprimido, "rb") as f_input, open(recovered_path, "wb") as f_output:
        bit_string = ""
        root = NodeTree()
        for code, char in huffmanCode.items():
            node = root
            for bit in code:
                if bit == "0":
                    if node.left is None:
                        node.left = NodeTree()
                    node = node.left
                elif bit == "1":
                    if node.right is None:
                        node.right = NodeTree()
                    node = node.right
            node.char = char
        node = root
