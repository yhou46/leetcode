//
//  LC_Solution20.h
//  leet_code_main
//
//  Created by Yunpeng Hou on 7/24/18.
//

#include <stack>
#include <string>

#ifndef LC_Solution20_h
#define LC_Solution20_h

// Bad practice
using namespace std;

/*
 Ref: https://leetcode.com/problems/valid-parentheses/description/
 */

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> charStack;
        
        for(int i=0;i < s.size(); ++i)
        {
            switch( s[i] )
            {
                case '(':
                case '[':
                case '{':
                    charStack.push(s[i]);
                    break;
                case ')':
                case ']':
                case '}':
                    if( charStack.empty() )
                    {
                        return false;
                    }
                    
                    char ch = charStack.top();
                    charStack.pop();
                    if( !isMatch(ch, s[i]) )
                    {
                        return false;
                    }
                    
                    break;
            }
            
            
        }
        return charStack.empty();
        
    }
    
    bool isMatch(char a, char b)
    {
        if( a == '(' && b == ')' ||
           a == '[' && b == ']' ||
           a == '{' && b == '}' )
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};

#endif /* LC_Solution20_h */
