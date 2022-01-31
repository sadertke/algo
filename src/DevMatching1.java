import java.util.Arrays;

public class DevMatching1 {
    public static int [][] arr;
    public static void main(String[] args) {
        int r=6 , c=3;

        arr = new int[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j <c ; j++) {
                arr[i][j] = i*c+j+1;
                System.out.print(arr[i][j]);
            }
            System.out.println("\n");
        }
        rotate(0,0,2,2);


    }

    //
     public static void rotate(int x1, int y1, int x2, int y2){

        int temp=arr[x1][y1];
        int i=x1,j=y1;
        while (i<x2)

        { arr[i][j]= arr[i+1][j];
            i++;
        }


        //i= x2; j= y1;
        while (j<y2)
        {
            arr[i][j]=arr[i][j+1];
            j++;
        }
       // i=x2; j=y2;
        while (i>x1)
        {
            arr[i][j]=arr[i-1][j];
            i--;
        }
        //i=x2; j=y2;
        while (j>y1+1)
        {
            arr[i][j]=arr[i][j-1];
            j--;
        }
        arr[i][j]=temp;


            }




}
