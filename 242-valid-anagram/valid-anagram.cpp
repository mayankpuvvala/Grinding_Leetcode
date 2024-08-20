class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<int,int> mp;

        for(auto &it: s){
            mp[it]++;
        }

        for(auto &i: t){
            mp[i]--;
        }

        for(auto &i: mp){
            if(i.second!=0){
                return false;
            }
        }
        return true;
    }
};