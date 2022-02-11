//Code_SimpleFunction.test
(SimpleFunction.test) 
@2 
D = A+1 
(SimpleFunction.test$__K) 
@SimpleFunction.test$__S 
D = D - 1 
D;JEQ 
@SP 
M = M + 1 
A = M - 1 
M = 0 
@SimpleFunction.test$__K 
0;JMP 
(SimpleFunction.test$__S)
//END_INIT_SimpleFunction.test 
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
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M + D 
//ADDorSUB_END 
//NEGorNOT_START 
@SP 
A = M - 1 
M = !M 
//NEGorNOT_END 
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
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M + D 
//ADDorSUB_END 
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
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M - D 
//ADDorSUB_END 
//Return_SimpleFunction.test_start 
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
//END_Retrun_SimpleFunction.test
