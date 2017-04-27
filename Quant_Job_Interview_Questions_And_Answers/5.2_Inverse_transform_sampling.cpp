#include <iostream>
#include <vector>
#include <random>
using namespace std;

double Simulate(const vector<double> &p, const vector<int> &v, double u){
int i = 0;
while (u > p[i]){
    u -= p[i];
    ++i;
}
return v[i];
}


int main()
{
vector<double> prob = {0.1, 0.02, 0.3, 0.58};
vector<int> value = {1, 10, 2, 40};
default_random_engine generator;
uniform_real_distribution<double> distribution(0.0,1.0);
for (int i=1; i<100; i++){
double u = distribution(generator);

cout<<i<<"th value generated  "<<Simulate(prob, value, u)<<endl;
}
}
