import bs4
import lxml
import requests


def get_input():
    print(" CHOOSE YOUR SIGN: \n \n "

          "1.ARIES \n "
          "2.TAURUS\n "
          "3.GEMINI\n "
          "4.CANCER\n "
          "5.LEO\n "
          "6.VIRGO\n "
          "7.LIBRA\n "
          "8.SCORPIO\n "
          "9.SAGITTARIUS\n "
          "10.CAPRICON\n "
          "11.AQUARIUS\n "
          "12.PISCES \n \n ")
    n = int(input("Your Number= "))

    print('DO YOU WANT YOUR HOROSCOPE FOR \n '
          '1.TODAY \n '
          '2.YESTERDAY \n '
          '3.TOMORROW \n \n  ')

    day = int(input('Day number= '))

    get_horro(n, day)


def get_horro(sign, day):
    global d
    if day == 1:
        d = 'today'
    elif day == 2:
        d = 'yesterday'
    elif day == 3:
        d = 'tomorrow'

    scrape_link = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-' + d + '.aspx?sign=' + str(
        sign)

    re = requests.get(scrape_link)

    soup = bs4.BeautifulSoup(re.text, 'lxml')
    soup.select('p')
    site_para = soup.select('p')[0].getText()

    print()
    print()
    print(site_para)
    print('\nThank You.')


def main():
    get_input()


if __name__ == '__main__':
    main()
