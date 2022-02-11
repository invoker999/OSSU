'''
Created on Oct 8, 2018

@author: Inovker
'''
CMD_TYPE = {"add":"C_ARITHMETIC","sub":"C_ARITHMETIC","neg":"C_ARITHMETIC","eq":"C_ARITHMETIC","eq":"C_ARITHMETIC","gt":"C_ARITHMETIC",
            "lt":"C_ARITHMETIC","and":"C_ARITHMETIC","or":"C_ARITHMETIC","not":"C_ARITHMETIC","pop":"C_POP","push":"C_PUSH",
            "label":"C_LABEL","goto":"C_GOTO","if-goto":"C_IF","function":"C_FUNCTION","call":"C_CALL","return":"C_RETURN"}

class Parser():
    def __init__(self,inputFileName, debug = False):
        '''
        Args: inputFileName(string) 
        return : -
        Opens the input file/stream and gets ready to parse it.
        (str InputFileName) -> bool success
        
        '''
        #Init variable to default value
        self.currentCommand = None 
        self.debug = debug #Save for debug purposes 
        self.inputFile = inputFileName
        inputFileName = inputFileName.split('/')[-1]
        #check valid file name for static variable name generation 
        if inputFileName.startswith(("0","1","2","3","4","5","6","7","8","9")):
            raise NameError("File should not start with a digit")
        else:
            for letter in inputFileName:
                if not ( letter.isalnum() or letter in ["_","$",":","."]):
                    raise NameError("Only alpha_numerics and ( _ , $ , : , . ) characters are allowed")
        
        #Check that the input file name a .vm file and one only
        if inputFileName.split('.')[-1] != "vm":
            raise NameError("Passed file is not a VM file(.vm)")
        else:
            #Generating a list of all commands from .vm file.
            #Extracting only commands with no comments and no extra spaces to simplify decoding.
            with open(self.inputFile, 'r') as file :
                #*******************this part omits comments after a valid command**************no empty lines********* no comments lines*****
                self.commandList = [line.split("//")[0].strip() for line in file.readlines() if line.strip() != "" and line.strip()[0]!="/"]
        
        if debug == True:       
            print("This is the list of commands")
            print(self.commandList)
        
    def hasMoreCommands(self):
        '''
        Args: -
        returns: -
        Are there more commands in the VM file
        '''
        return len(self.commandList) > 0
    
    def advance(self):
        '''
        Args: -
        Returns: -
        Reads the next command from the input and makes it the current command.
        Should be called only if hasMoreCommands() is true. Initially there is no command.
        '''
        if self.hasMoreCommands():
            self.currentCommand = self.commandList.pop(0)
            self.cmdType = CMD_TYPE.get(self.currentCommand.split()[0])
    
    def commandType(self):
        '''
        Args : -
        Returns: CMDTYPE(one of the command type in COMMANDLIST)
        Returns the type of the current VM command. C_ARITHMETIC is returned for all the arithmetic commands
        '''
        return self.cmdType
    
    def arg1(self):
        '''
        Args: -
        returns: fristArgOrCMD(string) 
        returns the first argument of the current command. In the case of C_ARITHMETIC, the command itself (add,sub, etc.) is returned.
        Should not be called if the current command is C_RETURN
        '''
        if self.cmdType == "C_ARITHMETIC":
         
            return self.currentCommand  #return add sub net etc...
        else:
            return self.currentCommand.split()[1]  #returns the first argument of a non Arithmetic command.
           
    def arg2(self):
        '''
        Args: -
        Returns: Arg2(int)
        Returns the second argument of the current command. Should be called only if the current command is C_PUSH, C_POP, C_FUNCTION OR C_CALL
        '''
        #it is up to the caller not to call this method on the wrong command type. 
        return eval(self.currentCommand.split()[2])  #eval to return an Int (not sure yet about this)
    
    def hasArg2(self):
        '''
        Args : -
        Returns : bool
        Returns True if current command has arg2 else returns false
        '''
        return self.commandType() in ["C_PUSH","C_POP","C_FUNCTION","C_CALL"]

if __name__ =="__main__":
    p = Parser("SimpleAdd.vm")
    while p.hasMoreCommands():
        p.advance()
        print(p.commandType(),end = " ")
        print(p.arg1(), end = " ")
        if p.hasArg2() : 
            print(p.arg2(), end = " ")
        print("")
        
        
        