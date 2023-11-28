#include <stdio.h>
#include <stdlib.h>

/**
 * can_place - Check if a queen can be placed at the given position.
 * @cols: The column indices where the queens are placed.
 * @ocuppied_rows: The number of occupied rows.
 *
 * Return: 1 if a queen can be placed at the given position, 0 otherwise.
 */
int can_place(int *cols, int ocuppied_rows)
{
	int i;

	for (i = 0; i < ocuppied_rows; i++)
	{
		if (cols[i] == cols[ocuppied_rows] ||
				cols[i] - i == cols[ocuppied_rows] - ocuppied_rows ||
				cols[i] + i == cols[ocuppied_rows] + ocuppied_rows)
		{
			return (0);
		}
	}
	return (1);
}

/**
 * place_queen - Place a queen in the given row.
 * @cols: The column indices where the queens are placed.
 * @start: The starting row index.
 * @end: The ending row index (the size of the chessboard).
 * @result: The result list that contains all possible solutions.
 * @solution_count: The number of solutions found.
 *
 * Return: None.
 */
void place_queen(int *cols, int start, int end,
		int **result, int *solution_count)
{
	int i;

	if (start == end)
	{
		for (i = 0; i < end; i++)
		{
			result[*solution_count][i] = cols[i];
		}
		(*solution_count)++;
		return;
	}
	for (i = 0; i < end; i++)
	{
		cols[start] = i;
		if (can_place(cols, start))
		{
			place_queen(cols, start + 1, end, result, solution_count);
		}
	}
}

/**
 * print_result - Print the result.
 * @result: The result list that contains all possible solutions.
 * @n: The number of queens and the size of the chessboard.
 * @solution_count: The number of solutions found.
 *
 * Return: None.
 */
void print_result(int **result, int n, int solution_count)
{
	int i, j;

	for (i = 0; i < solution_count; i++)
	{
		printf("[");
		for (j = 0; j < n; j++)
		{
			printf("[%d, %d]", j, result[i][j]);
			if (j != n - 1)
			{
				printf(", ");
			}
		}
		printf("]\n");
	}
}

/**
 * solve_nqueens - Solve the N queens problem.
 * @n: The number of queens and the size of the chessboard.
 *
 * Return: None.
 */
void solve_nqueens(int n)
{
	int *cols;
	int **result;
	int solution_count = 0;
	int i;

	if (n < 4)
	{
		printf("N must be at least 4\n");
		return;
	}
	cols = malloc(n * sizeof(int));
	result = malloc(10000 * sizeof(int *));
	for (i = 0; i < 10000; i++)
	{
		result[i] = malloc(n * sizeof(int));
	}
	place_queen(cols, 0, n, result, &solution_count);
	print_result(result, n, solution_count);
	free(cols);
	for (i = 0; i < 10000; i++)
	{
		free(result[i]);
	}
	free(result);
}

/**
 * main - Entry point.
 * @argc: The number of command line arguments.
 * @argv: The command line arguments.
 *
 * Return: 0 if successful, 1 otherwise.
 */
int main(int argc, char **argv)
{
	int n;

	if (argc != 2)
	{
		printf("Usage: nqueens N\n");
		return (1);
	}
	n = atoi(argv[1]);
	if (n == 0)
	{
		printf("N must be a number\n");
		return (1);
	}
	solve_nqueens(n);
	return (0);
}
