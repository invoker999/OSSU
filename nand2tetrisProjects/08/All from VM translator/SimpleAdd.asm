//PUSH_CONSTANT_START 
@7 
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
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M + D 
//ADDorSUB_END 
