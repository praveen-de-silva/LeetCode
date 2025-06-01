#define edge pair<int, int>
const static int INF = 1e6;

class Solution {
    void printArr(vector<int>& arr) {
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;
}

    class Graph {
    public:
        int size;
        vector<edge> g_edges;
        vector<int> g_weights;
        vector<int> dist;
        vector<int> parents;

        Graph (int size) {
            this->size = size;
        }

        void addEdge(int u, int v, int w) {
            g_edges.push_back(edge(u, v));
            g_edges.push_back(edge(v, u));
            g_weights.push_back(w);
            g_weights.push_back(w);
        }

        void relax(int u, int v, int w) {
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                parents[v] = u;
            }
        }

        vector<int> BellmanFord(int s) {
            dist = vector<int>(size, INF);
            parents = vector<int>(size, -1);
            
            dist[s] = 0;

            for (int j=0; j<size-1; j++) {
                for (int i=0; i<g_edges.size(); i++) {
                    relax(g_edges[i].first, g_edges[i].second, g_weights[i]);
                }
            }

//            for (int i=0; i<g_edges.size(); i++) {
//                if (dist[g_edges[i].second] > dist[g_edges[i].first] + g_weights[i]) {
//                    return false;
//                }
//            }
            return dist;
        }
    };

public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        int smallestCityCount = n;
        int resultantCity = 0;
        
        
        Graph gp(n);

        for (vector<int> ed : edges) {
            gp.addEdge(ed[0], ed[1], ed[2]);
        }

        

        for (int u=0; u<n; u++) {
            vector<int> crntDists = gp.BellmanFord(u);
            int tempSCCount = 0;
            printArr(crntDists);
            for (int v=0; v<n; v++) {
                
                if ((crntDists[v]<=distanceThreshold) && (v!=u)) tempSCCount++;
            }
            
            if (tempSCCount<=smallestCityCount) {
                resultantCity = u;
                smallestCityCount = tempSCCount;
            }
        }
        
        return resultantCity;
    }
};