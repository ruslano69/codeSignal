int rangeBitCount(int a, int b) {
	int counter = 0;
	for(int i = a; i < b; i++){
		for(int j = 0; j < 3; j++){
			if( i>> j & 1 == 1){
				counter++;
			}
		}
	}
	return counter;
}
