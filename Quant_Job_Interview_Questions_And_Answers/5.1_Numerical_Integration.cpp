#include <iostream>
using namespace std;


// the integration routine
template<typename Method, typename F, typename Float>
 double integrate(F f, Float a, Float b, int steps, Method m)
{
  double s = 0;
  double h = (b-a)/steps;
  for (int i = 0; i < steps; ++i)
    s += m(f, a + h*i, h);
  return h*s;
}

// methods
class rectangular
{
public:
  enum position_type { left, middle, right };
  rectangular(position_type pos): position(pos) {}
  template<typename F, typename Float>
   double operator()(F f, Float x, Float h) const
  {
    switch(position)
    {
    case left:
      return f(x);
    case middle:
      return f(x+h/2);
    case right:
      return f(x+h);
    }
  }
private:
  const position_type position;
};

//class trapezium
//{
//public:
//  template<typename F, typename Float>
//   double operator()(F f, Float x, Float h) const
//  {
//    return (f(x) + f(x+h))/2;
//  }
//};

double trapezium (f, double x, double h) const
{
   return (f(x) + f(x+h))/2;
}

class simpson
{
public:
  template<typename F, typename Float>
   double operator()(F f, Float x, Float h) const
  {
    return (f(x) + 4*f(x+h/2) + f(x+h))/6;
  }
};


// sample usage
double f(double x) { return x*x; }


int main()
{
// inside a function somewhere:
int steps = 100;
double rl = integrate(f, 0.0, 1.0, steps, rectangular(rectangular::left));
cout << "rectangular rule of integration yields "<<rl<< endl;
double rm = integrate(f, 0.0, 1.0, steps, rectangular(rectangular::middle));
cout << "rectangular rule of integration yields "<<rm<< endl;
double rr = integrate(f, 0.0, 1.0, steps, rectangular(rectangular::right));
cout << "rectangular rule of integration yields "<<rr<< endl;
double t  = integrate(f, 0.0, 1.0, steps, trapezium());
cout << "trapezium rule of integration yields "<<t<< endl;
double s  = integrate(f, 0.0, 1.0, steps, simpson());
cout << "simpson rule of integration yields "<<t<< endl;
}
