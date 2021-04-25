#include<iostream>
#include<omp.h>

#define ROW 3
#define COL 3
using namespace std;
int*** blur(int*** img, int r, int c, int ch){
    // paramters image matrix(img), no of rows(r), columns(c) and channels(ch)
    int*** blurred;
    blurred = new int**[r];
    for(int i=0;i<r;i++){
        blurred[i] = new int*[c];
        for(int j=0; j<c;j++){
            blurred[i][j] = new int[ch];
            for(int k=0;k<ch;k++){
                blurred[i][j][k] = img[i][j][k];
            }
        }
    }
    #pragma omp parallel for
    for(int i=0;i < r; i++){
        #pragma omp parallel for
        for(int j=0;j<r;j++){
            int channel = 0;
            #pragma omp parallel for reduction(+:channel)
            for(int k=0;k<ch;k++){
                // upper row
                if(i-1 >= 0 && j-1 >=0){
                    channel += img[i-1][j-1][k];
                }
                if(i-1 >= 0){
                    channel += img[i-1][j][k];
                }
                if(i-1 >= 0 && j+1 < c){
                    channel += img[i-1][j+1][k];
                }

                // middle row
                if(j-1 >= 0){
                    channel += img[i][j-1][k];
                }
                if(j+1 < c){
                    channel += img[i][j+1][k];
                }
                channel += img[i][j][k];

                // lower row
                if(i+1 < r && j-1 >=0){
                    channel += img[i+1][j-1][k];
                }
                if(i+1 < r){
                    channel += img[i+1][j][k];
                }
                if(i+1 < r && j+1 < c){
                    channel += img[i+1][j+1][k];
                }
                #pragma omp critical
                {
                    blurred[i][j][k] = channel/3;
                    channel = 0;
                }
            }
        }
    }
    return blurred;
}
int main(){
    int*** img;
    int r, c, ch;
    r = c = ch = 3;

    int temp[3][3][3]= {
        {{135, 131, 119}, {135, 131, 119}, {135, 131, 119}},
        {{112, 109,  94}, {111, 108,  93}, {111, 108,  93}},
        {{136, 132, 120}, {136, 132, 120}, {136, 132, 120}}
    };


    img = new int**[r];
    for(int i=0;i<r;i++){
        img[i] = new int*[c];
        for(int j=0; j<c;j++){
            img[i][j] = new int[ch];
            for(int k=0;k<ch;k++){
                img[i][j][k] = temp[i][j][k];
            }
        }
    }
    
    int*** blurred = blur(img, 3, 3, 3);
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            for(int k=0;k<ch;k++){
                cout << blurred[i][j][j] << "\t";
            }
            cout << endl;
        }
        cout << endl;
    }
    return 0;
}