'''
Created on Feb 16, 2019

@author: Inovker
'''

import JackTokenizer

class compilationEngine():
    '''
    Effects the actual compilation output. Get input form a JackTokenizer and emits its parsed structure into an output file/stream.
    '''
    types = {'int','char','boolean'} #To be appended with new Class names (not) sure yet if i will do a typecheck
    op = {'+','-','*','/','&','|','<','>','='}
    unaryOp = {'~','-'}
    subTypes = {'constructor','function','method'}
    keywordConstant = {'null','false','true','this'}
    
    def __init__(self, inputFile,outputFile,debug = True):
        '''
        (str InputFile,str outputFile) --> None
        Arguments: InputFile,OuputFile   (.jack, .xml)
        Returns: -
        Creates a new compilation engine with the given input and output. The next routine called must be comileClasse().
        '''
        #Init
        self.debug = debug
        self.statementCompilers = {"let":self.compileLet,'while':self.compileWhile,'if':self.compileIf,'do':self.compileDo,'return':self.compileRetrun}
        #Create the Tokens generator
        self.tokensGen = JackTokenizer.jackTokenizer(inputFile,genTXML=True)
        self.tokensGen.advance()
        #Create XML output File
        try:
            self.xmlFile = open(outputFile,"w")
        except:
            print("Could not create output File: ",outputFile)
    def __del__(self):
        if self.debug: print("Del compilerEngine and closing files.....",self.xmlFile.name)
        del(self.tokensGen)
        self.xmlFile.flush()
        self.xmlFile.close()
        
    def parse(self):
        '''
        Start parsing by calling compileClass as a first method 
        '''
        if self.debug: print("Start File compilation to an XML file..................................................")
        self.compileClass()
        if self.debug: print("End of File compilation to an XML file.................................................")
        
    def processIdentifier(self):
        '''
        Handles wiring varName (identifiers)
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
            self.xmlFile.write(self.tokensGen.getXml())   #This is done in case we need to time check class names
            self.tokensGen.advance()
            
        else: self.processIdentifier()    
      
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
        self.processIdentifier()
        
        self.processRule('{')
        
        while self.next() == 'static' or self.next() == 'field':
            self.compileClassVarDec()
            
        while self.next() in compilationEngine.subTypes:
            self.compileSubroutine()
            
        self.processRule('}')
        
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
        
        if self.next() == 'static': self.processRule('static')
        else: self.processRule('field')
        self.processType()
        self.processIdentifier()
        
        while self.next() == ',':
            self.processRule(',')
            self.processIdentifier()
            
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
        if self.debug : print("Start of processing a Subroutine............................")
        self.xmlFile.write("<subroutineDec>\n")
        
        if self.next() in compilationEngine.subTypes : self.processRule(self.next())
        else: raise SyntaxError("Expected one of subroutine types '{}' but received: {}".format(compilationEngine.subTypes,self.next()))
        
        if self.next() == 'void': self.processRule('void')
        else: self.processType()
        self.processIdentifier()
        self.processRule('(')
        self.compileParameterList()
        self.processRule(')')
        
        self.xmlFile.write("<subroutineBody>\n")
        self.processRule('{')
        while self.next() == 'var':
            self.compileVarDec()
        self.compileStatements()
        self.processRule('}')
        self.xmlFile.write("</subroutineBody>\n")
              
        self.xmlFile.write("</subroutineDec>\n")        
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
            self.processType()
            self.processIdentifier()
            while self.next() == ',':
                self.processRule(',')
                self.processType()
                self.processIdentifier()
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
        self.processRule('var')
        self.processType()
        self.processIdentifier()
        while self.next() == ',':
            self.processRule(',')
            self.processIdentifier()
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
        self.processIdentifier()
        
        if self.next() == '(':
            self.processRule('(')
            self.compileExpresionList()
            self.processRule(')')
        else:      
            self.processRule('.')
            self.processIdentifier()
            self.processRule('(')
            self.compileExpresionList()
            self.processRule(')')   
        
        self.processRule(';')   
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
        self.processIdentifier()
        #try to process '[' if they exist else skip to '='
        if self.next() == '[':                      
            self.processRule('[')
            self.compileExpression()
            self.processRule(']')  
        self.processRule('=')
        self.compileExpression()
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
        if self.debug : print("Start processing a while Statement...............................")
        self.xmlFile.write("<whileStatement>\n")
        self.processRule('while')
        self.processRule('(')
        self.compileExpression()
        self.processRule(')')
        self.processRule('{')
        self.compileStatements()
        self.processRule('}')
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
            
        self.processRule(';')
        
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
        if self.debug : print("Start of processing an if statement............................")
        self.xmlFile.write("<ifStatement>\n")
        
        self.processRule('if')
        
        self.processRule('(')
        self.compileExpression()
        self.processRule(')')
        
        self.processRule('{')
        self.compileStatements()
        self.processRule('}')
        
        if self.next() == 'else':
            self.processRule('else')
            self.processRule('{')
            self.compileStatements()
            self.processRule('}')
            
        self.xmlFile.write("</ifStatement>\n")        
        if self.debug : print("End of processing a if statement..............................")   
    
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
            self.processOp()
            self.compileTerm()
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
        ___________________________________________________________________________________________
        '''
        if self.debug : print("Start of processing an term............................")
        self.xmlFile.write("<term>\n")
        #self.processIdentifier()
        
        if self.next() in compilationEngine.unaryOp:
            self.processUnaryOp()
            self.compileTerm()
        
        
        elif self.next() == '(':
            self.processRule('(')
            self.compileExpression()
            self.processRule(')')
        
        elif self.tokensGen.tokenType() == "IDENTIFIER":
            self.processIdentifier()
            
            if self.next()=='[':
                self.processRule('[')
                self.compileExpression()
                self.processRule(']')
                
            elif self.next() == '(':
                self.processRule('(')
                self.compileExpresionList()
                self.processRule(')')
            
            elif self.next() == '.':
                self.processRule('.')
                self.processIdentifier()
                self.processRule('(')
                self.compileExpresionList()
                self.processRule(')')
        
        else:
            try:
                self.processConst() 
            except SyntaxError as e:
                print(e)              
                raise SyntaxError("Unable to compile Term : Pattern unmatched.........")   
        
        self.xmlFile.write("</term>\n")        
        if self.debug : print("End of processing a term..............................")   
    
    def processConst(self):
        '''
        Process INT_CONST, KeywordConst and stringConstant
        '''
        if self.debug : print('Processing CONSTANT : ',self.next())
        
        if self.tokensGen.tokenType() in {'INT_CONST','STRING_CONST'} or self.next() in compilationEngine.keywordConstant:  
            self.xmlFile.write(self.tokensGen.getXml())
            self.tokensGen.advance()
            
        else: raise SyntaxError("Expected token of type CONSTANT or KeywordCONSTANT but received {} of type {} ".format(self.next(),self.tokensGen.tokenType())) 
    
    
    def compileExpresionList(self):
        '''
        Compiles a (possibly empty) comma-separated list of expressions.
        expressionList: (expression (',' expression)*)?
        '''
        if self.debug : print("Start of processing an Expression List............................")
        self.xmlFile.write("<expressionList>\n")
        
        if self.next() != ')':
            self.compileExpression() 
               
            while self.next() == ',':
                self.processRule(',')
                self.compileExpression()
        
        self.xmlFile.write("</expressionList>\n")        
        if self.debug : print("End of processing an Expression list..............................")   
    