'''
Created on Feb 27, 2019

@author: Inovker

@version : 1.0.0

'''


class symbolTable(object):
    '''
    Provides a symbol table abstraction. The symbol table associates the identifier names 
    found in the program with identifier properties needed for compilation: type, kind and running index.
    the symbol table for Jack programs has two nested scopes (class/subrtouine).
    
    '''

    def __init__(self,debug = True):
        '''
        (None) ---> None
        Creates a new empty symbol table.
        '''
        self.debug = debug
        
        self.kinds = {"STATIC","FIELD","ARG","VAR"}
        
        self.kindsCount= {"STATIC":0,"FIELD":0,"ARG":0,"VAR":0}
        
        self.classTable = dict()
        self.methodTable = dict()
        self.methodsHistoryTables = []
    
    def __str__(self):
        
        myrepr = ("____________________________ CLASS TABLE _____________________________\n")
        for name ,value in self.classTable.items():
            myrepr += ("______________________________________________________________________\n")
            myrepr += ("Name : {} ".format(name) + str(value) +"\n")
            myrepr += ("______________________________________________________________________\n")
            
        myrepr += ("**********************************************************************\n\n")
        
        myrepr += ("___________________________ Method Table _____________________________\n")
        for name ,value in self.methodTable.items():
            myrepr += ("______________________________________________________________________\n")
            myrepr += ("Name : {} ".format(name) + str(value) +"\n")
            myrepr += ("______________________________________________________________________\n")
        myrepr += ("**********************************************************************\n\n")   
        
        return myrepr
    
    def startSubroutine(self):
        '''
        (None) ---> None
        Starts a new subroutine scope (i.e., rests the subroutine's symbol table, while keeping the class symbol table)
        '''
        
        #Rest count for arguments and var
        if self.debug : print("Starting a new subroutine Table")
        self.kindsCount["ARG"] = 0
        self.kindsCount["VAR"] = 0
        
        #Deleting current table and resting the new one to an empty dict
        self.methodsHistoryTables.append(self.methodTable)
        self.methodTable = dict()
        
    def define(self,Name,Type,Kind):
        '''
        (str name,str ttype, str kind) ---> None
        kind : STATIC,FIELD,ARG,VAR
        Defines a new identifier of a given name,type, and kind and assigns it a running index.
        STATIC and FIELD identifiers have a class scope,while ARG and VAR identifiers have a subrtouine scope
        '''
        if self.debug: print("\nDefining a new variable: Name = {} ::: Type = {} ::: Kind = {}:".format(Name,Type,Kind))
        #if the new variable is in a class scope, add that var to the class symbol Table
        if Kind in {"STATIC","FIELD"}:
            if self.debug: print("New variable is in a class scope")
            self.classTable[Name] = {"Type":Type,"Kind" : Kind,"Index" : self.kindsCount[Kind]}
            self.kindsCount[Kind] += 1
            
        #if the new variable is in a method scope, add that variable to the method symbole table
        elif Kind in {"VAR","ARG"}:
            if self.debug: print("New variable is in a method scope ")
            self.methodTable[Name] = {"Type" : Type,"Kind" : Kind,"Index" : self.kindsCount[Kind]}
            self.kindsCount[Kind] += 1
        else:
            raise SyntaxError("Undefined variable:",Name,Type,Kind)
    
    def varCount(self,Kind):
        '''
        (str kind) --> int count
        kind: STATIC,FIELD,ARG or VAR
        Returns the number of variables of the given kind already defined in the current scope.
        '''
        #the most compact way to check all kinds
        if self.debug: print("\nChecking count of {} variable ".format(Kind))
        count = self.kindsCount.get(Kind,self.kindsCount.get(Kind))
        
        if self.debug: print("var Count returns: Kind = {} ::: count = {}".format(Kind,count))
        
        return count
        
    def kindOf(self,name):
        '''
        (str name) --> kind
        kind: STATIC,FIELD,ARG,VAR,NONE
        Returns the kind of the named identifier in the current scope. If the identifier is unknown in the current scope, returns NONE
        '''
        if name in self.methodTable:
            if self.debug: print("\nThe identifier: {} found in Method Table".format(name))
            return (self.methodTable[name]).get("Kind")
        
        elif name in self.classTable:
            if self.debug: print("\nThe identifier: {} found in Class Table".format(name))
            return (self.classTable[name]).get("Kind")
        
        else:
            if self.debug: print("\nThe identifier: {} is NONE".format(name))
            return "NONE"
    
    def typeOf(self,name):
        '''
        (str name) --> str type
        Returns the type of the named identifier in the current scope.
        '''
        if name in self.methodTable:
            if self.debug: print("\nThe identifier: {} found in Method Table".format(name))
            return (self.methodTable[name]).get("Type")
        
        elif name in self.classTable:
            if self.debug: print("\nThe identifier: {} found in Class Table".format(name))
            return (self.classTable[name]).get("Type")
        
        else:
            raise TypeError("Unknown Type of identifier : " + str(name))
    
    def indexOf(self,name):
        '''
        (str name) --> int index
        returns the index assigned to the named identifier
        '''
        if name in self.methodTable:
            if self.debug: print("\nThe identifier: {} found in Method Table".format(name))
            return (self.methodTable[name]).get("Index")
        
        elif name in self.classTable:
            if self.debug: print("\nThe identifier: {} found in Class Table".format(name))
            return (self.classTable[name]).get("Index")
        else:
            raise TypeError("Unknown Index of identifier " + str(name))
               
    
