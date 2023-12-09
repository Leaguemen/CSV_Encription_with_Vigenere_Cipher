import csv

char_dic = {chr(i): i - 65 for i in range(65,91)}
char_dic.update({chr(i): i - 71 for i in range(97,123)})
char_dic.update({' ':52, "'":53,"1":54,"2":55,"3":56,"4":57,"5":58,"6":59,"7":60,"8":61,"9":62,"0":63, ".":64})

def replace_with_numbers(input_string, dictionary):
    result = []
    for char in input_string:
        if char in dictionary:
            result.append(dictionary[char])
        else:
            result.append(char)
    return result


#membuat key yang panjangnya sama dengan data csv dengan metode repetition
def make_key_repetition(csv_data,seed,dictionary):
    data_length = len(csv_data)
    resulting_key = []
    j = 0 #resulting key length
    while j < data_length:
        for i in seed:
           if j == data_length:
               break
           resulting_key.append(dictionary[i])
           j+=1 
    return resulting_key


#membuat key yang panjangnya sama dengan data csv dengan metode autokey
def make_key_autokey(seed,dictionary):
    file_path = 'Csv_Files/test2.csv'
    # Open the CSV file
    with open(file_path, 'r') as file:
        # Create a CSV reader
        csv_reader = csv.reader(file)

        # CSV dalam 1 string
        data_string = '\n'.join(','.join(row) for row in csv_reader)
    num_string = replace_with_numbers(data_string,char_dic)
    data_length = len(num_string)
    resulting_key = []
    for i in seed:
        resulting_key.append(dictionary[i])
    j = len(resulting_key)
    count = 0 #count how many comma's and \n, nantinya bakal dihapus soalnya
    for i in num_string:
        if i == ',' or i == '\n':
            count +=1
    filtered_list = [x for x in num_string if x != ',' and x != '\n']
    while j < data_length:
        for i in filtered_list:
           if j == data_length:
               break
           resulting_key.append(i)
           j+=1
    return resulting_key

def customListSum(list1,list2):
    result = []
    for i in range(len(list1)):
        if type(list1[i]) == int:
            result.append((list1[i]+list2[i])%63)
        else:
            result.append(list1[i])
    return result

def stringify(ciphered):
    result = ""
    for i in range(len(ciphered)):
         if type(ciphered[i]) == int:
             for k,v in char_dic.items():
                 if v == ciphered[i]:
                     result += k
         else:
             result+=ciphered[i]    
    return result


def customLisMin(list1,list2):
    result = []
    for i in range(len(list1)):
        if type(list1[i]) == int:
            result.append((list1[i]-list2[i])%64)
        else:
            result.append(list1[i])
    return result

def decipher_autokey(ciphered_text,key):
    dechiper = make_key_autokey(key,char_dic)
    decrypt = customLisMin(ciphered_text,dechiper)
    result = ""
    for i in range(len(decrypt)):
         if type(decrypt[i]) == int:
             for k,v in char_dic.items():
                 if v == decrypt[i]:
                     result += k
         else:
             result+=decrypt[i]
    print(result)

def decipher_repetition(ciphered_text,key):
    decipher = make_key_repetition(ciphered_text,key,char_dic)
    decrypt = customLisMin(ciphered_text,decipher)
    result = ""
    for i in range(len(decrypt)):
         if type(decrypt[i]) == int:
             for k,v in char_dic.items():
                 if v == decrypt[i]:
                     result += k
         else:
             result+=decrypt[i]
    print(result)

#main
input_file = input(str("Masukkan nama file CSV yang sudah di-enkrip : "))
file_path = 'Ciphered_Files/' + input_file


# Open the CSV file
with open(file_path, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # CSV dalam 1 string
    data_string = '\n'.join(','.join(row) for row in csv_reader)

num_string = replace_with_numbers(data_string,char_dic)
method = input(str("File tersebut di-enkrip dengan metode Repetition atau Autokey ? (R/A) "))
if method.lower() == 'a':
    key_rep = input(str("Key untuk file tersebut apa ? "))
    print("Isi dari file tersebut adalah sebagai berikut")
    decipher_autokey(num_string,key_rep) 
else:
    key_rep = input(str("Key untuk file tersebut apa ? "))
    print("Isi dari file tersebut adalah sebagai berikut")
    decipher_repetition(num_string,key_rep)