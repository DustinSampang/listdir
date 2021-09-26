import csv
#
# #the list(dictionary) of the file directories
dictio = {
 1: "dirst.txt",
 2: "second.txt",
 3: "dhird.txt",
 4: "dourth.txt"
 }

#how about a list instead?
alist = ["dirst.txt", "second.txt", "dhird.txt", "dourth.txt"]

#this saves the csv file name
def savefile():
    print("")
    csvname = input("Please give your CSV file a name: ")
    with open (csvname, 'x') as new_file:
        #csv = csv.writer(new_file)
        fieldnames = ['parent path ',   ' filename']
        csv_write = csv.DictWriter(new_file, fieldnames= fieldnames)


        csv_write.writeheader()
        csv_write.writerow({'parent path ' : 'D:\A Work\OJT stuff\python_experiments\ '  ,  ' filename': dictio[0]})
        # using the dictionary would not work and would only cause it to crash because apparently it couldnt read it
       # ^ i was tempted to hardcode this instead









userin = input("Please write something like 'csv list': ")

if userin == ("csv list"):
       print("parent path, filename, filesize, sha1, md5")
       print("D:\A Work\OJT stuff\python_experiments\ " + alist[0])
       print("D:\A Work\OJT stuff\python_experiments\ " + alist[1])
       print("D:\A Work\OJT stuff\python_experiments\ " + alist[2])
       print("D:\A Work\OJT stuff\python_experiments\ " + alist[3])
       print(" ")
       print("Do you want to save as CSV file? ")
       ques = input("Y  N    ")

       if ques == "Y" or "y":
           savefile()

       elif ques == "N" or "n":
           exit()


elif userin != ("csv list"):
    print("invalid")







# with open ('uhh.csv', 'r') as csv_file:
#     csv_readthis = csv.reader(csv_file)

