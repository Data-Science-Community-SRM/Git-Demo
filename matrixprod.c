#include<stdio.h>


int main(){
    int r1,c1,r2,c2;
    printf("Enter the number of rows and columns for matrix 1: ");
    scanf("%d %d", &r1,&c1);
    printf("Enter the number of rows and columns for matrix 2: ");
    scanf("%d %d", &r2, &c2);

    if(c1!=r2){
        printf("Column of the first matrix is not equal to the second matrix\n");
        return 0;
    }
    
    //Entering first matrix elements
    int a[r1][c1], b[r2][c2], res[r1][c2];
    printf("Enter the elements of the first matrix\n");
    for(int i=0; i<r1; i++){
        for(int j=0; j<c1; j++){
            scanf("%d", &a[i][j]);
        }
    }

    //Entering second matrix elements
    printf("Enter the elements of the second matrix\n");
    for(int i=0; i<r2; i++){
        for(int j=0; j<c2; j++){
            scanf("%d", &b[i][j]);
        }
    }

    //Multiplying them
    for(int i=0; i<r1; i++){
        for(int j=0; j<c2; j++){
            res[i][j]=0;
            for(int k=0; k<c1; k++){
                res[i][j] += a[i][k]*b[k][j];
            }
        }
    }

    //Printing the result matrix 
    printf("The Result matrix is:\n");
    for(int i=0; i<r1; i++){
        for(int j=0; j<c2; j++)
            printf("%d ", res[i][j]);
        printf("\n");

    }

    return 0;
}
