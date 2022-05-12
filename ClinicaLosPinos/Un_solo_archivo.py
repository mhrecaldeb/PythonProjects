import glob
# Python program to
# demonstrate merging of
# two files

# Creating a list of filenames
# primer_archivo = int(input("Ingresa el número del primer archivo (sin extensión ej. 12091 ): "))
# ultimo_archivo = int(input("Ingresa el número del ultimo archivo (sin extensión ej. 13599: ): "))


filenames = []
folder = "C:/Users/mhrec/OneDrive/Documents/Downloads/Gateway/"
# for archivo in range(primer_archivo, ultimo_archivo + 1, 1):
for file in glob.glob(folder + "*.log"):
    filenames.append(file)


#    filenames.append(str(archivo)+".log")

for item in filenames:
    
    print(item)



# Open file3 in write mode
with open(folder + 'final.txt', 'w') as outfile:

    #     # Iterate through list
    for names in filenames:

        #         # Open each file in read mode
        infile =  open(names, 'r')

        flag = 0

        for line in infile:

            if ('cgn:' and 'cdn:') in line:
                print(line)
                outfile.write(line)
                flag = 1
                break

        # if flag == 1:
        #     # for line in infile:

        #     #             # read the data from file1 and
        #     #             # file2 and write it in file3
        #     # if ("a") in line:

        #     outfile.write(infile.read())

#         # Add '\n' to enter data of file2
#         # from next line
# outfile.write("\n")
        infile.close()
    outfile.close()