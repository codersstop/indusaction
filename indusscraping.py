__author__ = 'vdogra'

import re
import requests
import bs4

import json

root_url = 'http://www.edudel.nic.in/'
middle_url = 'mis/Payroll/'
ews_entry_dist_wise_url = root_url + middle_url + 'frmReportewsdgentrydistwise.aspx'
vacancy_school_wise_report_url = root_url + middle_url + 'frmReportewsentrydistwiseschool.aspx?schtype=<schtype>&DistId=<DistId>&issubmitted=<issubmitted>'
vacancy_per_school_data_url= root_url + middle_url + 'frmewsdgentryschoolwisedist.aspx?schid=<schid>'

dist_to_distId = {
                    'East' : 10,  'North_East' : 11, 'North' : 12, 'North_West_A' : 13, 'North_West_B' : 14,
                    'West_A' : 15, 'West_B' :  16,  'South_West_A' :  17, 'South_West_B' : 18, 'South' : 19,
                    'New_Delhi' : 20 , 'Central' : 21, 'South_East' : 22
                 }

vacancy_filled_unfilled = {'Filled' : 1, 'Not Filled' : 2}

SCHOOL_TYPE = 1

filled_header = False
unfilled_header = False

#Constants

DIST_WISE_ENROLLMENT_INDEX_START = 3
DIST_SCHOOL_WISE_ENROLLMENT_INDEX_START = 1
DIST_WISE_ENROLLMENT_INDEX_END = 13
DIST_WISE_ENROLLMENT_FILE_NAME = 'Dist_Wise_Enrollment.csv'
DIST_SCHOOL_WISE_FILLED_ENROLLMENT_FILE_NAME = 'Dist_School_Wise_Filled_ENROLLMENT.csv'
DIST_SCHOOL_WISE_UNFILLED_ENROLLMENT_FILE_NAME = 'Dist_School_Wise_Unfilled_ENROLLMENT.csv'
RESULTS_DIR = 'results/'
RESULTS_DIR_SCHOOLS = 'results/schools/'

def surround_double_quotes(string):
    return '"'+string+'"'

def replace_space_with_underscore(string):
    return re.sub(' ','_', string)

def replace_slash_with_underscore(string):
    return re.sub('/','_', string)

def remove_new_line_character(string):
    return re.sub('\r','',re.sub('\n','', string))

def dist_school_wise_seats_info(file_name, link):
    response = requests.get(root_url + middle_url + link)
    table_soup = bs4.BeautifulSoup(response.text)
    school_seats_table = table_soup.find_all('tr')
    if school_seats_table.__len__():
        with open(RESULTS_DIR_SCHOOLS + replace_space_with_underscore(replace_slash_with_underscore(file_name)) + '.csv', 'a') as result_file:
            result_file.write('Class, , Total No.of Seats , , ,Admission given/enrollment, , ,Seats still Vacant, , ,No. of application received against, , Total\n')
            result_file.write (',Open seats,EWS/DG seats,Free Quota seats,Open seats/General, EWS/DG seats, Free Quota seats,Open seats/General, EWS/DG seats, Free Quota seats,Open seats,EWS/DG seats,Free Quota seats,,\n')
            for row in school_seats_table[4:7]:
                row_soup = bs4.BeautifulSoup(str(row))
                single_row_column_list = row_soup.find_all('td')
                result_file.write ('{0},{1},{2},{3},{4}, {5},{6},{7},{8},{9}, {10},{11},{12},{13}'.format(single_row_column_list[0].string, single_row_column_list[1].string, single_row_column_list[2].string,
                    single_row_column_list[3].string, single_row_column_list[4].string,
                    single_row_column_list[5].string, single_row_column_list[6].string, single_row_column_list[7].string,
                    single_row_column_list[8].string, single_row_column_list[9].string, single_row_column_list[10].string,
                    single_row_column_list[11].string,single_row_column_list[12].string, single_row_column_list[13].string))
                result_file.write('\n')
        result_file.close()

