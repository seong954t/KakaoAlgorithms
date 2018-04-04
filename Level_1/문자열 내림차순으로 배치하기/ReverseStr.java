public class ReverseStr {
	public String reverseStr(String str){
    int alph[] = new int[52];
    int value;
    String result = "";
		for(int i = 0; i < str.length(); i++){
      value = str.charAt(i);
      if(value > 96){
        alph[value-71]++;
      }else if(value > 64){
        alph[value-65]++;
      }
    }
    for(int i = 51; i>=0; i--){
    	for(int j = 0; j<alph[i]; j++){
      	if(i > 25){
          result += (char)(i+71);
      	}else {
          result += (char)(i+65);
      	}
      }
    }
		return result;
	}

	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	public static void main(String[] args) {
		ReverseStr rs = new ReverseStr();
		System.out.println( rs.reverseStr("Zbcdefg") );
	}
}