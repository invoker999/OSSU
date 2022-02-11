'''
Created on Feb 16, 2019

Author: invoker999
Course: OSSU/nand2tetris
Email: kaced.sofiane@gmail.com

'''

from JackTokenizer import jackTokenizer
from SymbolTable import symbolTable
from VMWriter import VMWriter

class compilationEngine():
    '''
    Effects the actual compilation output. Get input form a JackTokenizer and emits its parsed structure into an output file/stream.
    '''
    types = {'int','char','boolean'} #To be appended with new Class names (not) sure yet if i will do a typecheck
    op = {'+':'ADD','-':'SUB','*':"MUL",'/':"DIV",'&':"AND",'|':"OR",'<':"LT",'>':"GT",'=':"EQ"}
    unaryOp = {'~':"NOT",'-':"NEG"}
    subTypes = {'constructor','function','method'}
    keywordConstant = {'null','false','true','this'}
    kindToSegment = {'ARG':'ARG','STATIC':'STATIC','VAR':'LOCAL','FIELD':'THIS'}
    
    '''
    Maybe needed for OS Writing 
    
    SymbolKeys = {" " : 32, "!" : 33, '"' :34, "#":35, "$":36, "%":37, "&":38, "'":39, "(":40, ")":41, "*":42, "+":43, ",":44, "-":45, ".":46,
                  "/":47, ":":58, ";":59, "<": 60, "=":61, ">": 62, "?":63, "@":64, "[":91, "/":92, "]" :93, "^":94, "_": 95, "`":96 }
    
    CursorKeys = {"\n":128, "newline":128, "backspace":129, "\b":129, "left_arrow":130, "up_arrow":131, "right_arrow":132,
                  "down_arrow":133, "home":134, "end":135, "Page_up":136, "Page_down":137, "insert":138, "delete":139, "esc":140}
    
    FunctionKeys = {"f1":141, "f2":142, "f3":143, "f4":144, "f5":145, "f6":146, "f7":147, "f8":148, "f9":149, "f10":150, "f11":151, "f12":152}
            
    @classmethod         
    def AlphaNumKeys(cls,c):
        if c.isalpha() : 
            return ord(c)
        else:
            raise Exception("none Alpha was passed to AlphaNumKeys: ",c)
    '''
    
    def __init__(self, jackFile,xmlFile,vmFile,debug = False,debugCompiler = True ,debugCompilerSymbolTable = True):
        '''
        (str InputFile,str outputFile) --> None
        Arguments: InputFile,OuputFile   (.jack, .xml)
        Returns: -
        Creates a new compilation engine with the given input and output. The next routine called must be comileClasse().
        '''
        #Init

        self.debug = debug
        self.debugCompiler = debugCompiler
        self.expectedClassName = (((jackFile.split('.'))[0]).split('/'))[-1]
        self.debugCompilerSymbolTable = debugCompilerSymbolTable
        self.statementCompilers = {"let":self.compileLet,'while':self.compileWhile,'if':self.compileIf,'do':self.compileDo,'return':self.compileRetrun}
        self.loopCounter = {'while':0, 'if':0}
        #Create the Tokens generator
        self.tokensGen = jackTokenizer(jackFile,genTXML=False)
        self.tokensGen.advance()
        
        #Init class name ot None
        self.className = None
        self.subroutineName = None
        #Create an empty symbolTable
        self.mySymbolTable = symbolTable(debug = True)
        
        #Create a VM writer
        self.myVMWriter = VMWriter(vmFile,debugCompiler)
        
        #Create XML output File
        try:
            self.xmlFile = open(xmlFile,"w")
        except:
            print("Could not create xml output File: ",xmlFile)
                
    def close(self):
        
        if self.debug: print("Del compilerEngine and closing files.....",self.xmlFile.name)
        self.myVMWriter.close()
        self.xmlFile.flush()
        self.xmlFile.close()
        

    def parse(self):
        '''
        Start parsing by calling compileClass as every Jack file is a class
        '''
        if self.debug: print("Start File compilation to an XML and VM Files..................................................")
        self.compileClass()
        if self.debug: print("End of File compilation to an XML and VM files.................................................")
        
    def processIdentifier(self):
        '''
        Handles writing varName (identifiers)
        '''
        if self.debug : print('Processing an Identifier: ',self.next())
        
        if self.tokensGen.tokenType() == "IDENTIFIER" :  
            self.xmlFile.write(self.tokensGen.getXml())
            self.tokensGen.advance()
        else: raise SyntaxError("Expected token of type 'IDENTIFIER' but received {} of type {} ".format(self.next(),self.tokensGen.tokenType())) 
        
    def processType(self):
        '''
        Handles Writing type (className or Keywords(int,char...)
        '''
        if self.debug: print("Processing a Type: ",self.next())
        
        if self.next() in compilationEngine.types: 
            self.xmlFile.write(self.tokensGen.getXml())   
            self.tokensGen.advance()
            
        else: 
            self.processIdentifier()  #This is done in case we need to time check class names  
      
    def processRule(self,code):
        '''
        (str code) ---> None
        Process the expected code and raise an SyntaxError if there is a mismatch
        '''
        if self.debug : print("Processing Rule: ",code)
        
        if self.next() != code:
            raise SyntaxError("Syntax Error: Rule Expects '{}' but found '{}'".format(code,self.next()))
        
        else:
            if self.debug : print("....Processing Rule code : ",code)
            self.xmlFile.write(self.tokensGen.getXml())   
            if self.tokensGen.hasMoreTokens() : self.tokensGen.advance()
    
    def processOp(self):
        '''
        (str code) ---> None
        Process an op code and raise a SyntaxError if there is a mismatch
        '''
        
        if self.debug : print("Processing Op : ",self.next())
        
        if self.next() not in compilationEngine.op :
            raise SyntaxError("Syntax Error: Operator expected but received: ",self.nex())
        else:
            if self.debug : print("....Processing op: ",self.next())
            self.xmlFile.write(self.tokensGen.getXml())
            self.tokensGen.advance()
            
    def processUnaryOp(self):
        '''
        (str code) ---> None
        Process an op code and raise a SyntaxError if there is a mismatch
        '''
        if self.debug : print("Processing Op : ",self.next())
        
        if self.next() not in compilationEngine.unaryOp :
            raise SyntaxError("Syntax Error: Unary Operator expected but received: ",self.nex())
        else:
            if self.debug: print("....Processing unarOp: ",self.next())
            self.xmlFile.write(self.tokensGen.getXml())
            self.tokensGen.advance()

    def next(self):
        if self.debug: print("Next token called and returns: " + str(self.tokensGen.getToken()))
        return self.tokensGen.getToken()
    
    def processConst(self):
        '''
        Process INT_CONST, KeywordConst and stringConstant
        '''
        if self.debug : print('Processing CONSTANT : ',self.next())
        
        if self.tokensGen.tokenType() in {'INT_CONST','STRING_CONST'} or self.next() in compilationEngine.keywordConstant:  
            self.xmlFile.write(self.tokensGen.getXml())
            self.tokensGen.advance()
            
        else: raise SyntaxError("Expected token of type CONSTANT or KeywordCONSTANT but received {} of type {} ".format(self.next(),self.tokensGen.tokenType())) 
    
    def compileClass(self):
        '''
        Compiles a complete class.
        Rule: 
        ____________________________________________________________
        class: 'class' className '{' classVarDec* subroutineDec* '}'
        ____________________________________________________________
        '''
        if self.debug : print("Start of processing a class............................")
        self.xmlFile.write("<class>\n")
        
        self.processRule('class')
        self.className = self.next()
        self.processIdentifier()
        
        #Raise exception if fileName is not the same as className
        if self.className != self.expectedClassName: raise NameError("JackFile name: {}  should be the same as class name {}".format(self.className,self.expectedClassName))
        
        self.processRule('{')
        
        while self.next() == 'static' or self.next() == 'field':
            self.compileClassVarDec()
            
        while self.next() in compilationEngine.subTypes:
            
            #rest the symbol table for the new subroutine to zero
            self.mySymbolTable.startSubroutine()  
            self.compileSubroutine()
            if self.debugCompilerSymbolTable: 
                print("\n\n*** ::: *** ::: *** End of subroutine({}) compilation *** ::: *** ::: ***".format(self.subroutineName))
                print(self.mySymbolTable)
                
        self.processRule('}')
        
        if self.debugCompilerSymbolTable: 
            print("\n\n*** ::: *** ::: *** End of class({}) compilation *** ::: *** ::: ****".format(self.className))
            print(self.mySymbolTable)        
        
        self.xmlFile.write("</class>\n")        
        if self.debug : print("End of processing a class..............................")   
    
    def compileClassVarDec(self):
        '''
        Compiles a static declaration or a field declaration.
        Rule:
        ________________________________________________________________
        classVarDec :('static' | 'field') type varName(',' varName)* ';'
        ________________________________________________________________
        '''
        if self.debug : print("Start of processing a classVarDec............................")
        self.xmlFile.write("<classVarDec>\n")
        
        if self.next() == 'static':
            Kind = 'STATIC' 
            self.processRule('static')
        else: 
            Kind = 'FIELD'
            self.processRule('field')
        
        Type = self.next()
        self.processType()
        
        Name = self.next()
        self.processIdentifier()
        
        # Add the class field or static variable to symbol Table
        self.mySymbolTable.define(Name,Type,Kind)
        if self.debugCompilerSymbolTable : print("Add to Symbol Table: Name =  {} ::: Type = {} ::: Kind = {}".format(Name,Type,Kind))
        
        while self.next() == ',':
            self.processRule(',')
            Name = self.next()
            self.processIdentifier()
            #Keep adding the variable of the same type and kind
            self.mySymbolTable.define(Name,Type,Kind)
            if self.debugCompilerSymbolTable : print("Add to Symbol Table: Name =  {} ::: Type = {} ::: Kind = {}".format(Name,Type,Kind))
            
        self.processRule(';')
        
        self.xmlFile.write("</classVarDec>\n")        
        if self.debug : print("End of processing a classVardec..............................")   
    
    def compileSubroutine(self):
        '''
        Compiles a complete method,function,or constructor.
        Rule:
        ____________________________________________________________________________________________________________________
        subroutineDec: ('constructor'|'function'|'method')('void'| type) subroutineName '(' parameterList ')' subroutineBody
        subroutineBody: '{' varDec* statements '}
        ____________________________________________________________________________________________________________________
        '''
        #DEBUG
        ######################################################################################
        if self.debug : print("Start of processing a Subroutine............................")#
        ######################################################################################
        
        self.xmlFile.write("<subroutineDec>\n")
        
        if self.next() not in compilationEngine.subTypes : 
            raise SyntaxError("Expected one of subroutine types '{}' but received: {}".format(compilationEngine.subTypes,self.next()))
        
        comment = self.next() # saving needed tokens to create a comment of the compiled function.
        constructor = False
        if self.next() == 'constructor':
            #Moved the process of constructor initialization after function declaration
            constructor = True
            #self.mySymbolTable.define("this",self.className,"ARG")  #NOT SURE yet but I think we will need to have this as argument
            self.processRule('constructor')
            #Debug compiler
            ##########################################################################################################################################
            if self.debugCompiler: 
                if self.next() != self.className : 
                    raise TypeError("Constructor return type mismatch:  ClasseName = {} <:::> Return-Type = {}".format(self.className,self.next()))
            #########################################################################################################################################
        elif self.next() == 'method':
            #If the subroutine is a method Add this as the first argument
            self.mySymbolTable.define("this",self.className,"ARG") 
            self.processRule('method')
            #DEBUG_COMPILER_SYMBOLTABLE
            ############################################################################################################
            if self.debugCompilerSymbolTable :                                                                         #
                print("Add to SymbolTable: Name =  {} ::: Type = {} ::: Kind = {}".format('this',self.className,'ARG'))#
            ############################################################################################################ 
            
        elif self.next() == 'function':
            self.processRule('function')
        
        comment += ' '+self.next()
        if self.next() == 'void': 
            self.processRule('void')
        else: 
            self.processType()

        
        #Save current subroutine Name and write a comment for the start
        self.subroutineName = self.next()
        self.processIdentifier()
        self.processRule('(')
        self.compileParameterList()    
        self.processRule(')')
        

        
        self.xmlFile.write("<subroutineBody>\n")
        self.processRule('{')
        
        while self.next() == 'var':
            self.compileVarDec()
        
        self.myVMWriter.writeComment('\n//'+comment + ' ' + self.subroutineName +'\n')            #Comment at start of each subroutine
        
        #Subroutine declaration  function ClassName.method nLocals
        self.myVMWriter.writeFunction(self.className + "." + self.subroutineName,self.mySymbolTable.varCount('VAR')) 
        
        #Allocating Space to object if the called method is a constructor
        if constructor:
            self.myVMWriter.writePush('CONST',self.mySymbolTable.varCount('FIELD')) #retrieve number of fields needed for the constructed object
            self.myVMWriter.writeCall('Memory.alloc',1) #one argument for Memory.alloc function
            self.myVMWriter.writePop('POINTER',0)   # anchors this at the base address
            
        self.myVMWriter.writeComment("//{} <subroutineBody>\n".format(self.subroutineName))
        
        if self.mySymbolTable.kindOf('this') == 'ARG':
            self.myVMWriter.writePush('ARG', 0)      # PUSH this to Stack
            self.myVMWriter.writePop("POINTER", 0)   # POP this from stack : THIS = argument 0 = this(self) the object calling the method
            
        self.compileStatements()
        
        self.processRule('}')
        
        self.xmlFile.write("</subroutineBody>\n")
        self.xmlFile.write("</subroutineDec>\n")
        self.myVMWriter.writeComment('//{} END \n'.format(self.subroutineName))        
        if self.debug : print("End of processing a Subroutine..............................")   
    
    def compileParameterList(self):
        '''
        Compiles a (possibly empty) parameter list, not including the enclosing "()".
        Rule:
        ___________________________________________________
        pramaterList: ((type varName) (',' type varName)*)?
        ___________________________________________________
        '''
        if self.debug : print("Start of processing a prarameterList............................")
        self.xmlFile.write("<parameterList>\n")
        if self.next() != ')':
            #collect KIND,TYPE and NAME of arguments and adding them to symbol table
            Kind = "ARG"
            Type = self.next()
            self.processType()
            Name = self.next()
            self.processIdentifier()
            
            #Add the processed argument to symbol Table
            self.mySymbolTable.define(Name,Type,Kind)
            if self.debugCompilerSymbolTable : print("Add to Symbol Table: Name =  {} ::: Type = {} ::: Kind = {}".format(Name,Type,Kind))
            
            while self.next() == ',':
                self.processRule(',')
                Type = self.next()
                self.processType()
                Name = self.next()
                self.processIdentifier()
                #Add the remaining argument if any to the symobl Table
                self.mySymbolTable.define(Name,Type,Kind)
                if self.debugCompilerSymbolTable : print("Add to Symbol Table: Name =  {} ::: Type = {} ::: Kind = {}".format(Name,Type,Kind))
                
        self.xmlFile.write("</parameterList>\n")        
        if self.debug : print("End of processing a prameterList................................")   
    
    def compileVarDec(self):
        '''
        Compiles a variable declaration.
        Rule:
        ____________________________________
        varDec: 'var' type varName (','varName)*';'
        ____________________________________
        '''
        if self.debug : print("Start of processing a varDec............................")
        self.xmlFile.write("<varDec>\n")
        
        #collect all KIND,TYPE,NAME of declared variables and adding them to symbol table
        Kind = 'VAR'
        self.processRule('var')
        
        Type = self.next()
        self.processType()
        
        Name = self.next()
        self.processIdentifier()
        
        #Add to the symbol table the processed var declaration 
        self.mySymbolTable.define(Name,Type,Kind)
        if self.debugCompilerSymbolTable : print("Add to Symbol Table: Name =  {} ::: Type = {} ::: Kind = {}".format(Name,Type,Kind))
        
        while self.next() == ',':
            self.processRule(',')
            Name = self.next()
            self.processIdentifier()
            #Add all the var of the same type and kind to the symbol table
            self.mySymbolTable.define(Name,Type,Kind)
            if self.debugCompilerSymbolTable : print("Add to Symbol Table: Name =  {} ::: Type = {} ::: Kind = {}".format(Name,Type,Kind))
            
        self.processRule(';')
        self.xmlFile.write("</varDec>\n")        
        if self.debug : print("End of processing a varDec..............................")   
        
    def compileStatements(self):
        '''
        Compiles a sequence of statements, not including the enclosing "{}".
        Rule:
        ________________________
        Statements : statements*
        ________________________
        '''
        if self.debug : print("Start of processing Statements.................................")
        self.xmlFile.write("<statements>\n")
        
        while self.next() != '}':
            if self.debug : print("......Current statement: ",self.next())
            self.statementCompilers.get(self.next())()     #Use a dict to call the right statement
            
        self.xmlFile.write("</statements>\n")        
        if self.debug : print("End of processing Statements....................................")   
        
    def compileDo(self):
        '''
        Compiles a do statement.
        Rule
        ______________________________________________________________________________________________________________________________
        'do' subroutineCall ';'
        subroutineCall : (subroutineName '(' expresionList ')' ) || ((className | varName) '.' subroutineName '(' expresionList ')')
        ______________________________________________________________________________________________________________________________
        '''
        if self.debug : print("Start of processing a do Statement.............................")
        self.xmlFile.write("<doStatement>\n")
        
        self.processRule('do')
        
        VarMethClass = self.next() 
        self.processIdentifier()  #subroutine/class/var name
        
        if self.next() == '(':             #this means it is a subroutine call
            self.processRule('(')
            #POINTER 0 = THIS  should be pushed first
            self.myVMWriter.writePush("POINTER",0)              #PUSH this to Stack to set argument 0 to this of the method caller 
            nArgs = self.compileExpresionList() + 1             #Save number of arguments for the subroutine call
            self.myVMWriter.writeCall(self.className + "." +VarMethClass,nArgs)   #the complete className.method call
            self.processRule(')')
        else:      
            self.processRule('.')
            methodName = self.next()
            self.processIdentifier()
            self.processRule('(')
            
            if self.pushVar(VarMethClass):                      #Pushes the object on which the method is called to the operate (implicit parameter)
                nArgs = 1                                       #add count for the implicit (this) push before method call.
                Type = self.mySymbolTable.typeOf(VarMethClass) #if the the call is for a method get its className from the type of the object
                fullName = Type +'.'+methodName                 #full name is ClassName.methodName
            else:
                nArgs = 0                                       #if var was not in the symbolTable consider the call is for a function in className.function
                fullName = VarMethClass+'.'+methodName
                
            nArgs += self.compileExpresionList()                #add the previous state of nArgs 0(functionCall) or 1 (methodCall) to the pushed parameter list
            self.myVMWriter.writeCall(fullName,nArgs)           #finally call the the full named method with the correct number of parameters
            self.processRule(')')   
        self.processRule(';')
        self.myVMWriter.writePop("TEMP","0")                         #Do statement always discards the returned value from methods and functions 
        self.xmlFile.write("</doStatement>\n")        
        if self.debug : print("End of processing a do Statement...............................")
    
    def compileLet(self):
        '''
        Compiles a let statement.
        Rule:
        ________________________________________________________
        'let' varName ( '[' expression ']')? '=' expression ';'
        ________________________________________________________
        '''
        if self.debug : print("Start of processing a let statement............................")
        self.xmlFile.write("<letStatement>\n")
        self.processRule('let')
        
            
        
        varOrArray = self.next()     #keep the varName for later
        self.processIdentifier()
        
        #try to process '[' if they exist else skip to '='
        if self.next() == '[':                      
            self.processRule('[')
            #Handling Arrays                        #TO DO Arrays
            self.pushVar(varOrArray)                #PUSH array to stack  (base address of array: array[0]) 
            self.compileExpression()                #PUSHed whatever is the index i computed by the expression.
            self.myVMWriter.writeArithmetic("ADD")  #compute address of array[index] = array[0] + offset
            #self.myVMWriter.writePop("TEMP",0)      #POP array address to TEMP 0 instead of POINtER 1 to avoid losing it in the upcoming expression handling
            self.processRule(']')
            
            self.processRule('=') 
                                                    #THIS IS ALL DONE IN CASE OF  a[i] = b[j] possible assignment
            self.compileExpression()                #Handle expression and even array access operation with no risk of loosing the already computer address
            self.myVMWriter.writePop("TEMP",0)       #Save(pop) the value of expression into TEMP 0
            self.myVMWriter.writePop("POINTER",1)  #POP to POINTER 1 the hanging address on the stack of array[index] computer earlier
            self.myVMWriter.writePush("TEMP", 0)    #rePUSH the value back to the stack
            self.myVMWriter.writePop("THAT",0)      #POP the value of the expression to to array[index] = value | b[j] 
            self.processRule(';')

        
        else:                     #No array access
            self.processRule('=')
            self.compileExpression()    #PUSH expression
            self.popIntoVar(varOrArray) #pop into variable
            self.processRule(';')

        
        self.xmlFile.write("</letStatement>\n")        
        if self.debug : print("End of processing a let statement..............................")       
    
    def compileWhile(self):
        '''
        Compiles a while statement.
        Rule:
        ______________________________________________________________
        whileStatment : 'while' '(' expression ')' '{' statements '}'
        ______________________________________________________________
        '''
        L1,L2,whileCount = self.genLoopLabel('while')
        
        if self.debug : print("Start processing a while Statement...............................")
        self.xmlFile.write("<whileStatement>\n")
        self.myVMWriter.writeComment("\n//..............<whileStatement {}>\n".format(whileCount))
        
        self.processRule('while')
        self.processRule('(')
        
        self.myVMWriter.writeLabel(L1)          #label L1
                                    
        self.compileExpression()                    #Compiled(expression)         
        self.processRule(')')
        
        self.myVMWriter.writeArithmetic('NOT')      #not
        self.myVMWriter.writeIf(L2)                 #if-goto L2
    
        self.processRule('{')
        self.compileStatements()                    #compiled(statements)
        self.processRule('}')
        
        self.myVMWriter.writeGoto(L1)               #goto L1
        self.myVMWriter.writeLabel(L2)          #label L2
        
        self.myVMWriter.writeComment("//..............</whileStatement {}>\n\n".format(whileCount))        
        self.xmlFile.write("</whileStatement>\n")        
        if self.debug : print("End of processing a while Statement..............................")
        
    def compileRetrun(self):
        '''
        Compiles a return statement.
        Rule:
        ________________________
        'return expression? ';'
        _______________________
        '''
        if self.debug : print("Start of processing a return statement............................")
        self.xmlFile.write("<returnStatement>\n")
        
        self.processRule('return')
        
        if self.next() != ';':
            self.compileExpression()
        else:
            self.myVMWriter.writePush('CONST',0)   #the function should always return something!  if no statements found "PUSH constant 0" is the default mapping
            
        self.processRule(';')
        
        self.myVMWriter.writeReturn()
        self.xmlFile.write("</returnStatement>\n")        
        if self.debug : print("End of processing a return statement..............................")   
        
    def compileIf(self):
        '''
        Compiles an if statement.
        Rule:
        _________________________________________________________________________
        'if' '(' expression ')' '{' statements '}' ( 'else' '{' statements '}')?
        _________________________________________________________________________
        '''

        L1, L2 , ifCount  = self.genLoopLabel('if')
        
        if self.debug : print("Start of processing an if statement............................")
        self.xmlFile.write("<ifStatement>\n")
        self.myVMWriter.writeComment("\n\n//..............<ifStatement {}>\n".format(ifCount))    
            
        self.processRule('if')
        
        self.processRule('(')
        self.compileExpression()                #compiled(expression)
        self.processRule(')')        
        
        self.myVMWriter.writeArithmetic("NOT")  #not
        self.myVMWriter.writeIf(L1)             #if-goto L1
        
        self.processRule('{')
        self.compileStatements()
        self.processRule('}')
        
        self.myVMWriter.writeGoto(L2)           #goto L2
        self.myVMWriter.writeLabel(L1)          #label L1
        
        if self.next() == 'else':
            self.processRule('else')
            self.processRule('{')
            self.compileStatements()
            self.processRule('}')
        
        self.myVMWriter.writeLabel(L2)          #label L2

        self.myVMWriter.writeComment("//..............</ifStatement {}>\n\n".format(ifCount))             
        self.xmlFile.write("</ifStatement>\n")        
        if self.debug : print("End of processing a if statement..............................")   
    
    def genLoopLabel(self,statment):
        '''
        statement : ['while' | 'if']
        Generate label names for 'while and 'if' statement for flow control
        '''
        customize = 'LOOP' if statment == 'while' else 'ELSE'
        count = self.loopCounter[statment]
        self.loopCounter[statment] += 1
        
        
        return "{}_{}$${}".format(statment,customize,count) ,  "{}_END$${}".format(statment,count) , count
         
    def compileExpression(self):
        '''
        Compiles and expression. Pass for the moment
        Rule:
        ____________________________
        expression: term (op term)*
        ____________________________
        '''
        if self.debug : print("Start of processing a Expression............................")
        self.xmlFile.write("<expression>\n")
        self.compileTerm()
        while self.next() in compilationEngine.op:
            OP = self.next()
            self.processOp()
            self.compileTerm()
            self.myVMWriter.writeArithmetic(compilationEngine.op[OP])
            
        self.xmlFile.write("</expression>\n")        
        if self.debug : print("End of processing a Expression..............................")   
        
    def compileTerm(self):
        '''
        Compiles a term. This routine is faced with a slight difficulty when trying to decide between some of the alternative parsing rules.Specifically, 
        if the current token is an identifier,the routine must distinguish between a variable, and array entry,and a subroutine call,A single look-Ahead token, 
        which may be one of "[","(", or "." suffices to distinguish between the three possibilities. Any other token is not part of this term and should not be advance over.
        Rule:
        ___________________________________________________________________________________________
        term: integerConstant | stringConstant | keywordConstant | unaryOp term
              varName | varName '[' expression ']' | subroutineCall | '(' expression ')' 
        
        subrtoutineCall: subroutineName '(' expressionList ')' | 
                        (className | varName) '.' subroutineName '(' expreionList ')'
        ___________________________________________________________________________________________
        '''
        #CodeWriter(exp)
        
        if self.debug : print("Start of processing an term............................")
        self.xmlFile.write("<term>\n")
        #self.processIdentifier()
        
        if self.tokensGen.tokenType() == 'INT_CONST': 
            self.myVMWriter.writePush("CONST", self.next())      # if exp is a number n:
            self.processConst()                                  #      push n
            
        elif self.tokensGen.tokenType() == 'STRING_CONST':
            #Handling creation of constant strings
            #String constant are created using OS constructor String.new(length)
            #String assignment list x = "constanteString" are handled using a series of calls to String.apendCahr(c)*
            self.myVMWriter.writePush('CONST',len(self.next()))   #Push the maxLength of the sting to be created
            self.myVMWriter.writeCall("String.new",1)
            for c in self.next():
                self.myVMWriter.writePush('CONST',ord(c))
                self.myVMWriter.writeCall('String.appendChar',2)
            
            self.processConst()
                
        elif self.next() in compilationEngine.keywordConstant:
            if self.next() == 'this':
                #This is only encountered  in "return this' statement from a constructor  i.e always need to return push pointer 0 to the stack              
                self.myVMWriter.writePush('POINTER', 0)
                self.processConst()
                
            else:
                #Handling keyword constants  null = 0  false = 0, true = -1
                self.myVMWriter.writePush("CONST", self.next())  #if exp is keyword constant it will be mapped by writePush
                self.processConst()
            
        elif self.next() in compilationEngine.unaryOp:           # if exp is "op exp":
            OP = self.next()                                     # codeWrite(exp1)
            self.processUnaryOp()                                # command OP
            self.compileTerm()
            self.myVMWriter.writeArithmetic(compilationEngine.unaryOp[OP])
        
        elif self.next() == '(':
            self.processRule('(')
            self.compileExpression()                             #this means another list of expression will be handled recursively
            self.processRule(')')
            
        elif self.tokensGen.tokenType() == "IDENTIFIER":
            
            VarMethClass = self.next()    #save the none yet clear identifier ( variable | Method | ClassName )
            self.processIdentifier()
            
            if self.next()=='[':
                self.processRule('[')
                #Handling Arrays                        #TO DO Arrays
                self.pushVar(VarMethClass)              #PUSH array to stack  (base address of array: array[0]) 
                self.compileExpression()                #PUSHed whatever is the index i computed by the expression.
                self.myVMWriter.writeArithmetic("ADD")  #compute address of array[index] = array[0] + offset
                self.myVMWriter.writePop("POINTER",1)   #POP array address to THAT for handling arrays
                self.myVMWriter.writePush("THAT",0)     #PUSH array[index] (RAM[THAT]) into stack
                self.processRule(']')
                
            elif self.next() == '(':
                self.processRule('(')
                self.myVMWriter.push("POINTER",0)             #PUSH this to Stack to set argument 0 to this of the method caller
                nArgs = self.compileExpresionList() + 1       #Save number of arguments for the subroutine call  
                self.myVMWriter.writeCall(self.className + "." +VarMethClass,nArgs)   # Call the full name "Class.method"
                self.processRule(')')
            
            elif self.next() == '.': 
                
                self.processRule('.')
               
                methodName = self.next()      #save the yet to be used method name
                self.processIdentifier()
                
                self.processRule('(')
                
                if self.pushVar(VarMethClass):                           #Try to Pushes the object on which the method is called to the operate (implicit parameter)
                    nArgs = 1                                            #add the count of the implicit (object) to parameter count                  
                    Type = self.mySymbolTable.typeOf(VarMethClass)       #if the subroutine called is a method on an object we need to get its className from object type
                    fullName = Type +'.'+methodName                      #Full Name Class.method is used for the call.
                else:
                    nArgs = 0                                      #If pushVar failed the call is for a function don't add the implicit parameter count 
                    fullName = VarMethClass +'.'+methodName        #IF the call is to a function then VarMethClass is ClassName
    
                nArgs += self.compileExpresionList()        #nArgs: number of arguments in parameter list of the function called 
                self.myVMWriter.writeCall(fullName,nArgs)   #call object.method(self,nArgs)  or call ClassName.function(nArgs)
                self.processRule(')')
            
            else:
                #This means the none clear variable | Method | ClassName was a variable and needs to be pushed to the stack
                self.pushVar(VarMethClass)
        
        else:        
            raise SyntaxError("Unable to compile Term : Pattern unmatched.........")   
        
        self.xmlFile.write("</term>\n")        
        if self.debug : print("End of processing a term..............................")   
        
        '''
        According to the Jack syntax, If bar is a method then Foo is a variable you can push to the stack,
        but if bar is a function then Foo is the class name, so you can't push it anyway, 
        it won't even exist in the variable table.    
    
        Yes, the Jack syntax says that functions always have the class name prepended.
        fn(x) and <variable>.f(x) are always method calls.
        <ClassName>.f(x) is always a function or constructor call. (You don't need to know that it's a class name, just that it isn't a variable name.)
        his makes Jack easy to compile, if a bit awkward to use.
        
        '''
      
    def compileExpresionList(self):
        '''
        Compiles a (possibly empty) comma-separated list of expressions.
        expressionList: (expression (',' expression)*)?
        '''
        if self.debug : print("Start of processing an Expression List............................")
        self.xmlFile.write("<expressionList>\n")
        
        numOfExpression = 0     #counter of Number of expression in case of a function call to know number of arguments passed (nArgs)
        if self.next() != ')':
            self.compileExpression()
            numOfExpression += 1 
               
            while self.next() == ',':
                self.processRule(',')
                self.compileExpression()
                numOfExpression += 1
        
        self.xmlFile.write("</expressionList>\n")        
        if self.debug : print("End of processing an Expression list..............................")   
        return numOfExpression   #Used for function calls

    def pushVar(self,var): 
        '''
        (var) --> done boolean 
        var: variable to be looked up in the symbol table
        done: True if the variable was found and VM code written and False if not
        
        Lookup the variable in the symbol table and write the VM translation
        '''
        Kind = self.mySymbolTable.kindOf(var)
        if Kind == "NONE":
            #Not sure to raise an error or not
            #raise KeyError("variable {} not found in the symbole table".format(var))
            print("Table lookup for "+ str(var) +" as not conclusive")
            return False
        else:    
            #Type = self.symbolTable.typeOf(var)
            Index = self.mySymbolTable.indexOf(var)
        
        
        self.myVMWriter.writePush(compilationEngine.kindToSegment[Kind],Index)    
        
        return True 

    def popIntoVar(self,var): 
        '''
        (var) --> done boolean 
        var: variable to be looked up in the symbol table
        done: True if the variable was found and VM code written and False if not
        
        Lookup the variable in the symbol table and write the VM translation pop var command
        '''
        Kind = self.mySymbolTable.kindOf(var)
        #debug compiler: popping into a none declared variable is not allowed
        ###############################################################################
        if Kind == "NONE":
            raise Exception("Pop operation to a none declared variable: ",var)
        
        Index = self.mySymbolTable.indexOf(var)    
        self.myVMWriter.writePop(compilationEngine.kindToSegment[Kind],Index)  
          
        return True 
    
        
        
        
        
        
        
        
        
        
        
        
        
