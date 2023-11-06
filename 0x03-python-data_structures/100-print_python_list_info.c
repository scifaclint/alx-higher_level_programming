#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a Python list
 * @p: PyObject pointer representing a Python list
 *
 * This function prints information about the Python list provided. It displays
 * the size of the list and the allocated memory, followed by the type of
 * elements and their indices in the list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list = (PyListObject *)p;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; ++i)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
	}
}
