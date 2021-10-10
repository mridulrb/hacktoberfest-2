object arraySum{
  def main(args:Array[String]): Unit ={
    var myList = Array(1,3,5,9)
    var sum = 0
    // Calculating sum of array elements
      for ( i <- myList ) {
         sum = sum + i
      }
      println("Sum="+sum)
    }
}