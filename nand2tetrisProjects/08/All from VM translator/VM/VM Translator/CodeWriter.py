'''
Created on Oct 8, 2018

@author: Inovker
'''

class CodeWriter():
    
    def __init__(self,outFileName):
        '''
        Args : OutputFileName(sting)
        Returns: -
        Opens the output File and gets ready to write into it
        '''
        
        self.progFile = open(outFileName,"w")
        
        #Dict to keep track of auto_generated loops for EQ GT LT operations // makes code readable and neat
        self.loopCounters = {"EQ_TRUE":-1,"GT_TRUE":-1,"LT_TRUE":-1,"END_EQ":-1,"END_GT":-1,"END_LT":-1}
        
        #Method mapping for auto calling helper functions
        self.methods= {"add":self.ADDorSUB,"sub":self.ADDorSUB,"neg":self.NEGorNOT,"eq":self.EQorGTorLT,"gt":self.EQorGTorLT,"lt":self.EQorGTorLT,
                       "and":self.ANDorOR,"or":self.ANDorOR,"not":self.NEGorNOT,"C_PUSH":self.PUSH,"C_POP":self.POP,"C_LABEL":self.LABEL,
                       "C_GOTO":self.GOTO,"C_IF":self.IF}
        #Memory segments mapping for Hack assembly language.   Example temp is always at address 5
        self.SegmentsMapping={"local":"LCL","argument":"ARG","this":"THIS","that":"THAT","temp":"5"}
        
        #Function return labels Init to empty dictionary
        self.returnAddresses = {"Sys.init":-1}
        #Use list scope to manage function call and return labels 
        self.scope = ""
        
    def setFileName(self,VMFileName):
        '''
        Args :  VMFileName(sting)
        returns : -
        Informs the code writer that the translation of a new VM file is started. This is mainly for the static PUSH and POP auto variable name generation.
        '''
        #This is used to generate the static variable names for push and pop operation on static memory segments 
        self.VMFile = VMFileName
        print("IN PARSER::VM file name set to:",self.VMFile)
    
    def writeCode(self,code):
        '''
        Access file and write the passed down assembly code
        '''
        self.progFile.writelines(code.lstrip())
        
    def writeArithmetic(self,command):
        '''
        Args: command(string)
        returns : -
        Writes the Hack assembly code of the given arithmetic VM command.
        '''
        code = self.methods[command](command)
        
        self.writeCode(code)       
        
    def writePushPop(self,command,segment,index):
        '''
        Args: command(C_PUSH or C_POP), segment(string),index(int). 
        returns: -
        Writes the Hack assembly code of the given PUSH or POP VM command.
        '''
        code = self.methods[command](segment,index)
        self.writeCode(code)

    def writeLabelGotoIf(self,command,label):
        '''
        Args: command(string),label(string)
        returns : -
        Writes the Hack assembly code for the give branching VM command.
        '''
        code = self.methods[command](label)
        
        self.writeCode(code) 
    
    def writeInit(self):
        '''
        args: -
        return: -
        Writes the Bootstrap and Initialization at the beginning of file. Bootstrap = calling function sys.init, initialization ==> SP = 256
        '''
        code = ('//Bootstrap_CODE \n'
                '@256 \n'
                'D = A \n'
                '@SP \n'
                'M = D \n')
        
        self.writeCode(code)
        self.writeCall("Sys.init",0)

    def genReturnAdd(self,functionName):  
        '''
        Args: fucntionName
        return: RetrunAddress
        Helper function : generating return addressses
        '''  
        if functionName not in self.returnAddresses:
            self.returnAddresses[functionName] = 0
        else:
            self.returnAddresses[functionName] += 1
        
        return (functionName +"$ret."+ str(self.returnAddresses[functionName]))
                                             
    def writeCall(self,functionName,numArgs):
        '''
        args: FunctionName, numArgs
        return:  None
        Write the assembly code for a "call function numArgs" command.
        ''' 
     
        
        code = ('//Call_{FUNCTION} \n'
                '@{RET}\n' #Get return Address
                'D = A \n'
                '@SP \n'
                'M = M+1 \n' #SP++
                'A = M-1 \n' #(*A) ==> SP-- (top of current stack)
                'M = D \n'   #PUSH returnAddress     //push return-address // (Using the label declared below)
                '@LCL \n'    #                      //push LCL // Save LCL of the calling function
                'D = M \n'   #D = LCL  
                '@SP \n'
                'M = M + 1 \n' #SP++
                'A = M - 1 \n' #(*A) ==> SP--
                'M = D \n'     #PUSH LCL
                '@ARG \n'    #                  //push ARG // Save ARG of the calling function
                'D = M \n'   #D = ARG
                '@SP \n'
                'M = M + 1 \n' #SP++
                'A = M - 1 \n' #(*A) ==> SP--
                'M = D \n'     #PUSH ARG
                '@THIS \n'     #              //push THIS // Save THIS of the calling function
                'D = M \n'   #D = THIS
                '@SP \n'
                'M = M + 1 \n' #SP++
                'A = M - 1 \n' #(*A) ==> SP--
                'M = D \n'     #PUSH THIS
                '@THAT \n'     #              //push THAT // Save THAT of the calling function
                'D = M \n'   #D = THAT
                '@SP \n'
                'M = M + 1 \n' #SP++
                'A = M - 1 \n' #(*A) ==> SP--
                'M = D \n'     #PUSH THAT
                '@{N} \n'      #              //ARG = SP-n-5 // Reposition ARG
                'D = A \n'
                '@5 \n'                           
                'D = D + A \n' #D = n+5                      
                '@SP \n'
                'D = M - D \n' #D = SP-(n+5)
                '@ARG \n'      
                'M = D \n'     #ARG = SP-n-5 = D
                '@SP \n'       #              //LCL = SP // Reposition LCL
                'D = M \n'
                '@LCL \n'
                'M = D \n'        #LCL = SP = D
                '@{FUNCTION} \n' #           //goto f // Transfer control
                '0;JMP \n'             
                '({RET}) \n'  #        //(return-address) // Declare a label for the return-address
                '//CALL_END_{FUNCTION}\n').format(FUNCTION = functionName,N = str(numArgs),RET = self.genReturnAdd(functionName))
        
        self.writeCode(code)
    
    def writeReturn(self):
        '''
        Args: -
        Return : -
        Write the Hack assembly for a VM command return"
        '''
        code = ('//Return_{FUNCTION}_start \n' 
                '@LCL \n ' #FRAME = LCL // FRAME is a temporary variable
                'D = M \n'
                '@R11 \n'   #R11 = LCL = FRAME
                'M = D \n'  #R11 = LCL = FRAME
                '@5 \n'        #RET = *(FRAME-5) // Put the return-address in a temp. var.
                'A = D - A \n' #A = FRAME - 5 = D - 5   M = return-address
                'D = M \n'  #D =(*A) = *(FRAME -5) return Add
                '@R12 \n'    #R12 = return address   Store return address at R12
                'M = D \n'  #R12 = D = return address
                '@SP \n'    #ARG = pop() // Reposition the return value for the caller
                'M = M - 1 \n' #SP --
                'A = M \n'
                'D = M \n' #D = pop() = return value
                '@ARG \n'
                'A = M \n'
                'M = D \n'  #*ARG = pop() = return value
                '@ARG \n'   #SP = ARG+1 // Restore SP of the caller
                'D = M + 1 \n' # D = ARG + 1
                '@SP \n'
                'M = D \n'  # SP = ARG + 1 = D
                '@R11 \n'    #THAT = *(FRAME-1) // Restore THAT of the caller
                'M = M - 1 \n' #FRame = FRAME - 1 
                'A = M \n'     #*(FRAME-1)
                'D = M \n'     #D = *(FRAME-1)   
                '@THAT \n'
                'M = D \n'   #THAT = *(FRAME -1) = D
                '@R11 \n'     #THIS = *(FRAME-2) // Restore THIS of the caller
                'M = M - 1\n'
                'A = M \n'   #*A = *(FRAME-2)
                'D = M \n'      #D = *(FRAME-2)
                '@THIS \n'
                'M = D \n'   #THIS = *(FRAME-2) = D
                '@R11 \n'     #ARG = *(FRAME-3) // Restore ARG of the caller
                'M = M -1 \n'
                'A = M \n'   #A = FRAME-3
                'D = M \n'   #D = *(FRAME-3)
                '@ARG \n'
                'M = D \n'      #ARG = *(FRAME-3) = D
                '@R11 \n'    #LCL = *(FRAME-4) // Restore LCL of the caller
                'M = M - 1 \n'
                'A = M \n'     # A = FRAME-4
                'D = M \n'     # D = *(FRAME-4)
                '@LCL \n'
                'M = D \n'  # LCL = *(FRAME-4)
                '@R12 \n'    #goto RET // Goto return-address (in the caller’s code) = *(R12)
                'A = M \n'
                '0;JMP \n'
                '//END_Retrun_{FUNCTION}\n').format(FUNCTION = self.scope)
             
        self.writeCode(code)
        
    def writeFunction(self,functionName,numLocals):
        '''
        Args : FunctionName, numLocals
        return : -
        Write the assembly code of the command "function k"
        '''
        #Register scope for label generation
        self.scope = functionName
        
        code=('//Code_{FUNCTION}\n'
              '({FUNCTION}) \n' #(f) // Declare a label for the function entry
              '@{K} \n'         #repeat k times: // k  number of local variables
              'D = A+1 \n'          #PUSH 0 // Initialize all of them to 0
              '({FUNCTION}$__K) \n' #Declare Label for Init LCLs
              '@{FUNCTION}$__S \n'  #Function start label End of LCLs Init
              'D = D - 1 \n'
              'D;JEQ \n'
              '@SP \n'
              'M = M + 1 \n'  #SP++
              'A = M - 1 \n'  #M[A] = *SP
              'M = 0 \n'      #LCL #K = 0
              '@{FUNCTION}$__K \n'
              '0;JMP \n'
              '({FUNCTION}$__S)\n'
              '//END_INIT_{FUNCTION} \n').format(FUNCTION=functionName,K=numLocals)
        
        self.writeCode(code)        
        
        
    
    def close(self):
        '''
        Args: -
        returns: - 
        Closes the output file.
        '''
        self.progFile.flush()
        self.progFile.close()
        print("Output file was successfully generated! Amazing work done behind the scene (trust my words I coded this shit)")
        
    def loopNameGen(self,loopName):
        '''
        Args : OperationName (string= loopName)
        returns : genLoopName (string)
        '''
        #Generate label's names for auto generated loops to avoid conflicting names
        self.loopCounters[loopName] += 1
        return  loopName + "__" + str(self.loopCounters[loopName])
    
    def ADDorSUB(self,command):
        '''
        Args : OP(string)    OP = ['+','-'] 
        Returns : genHackCode(string)    
        Return the auto generated code for an add VM operation
        '''
        OP = '+' if command == "add" else '-'
        
        return ('//ADDorSUB_START \n' #Perform A-B on the stack 
                '@SP \n' 
                'M = M - 1 \n'      #(*SP) == > B       
                'A = M \n'          #(*A) ==> B   
                'D = M \n'          # Get B
                'A = A - 1 \n'      # NO need for SP++ operation because SP is already set for B location above. (subtle SP++)
                'M = M {CODE} D \n' # Compute A-B or A+B and save the result back to A place on the stack
                '//ADDorSUB_END \n').format(CODE=OP)
    
    def NEGorNOT(self,command):

        '''
        Args : -   (No need as the argument is in stack by convention) command is just for compatibility reason
        Returns : genHackCode(string)    
        Return the auto generated code for an neg VM operation
        '''
        OP = '- ' if command == "neg" else '!'
        return ('//NEGorNOT_START \n'
                '@SP \n'
                'A = M - 1 \n'
                'M = {CODE}M \n'
                '//NEGorNOT_END \n').format(CODE=OP)       
        
    def EQorGTorLT(self,command):

        '''
        Args : command = ['eq','gt','lt']   defines what operation hack assembly would be generated
        Returns : genHackCode(string)    
        Return the auto generated code for an eq VM operation
        '''
        OP = command.upper()
        return ('//EQorGTorLT_START \n'
                '@SP \n'
                'M = M - 1 \n'   #*SP ==> Y
                'A = M - 1 \n'   #*SP-- ==> x   or   *A ==> X     
                'D = M \n'       #D = *(SP--) = X
                'M = 0 \n'       #*SP-- = False = 0 (assume the result is FALSE change it if TRUE), While  SP ==> Y
                'A = A + 1 \n'   #A = SP ==> *(SP) = Y
                'D = D - M \n'   #D = X - Y       
                '@{TRUE} \n'
                'D;J{CODE} \n'   #Code mapping: EQ = D;JEQ    GT = D;JGT  LT =   D;JLT 
                '@{END} \n'
                '0;JMP \n'
                '({TRUE}) \n'
                '@SP \n'
                'A = M - 1 \n' #A = SP--
                'M = -1 \n'    #(*SP--) = -1 = TRUE
                '({END}) \n'
                '//EQorGTorLT_END \n').format(CODE = OP,TRUE=self.loopNameGen(OP+"_TRUE"),END = self.loopNameGen("END_"+OP),)

    def ANDorOR(self,command):
        
        '''
        Args : command =["and","or"]
        Returns : genHackCode(string)    
        Return the auto generated code for an AND/OR VM operation
        '''
        OP = command.upper()
        
        code = '&' if command == "and" else '|'
        
        return ('//ANDorOR_START \n'
                '@SP \n'
                'M = M - 1 \n'     #(*SP) ==> B
                'A = M \n'         #(*A)/M ==> B
                'D = M \n'         #D = B
                'A = A - 1 \n'     #(*A) ==> A
                'M = M{CODE}D \n'  # A = A (and/or) B
                '//ANDorOR_END \n').format(CODE = code)
 
    def PUSH(self,segment,index):
        '''
        Args : arg1(string) , [arg2(int)]
        Returns : genHackCode(string)    
        Return the auto generated code for an push VM operation
        '''
        #PUSH CONSTANT index
        if segment == "constant":
            return ('//PUSH_CONSTANT_START \n'
                    '@{CONST} \n'     #@Value
                    'D = A \n'        #Save value for later
                    '@SP \n'
                    'M = M + 1 \n'    #SP++   (tricky SP++ beforehand)
                    'A = M -1 \n'
                    'M = D \n'        #*(SP) = CONSTANT  
                    '//PUSH_CONSTANT_END \n').format(CONST = str(index))
        #PUSH LCL/ARG/THIS/THAT index
        if segment in self.SegmentsMapping:
            return('//PUSH_{SEGMENT}_START \n'
                   '@{INDEX} \n'    #Save index for addr computation 
                   'D = A \n'
                   '@{SEGMENT} \n'  #SEGMENT = LCL,ARG, THIS, THAT
                   'A = D + {MorA} \n'   #computer address and access it
                   'D = M \n'       #Save the value to be pushed to stack
                   '@SP \n'
                   'M = M + 1 \n'   #SP++
                   'A = M - 1 \n'   #*(SP--)  
                   'M = D \n'       #push the value *(SP==) = D (value)
                   '//PUSH_{SEGMENT}_END \n').format(SEGMENT = self.SegmentsMapping.get(segment), INDEX = str(index),MorA = "A" if segment == "temp" else "M")
        
        #PUSH Pointer 0/1  implementation ==  push THIS/THAT        
        if segment == "pointer":
            if index not in [0,1]: raise exception("Index out of range for pointer PUSH operation!")
            return('//PUSH_{SEGMENT}_START \n'
                   '@{SEGMENT} \n'  #SEGMENT = THIS/THAT
                   'D = M \n'       #Save the address in this or that
                   '@SP \n'
                   'M = M + 1 \n'   #SP++
                   'A = M - 1 \n'   
                   'M = D \n'       #*SP = THIS/THAT
                   '//PUSH_{SEGMENT}_END \n').format(SEGMENT = "THIS" if index == 0 else "THAT")
                   
        if segment == "static":
            return('//PUSH_STATIC_START \n'
                   '@{VARIABLE} \n'  #VARIABLE is the auto generated static variable name VMFILE.index  
                   'D = M \n'  
                   '@SP \n'
                   'M = M + 1 \n' #SP++
                   'A = M - 1 \n' #SP
                   'M = D \n').format(VARIABLE=self.VMFile[:-2]+str(index))  # VARIABLE = VMfile.inde                    
    
    def POP(self,segment,index):
        '''
        Args : arg1(string) , [arg2(int)]
        Returns : genHackCode(string)    
        Return the auto generated code for an POP VM operation
        '''
        #NO CONSTANT POP as the CONSTATN segment is a virtual one (no memory is holding integers it's just for simplicity) 
        
        #First segments + temp POP operations
        if segment in self.SegmentsMapping:
            return('//POP_{SEGMENT}_START \n'
                   '@{INDEX} \n'
                   'D = A \n'        #D = offset index
                   '@{SEGMENT} \n'
                   'D = D + {MorA} \n'    #computed D = segmentPointer + i = target address    MorA = A if segment == temp else M
                   '@R13 \n'   
                   'M = D \n'        #Saving target address to R13
                   '@SP \n'
                   'M = M - 1 \n'    #SP--
                   'A = M \n'        #(*A) ==> Value to be POPed
                   'D = M \n'        #saved POPed value to D  (D = *(SP--))//////  D = POP()    leaving SP ==> POPed place (subtle SP++)
                   '@R13 \n'
                   'A = M \n'        #A = (*R13) ==> target address  (computed above) #A = address 
                   'M = D \n'        #*address = *(SP--) =  D = POPed Value   (Done nicely) 
                   '//POP_{SEGMENT}_END \n').format(SEGMENT = self.SegmentsMapping.get(segment), INDEX = str(index),MorA = "A" if segment == "temp" else "M")
        
        if segment == "pointer":
            if index not in [0,1]: raise exception("Index out of range for pointer PUSH operation!")
            return('//POP_{SEGMENT}_START \n'
                   '@SP \n'
                   'M = M - 1 \n'  
                   'A = M \n'
                   'D = M \n'   #D = *(SP--)
                   '@{SEGMENT} \n'
                   'M = D \n'
                   '//POP_{SEGMENT}_END \n').format(SEGMENT = "THIS" if index == 0 else "THAT")
    
        if segment == "static":
            return('//PUSH_STATIC_START \n'
                   '@SP \n'  #VARIABLE is the auto generated static variable name VMFILE.index  
                   'M = M - 1 \n' #SP--
                   'A = M \n'
                   'D = M \n'
                   '@{VARIABLE} \n'
                   'M = D \n').format(VARIABLE=self.VMFile[:-2]+str(index))  #VARIABLE = VMfile.index              
        
    def LABEL(self,label):
        ''' 
        Hack code for Label label VM command
        '''
        return '({LABEL}) \n'.format(LABEL = self.scope+"$"+label)
        
    def GOTO(self,label):
        '''
        Hack code for Unconditional jump VM command 
        '''
        return('@{LABEL} \n'
                '0;JMP \n').format(LABEL = self.scope+"$"+label)        
    
    def IF(self,label):
        '''
        Hack code for if-goto VM command
        '''
        return('//GOTO_IF_START \n'
                '@SP \n'
                'M = M - 1 \n' #SP--
                'A = M \n' # A = SP  so next line *A = M = condition
                'D = M \n'  #  D != 0 else D = 0
                '@{LABEL} \n' # TRUE ==>  D != 0  ===>  D;JNE  jump if not eq to Zero 
                'D;JNE \n'
                '//GOTO_END \n').format(LABEL = self.scope+"$"+label)

       
       
        
if __name__ == "__main__":
    cw = CodeWriter()
    cw.setFileName("prog.vm")
    cw.writeArithmetic("lt")
    cw.writePushPop("C_PUSH", "constant",17)
    cw.close()
    import os 
    print(os.getcwd())
          
          
          
          