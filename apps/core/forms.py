from django import forms

class GeneralForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GeneralForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            widget = self.fields[field].widget
            class_name = "form-control"
            if isinstance(widget, forms.widgets.SelectMultiple):
                class_name = "form-control select2-multiple"
            elif isinstance(widget, forms.widgets.Select):
                class_name = "form-control select2"
            elif isinstance(widget, forms.widgets.CheckboxInput):
                class_name = "form-check-input"
            self.fields[field].widget.attrs.update({
                'class': class_name,
                'col_default': 6
            })