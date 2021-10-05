// program to find the implement staircase of n ladders

// take input from the user
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question("Enter a positive integer: ", (num) => {
  const n = parseInt(num);

  for (let i = 0; i < n; i++) {
    var s = "";
    for (let j = 0; j < n - i - 1; j++) s = s + " ";
    for (let j = n - i - 1; j < n; j++) s = s + "#";
    console.log(s);
  }
  readline.close();
});
