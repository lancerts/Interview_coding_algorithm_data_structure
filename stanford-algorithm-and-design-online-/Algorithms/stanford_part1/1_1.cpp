#include <iostream> 
#include <stdlib.h> 
#include <vector> 
#include <fstream> 
using namespace std; 
long long inversionNum = 0; 
vector<int> mergeSort(vector<int> &i); 
//pass vector by reference so the code does not creat copy of vector
vector<int> merge(vector<int> &left, vector<int> &right); 

vector<int> mergeSort(vector<int>& i) 
{ 
    if ( i.size() == 1) 
        return vector<int >(1, i[0]); // vector with one element i[0]
    if ( i.size() == 0) 
        return vector<int >(); 
     
	//i.begin() is the vector iterator
    vector<int>::iterator mid = i.begin() + i.size() / 2; 
    vector<int> left(i.begin(), mid); // iterating through i.begin to mid
    vector<int> right(mid, i.end()); 

    left = mergeSort( left ); 
    right = mergeSort( right ); 
    return merge( left, right); 
//recursive call down to the bottm then merge bcak to top
} 

vector<int> merge(vector<int> &left, vector<int> &right) { 
    vector<int> result; 
    vector<int>::size_type le = 0, ri = 0; 
    while ( le < left.size() && ri < right.size()) { 
        if ( left[le] > right[ri] ) {   //inversion 
            result.push_back(right[ri++]); 
            inversionNum += (left.size() - le); 
        } 
        else { 
            result.push_back(left[le++]); 
        } 
    } 
    while ( le < left.size() ) { 
        result.push_back(left[le++]); 
    } 
    while ( ri < right.size() ) { 
        result.push_back(right[ri++]); 
    } 
    return result; 
}

int main(){ 
    //read file,initial a integer vector 
    vector<int> ivec(100000,0); 
    vector<string> svec(100000); 
    ifstream fin("beforeSort.txt"); //the data file before Sort
    for (vector<string>::iterator sx = svec.begin(); sx != svec.end(); ++sx) 
        getline(fin, *sx); 
    fin.close(); 
    //change it into integer 
    for (int count = 0; count < 100000; ++count) 
        ivec[count] = atoi(svec[count].c_str()); 
    //merge sort 

    vector<int> result = mergeSort(ivec); 
    ofstream fout("afterSort.txt"); 
    for(vector<int>::iterator rx = result.begin(); rx != result.end(); ++rx) 
        fout << *rx << endl; 
    fout.close(); 
	
    cout << "The number of inversions is:" << inversionNum << endl; 
	cin.get();
    return 0; 
} 