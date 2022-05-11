"""
Name: Taha Andac
ID : 75785
Section : 03
"""
import csv

def check_name(file_name):
    """Try's to open given file name, if file not exists, exits the function"""
    try:
        infile = open(file_name, 'r')
    except FileNotFoundError:

        print (file_name, 'does not exist')
        exit()

    infile.close()

def get_admin_with_minor(file_name):
    """Iterates over lines of given file and creates a dictionary.
    Keys of dictionary corresponts to admin city names,
    values of dictionary corresponts to city counts and population as tuples."""
    admins ={}
    infile = open(file_name, 'r')
    next(infile)
    for line in infile:
        line = line.strip()
        line = line.split(',')
        admin = line[5]
        pop = 0
        if not line[7] == '':
            pop = int(line[7])
        if not admin in admins:
            admins[admin] = [0, 0]
        admins[admin][0] += 1
        admins[admin][1] += pop

    infile.close()
    return admins

def file_creator(file_name,admins):
    """Takes a desired name for file to be created, also takes a dictionary.
    Iterates over keys of dictionary and creates a list for every key and value pair.
    Appends those lists to a main list
    Using csv writer, writes components of main list into file."""
    outfile = open(file_name, 'w')
    dic = admins
    attributes=[['Administrative City', 'Number of Its Cities/Towns', 'Total Population']]
    
    for i in dic:
        L=[]
        L.append(i)
        L.append(dic[i][0])
        L.append(dic[i][1])
        attributes.append(L)

    writer = csv.writer(outfile, lineterminator='\n')
    writer.writerows(attributes)

    outfile.close()

def special_cities(file_name):
    """Iterates over lines of file and creates two separate dictionaries, city_lat and city_lng.
    Keys of city_lat corresponts to latitudes,
    values of city_lat corresponts to city names.
    Keys of city_lng corresponts to longitudes,
    values of city_lng corresponts to city names.
    Checks for the min-max keys of values and finds special cities.
    Also searchs for the capital city by checking admin names.
    """
    infile = open(file_name, 'r')
    city_lng ={}
    city_lat = {}
    next(infile)
    for line in infile:
        line = line.strip()
        line = line.split(',')
        lattitude = line[1]
        longitude = line[2]
        city= line[0]
        city_lng[float(longitude)] = city
        city_lat[float(lattitude)] = city
        if line[6]=='capital':
            capital=line[0]
    most_east = city_lng[max(city_lng.keys())]
    most_west = city_lng[min(city_lng.keys())]
    most_north = city_lat[max(city_lat.keys())]
    most_south = city_lat[min(city_lat.keys())]
    print ('Capital city: ' , capital)
    print('Most eastern city: ',most_east) 
    print('Most western city: ',most_west)
    print('Most northern city: ',most_north)
    print('Most southern city: ',most_south)

    infile.close()

def main():
    """Caller of the functions. After all functions are called, prints a message."""
    input_file = input('Enter an input filename: ')
    check_name(input_file)
    special_cities(input_file)
    output_file = input('Enter an output filename: ')
    admins = get_admin_with_minor(input_file)
    file_creator(output_file, admins)
    print('Cities are saved')

main()
