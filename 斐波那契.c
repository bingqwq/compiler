int fun(int n) {
    int f;
    if (n == 1) {
        f=1;
    }
    else {
        f = fun(n-1) * n;
    }
    return f;
}

int add(int x, int y) {
    return x + y;
}

int main() {
    int a = 4;
    int b = 5;
    int z = add(fun(a), fun(b));
    print(z);
    return 0;
}