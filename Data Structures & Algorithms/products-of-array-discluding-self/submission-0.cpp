class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> output(n, 1); // Inițializăm totul cu 1
        
        // Pasul 1: Calculăm produsele din stânga pentru fiecare element
        int leftProduct = 1;
        for (int i = 0; i < n; i++) {
            output[i] = leftProduct; // Salvăm produsul din stânga
            leftProduct *= nums[i];  // Actualizăm produsul pentru următorul pas
        }
        
        // Pasul 2: Calculăm produsele din dreapta și le înmulțim direct în output
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            output[i] *= rightProduct; // Înmulțim cu produsul din stânga deja existent
            rightProduct *= nums[i];   // Actualizăm produsul din dreapta
        }
        
        return output;
    }
};