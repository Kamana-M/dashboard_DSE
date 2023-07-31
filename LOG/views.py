from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import openpyxl 
from django.shortcuts import HttpResponse


# Create your views here.

#What we do here gonna affect the url where index is
def LOG(request):
    return render(request,"log.html")

def CARDS(request):
    #Charger les données
    df=pd.read_excel(
	io="Dashboard actuel.xlsx",
	engine='openpyxl',
	sheet_name='Elev_effec',
	skiprows=0,
	usecols='A:J',
	nrows=631,
)	
    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"',"")
	
    context = { 'table_data':table_content}
    return render(request, 'cards.html', context=context)
