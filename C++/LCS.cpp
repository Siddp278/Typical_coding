#include <iostream>
#include <string>

using namespace std;

int main() {
    string s1= "AGGTAB";
    string s2= "GGXTXAYB";
    string s3= "";
    int count = 0;
    int arr[10] = {99,99,99,99,99,99,99,99,99,99};
    for(int i=0;i<6;i++){   //6 is the size of s1
        for(int j=0;j<8;j++){   //8 is the size of s2.
            if(s1[i] == s2[j]){
                arr[count] = j;
                s3 = s3 + s2[j];
                //So that confusion doesnt arise in the cases where two or more than two same alphabets are present.
                s2.replace(j,1,"a");
                //cout<< s2<< endl;
                count = count + 1;
                break;
            }
        }
    }
    /* Now comes the comparison phase.
    for(int k=0;k<s3.length();k++){
        cout<< s3[k]<< endl;
        cout<< arr[k]<< endl;
    }
    */
    for(int k=0;k<s3.length()-1;k++){
        if(arr[k] - arr[k+1] > 0){
            char temp;
            temp = s3[k];
            s3[k] = s3[k+1];
            s3[k+1] = temp;
            int temp1;
            temp1 = arr[k];
            arr[k] = arr[k+1];
            arr[k+1] = temp1;
        }
    }
    cout<< "The string is:"<< s3<< endl;
    cout<< "The length of the string is:"<< s3.length();
    return 0;
}
