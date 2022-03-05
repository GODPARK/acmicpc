import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Solution {

    private void printListPretty(int[] array) {
        for (int value : array) {
            System.out.printf(Integer.toString(value));
            System.out.printf(",");
        }
        System.out.printf("\n");
    }
    public int solution(int U, int L, int[] C) {
        // write your code in Java SE 11
        Queue<CaseC> queue = new LinkedList<>();

        int []firstRow = new int[C.length];
        int []secondRow = new int[C.length];

        int checkCount = 0;
        for(int i = 0; i < C.length; i++) {
            if(C[i] == 2) {
                firstRow[i] = 1;
                secondRow[i] = 1;
            } else if (C[i] == 0) {
                firstRow[i] = 0;
                secondRow[i] = 0;
            } else if (C[i] == 1) {
                firstRow[i] = -1;
                secondRow[i] = -1;
                checkCount += 1;
            }
        }
        ArrayList<Integer> firstRowSumList = new ArrayList<>();
        ArrayList<Integer> secondRowSumList = new ArrayList<>();
        for (int i = 0; i < checkCount; i++) {
            int firstRowSum = 0;
            int secondRowSum = 0;
            for (int j = 0; j <  C.length; j++) {
                if (firstRow[i] == 1) {
                    firstRowSum += 1;
                }
                if (secondRow[i] == 1) {
                    secondRowSum += 1;
                }
                if (firstRow[i] == -1) {
                    firstRowSumList.add(firstRowSum + 1);
                    secondRowSumList.add(secondRowSum);

                    firstRowSumList.add(firstRowSum);
                    secondRowSumList.add(secondRowSum +1);
                }
            }
        }

        for (int i = 0;i <  firstRowSumList.size(); i++) {
            if (firstRowSumList.get(i) == U && secondRowSumList.get(i) == L) {
                return
            }
        }
    }
}
