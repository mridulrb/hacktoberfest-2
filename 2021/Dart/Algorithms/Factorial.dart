import 'dart:io';
import 'dart:core';

BigInt factorial(BigInt n) {
  BigInt product = BigInt.from(1);
  for (BigInt i = BigInt.from(1); i <= n; i += BigInt.from(1)) product *= i;
  return product;
}

void main() {
  stdout.write('Enter a number to find factorial: ');
  BigInt? n = BigInt.parse(stdin.readLineSync()!);
  stdout.write('$n! = ${factorial(n)}');
}
