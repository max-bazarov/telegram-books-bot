import gspread


gc = gspread.service_account(filename='credentials.json')

worksheet = gc.open('Books')
worksheet = worksheet.sheet1
