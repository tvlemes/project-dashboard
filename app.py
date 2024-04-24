'''
Analise de Dados com Streamlit

Autor: `Thiago Vilarinho Lemes`
Data: `23/04/2024`
'''

# import the necessary packages
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import seaborn as sns
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))

# set the web app page name (optional)
st.set_page_config(page_title='WEB APP DATA', page_icon=None, layout="wide")

# set markdown
st.markdown('# Visualização dos Dados')

# read the data
data_path = pd.read_csv ('./dataset/Housing.csv')
data_path.columns = data_path.columns.str.upper() # convert the columns to uppercase 

# write a text or comment ( the number of "#" symbols used determines the text size.)
st.write( '### 1. Visão geral dos Dados ')

# view the dataframe in streamlit
st.dataframe(data_path, use_container_width=True)

st.write( '### 2. Compreendendo os Dados ')

# creating sidebar and radio button simultaneously
selected = st.sidebar.radio("**O que você quer saber sobre os Dados?**", 
                            ["Descrição", "Amostra de Dados", "5 Primeiros Registros", "5 Últimos Registros", "Total de Linhas e Colunas"])

if selected == 'Descrição':
    st.dataframe(data_path.describe(), use_container_width=True)  # shows the basic data descriptive
elif selected == 'Amostra de Dados':
    st.dataframe(data_path.sample(10), use_container_width=True)  # select random rows

elif selected == '5 Primeiros Registros':
    st.dataframe(data_path.head(), use_container_width=True)  # shows the head of the dataframe 

elif selected == '5 Últimos Registros':
    st.dataframe(data_path.tail(), use_container_width=True)  # shows the head of the dataframe 
else:
    st.write('###### Total de Linhas e Colunas respectivamentes:',data_path.shape)  # shows the data shape 

# creating tabs 
tab1, tab2 = st.tabs(["PANDASPROFILE ANALYSIS","SWEETVIZ ANALYSIS"])

with tab1:
  # load the saved html file ( visualized using pandasprofile library)
  analysis_report1= open("./html/analysis_report_profilereport.html", 'r', encoding='utf-8')
  components.html(analysis_report1.read(), height=8000, width=1000, scrolling=False)
  
with tab2:
# load the saved html file ( visualized using sweetviz library)
  analysis_report2= open("./html/analysis_with_sweetviz.html", 'r', encoding='utf-8')
  components.html(analysis_report2.read(), height=8000, width=1500, scrolling=False)

##### Option-2 : make partial manual data visualization and show particular graphs

numerical_features = data_path.select_dtypes(exclude= 'object').columns 
categorical_features = data_path.select_dtypes('object').columns 

# creating mutiselect tab in the left sidebar
graph_options = st.sidebar.multiselect( "SELECIONE O TIPO DE GRÁFICO:", options=['HISTOGRAM','COUNT-PLOT','BOX-PLOT'], default=['HISTOGRAM','COUNT-PLOT','BOX-PLOT'])

# creating three columns to display on the streamlit web 

# creating three columns to display the graphs in three column
col1,col2,col3 = st.columns(3)

# defining columns to display in the streamlit
col1.write( '##### Histogram Plot ')
col2.write( '##### Box Plot ')
col3.write( '##### Count Plot')

categorical_features = data_path.select_dtypes('object').columns 

# if histogram is selected, show the histogram for each numerical feature
if  'HISTOGRAM' in graph_options:
    for feature in numerical_features: # looping to 
        fig1 = plt.figure()
        # plot the historgram graph 
        sns.histplot(data=data_path, x=feature, color="black") 
        col1.pyplot(fig1)

# if box plot is selected, display the box plot for each categorical features
if  'BOX-PLOT' in graph_options:
    for feature in categorical_features:
        fig2 = plt.figure()
        sns.boxplot( x=feature, y='PRICE',data=data_path, palette="Set1")
        # sns.catplot( data=data,x=feature, y='PRICE', kind="boxen")
        col2.pyplot(fig2)

# if count plot selected on the mulitselect, create count plot for each categorical features
if  'COUNT-PLOT' in graph_options:
    for feature in categorical_features:
        fig3 = plt.figure()
        sns.countplot(x=feature, data=data_path, palette="Set3")
        col3.pyplot(fig3)