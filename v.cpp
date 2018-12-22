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

int main() {
    int a = 4;
    int b;
    b = fun(a);
}