#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:

    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end()); // sort the array lexiographycally

        int day =0, index = 0, n=events.size();
        priority_queue<int, vector<int>, greater<int>> pq;
        int result = 0;

        while (!pq.empty() || index < n) {
            if (pq.empty()) {
                day = events[index][0];
            }

            while (index < n && events[index][0] <= day) {
                pq.push(events[index][1]);
                index++;
            }

            pq.pop();
            day++; 
            result++;

            while (!pq.empty() && pq.top() < day) {
                pq.pop();
            }


        }
        return result;
    }
};