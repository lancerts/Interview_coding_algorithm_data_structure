

#include<iostream>
#include<vector>
#include <stdlib.h>
using namespace std;

int main()
{
   unsigned int n, miss, index;
   uint64_t total, sum;
   vector<int> numbers;
   cout << "Enter the number of terms of you want" << endl;
   cin >> n;
   index = rand() % n;

   for (int i=1; i<=n; i++) numbers.push_back(i);
   cout << "The number erased  " << numbers[index]  << endl;
   numbers.erase((numbers.begin()+index));
   total = (1+n)*n/2;
   cout << "Correct total is  " << total << endl;
   sum = 0;
   for (auto i = numbers.begin(); i != numbers.end(); i++) {
    sum += *i;
   }
   miss = total - sum;
   cout << "Missing element is  " << miss << endl;
   return 0;
}
