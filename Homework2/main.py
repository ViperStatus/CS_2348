# Sokheng Ka 1968133
import datetime


def find(extract_date):
    mthtonum = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
                'September': 9, 'October': 10, 'November': 11, 'December': 12}

    yy = extract_date.split(',')[-1].strip()
    mm = extract_date.split(',')[0].split()[0]
    dd = extract_date.split(',')[0].split()[-1]
    mn = mthtonum[mm]
    int(yy)
    int(dd)
    return str(mn) + '/' + dd + '/' + yy
    except:
        return''

    with open('inputDates.txt') as f:
        for x in f.readlines():
            if x.strip() != '-1':
    print(fid(x.strip()))
