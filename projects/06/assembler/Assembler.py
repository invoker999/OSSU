from Code import Code
from Parser import Parser
import os
A_COMMAND ,C_COMMAND , L_COMMAND = 0, 1, 2

class Assembler():
    MAXVALUE = 32768
    
    def __init__(self,asmFileName,outFileName=None):
        #Creat HackFile (name outFileName name or asmFile.hack and stor it in self.hackFile
        if outFileName == None:
            outFileName = asmFileName[:-3]+"hack"
            
       
        
        try:
            self.hackFile = open(outFileName,mode='w')
            print("Created file .hack : " + outFileName)

        except Exception as ex:
            print("Couldn't creat or open " + outFileName + "for writing, OS returned following Error:")
            print(ex.message())
            
        
        #passe the asmFile to self.myParser and get ready to decode and advance to first instruction
        try:
            self.myParser = Parser(asmFileName)
            #self.myParser.advance()
        except Exception as ex:
            print("Error encountred while opening file "+ asmFileName+". OS returned following Error:")
            print(ex.message())


            
        #init self.instructionAddress stors the address of the current instruction to be decoded
        self.nextInstructionAddress = 0
        #slef.done == False  # bool to flag once the assemble is done
        self.done = False
        #self.closedHackFile = False   #if no way to check if file is closed

    @classmethod        
    def bin15(cls,value):
        """
        Return the binary represention of value with 16 digits with MSB = 0
        """
        if type(value) != int:
            raise TypeError("in bin15, value Type Error Type :" + str(type(value)))
        
        if value >= cls.MAXVALUE:
            raise Exception("Passed a @VALUE greater than " + str(cls.MAXVALUE-1) + " to an A instruction, VALUE =",value)

        return '0' + bin(cls.MAXVALUE+value)[3:]

    def _step(self):
        """
        Deocde one instruction from self.myParser not called if slef.done = True
        """
        #Advance parser by one instruction
        self.myParser.advance()
        #check if it is last instruction then set self.done = True
        if not self.myParser.hasMoreCommands:
            self.done = True
            #print("We are done")

        
        #Docde it.... A_COMMAND or C_COMMAND or L_COMMAND
        
        #Instruction A_COMMAND:
        if self.myParser.commandType() == A_COMMAND:
            
            #GET the value of the symbol form either symbol Value table or constant
            symbol = self.myParser.symbol()
            if not symbol.isnumeric() : 
                value = self.myParser.symbolTable.getAddress(symbol)  #retrieve the already storred or the declared variable address
            else:
                value = eval(symbol)
            
            
            return Assembler.bin15(value)
                
            
        #Instruction is C_Command:
        if self.myParser.commandType() == C_COMMAND:
            #print("C_COMMAND")
            return "111" + Code.comp(self.myParser.comp()) + Code.dest(self.myParser.dest()) +  Code.jump(self.myParser.jump())
            #print("C_COMMAND :"+machineCode)

        
        raise Exception("Command type Unkown!!!!!!!!")
        

    def assemble(self):
        """
        Code the whole asm file into a .hack file and say when done
        Close .hack files once done
        """
        count = 0
        cacheFile = []
        while not self.done:     
            #While not Done call step()
            codedInstruction = self._step()
            #if the instruction is None continue else write it to hackFile and increse Nextaddress
            if codedInstruction == None:
                continue
            #increment NextAddre
            cacheFile.append(codedInstruction+"\n")
            count +=1
            #print("instruction Writen : " + codedInstruction)
            self.nextInstructionAddress += 1
            if count > 1000:
                for cachedLine in cacheFile:
                    self.hackFile.write(cachedLine)
                print(".",end="")
                cacheFile = []
                count = 0
                
        if count != 0:
            for cachedLine in cacheFile:
                self.hackFile.write(cachedLine)
            print(".",end="\n...We are Done")
            cacheFile = []
            count = 0

        if not self.hackFile.closed:
            self.hackFile.flush()
            self.hackFile.close()
        
        print("Output File name : " + self.hackFile.name)
        print("Done assembling the file with "+ str(self.nextInstructionAddress) + " total Instructions") 
        

    def __del__(self):
        """
        Close file once deleted
        """
        if not self.hackFile.closed:
            self.hackFile.flush()
            self.hackFile.close()
        


if __name__ == "__main__":
    if len(os.sys.argv) != 2 and len(os.sys.argv) != 3:
        print(" Use : python Assembler input.asm [outputFile] ")
        
    elif len(os.sys.argv) == 3:
        prog = Assembler(os.sys.argv[1],os.sys.argv[2]+".hack")
        prog.assemble()
    else:
        prog = Assembler(os.sys.argv[1])
        prog.assemble()
    
        
    




























