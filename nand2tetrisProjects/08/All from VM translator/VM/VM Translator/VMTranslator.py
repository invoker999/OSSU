'''
Created on Oct 8, 2018

@author: Inovker
'''
from Parser import *
from CodeWriter import *
import sys
import os


#CMD_TYPE = {"add":"C_ARITHMETIC","sub":"C_ARITHMETIC","neg":"C_ARITHMETIC","eq":"C_ARITHMETIC","eq":"C_ARITHMETIC","gt":"C_ARITHMETIC",
          #  "lt":"C_ARITHMETIC","and":"C_ARITHMETIC","or":"C_ARITHMETIC","not":"C_ARITHMETIC","pop":"C_POP","push":"C_PUSH",
           # "label":"C_LABEL","goto":"C_GOTO","if-goto":"C_IF","function":"C_FUNCTION","call":"C_CALL","return":"C_RETURN"}

def getVmFiles(fileDir):
    '''
    Returns a list of paths to different .vm file 
    '''

    vmFileList = []
    if os.path.isfile(fileDir):
        #Generate a list of one vm File to process to .asm
        if fileDir.split(".")[-1] != "vm" :
            raise Exception("File passed is not a .vm file, please check again,File name:".format(fileDir))
        else:
            vmFileList.append(fileDir)
            #Generate asm File name from the passed file name
            asmFileName = fileDir.split(".")[0]+".asm"
            boot = False
            
    elif os.path.isdir(fileDir):
        #Generate asm outfile name
        asmFileName = fileDir +"/"+ fileDir + ".asm"
        #Generate a list of vm files in a list to process to .asm
        for fileInDir in os.listdir(fileDir):
            if fileInDir.split(".")[-1] != "vm":
                pass
                #raise Exception("File passed is not a .vm file, please check again, File name: {}".format(fileInDir))
                #Or maybe just ignore the file.....to decide later
            else:
                if fileInDir == "Sys.vm":
                    vmFileList.insert(0,fileDir + "/" + fileInDir)
                else:
                    vmFileList.append(fileDir + "/" + fileInDir)
                boot = True
    else:
        raise Exception("Please passe either a File.vm or Directory of .vm Files")
    
    
    return vmFileList, boot, asmFileName


if __name__ == '__main__':
 
    if len(sys.argv) != 2:
        raise Exception("Only one argument is allowed [File.vm or Directory]",sys.argv)
    
    print("Passed argument for vm translator : ",sys.argv[1])
    vmFileList,boot,asmFileName = getVmFiles(sys.argv[1])
    if len(vmFileList)==0 :
        raise exception("Error generating vm File list")
    print("Files set-up for translation are vmFileList",vmFileList)
    
    
    ############################
    cw = CodeWriter(asmFileName)
    
    ############################"Write bootstrap code if needed
    if boot:
        cw.writeInit()
    
    #Process VM files one by one and write assembly code    
    for file in vmFileList :
        print("Next file passed to parser:",file)
        pars = Parser(file)
        cw.setFileName(file.split("/")[-1]) 
        while(pars.hasMoreCommands()):
            pars.advance()
            if pars.commandType() == "C_ARITHMETIC" :
                    cw.writeArithmetic(pars.arg1())               
            elif pars.commandType() in ["C_PUSH","C_POP"]:
                    cw.writePushPop(pars.commandType(),pars.arg1(),pars.arg2())
            elif pars.commandType() in ["C_LABEL","C_GOTO","C_IF"]:
                    cw.writeLabelGotoIf(pars.commandType(),pars.arg1())
            elif pars.commandType() =="C_FUNCTION" :
                    cw.writeFunction(pars.arg1(),pars.arg2())
            elif pars.commandType() == "C_CALL":
                    cw.writeCall(pars.arg1(),pars.arg2())
            elif pars.commandType() == "C_RETURN":
                    cw.writeReturn()      
            else:
                    raise Exception("Unknown command Type returned by parser!!!")
        
        del pars
    
    cw.close()
    print("Finished processing files")
    
    
    
    
    
    
    
    
    
    
    
    