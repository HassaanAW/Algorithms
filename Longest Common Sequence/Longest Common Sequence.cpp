    #include <iostream>
    #include <string>
    using namespace std;

    void LCS(string first, string second, int x, int y);

    int main()
    {
     cout << " Enter two strings " << endl;
     string string1, string2;
     cout << " Enter String One: ";
     cin >> string1; // abcd
     cout << " Enter String Two: ";
     cin >> string2; // bd

     //cout << string1.substr(1,1) << endl;
     //cout << string2.substr(1,1) << endl;

     int len1 = string1.length(); //4
     int len2 = string2.length(); //2

     LCS(string1, string2, len1, len2);
    }

    void LCS(string first, string second, int x, int y){ // (abcd, bd, 4, 2)
        // Create a table first
        int rows = y+1; // associated with second value
        int cols = x+1; // associated with first value
        int table[rows][cols];

        for(int i=0; i<rows; i++){ //3
            for(int j=0; j<cols; j++){ //5
                if(i==0 || j==0)
                {
                    table[i][j] =0;
                }
                else if(first.substr(j-1,1) == second.substr(i-1,1)){
                    table[i][j] = table[i-1][j-1] + 1;
                    //final = final + first.substr(j-1,1);
                }
                else{
                    table[i][j] = max(table[i-1][j], table[i][j-1]);
                }
            }
        }
        // Population completes here in O(m*n)
        // Now we need to trace back which will also  be in O(m*n)
        int last_element = table[y][x];
        int temp_count = last_element;
        string final_string = "";

        int row_second=y; //2. Associated with second values (row)
        int col_first=x; //4

        while(row_second>0 && col_first>0){
            if(first.substr(col_first-1,1) == second.substr(row_second-1,1)){
                //cout << "Match" << endl;
                final_string = first.substr(col_first-1,1) + final_string;
                last_element = last_element-1;
                row_second = row_second-1;
                col_first = col_first-1;
            }
            else if(table[row_second-1][col_first] > table[row_second][col_first-1]){ //coming from above
                //cout << "Second" << endl;
                row_second = row_second-1;
            }
            else{
                //cout << " Third" << endl;
                col_first = col_first-1;
            }
        }
        cout << " Longest Common Substring: ";
        cout << final_string << endl;

    // Test Loop for printing state of Table generated

        /*for(int i=0; i <rows; i++)
        {
            for(int j=0; j<cols;j++){
                cout << table[i][j]<< " ";
            }
            cout << endl;
        }*/
    }


