// program to find the implement staircase of n ladders

// take input from the user
const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  
  readline.question("Enter an multiple numbers separated by comma. ex: 1,2,3,4: ", (numbers) => {
    const numbersArray = numbers.split(',').map(Number)
  
    let arraySum =  0
    for(let index = 0; index <= numbersArray.length - 1; index +=1) {
        arraySum += numbersArray[index]
    }

    console.log(`Sum of values: ${arraySum}`);

    readline.close();
  });
  