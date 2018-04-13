public class ReverseInt {
	public int reverseInt(int n){
    int result = 0;
    int []arr = new int[10];
    while(n > 0){
      arr[n%10]++;
      n /= 10;
    }
    for(int i = 9; i>=0; i--){
    	for(int j = 0; j<arr[i]; j++){
        if(arr[i] > 0){
        	result *= 10;
      		result += i;
        }
      }
    }
		return result;
	}
  
	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	public static void  main(String[] args){
		ReverseInt ri = new ReverseInt();
		System.out.println(ri.reverseInt(118372));
	}
}