#include <Python.h>
#include <stdio.h>

/* Function Prototypes */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic information about a Python list
 * @p: Pointer to a PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	long int size, alloc;
	int i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = (((PyListObject *)p)->ob_item[i]);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: Pointer to a PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size;
	int i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:", size < 10 ? size + 1 : 10);

	for (i = 0; i < size + 1 && i < 10; i++)
		printf(" %02hhx", str[i]);

	printf("\n");
}
