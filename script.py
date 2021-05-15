from collections import defaultdict
import csv
import sys
import os 

def readerfile(input, dir_path):
    file = open(dir_path + "/Input/" + input)
    filelist=[]
    for line in file.readlines():
        filelist.append(line.replace('\n',''))
    return filelist

def readerbin(dir_path):
    bintxt = open(dir_path + "/bin.txt")
    binlist=[]
    for line in bintxt.readlines():
        binlist.append(line.replace('\n',''))
    return binlist

def checkbin(filelist, binlist):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/Output/card_report.csv", 'w') as out_file:                   
        writer = csv.writer(out_file)
        writer.writerow(('Card Number', 'Expiry Date (Month)', 'Expiry Date (Year)', 'CVV', 'Holder', 'Bank'))
        m=0
        for fileitem in filelist:
            for binitem in binlist:
                if(fileitem[0:6]==binitem):
                    card = fileitem.split("|")      
                    writer.writerow(card)

try:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filelist=readerfile(sys.argv[1], dir_path)
    binlist=readerbin(dir_path)
    checkbin(filelist, binlist)
    print("Completed.")
except:
    print("Error.")

