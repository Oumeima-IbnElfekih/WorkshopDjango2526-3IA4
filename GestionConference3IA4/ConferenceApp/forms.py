from django import forms
from .models import Conference

class ConferenceModel(forms.ModelForm):
    class Meta:
        model=Conference
        fields =['name','theme','description','location','start_date','end_date']
        labels = {
            'name':"Titre de la conférence",
            'theme':"Thématiques",
            'description':"Description",
            'location':"Location",
            'start_date':"Date début de la conférence",
            'end_date':"Date fin de la conférence",
        }
        widgets ={
            'name': forms.TextInput(
                attrs= {
                    'placeholder' :"Ex - Conférence IA"
                }
            ),
                'start_date' : forms.DateInput(
                  attrs= {
                      
                      'type':'date',
                      'placeholder':"date de début"
                  }  
                ),
                 'end_date' : forms.DateInput(
                  attrs= {
                      'type':'date',
                      'placeholder':"date de fin"
                  }  
                )
        }