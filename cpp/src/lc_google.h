//
//  google.hpp
//  leet_code_main
//
//  Created by Yunpeng Hou on 6/12/18.
//

#ifndef google_hpp
#define google_hpp

// std
#include <stdio.h>
#include <string>
#include <unordered_set>
#include <functional>


using namespace std;

/*
 Given a robot cleaner in a room modeled as a grid. Each cell in the grid can be empty or blocked. The robot cleaner can move forward, turn left or turn right. When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
 */
class RobotCleaner
{
public:
    // returns true if next cell is open and robot moves into the cell.
    // returns false if next cell is obstacle and robot stays on the current cell.
    bool move() { return true; };
    
    // Robot will stay on the same cell after calling Turn*.
    // k indicates how many turns to perform.
    void turnLeft(int k) {};
    void turnRight(int k) {};
    
    // Clean the current cell.
    void clean() {};
    
    //---------------------------------------------------------------
    RobotCleaner(): d_x(0), d_y(0), d_direction(0) {}
    
    void traverse()
    {
        dfs();
    }
    
    // Call turnLeft once and update direction variable
    void turnLeftWithUpdate()
    {
        turnLeft(1);
        d_direction -= 1;
        if(d_direction < 0)
        {
            d_direction = 3;
        }
    }
    
    // Call turnRight once and update direction variable
    void turnRightWithUpdate()
    {
        turnRight(1);
        d_direction = (d_direction+1) % 4;
    }
    
    // move towards d_direction and update state if move succeed
    // return true if move succeed
    // otherwise return false
    bool moveWithUpdate()
    {
        pair<int, int> nextPoint = getNewPoint(d_x, d_y, d_direction);
        if( move() )
        {
            d_x = nextPoint.first;
            d_y = nextPoint.second;
            return true;
        }
        return false;
    }
    
    void dfs()
    {
        // Remember the position and direction when we first come to this cell
        int initDirection = d_direction;
        
        clean();
        visited.insert(std::make_pair(d_x, d_y));
        
        for(int i=0; i < 4; ++i)
        {
            if(i > 0)
            {
                turnRightWithUpdate();
            }
            pair<int, int> newPoint = getNewPoint(d_x, d_y, d_direction);
            
            if( visited.find(newPoint) == visited.end() && moveWithUpdate() )
            {
                dfs();
            }
            
        }
        
        // We need to move back to previous cell
        // 1st turn to  direction opposite initial direction
        int oppDirection = getOppositeDirection(initDirection);
        while( d_direction != oppDirection )
        {
            turnRightWithUpdate();
        }
        
        // move back 1 step
        moveWithUpdate();
        
        // Turn to the initial direction
        while( d_direction != initDirection )
        {
            turnRightWithUpdate();
        }
    }

private:
    int d_x;
    int d_y;
    
    /*
     direction: 0,1,2,3
     0 - inital facing direction
     1 - next direction from 0 in clock wise
     */
    int d_direction;
    
    struct pairHash
    {
        std::size_t operator() (const std::pair<int, int>& intPair)
        {
            std::size_t h1 = std::hash<int>{}(intPair.first);
            std::size_t h2 = std::hash<int>{}(intPair.second);
            return h1 ^ (h2 << 1);
        }
    };
    
    unordered_set<pair<int,int>, pairHash > visited;
    
    
    pair<int, int> getNewPoint(int x, int y, int direction)
    {
        switch(direction)
        {
            case 0:
                return std::make_pair(x-1, y);
            case 1:
                return std::make_pair(x, y+1);
            case 2:
                return std::make_pair(x+1, y);
            default:
                return std::make_pair(x, y-1);
        }
    }
    
    int getOppositeDirection(int direction)
    {
        switch(direction)
        {
            case 0:
                return 2;
            case 2:
                return 0;
            case 1:
                return 3;
            default:
                return 1;
        }
    }
};




#endif /* google_hpp */
