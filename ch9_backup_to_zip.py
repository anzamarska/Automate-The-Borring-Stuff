#! python3

import zipfile, os

def backupToZip(folder):
    
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number = number +1
    print("Creating %s" %(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, "w")
    
    for foldername, subfolders, filenames in os.walk(folder):
        print("The folderis" + foldername)
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print ("Done")

backupToZip("C:\\Users\\ANIA\\Desktop\\automate the boring stuff")

