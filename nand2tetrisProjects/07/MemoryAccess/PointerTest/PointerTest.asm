//PUSH_CONSTANT_START 
@3030 
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
@3040 
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
@32 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_THIS_START 
@2 
D = A 
@THIS 
D = D + M 
@SP 
A = M 
M = D 
@SP 
M = M - 1 
A = M 
D = M 
@SP 
A = M + 1 
A = M 
M = D 
//POP_THIS_END 
//PUSH_CONSTANT_START 
@46 
D = A 
@SP 
M = M + 1 
A = M -1 
M = D 
//PUSH_CONSTANT_END 
//POP_THAT_START 
@6 
D = A 
@THAT 
D = D + M 
@SP 
A = M 
M = D 
@SP 
M = M - 1 
A = M 
D = M 
@SP 
A = M + 1 
A = M 
M = D 
//POP_THAT_END 
//PUSH_THIS_START 
@THIS 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_THIS_END 
//PUSH_THAT_START 
@THAT 
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
//PUSH_THIS_START 
@2 
D = A 
@THIS 
A = D + M 
D = M 
@SP 
M = M + 1 
A = M - 1 
M = D 
//PUSH_THIS_END 
//ADDorSUB_START 
@SP 
M = M - 1 
A = M 
D = M 
A = A - 1 
M = M - D 
//ADDorSUB_END 
//PUSH_THAT_START 
@6 
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
