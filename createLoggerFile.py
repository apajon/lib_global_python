import os

############
# create a Logger file to write and save datas in CSV format
# File information are based on parameters set in 'config' from a .ini file
def createLoggerFile(config):
    #filename from config file
    filename,i=searchFileName(config.get('filenameLogger','folderPATH'),
                        config.get('filenameLogger','filename'))

    #create recording file
    print("Logger file name: "+config.get('filenameLogger','filename')+"%s.txt" % format(i, '02d'))
    fh = open(filename, "w")
    fh.write(config.get('filenameLogger','firstLine')+"\n")

    return fh

############
# Search indented filename and create an empty folder if needed
def searchFileName(folderPATH,filename_):
    #filename from config file
    filename = folderPATH+filename_

    # create indented filename
    i = 0
    while os.path.exists(filename+"%s.txt" % format(i, '02d')):
        i += 1
    filename=filename+"%s.txt" % format(i, '02d')

    #create repository if not exist
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    return filename, i
