'''
Created on Feb 16, 2019

Author: invoker999
Course: OSSU/nand2tetris
Email: kaced.sofiane@gmail.com

'''

from CompilationEngine import compilationEngine
import sys
import os

def getJackFiles(fileOrDir):
    '''
    ([jackFile|DirName) --> List jackFileList
    
    Returns a list of paths to different .Jack files 
    '''
    #Init list to empty
    jackFileList = []
    
    #Generate a single file name if the the argument passed is a file
    if os.path.isfile(fileOrDir):
        #Check if file name is .jack file
        if fileOrDir.split(".")[-1] != "jack" :
            raise Exception("File passed is not a .jack file, please check again,File name:".format(fileOrDir))
        else:
            jackFileList.append(fileOrDir)
    
    #Generate a list of files if the argument passed is a directory       
    elif os.path.isdir(fileOrDir):

        for fileInDir in os.listdir(fileOrDir):
            if fileInDir.split(".")[-1] == "jack":
                    jackFileList.append(fileOrDir + "/" + fileInDir)
    else:
        raise Exception("Please passe either a File.jack or Directory containing .jack Files")
    
    return jackFileList


if __name__ == '__main__':
 
    debug = True
    
    if len(sys.argv) != 2:
        raise Exception("Only one argument is allowed [File.jack or Directory]",sys.argv)
    
    print("Passed argument for jack compiler : ",sys.argv[1])
    
    jackFileList = getJackFiles(sys.argv[1])
    if len(jackFileList) == 0 :
        raise Exception("Error generating Jack File list")
    
    print("Files set-up for compilation are: ",jackFileList)

    
    #Process jack files one by one and write Xml files.  
    for jackFile in jackFileList :
        xmlFile = jackFile.split(".")[0] + "_01.xml"
        vmFile = jackFile.split(".")[0] + ".vm"
        if debug:
            print("**************compiling file: ",jackFile)
            print("**************generating xml file ",xmlFile) 
            print("**************generating vm file ",vmFile)
            # To be updated with Code generating statement
            compiler = compilationEngine(jackFile,xmlFile,vmFile,debug = False,debugCompiler = True, debugCompilerSymbolTable= False)
            compiler.parse()
            compiler.close()
            ##########################################################
            
        if debug:
            print("**************End compiling file: ",jackFile)
            print("**************End generating xml file ",xmlFile)        
            print("**************End generating vm file ",vmFile)
        
            
    
    print("Finished processing files")
    
    
