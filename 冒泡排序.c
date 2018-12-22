int main(){
    int a[10];
    //fuzhi
    int i=0;
    while(i<10) {
        a[i] = i;
        i = i + 1;
    }
    //shuchu
    i = 0;
    while(i<10) {
        print(a[i]);
        i = i + 1;
    }
    //paixu
    i = 0;
    while(i<9) {
        int j = 0;
        while(j<9-i) {
            if (a[j]<a[j+1]) {
                int t = a[j];
                a[j] = a[j+1];
                a[j+1] = t;
            }
            j = j + 1;
        }
        i = i + 1;
    }
    //shuchu
    i = 0;
    while(i<10) {
        print(a[i]);
        i = i + 1;
    }
    return 0;
}