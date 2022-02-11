//Bootstrap_CODE 
@256 
D = A 
@SP 
M = D 
//Call_Sys.init 
@Sys.init$ret.0
D = A 
@SP 
M = M+1 
A = M-1 
M = D 
@LCL 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@ARG 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@THIS 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@THAT 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@0 
D = A 
@5 
D = D + A 
@SP 
D = M - D 
@ARG 
M = D 
@SP 
D = M 
@LCL 
M = D 
@Sys.init 
0;JMP 
(Sys.init$ret.0) 
//CALL_END_Sys.init
//Code_Sys.init
(Sys.init) 
@0 
D = A+1 
(Sys.init$__K) 
@Sys.init$__S 
D = D - 1 
D;JEQ 
@SP 
M = M + 1 
A = M - 1 
M = 0 
@Sys.init$__K 
0;JMP 
(Sys.init$__S)
//END_INIT_Sys.init 
//PUSH_CONSTANT_START 
@6 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//PUSH_CONSTANT_START 
@8 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//Call_Class1.set 
@Class1.set$ret.0
D = A 
@SP 
M = M+1 
A = M-1 
M = D 
@LCL 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@ARG 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@THIS 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@THAT 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@2 
D = A 
@5 
D = D + A 
@SP 
D = M - D 
@ARG 
M = D 
@SP 
D = M 
@LCL 
M = D 
@Class1.set 
0;JMP 
(Class1.set$ret.0) 
//CALL_END_Class1.set
//POP_5_START 
@0 
D = A 
@5 
D = D + A 
@R13 
M = D 
@SP 
M = M - 1 
A = M 
D = M 
@R13 
A = M 
M = D 
//POP_5_END 
//PUSH_CONSTANT_START 
@23 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//PUSH_CONSTANT_START 
@15 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//Call_Class2.set 
@Class2.set$ret.0
D = A 
@SP 
M = M+1 
A = M-1 
M = D 
@LCL 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@ARG 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@THIS 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@THAT 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@2 
D = A 
@5 
D = D + A 
@SP 
D = M - D 
@ARG 
M = D 
@SP 
D = M 
@LCL 
M = D 
@Class2.set 
0;JMP 
(Class2.set$ret.0) 
//CALL_END_Class2.set
//POP_5_START 
@0 
D = A 
@5 
D = D + A 
@R13 
M = D 
@SP 
M = M - 1 
A = M 
D = M 
@R13 
A = M 
M = D 
//POP_5_END 
//Call_Class1.get 
@Class1.get$ret.0
D = A 
@SP 
M = M+1 
A = M-1 
M = D 
@LCL 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@ARG 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@THIS 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@THAT 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@0 
D = A 
@5 
D = D + A 
@SP 
D = M - D 
@ARG 
M = D 
@SP 
D = M 
@LCL 
M = D 
@Class1.get 
0;JMP 
(Class1.get$ret.0) 
//CALL_END_Class1.get
//Call_Class2.get 
@Class2.get$ret.0
D = A 
@SP 
M = M+1 
A = M-1 
M = D 
@LCL 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@ARG 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@THIS 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@THAT 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
@0 
D = A 
@5 
D = D + A 
@SP 
D = M - D 
@ARG 
M = D 
@SP 
D = M 
@LCL 
M = D 
@Class2.get 
0;JMP 
(Class2.get$ret.0) 
//CALL_END_Class2.get
(Sys.init$WHILE) 
@Sys.init$WHILE 
0;JMP 
//Code_Class1.set
(Class1.set) 
@0 
D = A+1 
(Class1.set$__K) 
@Class1.set$__S 
D = D - 1 
D;JEQ 
@SP 
M = M + 1 
A = M - 1 
M = 0 
@Class1.set$__K 
0;JMP 
(Class1.set$__S)
//END_INIT_Class1.set 
//PUSH_ARG_START 
@0 
D = A 
@ARG 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_ARG_END 
//PUSH_STATIC_START 
@SP 
M = M - 1 
A = M 
D = M 
@Class1.0 
M = D 
//PUSH_ARG_START 
@1 
D = A 
@ARG 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_ARG_END 
//PUSH_STATIC_START 
@SP 
M = M - 1 
A = M 
D = M 
@Class1.1 
M = D 
//PUSH_CONSTANT_START 
@0 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//Return_Class1.set_start 
@LCL 
 D = M 
