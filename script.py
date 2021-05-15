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

def checkbin_pb(filelist, binlist, dir_path):
    with open(dir_path + "/Output/card_report.csv", 'w') as out_file:                   
        writer = csv.writer(out_file)
        writer.writerow(('Card Number', 'Expiry Date (Month)', 'Expiry Date (Year)', 'CVV', 'Holder', 'Bank'))
        m=0
        for fileitem in filelist:
            for binitem in binlist:
                if(fileitem[0:6]==binitem):
                    card = fileitem.split("|")      
                    writer.writerow(card)

def checkbin_src(filelist, binlist, dir_path):
    with open(dir_path + "/Output/raw_with_bin.csv", 'w') as out_file:                   
        write = csv.writer(out_file)        
        for fileitem in filelist:
            for binitem in binlist:
                if binitem in fileitem:
                    card = fileitem.split("\n") 
                    write.writerow(card)

try:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filelist=readerfile(sys.argv[1], dir_path)
    binlist=readerbin(dir_path)
    if(sys.argv[2]=='-pb1'):
        checkbin_pb(filelist, binlist, dir_path)
        print("Completed.")
    elif(sys.argv[2]=='-src'):
        checkbin_src(filelist, binlist, dir_path)
        print("Completed.")
except:
    print("Error.")

