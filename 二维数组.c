int main(){
    int i = 0;
    int a[3][3];

	//fu zhi
	while(i<3) {
		int j = 0;
		while(j<3) {
			a[i][j] = i * j;
			j = j + 1;
		}
		i = i + 1;
	}

	//shu chu
	i = 0;
	while(i<3) {
		int j = 0;
		while(j<3) {
			print(a[i][j]);
			j = j + 1;
		}
		i = i + 1;
	}

    return 0;
}