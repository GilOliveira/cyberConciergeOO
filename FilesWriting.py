# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

def newFile(time, scope, company):
    """
        Opens a file in write mode and writes the required header in the first lines.
        Requires: time is DateTime
        Requires: company is str, the name of the company
        Requires: scope is str (must be either 'schedule' or 'experts').
        Ensures: the creation of a file with the required file name and header
        as stated in the project, the file is left open.
    """

    fileName = time.getYear()+'y'+time.getMonth()+'m'+ time.getDay() +\
               scope + time.getHour()+'h'+time.getMinute()+'.txt'
    file = open(fileName, 'w')
    file.writelines(['Day: \n', time.getDate(), '\n', 'Time: \n', time.getTime(),
                     '\n', 'Company: \n', company, '\n', scope.capitalize(), ': \n'])
    file.close()
    return fileName
