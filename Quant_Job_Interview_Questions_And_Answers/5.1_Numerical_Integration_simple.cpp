#include <iostream>
using namespace std;

double f(double x) { return 0.1*x*x; }

double trapezium (double (*funPtr)(double), double x, double h)
{
   return (funPtr(x) + funPtr(x+h))/2;
}

// the integration routine
double integrate(double (*funPtr)(double), double a, double b, int steps)
{
  double s = 0;
  double h = (b-a)/steps;
  for (int i = 0; i < steps; ++i)
    s += trapezium(funPtr, a + h*i, h);
  return h*s;
}


int main()
{
int steps = 100;
double (*funPtr)(double);
funPtr = &f;
cout<<"funPtr "<< funPtr <<"  funPtr(10) "<< funPtr(10)<<endl;
double t  = integrate(funPtr, 0.0, 1.0, steps);
cout << "trapezium rule of integration yields "<<t<< endl;
}
