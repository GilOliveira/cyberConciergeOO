from dateTime import dateTime
def readClientsFile(fileName):
    
    from collections import namedtuple
    Client = namedtuple('Client', ['name', 'place', 'beginning_day','beginning_hour','max_hourly_charge','min_rating', 'required_expertise','duration']) 
    
    clientList= []
        
    
    fileIn = open(fileName, 'r')
    #Skypping the header
    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")
    scope=fileIn.readline().replace(":", "")
    
    
    for line in fileIn:
        #Reading the words from the expert list, such as: name, location, expertise, etc
        words=line.split(",")
        
        #Erasing the space from expertise, done for improved search on scheduling
        words[6]=words[6].replace(' ','')
        
        #Adds the new expert onto the list
        New_expert=Client(words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7] )
        clientList.append(New_expert)

    
    client_header=(day,time,company,scope)
    
    
    fileIn.close()
    return (clientList,client_header)

def readExpertsFile(fileName):
    """
    Converts a given file listing experts into a collection
    Requires: fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: list whose first element is ... <to complete>
    """
    from collections import namedtuple
    Jean_Pierrexpert = namedtuple('Expert', ['name', 'place', 'expertise', 'rating', 'hourly_charge','date_of_last_order', 'end_time_of_last_order','moneyyyyyyy' ])
    outputList =  []
    outputList.append(readHeader(fileName))
    
    fileIn = open(fileName, 'r')
    #Skypping the header
    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")
    scope=fileIn.readline()#.replace(":", "")
    
    header_times= dateTime(readHeader(fileName), "header")
    
    for line in fileIn:
        #Reading the words from the expert list, such as: name, location, expertise, etc
        words=line.split(",")
        
        #Adds the new expert onto the list
        New_expert=Jean_Pierrexpert(words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7] )
        
        #Check if the expert's date is before or after the date on the header before appending
        current_times= dateTime(New_expert, "expert")
        
        #check year
        if(current_times[0][0]<header_times[0][0]):
            
            current_times=header_times
            
        elif(current_times[0][0]==header_times[0][0]):
            #check month, 
            if(current_times[0][1]<header_times[0][1]):
                current_times=header_times
                
            elif(current_times[0][1]==header_times[0][1]):
                #check day   
                if(current_times[0][2]<header_times[0][2]):
                    current_times=header_times
                elif(current_times[0][2]==header_times[0][2]):
                    #check hour
                    if(current_times[1][0]<header_times[1][0]):
                        current_times=header_times
                    elif(current_times[1][0]==header_times[1][0]):
                        #check minute
                        if(current_times[1][1]<header_times[1][1]):
                            current_times=header_times
                            
                            
        #giving the new time to the object
        #updating the date
#        aux_date=(current_times[0][0],'-',current_times[0][1],'-',current_times[0][2])
#        aux_time=(current_times[1][0],':',current_times[1][1])
#        New_expert=Jean_Pierrexpert(words[0], words[1], words[2], words[3], words[4], aux_date, aux_time, words[7] )
                   
        #if((current_times[0]>>header_times[0])&&(current_times[1]>>header_times[1])&&(current_times[2]<=header_times[2])):

        
        outputList.append(New_expert)

    fileIn.close()
    return outputList


def readHeader(fileName):
    
    #Opens file
    fileIn = open(fileName, 'r')
    
    #Reads Day, time and company
    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")
    scope=fileIn.readline().replace(":", "")
 
    fileIn.close()
    return (day, time, company, scope)






