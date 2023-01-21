
#include <iostream>
	using namespace std;
	int main() {
		double R0 = 0;
		double R1 = 0;
		cout << "Enter R1 = ";
		cin >> R1;
		double R2 = 0;
		cout << "Enter R2 = ";
		cin >> R2;
		double R3 = 0;
		cout << "Enter R3 = ";
		cin >> R3;
		double X = 1 / R1 + 1 / R2 + 1 / R3;
		cout << "1 / R0 = " << X;
		return 0;
		// Задание 2
		double L;
		cout << "Enter L = ";
		cin >> L;
		double R;
		const double Pi = 3.14;
		R = L / (Pi * 2);
		cout << "S = " << Pi * (R * R);
		return 0;





	}	
