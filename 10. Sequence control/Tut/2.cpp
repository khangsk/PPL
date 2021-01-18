#include <iostream>
using namespace std;

void swap(int x, int y) {
    int t = x;
    x = y;
    y = t;
}

int main() {
    int a[] = {2, 1, 0}, i = 0;
    swap(i, a[i]);
    cout << i << a[0] << a[1] << a[2];
}