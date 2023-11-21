#include <Python.h>

/* Function Prototypes */
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - A function that prints some basic info
 * about Python lists.
 * @p: PyObject list
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	printf("[*] Python list info\n");
	fflush(stdout);
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}

	list = (PyListObject *)p;
	size = ((PyVarObject *)p)->ob_size;

	printf("[*] Size of the Python List = %ld\n", size);
	fflush(stdout);
	printf("[*] Allocated = %ld\n", list->allocated);
	fflush(stdout);
	for (i = 0; i < size; i++)
	{
		item = *((PyObject **)(list->ob_item) + i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		fflush(stdout);
		if (strcmp(item->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(item);
		else if (strcmp(item->ob_type->tp_name, "float") == 0)
			print_python_float(item);
	}
}

/**
 * print_python_bytes - A function that prints some basic info
 * about Python bytes.
 * @p: PyObject bytes
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	PyBytesObject *bytes;
	char *str;

	printf("[.] bytes object info\n");
	fflush(stdout);
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}

	bytes = (PyBytesObject *)p;
	str = bytes->ob_sval;
	size = ((PyVarObject *)p)->ob_size;

	printf("  size: %ld\n", size);
	fflush(stdout);
	printf("  trying string: %s\n", str);
	fflush(stdout);
	printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
	fflush(stdout);
	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf(" %02hhx", str[i]);
		fflush(stdout);
	}
	printf("\n");
	fflush(stdout);
}

/**
 * print_python_float - A function that prints some basic info
 * about Python floats.
 * @p: PyObject float
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	fflush(stdout);
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n", PyOS_double_to_string(value, 'r', 0,
				Py_DTSF_ADD_DOT_0, NULL));
	fflush(stdout);
}
