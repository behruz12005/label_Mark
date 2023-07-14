from django.shortcuts import render, redirect
from .forms import MyForm
import pandas as pd



def my_view(request):
    sentences = None 
    df = pd.read_csv('data_collage.csv')
    row = df[df['Labels'] == 'Nan'].iloc[0].name
    sentences = df.iloc[row]['uzbek Comment']
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            my_value = form.cleaned_data['my_field']
            df.loc[[row], ['Labels']] = my_value
            df.to_csv('data_collage.csv', index=False)
            return redirect('home')
    else:
        form = MyForm()
    
    return render(request, 'home.html', {'form': form, 'sentences': sentences})
