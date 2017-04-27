#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int run(int numseats)
{
    int *seats = (int *)malloc(sizeof(int) * numseats);
    memset(seats, 0, sizeof(int) * numseats);

    // special case crazy guy
    int seat = rand() % numseats + 1;
    seats[seat - 1] = 1;

    int i;
    // continue with second dude
    for (i = 2; i <= numseats; i++) {
        if (seats[i - 1]) {
            // his seat is taken, randomly choose another
            int newseat;
            do {
                newseat = rand() % numseats + 1;
            } while (seats[newseat - 1]);
            seats[newseat - 1] = i;
        } else {
            // sits in his own seat
            seats[i - 1] = i;
        }
    }
    // is the last guy in his own seat?
    int ret = (seats[numseats - 1] == numseats);
    free(seats);

    return ret;
}

int main()
{
    int numseats, iterations;

    srand (1);

    cout << "number of seats?" << endl;
    cin >> numseats;
    cout << "number of iterations?" << endl;
    cin >> iterations;

    int succeed = 0;
    int i;
    for (i = 0; i < iterations; i++) {
        if (run(numseats)) {
            succeed++;
        }
    }

    cout <<("last guy sat in last seat %.2f%% of the time\n", (float)succeed / iterations) << endl;


    return 0;
}
