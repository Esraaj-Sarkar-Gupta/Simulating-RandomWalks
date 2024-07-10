#include <stdio.h>
#include <stdlib.h> // For rand()
#include <time.h>

int walk(); // Function prototype

int main() {

    int Number_of_Elements = 100;
    int Number_of_Iterations = 100;

    printf("> [Setting]: Number of independent elements: %i \n", Number_of_Elements);
    printf("> [Setting]: Number of iterations: %i \n", Number_of_Iterations);

    int ElementsX[Number_of_Elements]; // Array to hold all the elements that are to be simulated
    int Positions_Log[Number_of_Iterations][Number_of_Elements]; // Fixed size array

    for (int i = 0; i < Number_of_Elements; i++) {
        ElementsX[i] = i; // Place each element along the X axis
    }

    int Pos[Number_of_Elements]; // Array to hold the positions of each element

    for (int i = 0; i < Number_of_Elements; i++) {
        Pos[i] = 0; // The initial positions of every element is 0
    }

    clock_t start_time = clock();

    for (int t = 0; t < Number_of_Iterations; t++) {

        for (int i = 0; i < Number_of_Elements; i++) {
            int move = walk();
            int new_position = Pos[i] + move;
            Pos[i] = new_position;
        }

        for (int j = 0; j < Number_of_Elements; j++) {
            Positions_Log[t][j] = Pos[j]; // Store each element of Pos in Positions_Log
        }
    }

    clock_t end_time = clock();
    double CPU_usetime =((double) (end_time - start_time)) / CLOCKS_PER_SEC;
    printf("> Positions generated and logged. CPU time used: %f seconds\n" , CPU_usetime);

    FILE *file;

    file = fopen("results.txt", "w");
    if (file == NULL) {
        printf("[Error]: cannot open file results.txt\n");
        return 1;
    }
    for (int t = 0 ; t < Number_of_Iterations ; t++) {
        fprintf(file , "%d:" , t);
        for (int j = 0 ; j < Number_of_Elements; j++){
            fprintf(file , "%d,", Positions_Log[t][j]);
        }
        fprintf(file , ":");
    }
    fclose(file);
    printf("> Logged positions written into file result.txt\n");

    return 0;
}

int walk() {
    int direct;
    int random_num = rand() % 3; // Random number between 0 and 2 (inclusive)

    if (random_num == 0) {
        direct = 0;
    } else if (random_num == 1) {
        direct = 1;
    } else if (random_num == 2) {
        direct = -1;
    }
    return direct;
}