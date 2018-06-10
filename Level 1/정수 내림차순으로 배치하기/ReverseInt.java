class Solution {
  public long solution(long n) {
      long result = 0;
      int []arr = new int[10];
      while(n > 0){
          arr[(int)(n%10)]++;
          n /= 10;
      }
      for(int i = 9; i>=0; i--){
          for(int j = 0; j<arr[i]; j++){
              result *= 10;
              result += i;
          }
      }
  return result;
  }
}