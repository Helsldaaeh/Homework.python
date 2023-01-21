#include <iostream>

using  namespace std;

int main()
{
 int Seconds = 0;
 int Hours = 0;
 int Min = 0;

cout << "Enter: ";
cin >> Seconds;

while (Seconds >= 60) {
	Seconds = Seconds - 60;
	Min = Min + 1;

		while (Min >= 60) {
			Min = Min - 60;
			Hours = Hours + 1;
			}
	}
cout << Hours << "Hours" << Min << "Min" << Seconds << "Sec";
}
