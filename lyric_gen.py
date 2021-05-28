import sys


def song():
    while True:
        print(
            ' 1.Alone\n 2.BoneyM_Rasputin\n 3.Beliver\n 4.Dance_Monkey\n 5.Falling\n 6.Memories\n 7.Show_me_the_meaning\n 0.To change the Album\n *.EXIT')
        print('-' * 60)
        song = input("Please Choose the song:--")

        if song == '1':
            with open('Faded.txt', 'r') as song_lyries:
                for line in song_lyries:
                    print(line)


        elif song == '2':

            with open('Rasputin.txt', 'r') as song_lyries:
                for line in song_lyries:
                    print(line)


        elif song == '3':

            with open('Beliver.txt', 'r') as song_lyries:
                for line in song_lyries:
                    print(line)


        elif song == '4':

            with open('Dance_Monkey.txt', 'r') as song_lyries:
                for line in song_lyries:
                    print(line)


        elif song == '5':

            with open('Falling.txt', 'r') as song_lyries:
                for line in song_lyries:
                    print(line)


        elif song == '6':

            with open('Memories.txt', 'r') as song_lyries:
                for line in song_lyries:
                    print(line)




        elif song == '7':

            with open('Show_me_the_meaning.txt', 'r') as song_lyries:
                for line in song_lyries:
                    print(line)

        elif song == '0':
            song


        elif song == '*':
            sys.exit('Thank You!')

        else:
            print('Out Of Selection Choose Again')


song()

