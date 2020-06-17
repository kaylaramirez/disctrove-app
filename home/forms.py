from django import forms

class SearchForm(forms.Form):
    search_terms = forms.CharField(required=True, label="", widget=forms.TextInput(
                                attrs={ 'class': 'form-control form-control-sm',
                                        'placeholder': 'Basic Search',
                                        'aria-label': 'basic search', }))

#class AdvancedSearchForm(forms.Form):
#    manufacturer
