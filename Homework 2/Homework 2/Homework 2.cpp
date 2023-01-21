// Homework 2.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

int main()
{
	double L = 0;

	std:: cout << "Enter L = ";

	std:: cin >> L;
	double R;
	const double Pi = 3.14;
	R = L / (Pi * 2);
	std:: cout << "S = " << Pi * (R * R);
	return 0;
}

