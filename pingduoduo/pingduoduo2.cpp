#include <queue>
#include <set>
#include <iostream>
#include <algorithm>

using namespace std;

struct COMP1 {
    bool operator() (pair<int,pair<int,int>> i, pair<int,pair<int,int>> j) {
        return i.second.first < j.second.first;
    }
};

struct COMP2 {
    bool operator() (pair<int,pair<int,int>> i, pair<int,pair<int,int>> j) {
        return i.second.second < j.second.second;
    }
};

int main() {
    int N;
    vector<pair<int,pair<int,int>>> data;
    set<int> finished;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int t, w;
        cin >> t >> w;
        data.emplace_back(i,t,w);
    }
    sort(data.begin(), data.end(), COMP1());
    priority_queue<pair<int,pair<int,int>>, vector<pair<int,pair<int,int>>>, COMP2> q;
    int index = 0;
    int now = 0;
    int ans = 0;
    while (finished.size() < N) {
        auto temp = data[index];
        
        if (q.empty()) {
            now = temp.second.first;
            if (index+1 < N) {
                auto next = data[index+1];
                if (next.second.first < temp.second.first + temp.second.second) {
                    pair<int,int> p(temp.second.first, temp.second.first+temp.second.second-next.second.first);
                    q.push(pair<int,pair<int,int>>(temp.first, p));
                    now = next.second.first;
                    ++index;
                } else {
                    finished.insert(temp.first);
                    now += temp.second.second;
                    ans += (now - temp.second.first);
                    ++index;
                }
            } else {
                finished.insert(temp.first);
                now += temp.second.second;
                ans += (now - temp.second.first);
                ++index;
            }
        }
    }
}