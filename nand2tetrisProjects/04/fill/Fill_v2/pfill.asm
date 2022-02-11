// Author: invoker999
// Course: OSSU/nand2tetris
// Email: kaced.sofiane@gmail.com

//init constants
	WHITE = 0
	Black = 255
	NUMPIX = 8192

(LOOP)
	i = 0

(REFILL)
	if i - NUMPIX == 0 goto LOOP:
		
		if KBD == 0 then:
			fillColor = WHITE
		else:
			fillColor = BLACK

		
		M[SCREEN + i] = fillColor

		i = i+1

		goto REFILL


			
