function printStaircase(num) {
	let stairs = '';

	let i = 0;
	while (i < num) {
		stairs += '#';
		console.log(stairs.padStart(num, ' '));
		i++;
	}
}

printStaircase(4);
