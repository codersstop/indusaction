__author__ = 'vdogra'

import requests
import bs4
import re

#CONSTANT

RESULTS_FILE = 'file.csv'

def school_seats():
    response = requests.get('http://www.edudel.nic.in/mis/Payroll/frmewsdgentryschoolwisedist.aspx?schid=1001162')
    table_soup = bs4.BeautifulSoup(response.text)
    school_seats_table = table_soup.find_all('tr')
    print school_seats_table.__len__()
    with open(RESULTS_FILE, 'a') as result_file:
        result_file.write('Class, , Total No.of Seats , , ,Admission given/enrollment, , ,Seats still Vacant, , ,No. of application received against, , Total\n')
        result_file.write (',Open seats,EWS/DG seats,Free Quota seats,Open seats/General, EWS/DG seats, Free Quota seats,Open seats/General, EWS/DG seats, Free Quota seats,Open seats,EWS/DG seats,Free Quota seats,,\n')
        print re.sub(' ', '_',bs4.BeautifulSoup(str(school_seats_table[0])).find('td').string)
        for row in school_seats_table[4:7]:
            row_soup = bs4.BeautifulSoup(str(row))
            result_file.write ('{0},{1},{2},{3},{4}, {5},{6},{7},{8},{9}, {10},{11},{12},{13}'.format(row_soup.find_all('td')[0].string, row_soup.find_all('td')[1].string, row_soup.find_all('td')[2].string,
                row_soup.find_all('td')[3].string, row_soup.find_all('td')[4].string,
                row_soup.find_all('td')[5].string, row_soup.find_all('td')[6].string, row_soup.find_all('td')[7].string,
                row_soup.find_all('td')[8].string, row_soup.find_all('td')[9].string, row_soup.find_all('td')[10].string,
                row_soup.find_all('td')[11].string,row_soup.find_all('td')[12].string, row_soup.find_all('td')[13].string))
            result_file.write('\n')
    result_file.close()

if __name__ == '__main__':
    school_seats()