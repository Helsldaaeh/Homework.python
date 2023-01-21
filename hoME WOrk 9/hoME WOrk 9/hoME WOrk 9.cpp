#include <iostream>
using namespace std;
int main()
{
int Days = 0;
int week = 0;
cout << "Enter: ";
cin >> Days;
while (Days >= 7) {
	Days = Days - 7;
	week = week + 1;
}
cout << week << " week " << Days << " Days ";

}
