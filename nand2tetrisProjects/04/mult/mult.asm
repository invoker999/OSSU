// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
// RO = num0
// R1 = num1
// sum = 0  // to be moved to R2 at the end
// i = 1
// do (LOOP)
//    D = num1
//    sum = sum + D
//    i = i+1
//while(i - num0 != 0)
//do (END)
//while(TRUE)

//Start of program:
     // init
        @R2   
        M = 0  //init sum = 0
        @i
        M = 0  // init i = 1
	
	@R0
	D = M
	@END
	D;JLE   //Checking that num0 is greater than 0 or else just end as 0 x N = 0
(LOOP)
        @R1    //load num1 to be added
	D = M  //stor it in D
	@R2 
	M = M + D // M[R2] = M[R2] + num1  == sum = sum + num1
	@i
	M = M + 1 // i++
	@R0    
	D = M 
	@i
	D = D - M  // compute num0 - i
	@LOOP
	D;JGT  //JUMP to LOOP if i<num0
(END)
	@END
	0;JMP

