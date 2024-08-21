class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i=0,j=0,n=s.size(),maxi=INT_MIN;
        if(n==0){
            return 0;
        }
        set<char> newt;
        while(j<n){
            if(newt.find(s[j])==newt.end()){
                newt.insert(s[j]);
                maxi= max(maxi, j-i+1);
                j++;
            }
            else{
                newt.erase(s[i]);
                i++;
            }
        }
        return maxi;
    }
};