#include <iostream>
#include <fstream>
#include <string>
#include <cmath> // for logarithm function
#include <stdlib.h> // abs

using namespace std;

int input(string file, long a[])
{
  fstream fin;
  fin.open(file.c_str());
  int i = 0;
  long temp;
  while (fin >> temp)
    a[i++] = temp;
  fin.close();
  return i;
}

int primePick(int s)
{
  int flag = 0;
  int n = 100.8 * s; 
  while (flag == 0)
    {
      n++;
      int i;
      for (i = 2; i <= n / 2; i++)
	if (n % i ==0)
	  break;
      if (i == n/2 + 1)
	flag = 1;
    }
  cout << "log2(" << n << ") = " << log2(n) << endl;
  cout << "log10(" << n << ") = " << log10(n) << endl;
  return n;
}

int hashInput(long value, long h[], bool f[], int n, int shift)
{
  long v = abs(value);
  int position = v % n;
  int div = shift, i;
  int flag = -1;
  for (i = 0; i < div; i++)
    {
      int p = (position + i * n / div) % n;
      if (f[p] == 1 && h[p] == value) // already have
	{ 
	  flag = 1;
	  break;
	}
      else if (f[p] == 0) // empty, add new
	{
	  f[p] = 1;
	  h[p] = value;
	  flag = 0;
	  break;
	}
    }
  if (i == div)
    {
      cout << "------------------------" << endl;
      cout << "to enlarge the div or table?" << endl;
      for (i = 0; i < div; i++)
	{
	  int p = (position + i * n / div) % n;
	  cout << "occupied values: " << h[p] << endl;
	}
      cout << "p = " << (position + (i - 1) * n / div) % n << endl;
      cout << "value = " << value << endl;
      cout << "------------------------" << endl;
    }
  return flag;
}

bool hash(long value, long h[], bool f[], int n, int shift)
{
  long v = abs(value);
  int position = v % n;
  int div = shift, i;
  bool flag;
  for (i = 0; i < div; i++)
    {
      int p = (position + i * n / div) % n;
      if (f[p] == 1 && h[p] == value) // found
	  return 1;
    }
  if (i == div) // not found
    return 0;
  else
    cout << "error in hash function!!";
  return 0;
}

int main()
{
  // input numbers
  string file = "algo1-programming_prob-2sum.txt";
  int dim = 1000000;
  long *a;
  a = new long[dim];
  dim = input(file, a);
  cout << "There are " << dim << " elements in the file." << endl;

  // pick the prime
  int n = primePick(dim);
  cout << "We choose " << n << " slots for the hash function" << endl;

  // input all values into hash table
  long* h;
  bool* f;
  h = new long[n];
  f = new bool[n];
  for (int i = 0; i < n; i++)
    {
      f[i] = 0;
      h[i] = 0;
    }
  int j = 0, shift = 3;
  for (int i = 0; i < dim; i++)
    {
      int flag = hashInput(a[i], h, f, n, shift);
      if (flag == 0) // new element
	a[j++] = a[i];
    }
  cout << "There are " << j << " different elements." << endl;

  // two loops
  int length = j, sum = 0;
  for (int t = -10000; t <= 10000; t++)
    {
      if (abs(t) % 100 == 0)
	cout << t << endl;
      for (int i = 0; i < length; i++)
	{
	  long find = t - a[i];
	  bool flag = hash(find, h, f, n, shift);
	  if (flag == 1)
	    { 
	      sum++;
	      break;
	    }
	}
    }
  cout << "Result = " << sum << endl;
}
