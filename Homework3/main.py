

def song(Artist, Year, TrackNo):
    if (Artist == 'Lionel Richie') and (Year == 1992 or TrackNo == 11):
        print('Hello - Lionel Richie')
    # elif (Artist == 'Lionel Richie') and (Year == 1992 and TrackNo == 8):
    #     print('Truly - Lionel Richie')
    elif (Artist == 'Michael Jackson') and (Year == 1995 or TrackNo == 1):
        print('Human Nature - Michael Jackson')
    else:
        print('Song not found.')


print('bool=True')
song('Lionel Richie', 1992, 11)
song('Lionel Richie', 1992, 15)
song('Lionel Richie', 1995, 11)
song('Michael Jackson', 1992, 1)
song('Michael Jackson', 1995, 2)
# song('Lionel Richie', 1992, 8)
print('\nbool=False')
song('Lionel Richie', 1991, 10)
song('Kenny Rogers', 1992, 11)
song('Michael Jackson', 1991, 3)
