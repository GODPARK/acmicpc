public class Logic {
    private void printListPretty(int[] array) {
        for (int value : array) {
            System.out.printf(Integer.toString(value));
            System.out.printf(",");
        }
        System.out.printf("\n");
    }

    private void quickSort(int[] array,int start, int end) {
        int index =partition(array, start,end);
        if(start<index-1) quickSort(array, start,index-1);
        if(end>index) quickSort(array, index, end);
    }

    private int partition(int[] array,int start,int end) {
        int pivot=array[(start+end)/2];
        while(start<=end) {
            while(array[start]<pivot) start++;
            while(array[end]>pivot) end--;
            if(start<=end) {
                swap(array,start,end);
                start++;
                end--;
            }
        }
        return start;
    }

    private void swap(int[] array,int start,int end) {
        int tempValue =array[start];
        array[start]=array[end];
        array[end]=tempValue;
        return;
    }

    private int max(int a, int b) {
        if (a >= b) {
            return a;
        }
        return b;
    }

    private int min(int a, int b) {
        if (a <= b) {
            return a;
        }
        return b;
    }

    private int abs(int value) {
        if (value >= 0) {
            return value;
        } else {
            return value * -1;
        }
    }
}
