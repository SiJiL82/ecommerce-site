from django import forms
from .models import Request

class NewRequestForm(forms.ModelForm):
  class Meta:
    model = Request
    fields = (
      'category',
      'size',
      'description',
    )
    widgets = {
      'description': forms.Textarea(attrs={
        'rows': 4
      })
    }
  
  def __init__(self, *args, **kwargs):
    super(NewRequestForm, self).__init__(*args, **kwargs)
    self.fields['category'].label = 'Category:'
    self.fields['size'].label = 'Size:'
    self.fields['description'].label = 'Description:'



  #   name = CharField(max_length=254)
  # email_address = models.EmailField()
  # category = models.ForeignKey('products.Category', null=True, blank=True, on_delete=models.SET_NULL)
  # size = models.CharField(
  #   max_length=254,
  #   choices = SIZE_CHOICES
  # )
  # description = models.TextField()
  # date_created 