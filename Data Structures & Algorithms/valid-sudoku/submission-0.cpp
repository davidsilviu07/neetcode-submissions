#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Inițializăm 9 seturi pentru rânduri, coloane și sub-cadrane
        vector<unordered_set<char>> rows(9);
        vector<unordered_set<char>> cols(9);
        vector<unordered_set<char>> boxes(9);

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char val = board[r][c];
                
                // Ignorăm celulele goale
                if (val == '.') {
                    continue;
                }

                // Calculăm indexul sub-cadranului (0 până la 8)
                int box_index = (r / 3) * 3 + (c / 3);

                // Verificăm dacă valoarea a mai fost întâlnită
                // .count(val) returnează 1 dacă elementul există, 0 altfel
                if (rows[r].count(val) || cols[c].count(val) || boxes[box_index].count(val)) {
                    return false; // Am găsit un duplicat
                }

                // Dacă nu a fost întâlnită, o adăugăm în seturile corespunzătoare
                rows[r].insert(val);
                cols[c].insert(val);
                boxes[box_index].insert(val);
            }
        }

        return true; // Dacă am parcurs tot și nu am găsit duplicate, e valid
    }
};