@R11 
M = D 
@5 
A = D - A 
D = M 
@R12 
M = D 
@SP 
M = M - 1 
A = M 
D = M 
@ARG 
A = M 
M = D 
@ARG 
D = M + 1 
@SP 
M = D 
@R11 
M = M - 1 
A = M 
D = M 
@THAT 
M = D 
@R11 
M = M - 1
A = M 
D = M 
@THIS 
M = D 
@R11 
M = M -1 
A = M 
D = M 
@ARG 
M = D 
@R11 
M = M - 1 
A = M 
D = M 
@LCL 
M = D 
@R12 
A = M 
0;JMP 
//END_Retrun_Class1.set
//Code_Class1.get
(Class1.get) 
@0 
D = A+1 
(Class1.get$__K) 
@Class1.get$__S 
D = D - 1 
D;JEQ 
@SP 
M = M + 1 
A = M - 1 
M = 0 
@Class1.get$__K 
0;JMP 
(Class1.get$__S)
//END_INIT_Class1.get 
//PUSH_STATIC_START 
@Class1.0 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_STATIC_START 
@Class1.1 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M - D 
//ADDorSUB_END 
//Return_Class1.get_start 
@LCL 
 D = M 
@R11 
M = D 
@5 
A = D - A 
D = M 
@R12 
M = D 
@SP 
M = M - 1 
A = M 
D = M 
@ARG 
A = M 
M = D 
@ARG 
D = M + 1 
@SP 
M = D 
@R11 
M = M - 1 
A = M 
D = M 
@THAT 
M = D 
@R11 
M = M - 1
A = M 
D = M 
@THIS 
M = D 
@R11 
M = M -1 
A = M 
D = M 
@ARG 
M = D 
@R11 
M = M - 1 
A = M 
D = M 
@LCL 
M = D 
@R12 
A = M 
0;JMP 
//END_Retrun_Class1.get
//Code_Class2.set
(Class2.set) 
@0 
D = A+1 
(Class2.set$__K) 
@Class2.set$__S 
D = D - 1 
D;JEQ 
@SP 
M = M + 1 
A = M - 1 
M = 0 
@Class2.set$__K 
0;JMP 
(Class2.set$__S)
//END_INIT_Class2.set 
//PUSH_ARG_START 
@0 
D = A 
@ARG 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_ARG_END 
//PUSH_STATIC_START 
@SP 
M = M - 1 
A = M 
D = M 
@Class2.0 
M = D 
//PUSH_ARG_START 
@1 
D = A 
@ARG 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_ARG_END 
//PUSH_STATIC_START 
@SP 
M = M - 1 
A = M 
D = M 
@Class2.1 
M = D 
//PUSH_CONSTANT_START 
@0 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//Return_Class2.set_start 
@LCL 
 D = M 
@R11 
M = D 
@5 
A = D - A 
D = M 
@R12 
M = D 
@SP 
M = M - 1 
A = M 
D = M 
@ARG 
A = M 
M = D 
@ARG 
D = M + 1 
@SP 
M = D 
@R11 
M = M - 1 
A = M 
D = M 
@THAT 
M = D 
@R11 
M = M - 1
A = M 
D = M 
@THIS 
M = D 
@R11 
M = M -1 
A = M 
D = M 
@ARG 
M = D 
@R11 
M = M - 1 
A = M 
D = M 
@LCL 
M = D 
@R12 
A = M 
0;JMP 
//END_Retrun_Class2.set
//Code_Class2.get
(Class2.get) 
@0 
D = A+1 
(Class2.get$__K) 
@Class2.get$__S 
D = D - 1 
D;JEQ 
@SP 
M = M + 1 
A = M - 1 
M = 0 
@Class2.get$__K 
0;JMP 
(Class2.get$__S)
//END_INIT_Class2.get 
//PUSH_STATIC_START 
@Class2.0 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_STATIC_START 
@Class2.1 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M - D 
//ADDorSUB_END 
//Return_Class2.get_start 
@LCL 
 D = M 
@R11 
M = D 
@5 
A = D - A 
D = M 
@R12 
M = D 
@SP 
M = M - 1 
A = M 
D = M 
@ARG 
A = M 
M = D 
@ARG 
D = M + 1 
@SP 
M = D 
@R11 
M = M - 1 
A = M 
D = M 
@THAT 
M = D 
@R11 
M = M - 1
A = M 
D = M 
@THIS 
M = D 
@R11 
M = M -1 
A = M 
D = M 
@ARG 
M = D 
@R11 
M = M - 1 
A = M 
D = M 
@LCL 
M = D 
@R12 
A = M 
0;JMP 
//END_Retrun_Class2.get
