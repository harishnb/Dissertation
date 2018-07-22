# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:16:51 2018

@author: harisbha
"""

#!/usr/bin/python
import os
import re
import sys
import csv
import math
import operator

    
re_stbId = re.compile(r'<<(.*?)<<(.*)')
re_time = re.compile(r'(.*)>>(.*)')
var_headings = ["ID"] + ["Time"] + ["ScreenName"] + ["ActiveTime"]
var_prv_time = 0
var_prv_stbId = "0"
var_doc_list =[]
var_variable_list = [];
var_screen_time_list = {};
var_screen_time_spent_per_session = [];
var_total_time_spent_per_session = [];
var_avg_time_each_screen = {}
var_time_spent = 0;
sys.stdout=open("output_tfidf.txt","w")

def calculate_tf_idf() :
    exec(open('tf_idf_calculate.py').read())  

def store_total_time_spent():
    with open('output/time_spent.csv', 'w', newline='') as myCsvFile:
         csvWriter = csv.writer(myCsvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
         var_headings = ["session"]+["Time"]
         csvWriter.writerow(var_headings)
         for i in range (len(var_total_time_spent_per_session)):
             var_row = [i]+[var_total_time_spent_per_session[i]]
             csvWrite = csv.writer(myCsvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
             csvWrite.writerow(var_row)
    myCsvFile.close()


#def store_time_spent_session():
#    with open('time_spent_each_session.csv', 'w', newline='') as myCsvFile:
#         csvWriter = csv.writer(myCsvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#         var_headings = ["session"]+["Time"]
#         csvWriter.writerow(var_headings)
#         for i in range (len(var_total_time_spent_per_session)):
#             var_row = [i]+[var_total_time_spent_per_session[i]]
#             csvWrite = csv.writer(myCsvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#             csvWrite.writerow(var_row)
#    myCsvFile.close()


def calculate_avg_time_spent():
    global var_avg_time_each_screen
    var_master_count = {}
    for i in range (len(var_screen_time_spent_per_session)):
#        print(var_screen_time_spent_per_session[i])
        for y in var_screen_time_spent_per_session[i]:
            if i==0:
                var_avg_time_each_screen[y] = var_screen_time_spent_per_session[i][y]
                var_master_count[y] = 1
            else:
                if y in var_avg_time_each_screen:
                    var_avg_time_each_screen[y] = var_avg_time_each_screen[y] + var_screen_time_spent_per_session[i][y]
                    var_master_count[y] = var_master_count[y] + 1
                else:
                    var_avg_time_each_screen[y] = var_screen_time_spent_per_session[i][y]
                    var_master_count[y] = 1
#            print (y,"=","var_avg_time_each_screen[y]",var_avg_time_each_screen[y],"=",var_screen_time_spent_per_session[i][y])

    print ("master count", var_master_count)
    print ("var_avg_time_each_screen[y]", var_avg_time_each_screen)
    with open('output/Avg_time_spent.csv', 'w', newline='') as myCsvFile:
        csvWriter = csv.writer(myCsvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        var_headings = ["Screen_id"]+["Avg_Time"]
        csvWriter.writerow(var_headings)
        var_final_sorted = sorted(var_avg_time_each_screen.items(), key=lambda kv: kv[1],reverse=True)
        print("======var final sorted===",var_final_sorted)
        for x in range (len(var_final_sorted)):
             print("==",var_final_sorted[x][0],":",var_final_sorted[x][1])
             var_row = [var_final_sorted[x][0]]+[var_final_sorted[x][1]]
             csvWrite = csv.writer(myCsvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
             csvWrite.writerow(var_row)
#        for j in (var_final_sorted):
#            var_avg_time_each_screen[j] = round((var_final_sorted[j]/var_master_count[j]),2)
#            #print (j,"=",var_avg_time_each_screen[j])
#            var_row = [j]+[var_avg_time_each_screen[j]]
#            csvWrite = csv.writer(myCsvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#            csvWrite.writerow(var_row)
    myCsvFile.close()
            
#        
    
with open('output/data.csv', 'w', newline='') as myCsvFile:
    csvWriter = csv.writer(myCsvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    csvWriter.writerow(var_headings)
    for dir, subdirs, files in os.walk(os.curdir):
        for filename in files:
            path = os.path.join(dir, filename)
            if (path.endswith(".py")):
                continue
            with open(path,encoding='cp850') as log:
                #print ("============",path,"============")
                var_variable_list= []
                var_time_spent = 0
                var_screen_time_list = {}
                for line in log:
                    if line.isspace():continue
                    mvar = re_stbId.search(line)
                    if mvar:
                        var_row = ""
                        var_diff = 0
                        tmp = line.split("<<",2)
                        var_stbId = tmp[1]
                        # Get the STB ID and remove blank spaces
                        var_stbId = var_stbId.replace(" ","")
                        
                        # Extract the  Time and screenName   
                        tmp2 = tmp[2].split(">>",2)
                        
                        if len(tmp2) >= 2:
                            
                            #If the previous and current STB IDs are different then reset previous time
                            if var_stbId != var_prv_stbId:
                                #print ("!!Reset")
                                var_prv_time = 0
                                var_prv_stbId = var_stbId
                                
                            tmp3 = tmp2[0]
                            tmp4 = tmp3.split(':',4)
                            
                            #Time extracted
                            var_time = tmp4[3]
                            
                            #Screen Name extracted
                            var_screenName = tmp2[1].rstrip()
                            
                            #calculate the time diff in each screen
                            if (var_prv_time != 0):
                                var_diff = int(var_time) - int(var_prv_time)
                                if (var_diff < 0 ):
                                    var_diff = 0;
                                #print (var_time, var_prv_time, var_diff)
                            var_row = [var_stbId] +[var_time] + [var_screenName] + [var_diff]
                            
                            tmp_screen_time = (var_screenName, var_diff)
                            if var_screenName in var_screen_time_list:
                                var_screen_time_list[var_screenName] =  var_screen_time_list[var_screenName] + var_diff
                            else:
                                var_screen_time_list[var_screenName] = var_diff
                               
                            var_time_spent = var_time_spent + var_diff
                            var_variable_list.append(var_screenName)
                            var_prv_time = var_time
                           # print (var_row)
                            csvWrite = csv.writer(myCsvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                            csvWrite.writerow(var_row)
            if (len(var_variable_list)>0):
                #print ("filename = " ,filename)
                var_doc_list.append(var_variable_list)
                var_total_time_spent_per_session.append(var_time_spent)
                var_screen_time_spent_per_session.append(var_screen_time_list)
                
myCsvFile.close()

print ("sum of time spent in each session per screen")
print (var_screen_time_spent_per_session)
calculate_tf_idf()
store_total_time_spent()
calculate_avg_time_spent()

sys.stdout.close()
sys.exit(1)
    