def dist_school_wise_filled_enrollment(distt, link):
    response = requests.get(root_url + middle_url + link)
    dist_school_wise_filled_table_soup = bs4.BeautifulSoup(response.text)
    global filled_header
    if not filled_header:
        dist_school_wise_filled_table = dist_school_wise_filled_table_soup.find_all('tr')[DIST_SCHOOL_WISE_ENROLLMENT_INDEX_START:]
        filled_header = True
    else:
        dist_school_wise_filled_table = dist_school_wise_filled_table_soup.find_all('tr')[DIST_SCHOOL_WISE_ENROLLMENT_INDEX_START + 1:]
    with open(RESULTS_DIR + distt, 'a') as result_file_1:
        for row in dist_school_wise_filled_table:
            row_soup = bs4.BeautifulSoup(str(row))
            single_row_column_list = row_soup.find_all('td')
            for link in row_soup.find_all('a'):
                dist_school_wise_seats_info(single_row_column_list[1].string, link.get('href') )
            result_file_1.write('{0},{1},{2},{3},{4}'.format(surround_double_quotes(single_row_column_list[0].string),
                surround_double_quotes(single_row_column_list[1].string), remove_new_line_character(surround_double_quotes(single_row_column_list[2].string)),
                remove_new_line_character(surround_double_quotes(single_row_column_list[3].string)),
                remove_new_line_character(surround_double_quotes(str(single_row_column_list[4].string)))))
            result_file_1.write('\n')
    result_file_1.close()

def dist_school_wise_unfilled_enrollment(distt, link):
    response = requests.get(root_url + middle_url + link)
    dist_school_wise_unfilled_table_soup = bs4.BeautifulSoup(response.text)
    global unfilled_header
    if not unfilled_header:
        dist_school_wise_unfilled_table = dist_school_wise_unfilled_table_soup.find_all('tr')[DIST_SCHOOL_WISE_ENROLLMENT_INDEX_START:]

        unfilled_header = True
    else:
        dist_school_wise_unfilled_table = dist_school_wise_unfilled_table_soup.find_all('tr')[DIST_SCHOOL_WISE_ENROLLMENT_INDEX_START + 1:]
    with open(RESULTS_DIR + distt, 'a') as result_file_2:
        for row in dist_school_wise_unfilled_table:
            row_soup = bs4.BeautifulSoup(str(row))
            single_row_column_list = row_soup.find_all('td')
            if single_row_column_list[4].string:
                try:
                    result_file_2.write('{0},{1},{2},{3},{4}'.format(surround_double_quotes(single_row_column_list[0].string),
                    surround_double_quotes(single_row_column_list[1].string), remove_new_line_character(surround_double_quotes(single_row_column_list[2].string)),
                    remove_new_line_character(surround_double_quotes(single_row_column_list[3].string)), remove_new_line_character(surround_double_quotes(single_row_column_list[4].string ))))
                except UnicodeEncodeError:
                    print 'Unicode Encode Error: ',single_row_column_list[0].string, single_row_column_list[1].string,
                    single_row_column_list[2].string, single_row_column_list[3].string, single_row_column_list[4].string

            else:
                result_file_2.write('{0},{1},{2},{3}'.format(surround_double_quotes(single_row_column_list[0].string),
                surround_double_quotes(single_row_column_list[1].string), remove_new_line_character(surround_double_quotes(single_row_column_list[2].string)),
                remove_new_line_character(surround_double_quotes(single_row_column_list[3].string))))
            result_file_2.write('\n')
    result_file_2.close()


def dist_wise_enrollment():
    response = requests.get(ews_entry_dist_wise_url)
    table_soup = bs4.BeautifulSoup(response.text)
    dist_wise_enrollment_table = table_soup.find_all('tr')[DIST_WISE_ENROLLMENT_INDEX_START:]

    result_file = open(RESULTS_DIR + DIST_WISE_ENROLLMENT_FILE_NAME, 'a')
    # print 'S.No., District Id, District Id, Filled, Not Filled'
    print result_file.write('S.No., District Id, District, Filled, Not Filled\n')
    for row in dist_wise_enrollment_table[:-1]:
        row_soup = bs4.BeautifulSoup(str(row))
        single_row_column_list = row_soup.find_all('td')
        for link in row_soup.find_all('a')[:-1]:
            dist_school_wise_filled_enrollment('Filled', link.get('href'))
        for link in row_soup.find_all('a')[1:]:
            dist_school_wise_unfilled_enrollment('Unfilled', link.get('href'))
        result_file.write('{0}, {1}, {2}, {3}, {4}'.format(surround_double_quotes(single_row_column_list[0].string),
                            dist_to_distId[re.sub(' ', '_',single_row_column_list[1].string)],
                            surround_double_quotes(single_row_column_list[1].string),
                            remove_new_line_character(surround_double_quotes(single_row_column_list[2].string)),
                            remove_new_line_character(surround_double_quotes(single_row_column_list[3].string))))
        result_file.write('\n')
    result_file.close()

if __name__ == '__main__':
    dist_wise_enrollment()