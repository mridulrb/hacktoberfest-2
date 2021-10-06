package commonElementsInTwoSets;

public class CommonElementsInTwoSets {
    int binarySearch(int element){
      int setA[] = {12,34,11,9,3};
      
        
       int temp;
       for (int i = 0; i < setA.length; i++) {
            for (int j = i; j > 0; j--) {
                if (setA[j] < setA[j - 1]) {
                    temp = setA[j];
                    setA[j] = setA[j - 1];
                    setA[j - 1] = temp;
                }
            }
       }        
        int first=0;
        int last=setA.length-1;           
        while(last>=first){
            int mid=(first+last)/2;
            if(setA[mid]==element){
                return 1;
            }
            else if(setA[mid]>element){
                last=mid-1;
            }else{
                first=mid+1;
           }

       
    }
        return -1;
   }


   
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       Method3 bs=new Method3();
       int setB[] = {2,1,3,5};    
       int count=0;
	for (int i = 0; i < setB.length; i++){
		int c;
    c = bs.binarySearch(setB[i]);
		if(c==-1){
		
		}else{
			count++;
		}
	}
        
  if(count==1){
		System.out.println("Common element");
	}else{
		System.out.println("No common element");
	}
   
    }
}
