
count = 0

while True:
    input_count = input('8桁の数字をいれてください：')
    if input_count != 00000000:
        if  int(input_count) >=19000101 and int(input_count) <= 20501231:
            year = input_count[:4]
            input_count = input_count[4:]
            for num in range(1,12):
                if int(input_count) <= 100*num+31:
                    month = int(input_count[:2])
                    date = int(input_count[2:4])
        elif int(input_count) <= 12312050 and int(input_count)>= 1011900:
            #month = input_count[:2]
            #date = input_count[2:4]
            year = input_count[4:]
            input_count = input_count[:4]
            for num in range(1,12):

                #ここに31日以外の処理を書こう
                if int(input_count) <= 100*num+31:
                    month = int(input_count[:2])
                    date = int(input_count[2:4])
        else:
            print('1900～2050年の間で8桁の数字を入れてね！！')
            continue


    if int(year) >= 1900 and int(year) <= 2050:
            if int(year) <= 1911:
                meiji = int(year) - 1900 + 33
                print('明治' + str(meiji) + '年の'+ str(month) +'月'+ str(date) +'日です')

            elif int(year) <= 1925:
                taisyo = int(year)-1911
                if taisyo == 1:
                    print('大正元年の'+ str(date)+'月'+ str(date) +'日です')
                else:
                    print('大正' + str(taisyo) + '年の'+str(month) +'月'+ str(date) +'日です')

            elif int(year) <= 1988:
                syowa = int(year)-1925
                if syowa == 1:
                    print('昭和元年の'+ str(month)+'月'+ str(date) +'日です')
                else:
                    print('昭和' + str(syowa) + '年の'+  str(month)+'月'+ str(date) +'日です')

            elif int(year) <= 2018:
                heisei = int(year)-1988
                if heisei == 1:
                    print('平成元年の'+  str(month)+'月'+ str(date) +'日です')
                else:
                    print('平成' + str(heisei) +'年の'+  str(month)+'月'+ str(date) +'日です')

            elif int(year) <= 2050:
                reiwa = int(year)-2018
                if reiwa == 1:
                    print('令和元年の'+ str(month)+'月'+ str(date) +'日です')
                else:
                    print('令和' + str(reiwa) + '年の'+  str(month)+'月'+ str(date) +'日です')
                break

    elif int(year) == 0000:
                print('おわり')
                break

    else:
        print('1900～2050年の間で8桁の数字を入れてね！！')



