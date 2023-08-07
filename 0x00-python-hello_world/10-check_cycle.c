#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the list.
 * Return: 0 or 1.
 */
int check_cycle(listint_t *list)
{
listint_t *myNode, *is_cycle;
if (list == NULL || list->next == NULL)
return (0);
myNode = list;
is_cycle = list->next;
while (myNode != is_cycle)
{
if (is_cycle == NULL || is_cycle->next == NULL)
return (0);
myNode = myNode->next;
is_cycle = is_cycle->next->next;
}
return (1);
}
