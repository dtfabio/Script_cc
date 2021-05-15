from collections import defaultdict
import csv
import sys
import os 

try:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    card_file=sys.argv[1]
    file = open(dir_path + "/Input/" + sys.argv[1])
    bintxt = open(dir_path + "/bin.txt")
    filelist=[]
    binlist=[]
    for line2 in bintxt.readlines():
        binlist.append(line2.replace('\n',''))
    for line in file.readlines():
        filelist.append(line.replace('\n',''))

    with open(dir_path + "/Output/card_report.csv", 'w') as out_file:                   
        writer = csv.writer(out_file)
        writer.writerow(('Card Number', 'Expiry Date (Month)', 'Expiry Date (Year)', 'CVV', 'Holder', 'Bank'))
        m=0
        for fileitem in filelist:
            for binitem in binlist:
                if(fileitem[0:6]==binitem):
                    card = fileitem.split("|")      
                    writer.writerow(card)
        print("Completed.")
except:
    print("Error.")

