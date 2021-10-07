package main

import "fmt"

const max = 100
var fibonacci [max]int

func preCalculateFibonacci(n int) int{
	if n <= 1{
		fibonacci[n] = n
		return fibonacci[n]
	}
	if fibonacci[n] != -1{
		return fibonacci[n]
	}
	fibonacci[n] = preCalculateFibonacci(n-1) + preCalculateFibonacci(n-2)
	return fibonacci[n]
}

func setArray(){
	for i:= 0; i < max; i++ {
		fibonacci[i] = -1
	}
}
func main(){
	setArray()
	preCalculateFibonacci(max-1)
	for i :=0; i< 20; i++{
		fmt.Printf("%d ", fibonacci[i])
	}
}