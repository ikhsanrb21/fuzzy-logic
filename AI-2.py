import csv


#mendefinisikan rule-rule yg nanti akan dipakai
aturan1 = ["kecil","rendah","sangat layak"]
aturan2 = ["kecil","menengah","sangat layak"]
aturan3 = ["kecil","tinggi","sangat layak"]
aturan4 = ["medium","rendah","sangat layak"]
aturan5 = ["medium","menengah","layak"]
aturan6 = ["medium","tinggi","tidak layak"]
aturan7 = ["besar","rendah","tidak layak"]
aturan8 = ["besar","menengah","tidak layak"]
aturan9 = ["besar","tinggi","tidak layak"]

tebakan = []

#fungsi trapesium untuk menentukan nilai keanggotaan
def trapesium(x,a,b,c,d):
    if x<=a and x>=d:
        return 0
    elif a<x and x<b:
        return (x-a)/(b-a)
    elif b<=x and x<=c:
        return 1
    elif c<x and x<=d:
        return -(x-d)/(d-c)
    else:
        return 0

#fungsi untuk menghilangkan adanya duplikat
def clipp(label, hasil_interference, x, y):
    if len(hasil_interference) > 0: 
        found = False
        for hi in hasil_interference:
            if label == hi[0]:
                found = True
        if found:
            hi[1] = min(x, y)
            found = False
        else:
            hasil_interference.append([label, min(x, y)])
    else:
        hasil_interference.append([label, min(x, y)])

#fungsi untuk menguji hasil nilai keanggotaan yg telah dilabeli kedalam rule yg telah dibuat
def interference(x,y):
    hasil_interference = []

    if x[0][1]>0 and y[0][1]>0:
        if x[0][0] == aturan1[0] and y[0][0] == aturan1[1]:
            clipp(aturan1[2], hasil_interference, x[0][1], y[0][1])
    if x[0][1]>0 and y[1][1]>0:
        if x[0][0] == aturan2[0] and y[1][0] == aturan2[1]:
            clipp(aturan2[2], hasil_interference, x[0][1], y[1][1])
    if x[0][1]>0 and y[2][1]>0:
        if x[0][0] == aturan3[0] and y[2][0] == aturan3[1]:
            clipp(aturan3[2], hasil_interference, x[0][1], y[2][1])
    if x[1][1]>0 and y[0][1]>0:
        if x[1][0] == aturan4[0] and y[0][0] == aturan4[1]:
            clipp(aturan4[2], hasil_interference, x[1][1], y[0][1])
    if x[1][1]>0 and y[1][1]>0:
        if x[1][0] == aturan5[0] and y[1][0] == aturan5[1]:
            clipp(aturan5[2], hasil_interference, x[1][1], y[1][1])
    if x[1][1]>0 and y[2][1]>0:
        if x[1][0] == aturan6[0] and y[2][0] == aturan6[1]:
            clipp(aturan6[2], hasil_interference, x[1][1], y[2][1])
    if x[2][1]>0 and y[0][1]>0:
        if x[2][0] == aturan7[0] and y[0][0] == aturan7[1]:
            clipp(aturan7[2], hasil_interference, x[2][1], y[0][1])
    if x[2][1]>0 and y[1][1]>0:
        if x[2][0] == aturan8[0] and y[1][0] == aturan8[1]:
            clipp(aturan8[2], hasil_interference, x[2][1], y[1][1])
    if x[2][1]>0 and y[2][1]>0:
        if x[2][0] == aturan9[0] and y[2][0] == aturan9[1]:
            clipp(aturan9[2], hasil_interference, x[2][1], y[2][1])

    return hasil_interference

#fungsi untuk melabeli nilai keanggotaan dari pendapatan     
def cbcbP(dtListP):
    listData2 = []
    for c in range(1, len(dtListP)):
        if c==1:
            listDataP = ['kecil',dtListP[c]]
            listData2.append(listDataP)
            #print(listDataP)
        elif c==2:
            listDataP = ['medium',dtListP[c]]
            listData2.append(listDataP)
        elif c==3:
            listDataP = ['besar',dtListP[c]]
            listData2.append(listDataP)
    return listData2

#fungsi untuk melabeli nilai keanggotaan dari utang
def cbcbU(dtListU):
    listData1 = []
    for b in range(1, len(dtListU)):
        if b==1:
            listDataU = ['rendah',dtListU[b]]
            listData1.append(listDataU)            
        elif b==2:
            listDataU = ['menengah',dtListU[b]]
            listData1.append(listDataU)        
        elif b==3:
            listDataU = ['tinggi',dtListU[b]]
            listData1.append(listDataU)
    return listData1

