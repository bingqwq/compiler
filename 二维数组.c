int main() {
    int a[3][3];

    int i = 0;
    while(i < 3) {
        int j = 0;
            while(j < 3) {
                    a[i][j] = i + j;
                    j = j + 1;
            }
        i = i + 1;
    }
    i = 0;
    while(i < 3) {
        int j = 0;
            while(j < 3) {
                    print(a[i][j]);
                    j = j + 1;
            }
        i = i + 1;
    }


    return 0;
}
