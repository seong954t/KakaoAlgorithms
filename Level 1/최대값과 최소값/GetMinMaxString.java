class Solution {
    public String solution(String s) {
        String splits[] = s.split(" ");
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
    }