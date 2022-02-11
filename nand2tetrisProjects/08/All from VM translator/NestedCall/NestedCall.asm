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
@4000 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_THIS_START 
@SP 
M = M - 1 
A = M 
D = M 
@THIS 
M = D 
//POP_THIS_END 
//PUSH_CONSTANT_START 
@5000 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_THAT_START 
@SP 
M = M - 1 
A = M 
D = M 
@THAT 
M = D 
//POP_THAT_END 
//Call_Sys.main 
@Sys.main$ret.0
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
@Sys.main 
0;JMP 
(Sys.main$ret.0) 
//CALL_END_Sys.main
//POP_5_START 
@1 
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
(Sys.init$LOOP) 
@Sys.init$LOOP 
0;JMP 
//Code_Sys.main
(Sys.main) 
@5 
D = A+1 
(Sys.main$__K) 
@Sys.main$__S 
D = D - 1 
D;JEQ 
@SP 
M = M + 1 
A = M - 1 
M = 0 
@Sys.main$__K 
0;JMP 
(Sys.main$__S)
//END_INIT_Sys.main 
//PUSH_CONSTANT_START 
@4001 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_THIS_START 
@SP 
M = M - 1 
A = M 
D = M 
@THIS 
M = D 
//POP_THIS_END 
//PUSH_CONSTANT_START 
@5001 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_THAT_START 
@SP 
M = M - 1 
A = M 
D = M 
@THAT 
M = D 
//POP_THAT_END 
//PUSH_CONSTANT_START 
@200 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_LCL_START 
@1 
D = A 
@LCL 
D = D + M 
@R13 
M = D 
@SP 
M = M - 1 
A = M 
D = M 
@R13 
A = M 
M = D 
//POP_LCL_END 
//PUSH_CONSTANT_START 
@40 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_LCL_START 
@2 
D = A 
@LCL 
D = D + M 
@R13 
M = D 
@SP 
M = M - 1 
A = M 
D = M 
@R13 
A = M 
M = D 
//POP_LCL_END 
//PUSH_CONSTANT_START 
@6 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_LCL_START 
@3 
D = A 
@LCL 
D = D + M 
@R13 
M = D 
@SP 
M = M - 1 
A = M 
D = M 
@R13 
A = M 
M = D 
//POP_LCL_END 
//PUSH_CONSTANT_START 
@123 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//Call_Sys.add12 
@Sys.add12$ret.0
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
@Sys.add12 
0;JMP 
(Sys.add12$ret.0) 
//CALL_END_Sys.add12
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
//PUSH_LCL_START 
@0 
D = A 
@LCL 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_LCL_END 
//PUSH_LCL_START 
@1 
D = A 
@LCL 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_LCL_END 
//PUSH_LCL_START 
@2 
D = A 
@LCL 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_LCL_END 
//PUSH_LCL_START 
@3 
D = A 
@LCL 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_LCL_END 
//PUSH_LCL_START 
@4 
D = A 
@LCL 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_LCL_END 
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M + D 
//ADDorSUB_END 
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M + D 
//ADDorSUB_END 
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M + D 
//ADDorSUB_END 
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M + D 
//ADDorSUB_END 
//Return_Sys.main_start 
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
//END_Retrun_Sys.main
//Code_Sys.add12
(Sys.add12) 
@0 
D = A+1 
(Sys.add12$__K) 
@Sys.add12$__S 
D = D - 1 
D;JEQ 
@SP 
M = M + 1 
A = M - 1 
M = 0 
@Sys.add12$__K 
0;JMP 
(Sys.add12$__S)
//END_INIT_Sys.add12 
//PUSH_CONSTANT_START 
@4002 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_THIS_START 
@SP 
M = M - 1 
A = M 
D = M 
@THIS 
M = D 
//POP_THIS_END 
//PUSH_CONSTANT_START 
@5002 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_THAT_START 
@SP 
M = M - 1 
A = M 
D = M 
@THAT 
M = D 
//POP_THAT_END 
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
@12 
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
M = M + D 
//ADDorSUB_END 
//Return_Sys.add12_start 
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
//END_Retrun_Sys.add12
