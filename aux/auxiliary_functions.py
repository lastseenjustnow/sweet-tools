from datetime import timedelta


# create dates range

def daterange_delta89(start_date, end_date):
    for n in range(int(round((end_date - start_date).days / 89))):
        yield start_date + timedelta(n * 89)

