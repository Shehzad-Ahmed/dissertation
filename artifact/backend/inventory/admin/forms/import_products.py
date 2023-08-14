from django.forms import Form, FileField


class ProductImportForm(Form):
    """
    Product import form class used for bulk imports.
    """

    import_file = FileField(label="Import CSV", required=True)
