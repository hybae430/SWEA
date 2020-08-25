#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
  		int N;
    	cin >> N;
			vector<int> p;
			for (int j = 0; j < N; j++)
			{
				int input;
				cin >> input;
				p.push_back(abs(input));
			}
			sort(p.begin(), p.end());
			cout << '#' << i << ' ' << p[0] << ' ' << count(p.begin(), p.end(), p[0]) << '\n';
	}
}