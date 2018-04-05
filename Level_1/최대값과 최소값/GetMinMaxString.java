public class GetMinMaxString {
    public String getMinMaxString(String str) {
      	String splits[] = str.split(" ");
      	int min = Integer.parseInt(splits[0]);
      	int max = Integer.parseInt(splits[0]);
      	int current;
      	for(int i = 1; i<splits.length; i++){
					current = Integer.parseInt(splits[i]);
          if(current < min){
          	min = current;
          }
          if(current > max){
          	max = current;
          }
        }
        return min+" "+max;
    }

    public static void main(String[] args) {
        String str = "1 2 3 4";
        GetMinMaxString minMax = new GetMinMaxString();
        //아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println("최대값과 최소값은?" + minMax.getMinMaxString(str));
    }
}