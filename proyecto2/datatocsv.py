import csv

with open("datos.txt", "r") as input_file, open("datos.csv", "w", newline="") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["Archivo utilizado", "Entropía de la fuente", "Longitud media del código de Huffman",
                     "Varianza del código de Huffman", "Eficiencia de la codificación original de la fuente",
                     "Eficiencia del nuevo código de Huffman", "Memoria original","Memoria comprimida", "Tasa de compresión",
                     "Incoherencias"])

    archivo_utilizado = None
    for line in input_file:
        if line.startswith("Running command"):
            archivo_utilizado = line.split("-i ")[1].strip()
        else:
            campos = line.split(":")
            for i in range(len(campos)):
                campos[i] = campos[i].strip()

            if archivo_utilizado:
                writer.writerow([archivo_utilizado] + campos)
            else:
                writer.writerow([""] + campos)
