// Fill SCREEN of the HACK computer if KBD is pressed or clear it otherwise 

        @256
	D = A
	@R0        //number of rows
	M = D

	@32
	D = A
	@R1       //number of columns
	M = D

	@SCREEN
	D = M 
	@pix     //saving a pointer to a pix to be set while clearing and filling 
	M = D 
(LOOP)
	@SCREEN //init all needed variables
	D = A 
	@pix    //save witch pix to set to avoid multiplying
	M = D 

        @0
	D = A
        @row
	M = D

	@0
	D = A
	@col
	M = D
	
	@0
	D = A
	@color  //bit we are setting to 0 to clear
	M = D

	@KBD    //Checking KBD if pressed to set color to white(0) or black(-1)
	D = M 
	@FILL
        D;JEQ 
	@0
	D = A
	D = D - 1
        @color
	M = D 
(FILL)
  (ROW)        
        @0
	D = A
        @col   //resting col to 0 after each row
	M = D
	
	@row
	MD = M+1 
        @R0
	D = M - D
	@LOOP
	D;JLT
  (COL) 
  	@col
	MD = M + 1
	@R1
	D = M - D 
	@ROW
	D;JLT    //check if we finished writing current row
	@color
	D = M
	@pix    //load the address stored at pix to A
	A = M
        M = D
	@pix   //increment the address saved in pix by one
	M = M + 1
	@COL
	0;JMP

	
        	
	
