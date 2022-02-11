//PUSH_CONSTANT_START 
@0 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_LCL_START 
@0 
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
($LOOP_START) 
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
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M + D 
//ADDorSUB_END 
//POP_LCL_START 
@0 
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
//POP_ARG_START 
@0 
D = A 
@ARG 
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
//POP_ARG_END 
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
//GOTO_IF_START 
@SP 
M = M - 1 
A = M 
D = M 
@$LOOP_START 
D;JNE 
//GOTO_END 
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
