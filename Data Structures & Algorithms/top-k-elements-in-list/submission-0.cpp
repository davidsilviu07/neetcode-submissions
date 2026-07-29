class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // 1. Numărăm frecvența fiecărui element
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        // 2. Creăm "gălețile" (buckets)
        // Dimensiunea este nums.size() + 1 deoarece un element poate apărea de maxim N ori
        int n = nums.size();
        vector<vector<int>> buckets(n + 1);
        
        for (auto& pair : count) {
            int numar = pair.first;
            int frecventa = pair.second;
            buckets[frecventa].push_back(numar);
        }
        
        // 3. Extragem top k elemente parcurgând de la frecvența maximă la cea minimă
        vector<int> result;
        for (int i = n; i >= 0; --i) {
            for (int num : buckets[i]) {
                result.push_back(num);
                // Ne oprim imediat ce am adunat k elemente
                if (result.size() == k) {
                    return result;
                }
            }
        }
        
        return result;
    }
};