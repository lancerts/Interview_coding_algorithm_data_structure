#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

void getGrades(vector<int>&);
void copyVector(vector<int>, vector<int>&);
void deleteDuplicates(vector<int>&);
void getCount(vector<int>, vector<int>, vector<int>&);
void vectorToDArray(int [], int, vector<int>);
void printArray(int [], int [], int);

typedef int* IntPtr;

int main()
{
	vector<int> grades, gradesCopy, uniqueCount;

	getGrades(grades);
	sort(grades.begin(), grades.end()); //#include<algorithm>
	copyVector(grades, gradesCopy);
	deleteDuplicates(grades);
	getCount(grades, gradesCopy, uniqueCount);

	int size = uniqueCount.size();
	IntPtr gradeArray, countArray;
	gradeArray = new int [size];
	countArray = new int [size];

	vectorToDArray(gradeArray, size, grades);
	vectorToDArray(countArray, size, uniqueCount);
	printArray(gradeArray, countArray, size);

	delete [] gradeArray;
	delete [] countArray;

	return 0;
}

//will prompt the user in a do-while loop to get the grades and will end when -1 is entered
//push_back will be used to store the grades into a created vector
void getGrades(vector<int>& grades) {

	int grade;

	cout << "**************************************************************************************" << endl;
	cout << endl;
	cout << "               WELCOME TO THE HISTOGRAM OF STUDENT GRADES MAKER THINGY" << endl;
	cout << endl;
	cout << "**************************************************************************************" << endl;
	cout << endl;
	cout << "Please enter the student's grades. When you have entered a single grade, press enter. " << endl;
	cout << "When finished entering all grades, type in '-1' and then press enter. " << endl;
	cout << endl;
	do {
		cin >> grade;
		if (grade != -1) {
			grades.push_back(grade);
		}
	} while (grade != -1);
}

//gets the grades with the original vectors and will use push_back
//to be put and copied into another vector
void copyVector(vector<int> grades, vector<int>& gradesCopy) {
	for (int i = 0; i < grades.size(); i++) {
		gradesCopy.push_back(grades[i]);
	}
}

//deletes the duplicates in the first vector
//needed to compare to second vector
void deleteDuplicates(vector<int>& grades) {
	for (int i = 0; i < grades.size(); i++) {
		for (int j = i + 1; j < grades.size();)
            {
			if (grades[i] == grades[j]) {
				grades.erase(grades.begin() + j);
			}
			else {++j;}
	}
}
}

//compares the two vectors and when one equals the other the count goes up
//count is then pushed back to another vector to hold the count for each number
void getCount(vector<int> g1, vector<int> g2, vector<int>& c) {
	int count = 0;
	for (int i = 0; i < g1.size(); i++) {
		for (int j = 0; j < g2.size(); j++) {
			if (g1[i] == g2[j]) {
				count++;
			}
		}
		c.push_back(count);
		count -= count;
	}
}

void vectorToDArray(int a[], int size, vector<int> v) {
	for (int i = 0; i < size; i++) {
		a[i] = v[i];
	}
}

void printArray(int a[], int b[], int size) {
	for (int i = 0; i < size ; i++) {
		cout << "Number of " << a[i] << "'s : " << b[i] << endl;
	}
}
