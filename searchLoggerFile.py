import os

############
# Search the last indented .txt logger file, starting with 00
# Warning : it there in a missing intendation, (ie:00,01,02,04), 03 is missing
# and 02 is returned
# File folder and pre-indented name information are based on parameters set in
# 'config' from a .ini file
def searchLoggerFile(config):
    #filename from config file
    filename = config.get('filenameLogger','folderPATH')+config.get('filenameLogger','filename')

    # create indented filename
    i = 0
    while os.path.exists(f"{filename}{format(i, '02d')}.txt"):
        i += 1
    filename = f"{filename}{format(i - 1, '02d')}.txt"

    return filename
