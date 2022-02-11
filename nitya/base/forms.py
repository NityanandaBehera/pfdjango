from django.forms import ModelForm
from django import forms
from.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link',
                  'source_link', 'tags', 'featured_img', ]

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


def __ini__(self, *args, **kwargs):
    super(ProjectForm, self).__init__(*args, **kwargs)
    for name, field in self.fields.items():
        field.widget.attrs.update({'class': input})
    #self.fields['title'].widget.attrs.update({'class': 'input'})
