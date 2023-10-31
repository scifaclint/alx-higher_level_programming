#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * * struct listint_s - singly linked list
 * * @n: integer
 * * @next: points to the next node
 * *
 * * Description: singly linked list node structure
 * * for ALX project
 * *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */