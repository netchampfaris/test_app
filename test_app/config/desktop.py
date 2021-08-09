from frappe import _

def get_data():
	return [
		{
			"module_name": "Test App",
			"color": "orange",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Test App")
		}
	]
