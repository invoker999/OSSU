//PUSH_START 
@7 
D = A 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
//PUSH_END 
//PUSH_START 
@8 
D = A 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
//PUSH_END 
//ADDorSUB_START 
@SP 
A = M - 1 
D = M 
A = A - 1 
M = M + D 
A = A + 1 
D = A 
@SP 
M = D 
//ADDorSUB_END 
