#include <iostream>

using namespace std;

int main()
{
 float Number = 0;
 int Dollar = 0;
 int Cents = 0;
 cout << "Enter number: ";
 cin >> Number;
 Dollar = Number;
 Cents = (Number - Dollar) * 100;
 cout << Dollar << "Dollar" << Cents << "Cent";
 return 0;
}