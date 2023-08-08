#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head of the list.
 * @number: number.
 * Return: the pointer tothe new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *my_node;
new_node = malloc(sizeof(listint_t));

if (new_node == NULL)
return (NULL);
new_node->n = number;
new_node->next = NULL;
if (*head == NULL || number < (*head)->n)
{
new_node->next = *head;
*head = new_node;
}
else
{
my_node = *head;
while (my_node->next != NULL &&
my_node->next->n < number)
{
my_node = my_node->next;
}
new_node->next = my_node->next;
my_node->next = new_node;
}

return (new_node);
}
