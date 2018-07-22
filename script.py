# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:00:46 2018

@author: Harish
"""

import pandas as pd
import matplotlib.pyplot as plt
import warnings


warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = 8,4

data = pd.read_csv('tf_idf_values.csv')
data_time_spent = pd.read_csv('time_spent.csv')
avg_time_spent = pd.read_csv('Avg_time_spent.csv')

with open("output/stat_index.html", mode='w') as html:
    starting_lines = ["<!DOCTYPE html>",
                      '<html lang="en" dir="ltr">',
                      '<head>',
                      '<meta charset="utf-8">',
                      '<title>GUI Measurement</title>',
                      '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">'
                      '</head>',
                      '<body>',
                      '<div class="container"> <h3>GUI Measurement</h3>',
                      '</div>',
                      '<div class="container">',
                      ]
    ending_lines = ['</div>',
                    '</body>',
                    '</html>',]
    html.writelines(starting_lines)
    body_lines = []
    body_lines.append('<table><tr>')
    
    body_lines.append('<td>')
    body_lines.append('<table><tr><th></th><th>GUI</th><th>Priority</th></tr>')
    for idx in list(range(0,len(data))):
          body_lines.append('<tr><td>{}</td><td>{}  </td><td> {} </td></tr>'.format(idx+1, data.GUI[idx], data.Priority[idx]))
    body_lines.append('</table></td>')
    
    body_lines.append('<td> <object type="image/svg+xml" data="static/images/Avg_chart.svg"> Your browser does not support SVG </object></td>')
#    body_lines.append('<td> <img width=800 height=500 src="plot1.png"></td>')
    
    body_lines.append('</tr> </table>')
    
    body_lines.append('<td>')
    body_lines.append('<table><tr><th>Session</th><th> </th><th> </th><th>Avg time</th></tr>')

    for idx1 in list(range(0,len(data_time_spent))):
        body_lines.append('<tr><td>{}</td><td>{}  </td><td> {}</td><td> {} </td></tr>'.format(idx1+1, " ","           ", data_time_spent.Time[idx1]))
    body_lines.append('</table></td>')
    #body_lines.append('<img width=800 height=500 src="test.png">')
    
    body_lines.append('<td>')
    body_lines.append('<table><tr><th>Screen ID </th><th> </th><th>Avg time</th></tr>')

    for idx1 in list(range(0,len(avg_time_spent))):
        body_lines.append('<tr><td>{}</td><td>{}  </td><td> {} </td></tr>'.format(avg_time_spent.Screen_id[idx1],"         ",avg_time_spent.Avg_Time[idx1]))
    body_lines.append('</table></td>')
    
    html.writelines(body_lines)
    html.writelines(ending_lines)
