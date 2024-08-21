class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        int i=0, n= nums.size();
        int j=n-1, count=0;
        for(i=0; i<j; i++){
            for(j=i+1;j<n;j++){
                if(nums[i]==nums[j] && (i*j)%k==0){
                    count++;
                }
            }
        }
        return count;
    }
};