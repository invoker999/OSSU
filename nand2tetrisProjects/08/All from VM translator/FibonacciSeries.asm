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
//POP_THAT_START 
@SP 
M = M - 1 
A = M 
D = M 
@THAT 
M = D 
//POP_THAT_END 
//PUSH_CONSTANT_START 
@0 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_THAT_START 
@0 
D = A 
@THAT 
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
//POP_THAT_END 
//PUSH_CONSTANT_START 
@1 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_THAT_START 
@1 
D = A 
@THAT 
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
($MAIN_LOOP_START) 
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
@$COMPUTE_ELEMENT 
D;JNE 
//GOTO_END 
@$END_PROGRAM 
0;JMP 
($COMPUTE_ELEMENT) 
//PUSH_THAT_START 
@0 
D = A 
@THAT 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_THAT_END 
//PUSH_THAT_START 
@1 
D = A 
@THAT 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_THAT_END 
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M + D 
//ADDorSUB_END 
//POP_THAT_START 
@2 
D = A 
@THAT 
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
//POP_THAT_END 
//PUSH_THAT_START 
@THAT 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_THAT_END 
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
M = M + D 
//ADDorSUB_END 
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
@$MAIN_LOOP_START 
0;JMP 
($END_PROGRAM) 
