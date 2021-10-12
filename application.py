#Links:

#Plotly
#https://www.datacamp.com/community/tutorials/learn-build-dash-python
#https://plotly.com/python/getting-started/
#Multiple graphs: https://stackoverflow.com/questions/63459424/how-to-add-multiple-graphs-to-dash-app-on-a-single-browser-page

#World-o-meter:
#https://www.worldometers.info/world-population/

#API:

#------------------------------------------------------

#Package Installations:
#dash, requests, dash-renderer

from flask import Flask, render_template

import dash
from dash import dcc
from dash import html

import requests  
import pandas as pd
import plotly.graph_objects as go

application = app = Flask(__name__)

app = dash.Dash(__name__)

import plotly.express as px
figpop2019 = px.bar(
    x=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
    'Illnois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
    'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
    'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'], 
    
    y=[4903185, 731545, 7278717, 3017825, 39512223, 5758736, 3565287, 973764, 21477737, 10617423, 1415872, 1787065,
                12671821, 6732219, 3155070, 2913314, 4467673, 4648794, 1344212, 6045680, 6949503, 9986857, 5639632, 2976149, 6137428, 1068778,
                1934408, 3080156, 1359711, 8882190, 2096829, 19453561, 10488084, 762562, 11689100, 3956971, 4217737, 12801989,
                1059361, 5148714, 884659, 6833174, 28995881, 3205958, 623989, 8535519, 7614893, 1792147, 5822434, 578759],
    
    
    labels=dict(x="State", y="Population in 2019")
)

figpop2019.update_layout(title_text="Population of Each State in 2019")
figpop2019.show()

figpop2020 = px.bar(
    x=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
    'Illnois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
    'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
    'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'], 
    
    y=[5024279, 733391, 7151502, 3011524, 39538223, 5773714, 3605944, 989948, 21538187, 10711908, 1455271, 1839106, 12812508, 6785528,
    3190369, 2937880, 4505836, 4657757, 1362359, 6177224, 7029917, 10077331, 5706494, 2961279, 6154913, 1084225, 1961504, 3104614,
    1377529, 9288994, 2117522, 20201249, 10439388, 779094, 11799448, 3959353, 4237256, 13002700, 1097379, 5118425, 886667, 6910840, 29145505,
    3271616, 643077, 8631393, 7705281, 1793716, 5893718, 576891],
    
    
    labels=dict(x="State", y="Population in 2020")
)

figpop2020.update_layout(title_text="Population of Each State in 2020")
figpop2020.show()



app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='What is Smoking?'),
        html.Div(children='''
            Smoking is when people inhale smoke from a source such as a cigarette, electronic cigarette or cigar.
            People afterwards exhale the smoke. 
        '''),
    ]),

    html.Div([
        html.H1(children='When did Smoking first start?'),
        html.Div(children='''
            Smoking originated from tobacco’s popularity. In 1492, Christopher Columbus met with Native Americans and saw they used tobacco for medicinal treatment. 
            After Columbus landed in Portugal after his meetings with the Natives, he showed Europeans what tobacco was used for and they started to use tobacco for smoking [1]. 
            Europe popularized smoking since the late 15th century which encourage other people from across the world to smoke. 
            In the early 20th century, cigarettes containing tobacco were being sold, though in 1964 a Surgeon’s Report declared smoking can deteriorate a person’s health badly [2].
            Today people still smoke cigarettes or cigars that contain tobacco.  
        '''),
    ]),

    html.Div([
        html.H1(children='Why do People Smoke'),
        html.Div(children='''
            People start smoking for various reasons.  People often see their family, friends or others smoke which influences them to start smoking or they think smoking can relive their stress from the problems they currently face. 
            Smoking habits often occur due to social influence.   
        '''),
    ]),

    html.Div([
        html.H1(children='What is in a Cigarette'),
        html.Div(children='''
            A cigarette has 599 ingredients! Some of the ingredients include Benzene, 2-napthylamine, 4-aminobiphenyl and more chemicals humans shouldn’t digest [3].
            Due to consuming these chemicals, smokers increase their chances of developing one or more diseases.   
        '''),
    ]),

    html.Div([
        html.H1(children='Smoking Disadvantages'),
        html.Div(children='''
            Smoking can cause the following:
            '''),
        html.Div(children='''
            Changes in behavior due to the urge to smoke
            '''),
        html.Div(children='''
            Expensive
            '''),
        html.Div(children='''
            Develop more diseases, problems breathing, energy
            '''),
        html.Div(children='''
            Aging and Physical Appearance Changes
            '''),
        html.Div(children='''
            Smoking leaves a strong smell non-smokers do not like
            '''),
        html.Div(children='''
            Possible second-hand smoke exposure to others
            '''),
    ]),

    html.Div([
        html.H1(children='Diseases'),
        html.Div(children='''
            Smoking can cause the following diseases:
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Lung Cancer
        '''),
    ]),

    html.Div([
        html.Div(children='''
            COPD: Chronic Obstructive Pulmonary Disease
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Heart Disease
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Stroke
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Asthma
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Diabetes
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Blindness
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Cataracts
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Age-Related Macular Degeneration
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Colon Cancer
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Cervix Cancer
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Liver Cancer
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Stomach Cancer
        '''),
    ]),

    html.Div([
        html.Div(children='''
            Pancreatic Cancer
        '''),
    ]),


    html.Div([
        html.H1(children='Smoking Statistics'),
        html.Div(children='''
               
        '''),


        html.Div([

        dcc.Graph(
            id='graph1',
            figure=figpop2019
        ),  
        ]),

        html.Div([

        dcc.Graph(
            id='graph2',
            figure=figpop2020
        ),  
        ]),

    ]),

    html.Div([
        html.H1(children='Why People Continue to Smoke'),
        html.Div(children='''
            People continue to smoke cigarettes since it has an addictive chemical called nicotine. 
            Nicotine is responsible for changing the nervous system which why people often see smokers have changes in their mood or behavior. [6]  
        '''),
    ]),

    html.Div([
        html.H1(children='Getting Help Today'),
        html.Div(children='''
             There are organizations dedicated to help people quit smoking. Please contact the CDC or Quit.com for assistance.  
        '''),
    ]),


    



    # New Div for all elements in the new 'row' of the page
    # html.Div([
    #     html.H1(children='Hello Dash'),

    #     html.Div(children='''
    #         Dash: A web application framework for Python.
    #     '''),

    #     dcc.Graph(
    #         id='graph2',
    #         figure=fig1
    #     ),  
    # ]),

])

if __name__ == "__main__":
    app.run_server(host='localhost', port = 8050, debug=True)