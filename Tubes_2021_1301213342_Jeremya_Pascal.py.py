#Pertama kita buka file untuk mengakses file text.txt

def daftar_mobil(filename):
    file = open (filename, "r")
    teks = file.readline().replace("\n","")

#Buat dictionary kosong untuk memasukkan data 
    daftar_mobil = {}
    
#Buat perulangan untuk memasukkan data ke dictionary
    
    while teks != "" :
        mobil = teks.split("#")
        daftar_mobil[mobil[0]] = list(mobil[1:4])
        daftar_mobil[mobil[0]][2] = int( daftar_mobil[mobil[0]][2])
        teks = file.readline().replace("\n","")
    file.close()
    return daftar_mobil

#Buat fungsi report untuk memnentukan stok terbanyak dan tersedikit
 
def report(data): 
    min_m = ""
    max_m = ""
    max = 0
    min = 0

    #Looping variabel key mengakses key dan value satu per satu dari dict nya
    for ii in data:
       
        if (int(data[ii][2]) > int(max)): 
            max = (int(data[ii][2])) 
            max_m = ii 
        
        if min == 0: 
            min = (int(data[ii][2])) 
            min_m = ii 
    
        else:
            if int(data[ii][2]) < int(min): 
                min = (int(data[ii][2])) 
                min_m = ii 
    

    print("Terbanyak : ", max_m)
    print("Tersedikit : ", min_m)

#Buat fungsi bahan_bakar untuk mengembalikan bahan bakar suatu mobil tertentu

def bahan_bakar(data, jenis) :
    for ii in data :
        if ii == jenis :
            return data[ii][1]

#Main Program untuk menampilkan atau memanggil fungsi yang telah dibuat 

a = daftar_mobil("text.txt")
print(a)
jenis = input('Masukan Jenis Mobil : ')
c = bahan_bakar(a,jenis)
report(a)
print(c)       