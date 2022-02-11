import os
import io


A_COMMAND ,C_COMMAND , L_COMMAND = 0, 1, 2

class SymbolTable():
    def __init__(self):
        """
            Init the Hack machine defined symbols and Constants 
        """
        self._symbolTable = dict(SP=0,LCL=1,ARG=2 ,THIS=3 ,THAT=4,R0=0,R1=1,R2=2,R3=3,R4=4,R5=5,R6=6,R7=7,R8=8,R9=9,R10=10
                                 ,R11=11,R12=12,R13=13,R14=14,R15=15,SCREEN=16384,KBD=24576)
        self._freeRAM = 16

    def print(self):
        """
        Print all values stored in Table for debug only
        """
        print(self._symbolTable)

        
    def addEntry(self,symbol,address):
        """
            add Entry to table with (symbol = address)
        """
        if symbol not in self._symbolTable:
            self._symbolTable[symbol]=address
        else:
            raise Exception("Deplicated ("+symbol+") lable in code")
        
    def contains(self,symbol):
        """
        True if symbole is in table else false
        """
        return symbol in self._symbolTable

    def getAddress(self,symbol):
        """
        Return address matching the symbol
        """
            #IF symbol is not in table already, that's a first declared variable in second pass,
            #add it to table and increment Free pointer RAM to next address
        if symbol not in self._symbolTable:
            self._symbolTable[symbol] = self._freeRAM
            self._freeRAM +=1


        return self._symbolTable[symbol]
            
                
    
class Parser():
    DEST, COMP, JUMP = 0, 1, 2
    
    def __init__(self, asmFileName):
        
        ######################### Reading File .asm and init .prs file name
        try:
            if asmFileName.split(".")[-1].lower() != "asm": #accept .asm file no case senstive
                raise Exception("File format Erro")
            
            self.asmFile = open(asmFileName,mode = 'r') #set .asm file for reading
            
        except Exception as ex :
            print(ex.message) #print error message
            exit(0)
            
        ######################### Init
        self.currentCommand = None
        self._PC = 0  # program counter to -1 as program counter start from zero
        self.hasMoreCommands = False
        self.symbolTable = SymbolTable()
        ###############################################################
        

        try:
            self.parseFileName = self._cleanAndFirstPass() # Clean and first pass building up Symbole table
            self.parseFile = open(self.parseFileName,mode = 'r')
            if self._PC == 0:
                raise Exception("Empty asm file")
            else:
                self.hasMoreCommands = True
        except Exception as ex:
            print(ex.message)

    def printSymbolTable(self):

        self.symbolTable.print()
            
            
               
    def advance(self):
        """
        Get the next command on the cleaned file to parse it
        
        """

        self.currentCommand = self.parseFile.readline().strip()
        self._PC -= 1
        
           
        if self._PC == 0 :
            self.hasMoreCommands = False
        
        #print("CMD = ", self.currentCommand , end = " :: ")

    def commandType(self):
        """
        return currenCommand type  A,C or L
        """
        
        if self.currentCommand[0] == '@':
            #print("{} type A ".format(self._PC), end = " :: ")
            return  A_COMMAND
        elif self.currentCommand[0] == '(' and self.currentCommand[-1]== ')':
            #print("{} type L ".format(self._PC), end = " :: ")
            return L_COMMAND
        else:
            #print("{} type C ".format(self._PC), end = " :: ")
            return C_COMMAND

        raise Exception("Called commandType on \"None\" currentCommand, Hell what the fuck")

    def symbol(self):
        """
        Called only on type A = @VVV or L = (XXX) and returns either "VVV" or "XXX"
        """
            
        if self.commandType() == A_COMMAND :
            return self.currentCommand[1:]
        elif self.commandType() == L_COMMAND :
            return self.currentCommand[1:-1]

        raise Exception("symbol called an C_COMMAND or something went wrong with the update of symbol table")

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
        self.asmFile.close()
        print(self.asmFile.name + " closed!")
        self.parseFile.close()
        print(self.parseFile.name + " closed and removed!")
        os.remove(self.parseFile.name)
        
        
    def _cleanAndFirstPass(self):  # and First pass, building up VariableTabel
        ''' input < asmFile 
            output > cleanFileName, numberOfline
            __doc__: Help function that creats a .cl file clean from comments and spaces ready to be parsed
            called only once to clean the asm file
        '''
        cleanFileName = self.asmFile.name.split(".")[0]+".cl" #Generate a  temp file
        print("Generated Clean name is: " + cleanFileName)
        
        cacheList = []
        self._PC = 0
        
        print("First pass on asm File, Building up symbol Table and cleaning spaces and comments!")        
        try:
            with open(cleanFileName, 'w') as cleanFile:
                for lines in self.asmFile.readlines():
                    #print(lines) #for debug only
                    cleanLine = lines.split("//")[0].strip().replace(' ','') #strip spaces and comment out and building symbol Table
                    if cleanLine != '':
                        self.currentCommand = cleanLine
                        if  self.commandType() != L_COMMAND:
                            cacheList.append((cleanLine + "\n"))
                            self._PC +=1
                        else:
                            self.symbolTable.addEntry(self.symbol(),self._PC)
                            #print("Lable :: "+ self.symbol() + " :: added with address: ",self._PC)
                        
                                     
                            
                if len(cacheList):
                    for cachedLine in cacheList:
                        cleanFile.write(cachedLine)
                        
                    del cacheList
                    print("....................................................Done!")
                else:
                    raise Exception("First pass and cleaning Error, File empty!")
                        
        except Exception as ex :
            print("The following Error occured during cleaning ")
            print(ex.message)


        self.currentCommand = None
        self.asmFile.seek(io.SEEK_SET) #rewind the .asm file to Zero
        return cleanFileName 

if __name__ == "__main__":

    Max = Parser("Pong.asm")
    PC = 0
    while(Max.hasMoreCommands):
        
        Max.advance()
        if Max.commandType() == C_COMMAND:
            pass
            #print("{3}::Dest = {0},Comp = {1},Jump = {2}".format(Max.dest(),Max.comp(),Max.jump(),PC))

        elif Max.commandType() == A_COMMAND :
            pass
            #print("{0}::@Value/(xxx) = {1} ".format(PC,Max.symbol()))
        else:
            pass
            #print("what the Fuck there is no L_COMMANDS")

        PC+=1















    
