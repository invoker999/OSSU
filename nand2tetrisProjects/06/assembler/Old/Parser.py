import os
import io

A_COMMAND ,C_COMMAND , L_COMMAND = 0, 1, 2

class Parser():
    DEST, COMP, JUMP = 0, 1, 2
    
    def __init__(self, asmFileName):
        
        ######################### Reading File .asm and init .prs file name
        try:
            if asmFileName.split(".")[-1].lower() != "asm": #accept .asm file no case senstive
                raise Exception("File format Erro")
            
            self.asmFile = open(asmFileName,mode = 'r') #set .asm file for reading
            
            self.cleanFileName = asmFileName.split(".")[0]+".cl" #Generate a .psd temp file
            print("Generated Clean name is: " + self.cleanFileName)
            self.cleaned = False
            
        except Exception as ex :
            print(ex.message) #print error message
            exit(0)
            
        ######################### Init
        self.currentCommand = None
        self._commandType = None
        self._PC = -1  # program counter to -1 as program counter start from zero
        self.hasMoreCommands = False
        ###############################################################

        try:
            self.parseFileName,self.countCommand = self._clean()
            self.parseFile = open(self.parseFileName,mode = 'r')
            if self.countCommand == 0:
                raise Exception("Empty asm file")
            else:
                self.hasMoreCommands = True
        except Exception as ex:
            print(ex.message)
               
    def advance(self):
        """
        Get the next command on the cleaned file to parse it
        
        """

        self.currentCommand = self.parseFile.readline().strip()
        self.countCommand -= 1
        self._PC += 1
        self._commandType = self.commandType()
           
        if self.countCommand == 0 : self.hasMoreCommands = False
        
        print("CMD = ", self.currentCommand , end = " :: ")

    def commandType(self):
        """
        return currenCommand type  A,C or L
        """
        
        if self.currentCommand[0] == '@':
            print("{} type A ".format(self._PC), end = " :: ")
            return  A_COMMAND
        elif self.currentCommand[0] == '(' and self.currentCommand[-1]== ')':
            print("{} type L ".format(self._PC), end = " :: ")
            return L_COMMAND
        else:
            print("{} type C ".format(self._PC), end = " :: ")
            return C_COMMAND

        raise Exception("Called commandType on \"None\" currentCommand, Hell what the fuck")

    def symbol(self):
        """
        Called only on type A = @VVV or L = (XXX) and returns either "VVV" or "XXX"
        """
        c = self._commandType
            
        if c == A_COMMAND :
            return self.currentCommand[1:]
        elif c == L_COMMAND:
            return self.currentCommand[1:-1]

        raise Exception("symbol called an C_COMMAND")

    def dest(self):
        
        return self._cPartition()[Parser.DEST]
    
    def comp(self):
        
        return self._cPartition()[Parser.COMP]

    def jump(self):
        
        return self._cPartition()[Parser.JUMP]

    def _cPartition(self):
        """
           Unpacking the current command into 3 fileds dest=comp;jump
        """
        
        cmd = self.currentCommand 
        
        if len(cmd.split("=")) == 2 :
            dest,comp = cmd.split("=")
        else:
            dest,comp = "null", cmd
  
        if len(comp.split(";")) == 2 :
            comp,jump = comp.split(";")
        else:
            jump = "null"
            
        return [dest,comp,jump]
 
    
    def __del__(self):
        print("Del of parser: closing asm file.....closing parseFile")
        self.asmFile.close()
        self.parseFile.close()
        
    def _clean(self):
        ''' input < asmFile 
            output > cleanFileName, numberOfline
            __doc__: Help function that creats a .cl file clean from comments and spaces ready to be parsed
            called only once to clean the asm file 
        '''
        if self.cleaned : return self.cleanFileName, self.numberOfLines
        
        self.numberOfLines = 0
        print("clean asm file .",end="")        
        try:
            with open(self.cleanFileName, 'w') as cleanFile:
                for lines in self.asmFile.readlines():
                    #print(lines) #for debug only
                    cleanLine = lines.split("//")[0].strip() #strip spaces and comment out
                    if cleanLine != '':
                        
                        cleanFile.write(cleanLine.replace(' ','') +"\n")  
                        self.numberOfLines += 1
                        print("...",end="")
        except Exception as ex :
            print("The following Error occured during cleaning ")
            print(ex.message)
            exit(0)

        else:
            print("\n")
            self.cleaned = True  
            self.asmFile.seek(io.SEEK_SET) #rewind the .asm file to Zero
            return self.cleanFileName, self.numberOfLines

if __name__ == "__main__":

    Max = Parser("MaxL.asm")

    while(Max.hasMoreCommands):
        
        Max.advance()
        if Max._commandType == C_COMMAND:
            print(" Dest={0},Comp={1},Jump = {2} ".format(Max.dest(),Max.comp(),Max.jump()), end = "\n\n")

        else :
            print(" @Value/(xxx) = ",Max.symbol(), end = "\n\n")
















    
