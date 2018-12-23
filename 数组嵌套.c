
//1
int main(){
    int a[3];
    a[0] = 1; // a[0]=1
    a[a[0]] = 2; // a[1] = 2
    a[a[a[0]]] = 3;  // a[2] = 3
    print(a[0]);
    print(a[1]);
    print(a[2]);
    return 0;
}


//2
int main(){

    int a[3];
    int b[3][3];
    int c[3][3][3];

    a[0] = 1;
    a[1] = 2;

    b[a[0]][a[1]] = 2;  //b[1][2] = 2
    c[b[a[0]][a[1]]][a[0]][a[1]] = 9; // c[2][1][2] = 9
    print(c[2][1][2]);
    return 0;

}