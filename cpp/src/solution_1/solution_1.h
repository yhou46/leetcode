//
//  solution_931.h
//
//

#include <vector>
#include <string>
#include <unordered_map>
#include <iostream>

#ifndef LC_solution_1_h
#define LC_solution_1_h

/*
 Ref: https://leetcode.com/problems/two-sum/description/
 
 Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 
 You may assume that each input would have exactly one solution, and you may not use the same element twice.
 
 Example:
 
 Given nums = [2, 7, 11, 15], target = 9,
 
 Because nums[0] + nums[1] = 2 + 7 = 9,
 return [0, 1].
 */

using namespace std;

class Solution {
public:
    
    /*
     Do it in one pass. We can check when we insert input to a map
     Time complexity: O(n)
     Space complexity: O(n)
     */
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> tempMap;
        vector<int> result;
        
        for( int i=0; i < nums.size(); ++i )
        {
            int complement = target - nums[i];
            if( tempMap.find(complement) != tempMap.end() )
            {
                result.push_back(tempMap[complement]);
                result.push_back(i);
                return result;
            }
            tempMap.insert(std::make_pair(nums[i], i));
        }
        return result;
        
    }
};

#endif /* LC_solution_1_h */
