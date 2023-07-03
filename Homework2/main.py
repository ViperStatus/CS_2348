# Sokheng Ka 1968133
import datetime


def find(extract_date):
    mthtonum = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
                'September': 9, 'October': 10, 'November': 11, 'December': 12}
@@ -19,4 +18,7 @@ def find(extract_date):
    with open('inputDates.txt') as f:
        for x in f.readlines():
            if x.strip() != '-1':
    print(fid(x.strip()))
    res = find(x.strip()))
    if res != '':
        with open('parsedDAtes.txt') as w:
            w.write(res + '/n')
