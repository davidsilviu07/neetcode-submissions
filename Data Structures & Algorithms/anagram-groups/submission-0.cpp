class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;
        
        for (const string& s : strs) {
            // 1. Vectorul de frecvență pentru cuvântul curent
            vector<int> freq(26, 0);
            for (char c : s) {
                freq[c - 'a']++;
            }
            
            // 2. Crearea cheii unice sub formă de string
            string key = "";
            for (int count : freq) {
                key += to_string(count) + "#";
            }
            
            // 3. Adăugarea cuvântului în Hash Map la cheia corespunzătoare
            anagramMap[key].push_back(s);
        }
        
        // 4. Extragerea grupurilor pentru rezultatul final
        vector<vector<string>> result;
        for (auto& pair : anagramMap) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};