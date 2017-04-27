#include<iostream>
#include<vector>


using namespace std;

bool IsLeapDayNext (int year, int month, int day)
{
    if (month != 2) return false;
    if (day !=28)  return false;
    if (year % 4 > 0) return false;
    if (year % 100 > 0) return true;
    if (year % 400 == 0) return true;
}
void AddOneToDate (int &year, int &month, int &day)
{
    static double month_lengths[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if (day < month_lengths[month-1]) {++day; return;}
    if (IsLeapDayNext(year, month, day))
    {
        ++day;
        return;
    }
    day = 1;
    ++month;
    year = year + month/13;
    month = month % 13;
    if (month == 0) month = 1;
}
void AddToDate(int &year, int &month, int &day, int N_days)
{
    for (int i=0; i<N_days; ++i){
        AddOneToDate(year, month, day);
    }
}

int main(){
int year = 2016;
int month = 11;
int day = 28;
int N_days = 4000;
AddToDate(year, month, day, N_days);
cout<<"The current date is "<< year <<"/"<<month<<"/"<<day;}
