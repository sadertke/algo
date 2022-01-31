import java.util.*;
import java.util.stream.Collectors;

public class DevMatching3 {
    public static int [] answer;
    public static int[] arr;
    public static void main(String[] args) {
        String[] tmp = {"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"};
        String[] tmp1 = {"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"};
        String[] tmp2 = {"young", "john", "tod", "emily", "mary"};
        int[] tmp3 = {12, 4, 2, 5, 10};
        solution(tmp,tmp1,tmp2,tmp3);
        for(int i:answer){
            System.out.println(i);

        };




    }

        public static int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
          answer = new int[enroll.length+1];
            Map<String,Integer> map = new HashMap<>();
            int i;
            for( i=1; i<=enroll.length;i++){

                map.put(enroll[i-1],i);
            }
            map.put("-",0);
            arr = new int[enroll.length+1];

            arr[0]=0;
            for (int j = 0; j <referral.length ; j++) {

              arr[j+1]= map.get(referral[j]);
            }

            for (int j = 0; j <seller.length ; j++) {

               start( map.get(seller[j]),amount[j]*100);
            }



            return answer;
        }

        static void  start(int s,int m){
            int v = (int) ((int)m*0.1);

         if(arr[s]==s){

             answer[s]=m;
             return;
         }

         answer[s] +=(m-v);

         start(arr[s],v);

        }





}
