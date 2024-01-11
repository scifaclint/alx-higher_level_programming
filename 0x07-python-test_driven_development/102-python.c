#include <Python.h>

/**
 * print_python_string - Prints Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	wchar_t *str;

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	str = PyUnicode_AsWideCharString(p, &len);
	printf("  type: %s\n", (PyUnicode_IS_COMPACT_ASCII(p) ?
				"compact ascii" : "compact unicode object"));
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", str);
}
