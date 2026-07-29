#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // 1. Inserăm toate elementele într-un Hash Set
        // Folosim un constructor care preia elementele direct din vector
        unordered_set<int> numSet(nums.begin(), nums.end());
        
        int maxLength = 0;

        // 2. Parcurgem elementele direct din Set (fără duplicate)
        for (int num : numSet) {
            // Verificăm dacă 'num' este INCEPUTUL unei secvențe
            // Dacă num - 1 NU există în set, înseamnă că am găsit un început valid
            if (numSet.find(num - 1) == numSet.end()) {
                int currentNum = num;
                int currentLength = 1;

                // 3. Cât timp găsim următorul număr consecutiv, creștem lungimea
                while (numSet.find(currentNum + 1) != numSet.end()) {
                    currentNum += 1;
                    currentLength += 1;
                }

                // 4. Actualizăm lungimea maximă găsită până acum
                maxLength = max(maxLength, currentLength);
            }
        }

        return maxLength;
    }
};