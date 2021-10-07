package main

import (
	"fmt"
)

func linear_search(list_value []int, key int) bool {
	for _, item := range list_value {
		if item == key {
			return true
		}
	}
	return false
}

func main() {
	items := []int{234, 56, 85678, 345, 335, 22, 77, 89, 567, 34, 1, 45, 789, 567, 35}
	fmt.Println(linear_search(items, 77))
}
