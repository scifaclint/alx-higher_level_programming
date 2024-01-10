#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct StatusCode - status code struct
 * @code: status code
 * @count: count of status code
 * @next: pointer to the next node
 */
typedef struct StatusCode
{
	char *code;
	int count;
	struct StatusCode *next;
} StatusCode_t;

/* Function Prototypes */
void print_statistics(StatusCode_t *head, size_t total_size);
StatusCode_t *add_or_update_status_code(StatusCode_t **head, char *code);

/**
 * main - entry point
 *
 * Return: always 0
 */
int main(void)
{
	char *line = NULL;
	size_t len = 0;
	ssize_t n_read;
	size_t total_size = 0, line_count = 0;
	StatusCode_t *head = NULL;
	int i;

	while ((n_read = getline(&line, &len, stdin)) != -1)
	{
		char *token;
		char *status_code;
		size_t size;

		token = strtok(line, " ");
		for (i = 0; token != NULL; i++)
		{
			if (i == 7)
				status_code = strdup(token);
			if (i == 8)
				size = atoi(token);
			token = strtok(NULL, " ");
		}

		total_size += size;
		add_or_update_status_code(&head, status_code);
		free(status_code);

		line_count++;
		if (line_count % 10 == 0)
			print_statistics(head, total_size);
	}

	print_statistics(head, total_size);

	free(line);
	while (head != NULL)
	{
		StatusCode_t *temp_node = head;

		head = head->next;
		free(temp_node->code);
		free(temp_node);
	}

	return (0);
}

/**
 * print_statistics - prints the statistics
 * @head: pointer to the first node
 * @total_size: total size
 */
void print_statistics(StatusCode_t *head, size_t total_size)
{
	printf("File size: %lu\n", total_size);
	while (head != NULL)
	{
		printf("%s: %d\n", head->code, head->count);
		head = head->next;
	}
}

/**
 * add_or_update_status_code - adds a new node or updates an existing one
 * @head: pointer to pointer to the first node
 * @code: status code
 *
 * Return: pointer to the new node
 */
StatusCode_t *add_or_update_status_code(StatusCode_t **head, char *code)
{
	StatusCode_t *temp = *head;
	StatusCode_t *new_node;

	while (temp != NULL)
	{
		if (strcmp(temp->code, code) == 0)
		{
			temp->count++;
			return (temp);
		}
		temp = temp->next;
	}

	new_node = malloc(sizeof(*new_node));
	if (new_node == NULL)
	{
		perror("malloc failed");
		return (NULL);
	}
	new_node->code = strdup(code);
	new_node->count = 1;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}
