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