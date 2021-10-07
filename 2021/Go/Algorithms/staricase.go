package main

import "fmt"

func main() {
  var height int
  fmt.Scan(&height)
  
  var stair int = height - 1; 

  for i:= 0; i <height; i++ {
  for j:= 0; j <height; j++ {
    if(j >= stair) {
      fmt.Print("#") 
    } else  {
      fmt.Print(" ")  }
      
  } 
    stair = stair - 1 
    fmt.Print("\n")
  }


}
