import timeit
from matplotlib import pyplot as plt


def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for k in range(0, size):
        index = array[k] // place
        count[index % 10] += 1

    for k in range(1, 10):
        count[k] += count[k - 1]

    k = size - 1
    while k >= 0:
        index = array[k] // place
        output[count[index % 10] - 1] = array[k]
        count[index % 10] -= 1
        k -= 1

    for k in range(0, size):
        array[k] = output[k]


def basamakBul(array):
    sayac = 0
    newsayac = 0
    for j in array:
        for k in str(j):
            sayac += 1
            if k == ".":
                sayac = 0
        if sayac > newsayac:
            newsayac = sayac
        sayac = 0
    donusdegeri = 1
    for k in range(newsayac):
        donusdegeri = donusdegeri * 10
    return donusdegeri


def crateData(txt):
    sayi = ""
    data = []
    for k in txt:
        if k == "\n":
            data.append(float(sayi))
            sayi = ""
        else:
            sayi += k
    return data


def radixSort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0.999:
        countingSort(array, place)
        place *= 10


def returnToInt(data, katsayi):
    for k in range(len(data)):
        data[k] = int(data[k]*katsayi)
    return data


def returnToFloat(data, katsayi):
    for k in range(len(data)):
        data[k] = data[k] / katsayi
    return data


def kontrol(arr):
    for k in range(0, len(arr)-1):
        if arr[k] > arr[k+1]:
            return True
    return False


def calistir(dosya):
    data = crateData(dosya.read())
    katsayi = basamakBul(data)
    data = returnToInt(data, katsayi)
    radixSort(data)
    data = returnToFloat(data, katsayi)
    dosya.close()
    if kontrol(data):
        print("Hatalı sıralanmış sayılar var")
    else:
        print("Sıralanmış dizi : ", end="")
        print(data)


txtler = ["10lukliste 7.txt", "100lükliste 4.txt", "100000likliste 4.txt"]
zamanlar = []

for i in range(3):
    start = timeit.default_timer()
    f = open(str(txtler[i]), "r")
    calistir(f)
    stop = timeit.default_timer()
    zamanlar.append(stop - start)
plt.xlabel("Zaman")
plt.ylabel("Boyut")
print(zamanlar)
plt.plot(zamanlar, [10, 100, 100000])
plt.show()
input("Çıkış yapmak için Entera basınız.")
