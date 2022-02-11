//PUSH_CONSTANT_START 
@111 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//PUSH_CONSTANT_START 
@333 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//PUSH_CONSTANT_START 
@888 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//PUSH_STATIC_START 
@SP 
M = M - 1 
A = M 
D = M 
@StaticTest.8 
M = D 
//PUSH_STATIC_START 
@SP 
M = M - 1 
A = M 
D = M 
@StaticTest.3 
M = D 
//PUSH_STATIC_START 
@SP 
M = M - 1 
A = M 
D = M 
@StaticTest.1 
M = D 
//PUSH_STATIC_START 
@StaticTest.3 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_STATIC_START 
@StaticTest.1 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//ADDorSUB_START 
@SP 
A = M - 1 
D = M 
A = A - 1 
M = M - D 
A = A + 1 
D = A 
@SP 
M = D 
//ADDorSUB_END 
//PUSH_STATIC_START 
@StaticTest.8 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
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
