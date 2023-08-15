#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - Print some basic info about Python lists
 * @p: PyObject
 *
 * Return: Nothing
 */

/*PyObject is a type in the C programming language that */
/*represents a generic Python object*/

void print_python_list_info(PyObject *p)
{
PyObject *objectP;
PyListObject *listP = (PyListObject *)p;
int index, length, memory;

length = Py_SIZE(p);
memory = listP->allocated;
printf("[*] length of List = %d\n", length);
printf("[*] allocation = %d\n", memory);

for (index = 0; index < length; index++)
{
objectP =  PyList_GetItem(p, index);
printf("Element %d: %s\n", index, Py_TYPE(objectP)->tp_name);
}
}