if __name__ == "__main__":
    

    
        #Testing Define method
        table = symbolTable()
        table.define("id","int","STATIC")
        table.define("owner","String","FIELD")
        table.define("this","bankAcount","ARG")
        table.define("sum","int","VAR")
        table.define("when","Date","ARG")
        table.define("i","int","VAR")
        table.define("j","int","VAR")
        
        print("**************Class table***************")
        for k,v in table.classTable.items():
            print(k,v)
        
        
        print("\n************Method Table***************")
        for k,v in table.methodTable.items():
            print(k,v)

        
        table.startSubroutine()
        
        print("\n NEW Subroutine..................................................")
        print("************Method Table***************")
        for k,v in table.methodTable.items():
            print(k,v)
        
        table.define("this","bankAcount","ARG")
        table.define("sumNew","int","VAR")
        table.define("whenNew","Date","ARG")
        table.define("jNew","int","VAR")
        table.define("iNew","int","VAR")

        
        print("\n Updated NEW Subroutine..................................................")
        print("************Method Table***************")
        for k,v in table.methodTable.items():
            print(k,v)
        
            
        table.startSubroutine()
        table.define("this","bankAcount","ARG")
        table.define("sum","int","VAR")
        table.define("when","Date","ARG")
        table.define("i","int","VAR")
        table.define("j","int","VAR")
        
        
        #Testing varCount, kindOf, typeOf and indexOF
        #varCount
        print("Number of STATIC variables: ",table.varCount("STATIC"))
        print("Number of FIELD variables: ",table.varCount("FIELD"))
        print("Number of ARG variables: ",table.varCount("ARG"))
        print("Number of VAR variables: ",table.varCount("VAR"))
        
        #kindOf
        print("The kind of 'id' is : ",table.kindOf("id"))
        print("The kind of 'owner' : ",table.kindOf("owner"))
        print("The kind of 'this' : ",table.kindOf("this"))
        print("The kind of 'sum': ",table.kindOf("sum"))
        print("The kind of 'when': ",table.kindOf("when"))
        print("the kind of 'i': ",table.kindOf("i"))
        print("the kind of 'j': ",table.kindOf("j"))
        print("The kind of 'notKnown' : ",table.kindOf("notKnown"))
        
        #Typeof 
        print("The Type of 'id' is : ",table.typeOf("id"))
        print("The Type 'owner' : ",table.typeOf("owner"))
        print("The Type of 'this' : ",table.typeOf("this"))
        print("The Type of 'sum': ",table.typeOf("sum"))
        print("The Type of 'when': ",table.typeOf("when"))
        print("the Type of 'i': ",table.typeOf("i"))
        print("the Type of 'j': ",table.typeOf("j"))
        #print("The kind of 'notKnown' : ",table.typeOf("notKnown"))
        
        #indexOf
        print("The Index of 'id' is : ",table.indexOf("id"))
        print("The Index 'owner' : ",table.indexOf("owner"))
        print("The Index of 'this' : ",table.indexOf("this"))
        print("The Index of 'sum': ",table.indexOf("sum"))
        print("The Index of 'when': ",table.indexOf("when"))
        print("the Index of 'i': ",table.indexOf("i"))
        print("the Index of 'j': ",table.indexOf("j"))
        #print("The kind of 'notKnown' : ",table.typeOf("notKnown"))
        
        
        print(table)
        
        
        