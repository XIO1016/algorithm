class Solution {
    public int mySqrt(int x) {
        if(x==0||x==1) return x;
        int start = 1;
        int end = x;
        while(start<=end){
            int mid = start + (end - start) / 2;
            if(Math.pow(mid,2) > x){
                end = mid -1;
            }
            else if (Math.pow(mid,2) == x){
                return mid;
            }
            else{
                start = mid+1;
            }
        }
        return end;
    }
}