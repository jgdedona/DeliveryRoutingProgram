import csv
import Hash
import Packages

packageHash = Hash.HashMap()

if __name__ == '__main__':
    with open('WGUPS Package File.csv') as file:
        packageInfo = csv.reader(file, delimiter=',')

        for row in packageInfo:
            if len(row[7]) == 0:
                notes = 'None'
            else:
                notes = row[7]
            packageHash.insert(row[0], Packages.Package(row[0], row[1], row[2], row[3], row[4],
                                                        row[5], row[6], notes, 'Unknown'))
            print(packageHash.search(row[0]))

