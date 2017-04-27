
#include<stdio.h>

/* Searches the element x in mat[][]. If the element is found,
    then prints its position and returns true, otherwise prints
    "not found" and returns false */
int search(int mat[][5], int n, int x)
{
   int i = 0, j = n-1;  //set indexes for top right element
   while ( i < n && j >= 0 )
   {
      if ( mat[i][j] == x )
      {
         printf("\n Found at %d, %d", i, j);
         return 1;
      }
      if ( mat[i][j] > x )
        j--; //move left
      else //  if mat[i][j] < x
        i++; //move down
   }

   printf("\n Element not found");
   return 0;  // if ( i==n || j== -1 )
}

// driver program to test above function
int main()
{
  int mat[4][5] = { {10, 20, 30, 40, 60},
                    {15, 25, 35, 45, 70},
                    {27, 29, 37, 48, 80},
                    {32, 33, 39, 50, 90},
                  };
  search(mat, 5, 37);
  getchar();
  return 0;
}
