'''
Created on Feb 27, 2019

@author: Inovker

@version: 1.0.0

VMWriter for "From NAND to Tetris courses"
'''


class VMWriter(object):
    '''
    Emits VM commands into a file, using the VM command syntax
    '''
    ARITHMETICS = {"ADD","SUB","NEG","EQ","GT","LT","AND","OR","NOT"}
    ARITHMETICS_OS = {'MUL','DIV'}
    
    UnitIndent = 4
    IndentChar = ' '
    SEGMENTS = {"CONST":"constant","ARG":"argument","LOCAL":"local","STATIC":"static",
                "THIS":"this","THAT":"that","POINTER":"pointer","TEMP":"temp"}
    
    #CONSTANT to be translated to int:  ture = -1, false = 0, null = 0.    
    #NOTE: 'true' is -1 but it will be followed by a "NEG" operation   (Pushing negative constant is not allowed)
    keywrodToConst = {'true':1,'false':0,'null':0}

    def __init__(self,VMfile,debug = True, commenting = False):
        '''
        (Output file/stream) --> None
        Creates a new file and prepares it for writing 
        '''
        self.commenting = commenting
        self.indent = ""
        self.labelIndent = 0
        self.debug = debug
        try:
            self.vmFile = open(VMfile,"w")
        
        except IOError as ioE:
            print(ioE)
            print("unable to create VM file : "+VMfile)
        
        if debug: print(VMfile + " open and ready for compiling!")
            
    def incrementIndent(self):
        if len(self.indent) <= VMWriter.UnitIndent:
            self.indent = 0
        else:
            self.indent = self.indent[0:- VMWriter.UnitIndent]
            
    def dicrementIndent(self):
        self.indent = self.indent + (VMWriter.UnitIndent * VMWriter.IndentChar)
        
    def writePush(self, segment,index):
        '''
        (str Segment,int ndex) --> None
        segment: CONST,ARG,LOCAL,STATIC,THIS,THAT,POINTER,TEMP 
        Writes a VM push command.
        '''
    
        #Check if index is a keyword constant to be maped to its value
        negate = True if index == 'true' else False
        index = VMWriter.keywrodToConst.get(index,index)
        
        #Handling pushing negative CONSTANT numbers 
        
        if self.debug : print("Writing :: PUSH {} {}".format(segment,index))
        code = ('{INDENT}push {SEGMENT} {INDEX}\n').format(INDENT = self.indent,SEGMENT = VMWriter.SEGMENTS[segment],INDEX = index)
        if negate:
            code += '{INDENT}neg\n'.format(INDENT = self.indent)
        
        self.vmFile.write(code)
        
    def writePop(self, segment,index):
        '''
        (str segment,int index) --> None
        segment: CONST,ARG,LOCAL,STATIC,THIS,THAT,POINTER,TEMP 
        Writes a VM PoP command.
        '''
        if segment == 'CONST':
            raise SyntaxError("Pop into a constant-segment is not allowed")
        
        if self.debug : print("Writing :: POP {} {}".format(segment,index))
        
        code = ('{INDENT}pop {SEGMENT} {INDEX}\n').format(INDENT = self.indent,SEGMENT = VMWriter.SEGMENTS[segment],INDEX = index)
        
        self.vmFile.write(code)
        
    def writeArithmetic(self,command):
        '''
        (str command) --> None
        command : ADD,SUB,NEG,EQ,GT,LT,AND,OR,NOT
        Writes a VM arithmetic command.
        '''
        if self.debug : print("Writing :: command {}".format(command))
        
        if command in VMWriter.ARITHMETICS : 
            command = command.lower()
            code = ('{INDENT}{COMMAND}\n').format(INDENT=self.indent,COMMAND = command)
            self.vmFile.write(code)
            
        elif command in VMWriter.ARITHMETICS_OS:
           
            if command == 'MUL':
                self.writeCall('Math.multiply', 2)
                
            else:
                self.writeCall('Math.divide',2)
            
        else:
            raise SyntaxError("Unknown command passed to writeArithmetic command = "+command)   
              
    def writeLabel(self,label):
        '''
        (str label) --> None
        Writes a VM label command
        '''
        
        if self.debug : print("Writing :: lable  {}".format(label))
        
        code = ('{INDENT}label {LABEL}\n').format(INDENT = self.indent*self.labelIndent,LABEL = label)
        
        self.vmFile.write(code)
          
    def writeGoto(self,label):
        '''
        (str label) --> None
        Writes a VM goto command
        '''
        if self.debug : print("Writing :: goto label  {}".format(label))
        
        code = ('{INDENT}goto {LABEL}\n').format(INDENT=self.indent,LABEL = label)
        
        self.vmFile.write(code)
    
    def writeIf(self,label):
        '''
        (str label) --> None
        Writes a VM if-goto command
        '''
        if self.debug : print("Writing :: if-goto "+label)
        
        code = ('{INDENT}if-goto {LABEL}\n').format(INDENT=self.indent,LABEL =label)
        
        self.vmFile.write(code)

    def writeCall(self,name,nArgs):
        '''
        (str name, int nArgs) --> None
        Writes a call command
        '''
        if self.debug: print("Writing :: call " + name + " " + str(nArgs))
        
        code = ('{INDENT}call {F_NAME} {N_ARGS}\n').format(INDENT=self.indent,F_NAME = name, N_ARGS = nArgs)
        
        self.vmFile.write(code)
    
    def writeFunction(self,name,nLocals):
        '''
        (str name, int nLocals) --> None
        Writes a VM function command
        '''
        if self.debug: print("Writing :: call " + name + " " + str(nLocals) )
        
        code = ('{INDENT}function {F_NAME} {N_LOCALS}\n').format(INDENT=self.indent,F_NAME = name, N_LOCALS = nLocals)
        
        self.vmFile.write(code)
        
    def writeReturn(self):
        '''
        (None) --> None
        Writes a return command
        '''
        if self.debug : print("Writing :: return")
        code = ('{INDENT}return\n'.format(INDENT=self.indent))
        
        self.vmFile.write(code)
    
    def writeComment(self,comment):
        '''
        (str comment) --> None
        Write to the VM file the passed comment
        '''
        
        if self.commenting: self.vmFile.write(comment)
        
    def close(self):
        '''
        Closes the output file
        '''
        if self.debug: print("Finished writing vm file : {}\nClosing...........!".format(self.vmFile.name))
        self.vmFile.flush()
        self.vmFile.close()
        
        
        
if __name__ == "__main__":
    
    writer = VMWriter("Test_VMWriter.vm")
    
    writer.writePush("STATIC",0)
    writer.writePop("TEMP",1)
    writer.writeArithmetic("ADD")
    writer.writeArithmetic("NOT")
    writer.writeLable("QUIT___01")
    writer.writeGoto("END___01")
    writer.writeIf("NOt_ZERO")
    writer.writeCall("moveCharacter",3)
    writer.writeFunction("findMax",2)
    writer.writeReturn()
    writer.close()
     
     
     
     
     
     
     
     
     
        
        
        
        
        
        
        
        
        
        