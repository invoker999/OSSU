//The first program was not elgant so making a second version

// C instructions des = comp; jump

// A instruction @Value   A = Value

	@WHITE
	M = 0    // WHITE = 0  Saving White color code in a CONSTANT "WHITE"

	@255
	D = A
	@BLACK   // BLACK/WHITE = 255 = ~(111111110000000) :  Saving White/Black color patern code in a CONSTANT "BLACK"
	M = D

	@8192
	D = A
	@NUMPIX //Saving the MAX number of avialble Pixels
	M = D
	@pix
	M = 0   // init pix pointer to Zero

(LOOP)         // init i counter to 0 when whole screen was filled	

	@i
	M = 0

(FILL)       // Filling the screen word by word from 0 to the MAX number of Pixels 
	@i
	D = M
	@NUMPIX
	D = M - D  // NUMPIX - i
	@LOOP
	D;JLE     //jump to LOOP if i => 8192
	
	@WHITE
	D = M 
	@fillColor
	M = D
	@KBD
	D = M
	@NOPRESS
	D;JEQ     // jump to NOPRESS if KBD = 0  & Keep fillColor = WHITE
	@BLACK
	D = M
	@fillColor
	M = D     // Else set fillColor to BLACK

(NOPRESS)

	@SCREEN
	D = A
	@i
	D = D + M
	@pix      //Save pointer to current pix = [SCREEN + i ] 
	M = D
	@fillColor
	D = M
	@pix
	A = M
	M = D    // M[pix] = M[SCREEN + i] = fillColor
	@i
	M = M + 1
	@FILL
	0;JMP
	
	
	










