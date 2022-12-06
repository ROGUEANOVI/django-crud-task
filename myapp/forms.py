from django import forms

class CreateNewTask(forms.Form):
  title = forms.CharField(label="Titulo de tarea", widget=forms.TextInput(attrs={'class':'input'}), max_length=200,required=True)
  description = forms.CharField( label="Descripcion de tarea",widget=forms.Textarea(attrs={'class':'input'}))

class CreatenewProject(forms.Form):
  name = forms.CharField(label="Nombre del proyecto", widget=forms.TextInput(attrs={'class':'input'}), max_length=200,required=True)