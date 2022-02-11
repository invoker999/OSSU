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
@4 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//Call_Main.fibonacci 
@Main.fibonacci$ret.0
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
@1 
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
@Main.fibonacci 
0;JMP 
(Main.fibonacci$ret.0) 
//CALL_END_Main.fibonacci
(Sys.init$WHILE) 
@Sys.init$WHILE 
0;JMP 
//Code_Main.fibonacci
(Main.fibonacci) 
@0 
D = A+1 
(Main.fibonacci$__K) 
@Main.fibonacci$__S 
D = D - 1 
D;JEQ 
@SP 
M = M + 1 
A = M - 1 
M = 0 
@Main.fibonacci$__K 
0;JMP 
(Main.fibonacci$__S)
//END_INIT_Main.fibonacci 
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
//PUSH_CONSTANT_START 
@2 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//EQorGTorLT_START 
@SP 
M = M - 1 
A = M - 1 
D = M 
M = 0 
A = A + 1 
D = D - M 
@LT_TRUE__0 
D;JLT 
@END_LT__0 
0;JMP 
(LT_TRUE__0) 
@SP 
A = M - 1 
M = -1 
(END_LT__0) 
//EQorGTorLT_END 
//GOTO_IF_START 
@SP 
M = M - 1 
A = M 
D = M 
@Main.fibonacci$IF_TRUE 
D;JNE 
//GOTO_END 
@Main.fibonacci$IF_FALSE 
0;JMP 
(Main.fibonacci$IF_TRUE) 
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
//Return_Main.fibonacci_start 
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
//END_Retrun_Main.fibonacci
(Main.fibonacci$IF_FALSE) 
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
//PUSH_CONSTANT_START 
@2 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M - D 
//ADDorSUB_END 
//Call_Main.fibonacci 
@Main.fibonacci$ret.1
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
@1 
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
@Main.fibonacci 
0;JMP 
(Main.fibonacci$ret.1) 
//CALL_END_Main.fibonacci
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
//PUSH_CONSTANT_START 
@1 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M - D 
//ADDorSUB_END 
//Call_Main.fibonacci 
@Main.fibonacci$ret.2
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
@1 
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
@Main.fibonacci 
0;JMP 
(Main.fibonacci$ret.2) 
//CALL_END_Main.fibonacci
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M + D 
//ADDorSUB_END 
//Return_Main.fibonacci_start 
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
//END_Retrun_Main.fibonacci