#fungsi untuk mengembalikan hasil nilai dari beberapa kelayakan/ satu kelayakan menjadi satu nilai presentase
def defuzzifikasi(interference):
    if len(interference) == 1:
        area1_atas = 0
        area1_bawah = interference[0][1]
        if interference[0][0] == 'tidak layak':
            area1_atas = interference[0][1] * 40
        elif interference[0][0] == 'layak':
            area1_atas = interference[0][1] * 60
        elif interference[0][0] == 'sangat layak':
            area1_atas = interference[0][1] * 80
        return area1_atas / area1_bawah
    elif len(interference) == 2:
        area1_atas = 0
        area1_bawah = interference[0][1]
        if interference[0][0] == 'tidak layak':
            area1_atas = interference[0][1] * 40
        elif interference[0][0] == 'layak':
            area1_atas = interference[0][1] * 60
        elif interference[0][0] == 'sangat layak':
            area1_atas = interference[0][1] * 80
            
        area2_atas = 0
        area2_bawah = interference[1][1]
        if interference[1][0] == 'tidak layak':
            area1_atas = interference[1][1] * 40
        elif interference[1][0] == 'layak':
            area1_atas = interference[1][1] * 60
        elif interference[1][0] == 'sangat layak':
            area1_atas = interference[1][1] * 80
        return (area1_atas + area2_atas) / (area1_bawah + area2_bawah)
    else:
        area1_atas = 0
        area1_bawah = interference[0][1]
        if interference[0][0] == 'tidak layak':
            area1_atas = interference[0][1] * 40
        elif interference[0][0] == 'layak':
            area1_atas = interference[0][1] * 60
        elif interference[0][0] == 'sangat layak':
            area1_atas = interference[0][1] * 80
            
        area2_atas = 0
        area2_bawah = interference[1][1]
        if interference[1][0] == 'tidak layak':
            area2_atas = interference[1][1] * 40
        elif interference[1][0] == 'layak':
            area2_atas = interference[1][1] * 60
        elif interference[1][0] == 'sangat layak':
            area2_atas = interference[1][1] * 80

        area3_atas = 0
        area3_bawah = interference[2][1]
        if interference[2][0] == 'tidak layak':
            area3_atas = interference[2][1] * 40
        elif interference[2][0] == 'layak':
            area3_atas = interference[2][1] * 60
        elif interference[2][0] == 'sangat layak':
            area3_atas = interference[2][1] * 80
        return (area1_atas + area2_atas + area3_atas) / (area1_bawah + area2_bawah + area3_bawah)

#membaca data dari csv untuk dimasukan ke dalam list
with open('DataTugas2.csv', newline='') as datatugas2:
    next(datatugas2)
    spamreader = csv.reader(datatugas2, delimiter=' ', quotechar='|')
    listDataA = []
    for col in spamreader:
        dtListA = [col[0].replace(",",""),col[1].replace(",",""),col[2]]
        dtListA = [float(d) for d in dtListA]
        listDataA.append(dtListA)
    for i in range(0,100):
        nurut = int(listDataA[i][0])
        listDataA[i][0] = nurut
    for a in listDataA:
        #mengubah nilai awal menjadi nilai keanggotaan
        smallP = trapesium(a[1], 0, 0, 0.5, 0.8)
        mediumP = trapesium(a[1], 0.5, 0.8, 1.3, 1.6)
        largeP = trapesium(a[1], 1.3, 1.6, 2.0, 2.0)
        
        lowU = trapesium(a[2], 0, 0, 20, 40)
        mediumU = trapesium(a[2], 20, 40, 60, 80)
        highU = trapesium(a[2], 60, 80, 100, 100)

        #memasukan nilai keanggotaan ke dalam list masing-masing
        dtListP = [a[0],smallP,mediumP,largeP]
        dtListU = [a[0],lowU,mediumU,highU]

        #melakukan fuzzifikasi
        cbcb2P = cbcbP(dtListP)
        cbcb1U = cbcbU(dtListU)
        
        #melakukan interference
        cbcb1 = interference(cbcb2P,cbcb1U)
        
        #melakukan defuzzifikasi
        cbcb2 = defuzzifikasi(cbcb1)

        #melakukan pengecekan skor
        if cbcb2 > 30:
            tebakan.append([a[0], cbcb2])

#melakukan sortir dan menyisakan 20 keluarga terlayak
tebakan.sort(key=lambda z:int(z[1]), reverse=True)
tebakan = tebakan[:20]

#memasukan data yg telah disortir ke dalam file csv
with open('TebakanTugas2.csv', 'w', newline='') as tebakantugas2:
    spamwriter = csv.writer(tebakantugas2, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for v in tebakan:
        nampung = [v[0]]
        spamwriter.writerow(nampung)






    

