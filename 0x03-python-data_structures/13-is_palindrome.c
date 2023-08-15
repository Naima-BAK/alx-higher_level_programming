#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer.
 * Return: 0 != palindrome, 1 = palindrome.
 */
int is_palindrome(listint_t **head)
{
listint_t *myList = *head, *the_palindrome = *head;
int i = 0, j = 0, n = 0;

if (!*head)
{
return (1);
}

while (myList)
{
myList = myList->next;
n++;
}

myList = *head;

for (i = 1; i <= n; i++)
{
for (j = i; j <= n - i; j++)
the_palindrome = the_palindrome->next;
if (myList->n != the_palindrome->n)
return (0);
myList = myList->next;
the_palindrome = myList;
}

return (1);

}
