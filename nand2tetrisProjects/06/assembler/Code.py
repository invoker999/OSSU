# Author: invoker999
# Course: OSSU/nand2tetris
# Email: kaced.sofiane@gmail.com


class Code():
    
    DEST = {"null":"000","M":"001","D":"010","MD":"011","A":"100","AM":"101","AD":"110","AMD":"111"}
    
    COMP = {"0":"0101010","1":"0111111","-1":"0111010","D":"0001100","A":"0110000","!D":"0001101"
            ,"!A":"0110001","-D":"0001111","-A":"0110011","D+1":"0011111","A+1":"0110111","D-1":"0001110"
            ,"A-1":"0110010","D+A":"0000010","D-A":"0010011","A-D":"0000111","D&A":"0000000","D|A":"0010101"
            ,"M":"1110000","!M":"1110001","-M":"1110011","M+1":"1110111","M-1":"1110010","D+M":"1000010"
            ,"D-M":"1010011","M-D":"1000111","D&M":"1000000","D|M":"1010101"}
    
    JUMP = {"null":"000","JGT":"001","JEQ":"010","JGE":"011","JLT":"100","JNE":"101","JLE":"110","JMP":"111"}

    @classmethod
    def dest(cls,strDest):
        """
            strDest ==> string represting DEST filed of a C command
            output  ==> string "bbb"(3bits) the Hack machine translation

        """
        #Find the strDest representation from a dict DEST
        #return the representation
        #raise Translation error Exception if not found
        trans = cls.DEST.get(strDest,None)
        if trans == None:
            raise Exception("Machine Code not found for Dest = "+strDest)
        else:
            return trans

    @classmethod
    def comp(cls,strComp):
        """
            strComp ==> string represting COMP filed of a C command
            output  ==> string "bbbbbbb"(7bits) the Hack machine translation

        """
        #Find the strcomp representation from a dict COMP
        #return the representation
        #raise Translation error Exception if not found
        trans = cls.COMP.get(strComp,None)
        if trans == None :
            raise Exception("Machine Code not found for Comp = "+strComp)
        else:
            return trans
        
    @classmethod
    def jump(cls,strJump):
        """
            strJUMP ==> string represting JUMP filed of a C command
            output  ==> string "bbb"(3bits) the Hack machine translation

        """
        #Find the strJump representation from a dict JUMP
        #return the representation
        #raise Translation error Exception if not found
        trans = cls.JUMP.get(strJump,None)
        if trans == None:
            raise Exception("Machine Code not found for Jump = "+strJump)
        else:
            return trans
    












    
