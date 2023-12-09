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
def make_key_autokey(csv_data,seed,dictionary):
    data_length = len(csv_data)
    resulting_key = []
    for i in seed:
        resulting_key.append(dictionary[i])
    j = len(resulting_key)
    count = 0 #count how many comma's and \n, nantinya bakal dihapus soalnya
    for i in csv_data:
        if i == ',' or i == '\n':
            count +=1
    filtered_list = [x for x in csv_data if x != ',' and x != '\n']
    while j < data_length:
        for i in filtered_list:
           if j == data_length:
               break
           resulting_key.append(i)
           j+=1
    print(resulting_key)      
    return resulting_key

def customListSum(list1,list2):
    result = []
    for i in range(len(list1)):
        if type(list1[i]) == int:
            result.append((list1[i]+list2[i])%64)
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


#Main
input_file = input(str("Masukkan nama file CSV yang ingin di-enkrip : "))
file_path = 'Csv_Files/' + input_file


# Open the CSV file
with open(file_path, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # CSV dalam 1 string
    data_string = '\n'.join(','.join(row) for row in csv_reader)

num_string = replace_with_numbers(data_string,char_dic)
method = input(str("Anda ingin mencipher dengan metode Repetition atau Autokey ? (R/A) "))
if method.lower() == 'a':
    print("Mencipher dengan metode autokey")
    word = input(str("Masukkan kata / kalimat yang menjadi key dari cipher ini : "))
    cipher = make_key_autokey(num_string,word,char_dic)
    ciphered_data = stringify(customListSum(num_string,cipher))
else:
    print("Mencipher dengan metode repetition")
    word = input(str("Masukkan kata / kalimat yang menjadi key dari cipher ini : "))
    cipher = make_key_repetition(num_string,word,char_dic)
    ciphered_data = stringify(customListSum(num_string,cipher))

print("CSV berhasil dicipher.")
save_name= input(str("Tuliskan nama file untuk menaruh hasil cipher : "))
path_save ="C:/Users/Sean Nugroho/Documents/Semester3/MatDis/Makalah/Ciphered_Files/"+save_name
file1 = open(path_save,'w')
file1.write(ciphered_data)