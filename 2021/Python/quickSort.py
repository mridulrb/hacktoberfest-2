def partition( start, end, array ):
    '''
    This function handles sorting part of quick sort. Set start and
    end points to first and last element of an array respectively.
    '''
    # Initializing pivot's index to start
    pivotIndex = start
    pivotElem = array[ start ]
    
    # This loop runs till start pointer crosses end pointer, and when it 
    # does we swap the pivot with element on end pointer
    while start < end:
        
        # Increment the start pointer till it finds an 
        # element greater than  pivot element
        while start < len( array ) and array[ start ] <= pivotElem:
            start += 1
        # Decrement the end pointer till it finds an 
        # element less than pivot element.
        while array[ end ] > pivotElem:
            end -= 1
        # If start and end indices have not crossed each other, 
        # swap the numbers on start and end.
        if( start < end ):
            array[ start ], array[ end ] = array[ end ], array[ start ]
    # Swap the pivot element with element on end pointer.
    # This puts the pivot element in its correct sorted place.
    array[ end ], array[ pivotIndex ] = array[ pivotIndex ], array[ end ]
    return end

def quickSort( start, end, array ):
    '''
    This is the main recursive function that implements the quickSort.
    It finds the partition index, and recursively sorts before the 
    partitioning index and after the partitioning index. In each
    iteration it ensures that element at the partitioning index is
    at the right index.
    '''
    if( start < end ):
        # pi is the partitioning index. After each iteration of the
        # sort method, we guarantee that array[ pi ] is at the right
        # position.
        pi = partition( start, end, array )
        
        # Sort elements before and after partition index
        quickSort( start, pi-1, array )
        quickSort( pi+1, end, array )
        
array = []
length = int( input( "Enter length of array: " ) )
for idx in range( length ):
    x = int( input( "Numbers: " ) )
    array.append( x )

print( "Before Sorting: " )
print( array )
# Call quickSort method
quickSort( 0, length-1, array )
print( "After Sorting: " )
print( array )
