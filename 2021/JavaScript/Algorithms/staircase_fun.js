// function to print staircase 

// take input from the user
const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  readline.question("Enter a positive integer: ", (int) => {
    const n = parseInt(int);

    for(let i = 0; i < n; i++){
        // Clear the output after each loop
        let output = '';
        for(let j = 0; j < n; j++){
          // Loop through, whenever (n-1-i) is bigger than j concat a space else #
           j < (n -1 -i) ? output += ' ': output += '#';
        }
        console.log(output);
    }
    readline.close();
  });
