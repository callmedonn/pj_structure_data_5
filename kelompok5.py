print("================================================================")
print("                       DATA PEMBELIAN KUE                       ")
print("================================================================")


def queue():
    s = []
    return s


def enqueue(s, i):
    s.insert(0, i)
    return s


def dequeue(s):
    return s.pop()


def rear(s):
    return(s[0])


def front(s):
    return(s[len(s)-1])


def size(s):
    return len(s)


def isEmpty(s):
    return s == []


def No2():
    s = queue()
    k = ''
    while True:
        banyak = int(input('masukan banyak pembeli secara keseluruhan = '))
        for j in range(banyak):
            orang = input(
                'masukan nama pembeli ke %i yang masuk di antrian = ' % (j+1))
            enqueue(s, orang)
        s.reverse()
        print('Data nama seluruh pembeli adalah : %s' % (s))
        s.reverse()
        o = input('Masukan nama pembeli yang dicari = ')
        ditemukan = 't'
        itung = 0
        while ditemukan == 't':
            if o == front(s):
                print('congrats! pembeli sudah ditemukan')
                ditemukan = 'y'
                print('pembeli berada pada antrian yang ke -',
                      str(itung-1+2), 'dari data nama seluruh pembeli')
                print('dengan looping', str(itung-1+1), 'kali')
            elif o != front(s):
                masukan = dequeue(s)
                enqueue(s, masukan)
                ditemukan = 't'
                s.reverse()
                print('looping %i = %s' % ((itung+1), s))
                s.reverse()
            itung += 1
            if itung > len(s):
                print('maaf! nama yang dimaksud tidak ada')
                print()
                print(
                    'silahkan tambahkan nama jika ingin memesan dengan ketik (yes/no) dibawah ini')
                ditemukan = 'y'
        k = input('apakah masih ada yang bisa dibantu? --ketik (yes/no)-- ? ')
        if k != 'yes':
            print("================================================================")
            print("                        TERIMAKASIH                             ")
            print("                    DATA PEMBELIAN KUE                          ")
            print("================================================================")
            break
        else:
            print("Ketik nama yang ingin memesan")


No2()
