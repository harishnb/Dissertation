# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:12:06 2018

@author: harisbha
"""
import math


dic_screenId = {"id1":10,"id2":2,"id3":30};
sum_ids = sum(dic_screenId.values())
print (sum_ids)

#var_screenId = {}


def tf_calculation(p_screenId):
    for j in (p_screenId):
        temp_res = p_screenId[j]/sum(p_screenId.values())
        tf_val = round(temp_res,4)
        print (j,"=",tf_val)
        tf_values[j]=tf_val

        
def idf_calculation(p_doc_list):
    global master_screen_id_count
    global master_screen_id_log_value
    print ("====debug==")
    for x in range (len(p_doc_list)):
        if x == 0:
            master_screen_id_count = {key:1 for key in p_doc_list[x]}
            print("masterid for 0==",master_screen_id_count)
        else:
            print ("x=",x)
            updated_value = {}
            for i in p_doc_list[x].keys():
                if i in updated_value:
                    continue
                elif  i in master_screen_id_count:
                    master_screen_id_count[i] = master_screen_id_count[i] + 1
                    updated_value[i] = 1
                else:
                    master_screen_id_count[i] = 1
   # print ("<<masterid>>",master_screen_id_count)
    var_total_doc = len(total_doc);
   # print ("Total doc=",var_total_doc);
    for j in master_screen_id_count:
        temp_res = round(math.log(var_total_doc/master_screen_id_count[j],10),4)
        master_screen_id_log_value[j]= temp_res
   # print ("==masterid_log_values=",master_screen_id_log_value)
    print 
        
        
def tf_idf(p_doc_list):
    global master_screen_id_log_value
    global var_tf_idf
    for x in range (len(doc_list)):
     temp_val = doc_list[x]
     #print (temp_val)
     #print (master_screen_id)
     for y in (temp_val):
         temp_res= round((temp_val[y]*master_screen_id_log_value[y]),4)
         print(y,"=",temp_res,"=",temp_val[y],"*",master_screen_id_log_value[y],"count=",master_screen_id_count[y])
         if y in var_tf_idf:
             var_tf_idf[y] = round(((temp_res + var_tf_idf[y])),4)
         else:
             var_tf_idf[y] = temp_res
     
     for y in (var_tf_idf):
         print (y,"=",var_tf_idf[y],"/",master_screen_id_count[y])
         var_tf_idf[y] = round(var_tf_idf[y]/master_screen_id_count[y],4)
         
            
             

             
    
print ("=====Start========")    
doc1 = ["this","is","a","a","sample","junk","text","validate","python","program"];
doc2 = ["this","is","another","another","example","example","example"];
doc3 = ["my","is","a","another","sample","example","a","the"];
doc4 = ["this","is","my","test","tf-idf","python","example","program"]
var_tf_idf = {}

tf_values ={}
doc_list = []
master_screen_id_log_value = {}
master_screen_id_count = {}
total_doc = [];
total_doc.append(doc1)
total_doc.append(doc2)
total_doc.append(doc3)
total_doc.append(doc4)
print (len(total_doc))
for x in range (len(total_doc)):
    var_screenId = {}
    doc_len = len(total_doc[x])
    print ("x=",x,doc_len)
    tf_values = {}
    for y in range (doc_len):
        var_id = total_doc[x][y]
        var_count = total_doc[x].count(var_id)
        #print ("v=",total_doc[x][y]," count=",var_count)
        var_screenId [var_id] = var_count
    print (sum(var_screenId.values()))
    print (var_screenId)
    tf_calculation(var_screenId)
    print (tf_values)
    doc_list.append(tf_values)
print ("=======Final values===")
print (doc_list)
idf_calculation(doc_list)
tf_idf(doc_list)
#print("Master screen count" , master_screen_id_count)
#print("master_screen_id_log_value" , master_screen_id_log_value)
print(var_tf_idf)      
        
        
    