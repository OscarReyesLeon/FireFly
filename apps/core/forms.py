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

    def validate_unique_field(self, field, value):
        if not field.unique:
            return
        qs = self.Meta.model.objects
        try:
            qs = qs.filter(**{field.name:
                 value.upper() if isinstance(value, str) else value})
        except:
            qs = qs.none()
        if self.instance.pk is not None:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError({
                field.name: 'Ya existe un registro con este valor'
            })
        
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if field in cleaned_data:
                try:
                    current_field = self._meta.model._meta.get_field(field)
                except:
                    continue
                self.validate_unique_field(
                    current_field,
                    cleaned_data[field]
                )
        return cleaned_data
            

class GeneralFormVue(GeneralForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'v-model': 'form.' + field,
            })
