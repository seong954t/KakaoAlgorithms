class Solution {
  public String solution(String s) {
    int alph[] = new int[52];
    int value;
    String result = "";
    for(int i = 0; i < s.length(); i++){
        value = s.charAt(i);
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
}