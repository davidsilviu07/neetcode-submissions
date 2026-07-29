class Solution {
public:
    // Codifică o listă de șiruri într-un singur șir de caractere.
    string encode(vector<string>& strs) {
        string encoded_string = "";
        for (const string& s : strs) {
            // Adăugăm lungimea, delimitatorul '#' și șirul efectiv
            encoded_string += to_string(s.length()) + "#" + s;
        }
        return encoded_string;
    }

    // Decodifică un singur șir de caractere înapoi în lista originală.
    vector<string> decode(string s) {
        vector<string> decoded_strs;
        int i = 0; // Pointer pentru a parcurge șirul codificat
        
        while (i < s.length()) {
            int j = i;
            // Căutăm delimitatorul '#' pentru a afla unde se termină numărul
            while (s[j] != '#') {
                j++;
            }
            
            // Extragem lungimea cuvântului folosind stoi (string to integer)
            int length = stoi(s.substr(i, j - i));
            
            // Extragem cuvântul exact pe baza lungimii găsite
            string word = s.substr(j + 1, length);
            decoded_strs.push_back(word);
            
            // Mutăm pointerul 'i' direct la începutul următorului bloc
            i = j + 1 + length;
        }
        
        return decoded_strs;
    }
};