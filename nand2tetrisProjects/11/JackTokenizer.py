'''
Created on Feb 16, 2019

@author: Inovker 

jackTokenizer: Nand to Tetris project 11  compiler I
'''






class jackTokenizer(object):
    '''
    Input : Input file.jack
    Removes all comments and white space from the input stream and breaks it into Jack-language tokens, as specified by the jack grammar "
    '''
    KeyWords = ["CLASS", "METHOD","FUNCTION","CONSTRUCTOR","INT","BOOLEAN",
           "CHAR","VOID","VAR","STATIC","FIELD","LET","DO","IF","ELSE",
           "WHILE","RETURN","TRUE","FALSE","NULL","THIS"]
    
    Symbols = ['{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=','~']

    TokenTypes = ["KEYWORD","SYMBOL" ,"IDENTIFIER","INT_CONST","STRING_CONST"]
    
    SpecialChars = {'<':'&lt;','>':'&gt;','"':"&quot;",'&':'&amp;'}
    
    MaxInt = 32767
    MinInt = 0

    def __init__(self,inputFileName, debug = False ,genTXML = False):
        '''
        Opens the input file/stream and gets ready to tokenize it.
        
        options:
            debug : Print some useful info for debugging purposes
            genTXML: Write the fileT.xml 
        '''
        self.getTokenMethods = {"KEYWORD":self.keyWord,"SYMBOL":self.symbol ,"IDENTIFIER":self.identifier,"INT_CONST":self.intVal,"STRING_CONST":self.stringVal}
        self.debug = debug
        self.genTXML = genTXML
        self.tokenStream = []
        self.currentToken = ""
        #The checking for the .jack file names is done in the caller module
        try:
            self.inputFile = open(inputFileName,mode ='r')
            
            #Creat the .XML output Tokenized file 
            outputFileName, extension =  inputFileName.split(".")[0] + "TT.xml",inputFileName.split(".")[-1]
            
            #Check that the file name passed is .jack file
            if extension.lower() != "jack":
                raise(Exception("File passed to Tokenizer is not a .jack file: "+inputFileName))
            elif genTXML:
                try:
                    self.outputFile = open(outputFileName,"w")
                    self.outputFile.write("<tokens>\n")
                except:
                    print("Unable to open output file for writing :"+ self.outputFile.name)
        except: 
            print("Unable to open input file ({}) for reading".format(outputFileName))
            
        if(debug):
            print("Ready to process input File..\n Input File name: ",self.inputFile.name)
            if genTXML : print("Output file was successfully created for writing...\n Output File Name: ",self.outputFile.name)
        
        #Process all line to take out comment and leave only viable tokens
        nextLine = self.inputFile.readline()
        inComment = False   
        stream = []
        lineCounter = 0
        #Assuming that there are no indented comments either // or /* or /** comments are used 
        while(nextLine != ""):
            lineCounter += 1
            nextLine = nextLine.strip()
            if (debug):
                print("\nProcessing Line " + str(lineCounter) + " : " + nextLine)
                
            #1)Processing bloc comments
            if nextLine.startswith("/*"):
                if inComment:
                    raise Exception("Error Line {} : Nested comments are not allowed ".format(lineCounter)) 
                else:  
                    inComment = True
                    if (debug): print(nextLine + " : Comment line suppressed")
             
            if nextLine.endswith("*/"):
                    if not inComment: 
                        raise Exception("Error Line {} : End of comment not matched with a start of comment".fomrat(lineCounter))
                    else:
                        if (debug): print(nextLine + " : Comment line suppressed")       
                        inComment = False
                        nextLine = self.inputFile.readline()
                        continue
            elif inComment:  # if no End of comment found skip the line as we are still inside 
                nextLine = self.inputFile.readline()
                continue
                  
            #End of bloc comments processing
            
            #2) processing in line comment if it was a block comment
            nextLine = ((nextLine.strip()).split("//")[0]) #strip off all in line comment 
            if nextLine == "":       
                nextLine = self.inputFile.readline()
                if debug: print("Line {} :comment suppressed".format(lineCounter))
                continue                              
            #End of comments processing  
            
            
            #Start of Tokenizing all lines 
            if (debug): print("\n\nStart of streaming and Tokenizing......\nCurrent line is :" + nextLine)
            
            #assure that Chars are split by space before tokenizing 
            for symbol in jackTokenizer.Symbols :
                nextLine = nextLine.replace(symbol,' '+symbol+' ')
                
            #Extracting string constant and using codes #sNumber of the string to replace it
            strConstCount = nextLine.count('"')
            if strConstCount % 2 != 0:
                raise(Exception("Line {} :Number of string delimiters found mismatch detected ".format(lineCounter)))
    
            strConstCount /= 2
            strList = []
            strCount = 0
            inStr = False
            newLine = ""
            curStr = ""
            if strConstCount != 0:
                for char in nextLine:
                    if char == '"':
                        if not inStr:
                            inStr = True
                            newLine += ' #S' + str(strCount) +' '    #Mark up constant strings with #S_NumberOfString in the that line to simplify tokenizing
                        else:
                            inStr = False
                            strCount += 1
                            strList.append(curStr)
                            curStr = ""
                    else:
                        if inStr:
                            curStr += char
                        else:
                            newLine += char
                            
                nextLine = newLine
            
            if (debug and strCount > 0):
                print("Number of stingConst found in line {} is : {}".format(lineCounter,strCount))
                print("List of the stingConst: ",strList)
                print("Marked up newLine : ",newLine)
            
            #Finally line is ready for Tokenizing
            stream = nextLine.split()
            
            if (debug):
                print("Initial marked up & split stream before final and absolute tokenizing")
                print(stream)
            
            for token in stream:
                if token.startswith("#"):
                    token='"'+ strList[eval(token.split("S")[1])] + '"'  # Marking strings constant with '"' at the start
                    
                self.tokenStream.append(token)  
                
            nextLine = self.inputFile.readline()
         
        #Input stream generated
        #Take  
        if (debug): print("Tokenizing stream was successfully created with {} tokens".format(len(self.tokenStream)))  
        if (debug): print(self.tokenStream)
    
    def __del__(self):
        
        if self.debug: print("Flush and closing Files: {} , {} ".format(self.inputFile.name,self.outputFile.name))
        if self.genTXML : 
            self.outputFile.flush()
            self.outputFile.close()
        self.inputFile.close()
        
    
    def hasMoreTokens(self):
        '''
        Arguments: -
        Returns: Boolean
        Returns True if we still have more tokens in the input stream else False 
        '''
        if len(self.tokenStream): 
            return True
        else:
            return False
        
    
    def advance(self):
        '''
        Arguments: -
        Returns: -
        Get the next token from the input and makes it the current token.This method should only be called if hasMoreTokens() is True.
        Initially there is no current token.
        '''
        self.currentToken = self.tokenStream.pop(0)
        
        if self.debug: print("Advanced Current Token to : "+ self.currentToken)
        
        if self.genTXML : 
            self.outputFile.write(self.getXml())
            if not self.hasMoreTokens(): self.outputFile.write("</tokens>")
    
    def getXml(self):
        Ttype = self.tokenType()
        token = self.getToken() 
        if token in jackTokenizer.SpecialChars: token = jackTokenizer.SpecialChars[token]
        
        
        #Doing some magic to make the markup match the markup of the nand To tetris courses 
        '''
        if token in jackTokenizer.KeyWords: 
            token = token.lower()
        '''
        #not sure is needed any more 
        
        if Ttype == "STRING_CONST" : 
            Ttype = "stringConstant"
        elif Ttype == "INT_CONST":
            Ttype ="integerConstant"
        else: 
            Ttype = Ttype.lower()
            
        #Markup matching ended...............................................................
        
        markup = "<{0}> {1} </{0}>\n".format(Ttype,token)
        
        if self.debug: print("Generated TXML markup {} ==> {}".format(token,markup))
        return markup
        
    def tokenType(self):
        '''
        Arguments: -
        Returns: TokenType (KEYWORD,SYMBOL.....)
        Returns the type of the current token
        '''
        if self.debug : print("\nToken passed to tokenTyme: ",self.currentToken)
        
        if self.currentToken in jackTokenizer.Symbols: return "SYMBOL" 
        if self.debug : print("Token not a SYMBOL let see if it is a KEYWORD....")
        
        if self.currentToken.swapcase() in jackTokenizer.KeyWords: return "KEYWORD"
        if self.debug : print("Token not a KEYWORD let see if it is a STRING_CONST....")        
        
        if self.currentToken.startswith('"'): return "STRING_CONST"
        if self.debug : print("Token not a STRING_CONST let see if it is a IDENTIFIER....")        
        
        if (self.currentToken.replace("_","A")).isalpha(): return "IDENTIFIER"
        if self.debug : print("Token not a IDENTIFIER let see if it is a INT_CONST....")        
        
        if self.currentToken.isalnum():
            if ( eval(self.currentToken) >= jackTokenizer.MinInt ) or (eval(self.currentToken) <= jackTokenizer.MaxInt):
                return "INT_CONST"
            else:
                raise Exception("INT_CONST({}) out of range value: range [0..32767], ".fomrat(self.currentToken))
            
        if self.debug : 
            print("Token not a INT_CONST let see if it is a Ow FUCK something is wrong.!!!!!!!!!")        
            raise Exception("Unknown Token Type : ".fmat(str (self.currentToken)))
    

    def keyWord(self):
        '''
        Arguments: -
        Returns KeyWord (CLASS,METHOD....)
        Return the keyword which is the current token. Should be called only when tokenType() is KEYWORD.
        '''
        if self.debug : print("Token is a Keyword: ",self.currentToken.swapcase())
        return self.currentToken
    
    def symbol(self):
        '''
        Arguments: -
        Returns: Char (The Symbol/Token itself)
        Returns the character which is the current token. Should be called only when tokenType() is SYMBOL.
        '''
        if self.debug : print("Token is a Symbol: ",self.currentToken)
        return self.currentToken
    
    def identifier(self):
        '''
        Arguments: -
        Returns: string 
        Return the identifier which is the current token. Should be called only when tokenType() is IDENTIFIER.
        '''
        if self.debug : print("Token is a Identifier: ",self.currentToken)
        return self.currentToken
    
    def intVal(self):
        '''
        Arguments: -
        Returns: Int (Value of the current token)
        Returns the integer value of the current token. Should be called only when tokenType() is INT_CONST.
        '''
        if self.debug : print("Token is a IntVAL : ",self.currentToken)
        return eval(self.currentToken)
    
    def stringVal(self):
        '''
        Argument: -
        Returns: String 
        Returns the string value of the current token, without the double quotes. should be called only when tokenType() is STRING_CONST
        '''
        if self.debug : print("Token is a String: ",self.currentToken)
        #Storing stringConst as  "string. striping away the (") before returning 
        return self.currentToken[1:-1]
        
    def getToken(self):
        '''
        (None) --> (str token)  
        Retrun the current token
        '''
        if self.debug: print("getToken current token: " + str(self.currentToken))
        return (self.getTokenMethods[self.tokenType()])()
        
        
        