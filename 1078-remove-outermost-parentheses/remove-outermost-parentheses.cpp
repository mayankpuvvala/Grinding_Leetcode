class Solution {
public:
    string removeOuterParentheses(string s) {
        string res;
        int start=0;
        for(char &c: s){
            if(c=='('&& start++>0)  res+=c;
            else if(c==')' && start-->1)    res+=c;

        }
        return res;
    }
};