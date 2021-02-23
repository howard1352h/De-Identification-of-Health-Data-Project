# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:33:04 2020

@author: user
"""
import pandas as pd 
import math
import re
import numpy as np
def strip_str(s):
    return s.strip()
def split_str_n(s):
    return s.split('\n',1)

def split_str_t(s):
    a = s.split('\t')
    if a[1]!='start_position':
        a.insert(1,int(a.pop(1)))
            
    return a

def list_to_str(l):
    result=''
    for n,i in enumerate(l):
        if n !=4:       
            result += str(i)+'\t'
        else :
            result += str(i)
            
    return result   

def takeSecond(elem):
    return elem[1]   

# type_dict = {}
# wordnet_2 = pd.read_csv(r"G:\共用雲端硬碟\AI-CUP\Dataset\修改.csv",encoding='big5')
# wordnet_2.fillna(value=0, inplace=True)
# cols = wordnet_2.columns.values
# first_name ='''王，李，張，劉，陳，楊，黃，吳，趙，周，徐，孫，馬，朱，胡，林，郭，何，高，羅，鄭，梁，謝，宋，唐，許，鄧，馮，韓，曹，
# 曾，彭，蕭，蔡，潘，田，董，袁，於，余，
# 葉，蔣，杜，蘇，魏，程，呂，丁，沈，任，
# 姚，盧，傅，鍾，姜，崔，譚，廖，范，汪，
# 陸，金，石，戴，賈，韋，夏，邱，方，侯，
# 鄒，熊，孟，秦，白，江，閻，薛，尹，段，
# 雷，黎，史，龍，陶，賀，顧，毛，郝，龔，
# 邵，萬，錢，嚴，賴，覃，洪，武，莫，孔'''
# first_names=''
# for i in first_name:
#     if i != '，' and i != '\n':
#         first_names += i
# first_names = '['+first_names+']'
# for col in cols:
    
#     type_list =[w for w in wordnet_2[col] if w != 0]

#     for w in type_list :
#         type_dict[w] = col
    
# keys=(str(type_dict.keys())[11:-2]).split(',')
type_dict = {'B肝':'others','C肝':'others','愛滋病':'others','糖尿病':'others','梅毒':'others'}
keys=(str(type_dict.keys())[11:-2]).split(',')
with open(r'G:\共用雲端硬碟\AI-CUP\手動label\train_1227_v2.txt','r',encoding='utf-8') as f :
            data = f.read()
                        
paragraph = list(map(strip_str,data.split('--------------------')))
paragraphs = list(map(split_str_n,paragraph))

for p in range(len(paragraphs)):
    article,sent,label_old =p,paragraphs[p][0],paragraphs[p][1]
    label_new  = label_old.split('\n')

    label_new_item = list(map(split_str_t,label_new))[1:]
    

    label_new_pos =[]
    for j in label_new_item:
        label_new_pos.append(j[1])
    add_item= []
    for word in keys:
        word = word.strip()[1:-1]
        for i in range(len(sent)-len(word)):
                if sent[i:i+len(word)] == word:
                    add_item.append([p,i,i+len(word),word,type_dict[word]])

    print(add_item)
                  
    
    if add_item !=[]:
        for i in range(len(add_item)):
            
            if add_item[i][1] not in label_new_pos:                
                label_new_item.append(add_item[i])
                
    label_new_item.sort(key = takeSecond)     
    result = list(map(list_to_str,label_new_item))
            
    label_new_str ='article_id\tstart_position\tend_position\tentity_text\tentity_type\n'
    s_end='--------------------'+'\n'
    for a in result:
        label_new_str += a + '\n'
    new_result = '\n'+sent+'\n'+ label_new_str +'\n'+s_end
             
    with open('train_1227_v3.txt','a',encoding = 'utf-8') as a:
        a.write(new_result)
   

            
    

####################################################################
# wordnet_1 = pd.read_csv(r"G:\共用雲端硬碟\AI-CUP\Dataset\修改v2.csv",encoding='utf-8')
# wordnet_1.fillna(value=0, inplace=True)
# cols = wordnet_1.columns.values
# w = np.array(wordnet_1)
# w = dict(wordnet_1)

# for word in keys:
#         word = word.strip()[1:-1]
#         if 'X' in word:
#             word = word.replace('X','\w')
#             print(word)
            

# sent='醫師：成大系統系父親節11.56最近還好嗎？民衆37度j五千：ok啊。醫師：啊，好，都還好。啊那你爲什麽戴這種N95。www.pssrep.gov民衆：這是朋友給的。醫師：哦，真的？民衆：這是N95嗎？醫師：這是N95啊。好，看起來是……我們看一下……你一陣子沒有抽血了勒？民衆：上一次有。醫師：上一次有？但是還沒看到報告對不對？民衆：還沒還沒。醫師：你的2月20號血糖是78，第8號然後肝功能，血脂肪……哇！年輕啦，都沒問題。我看一下……C肝沒問題，A肝已經有抗體了。但是，你B肝的抗體不夠，www.dcl.qwrgg.ss有沒有……有沒有建議，我有沒有給你講建議說，建議可以打，打疫苗。民衆：沒有欸。是之前有打過一次嘛？忘記了，很久了。醫師：還是A肝？你有沒有考慮打個B肝疫苗？民衆：下一次回診的時候啊。還是這一次？醫師：唔……它要打，打三劑……就是……對啊，第96號就是可能你要……看一下哦，我是覺得能打最好，因爲我們臺灣B肝的人很多哦。民衆：好。醫師：看一下他的時辰，好像今天打完一個月後跟第六個月，所以，第一周，今天嘛，然後四周后，然後24周后，這樣子。不過這個要自費大概500塊，0960-711-242一次大概500塊。不然今天打一打好不好？民衆192.168.157.1：好。醫師：你同意嗎？民衆：可以。醫師：可以哦。你家裏有沒有人B、C肝炎？民衆：不知道欸。醫師：沒有齁，啊還好啦，這個不太會痛這樣子。就是第一劑，然後一個月後是打第二劑，然後第六個月之後是第三劑這樣。所以你會，下，下一個月會多，多來一次這樣，這樣可以嗎？民衆：可以。醫師：好啊，那我們就……民衆：下個月是幾號？等下再談嗎？醫師：嗯，下個月的話假如是4月20號……還是你要……可以嗎？還是？民衆：可能要5月。醫師：可能要5月。那我們就5月初。那你家裏還有沒有剩藥？民衆：有。醫師：兩個禮拜夠不夠？民衆：夠吧。醫師：夠一個半月嗎？因爲假如是約5月1號的話……那就是六周，就，就怕你藥不夠。民衆：比較少，那應該提早。醫師：提早哦，5月……再早一點……四個禮拜，要不然就四個禮拜，好哦？民衆：4月17？醫師：提早打應該ok，提早一個禮拜打ok。4月17哦？你工作還好嗎？民衆：還好，比較忙。醫師：哇，那不錯。民衆：沒有受到影響。醫師：沒有受到疫情的影響這樣子，今天是3月20號第一劑，那這裏你打過之後有免疫力，大概就不太會受到B肝的感染這樣子。民衆：ok。醫師：那我們今天就開四個禮拜的藥，然後今天去打流感這樣，啊不是，是打B肝這樣子。好哦，因爲抗體不夠，因爲你的B肝，B的抗體小於2.1，太低。民衆：狀況都還好？醫師：嗯，其他都還好。肝腎功能血糖都很好。然後病毒的，病毒要變得很小。2月20號病毒是測不到。民衆：嘿。醫師：然後這個血液的CD4是371。民衆：那時候是感冒。醫師：哦，難怪，會稍微低一點。民衆：感冒會這樣？醫師：哦，會。你的免疫系統。民衆：C那個什麽，剛好感冒。醫師：剛好感冒哦，因爲那時候可能免疫系統都消耗在跟感冒病毒對抗這樣子，ok。'
# #aa=[]
# add_item = []
# for word in keys:
#         p =2
#         word = word.strip()[1:-1]
#         if 'X' in word:          
#             if type_dict[word] == 'time':
#                 if word == 'XX節':
#                     word_replace = word.replace('X','[\w]')
#                     m = re.findall(word_replace,sent)
#                     for w in m:
#                         for i in range(len(sent)-len(word)):
#                             if sent[i:i+len(word)] == w:
#                                 add_item.append([p,i,i+len(word),w,type_dict[word]])
                                                
#                     #aa.append(m)  
#                 else:
#                     word_replace = word.replace('X','[一二三四五六七八九零日\d{1,2}]+')
#                     m = re.findall(word_replace,sent)
#                     for w in m:
                        
#                         for i in range(len(sent)-len(w)):
#                             if sent[i:i+len(w)] == w:
#                                 add_item.append([p,i,i+len(word),w,type_dict[word]])
#                     #aa.append(m)  
                
#             if type_dict[word] == 'education':
#                 word_replace = word.replace('X','[\w]')
#                 m = re.findall(word_replace,sent)
#                 for w in m:
#                         for i in range(len(sent)-len(word)):
#                             if sent[i:i+len(word)] == w:
#                                 add_item.append([p,i,i+len(word),w,type_dict[word]])
#                 #aa.append(m)  
            
#             if type_dict[word] == 'name':
#                 word_replace = word.replace('X','[\w]')
#                 m = re.findall(word_replace,sent)
#                 for w in m:
#                         for i in range(len(sent)-len(word)):
#                             if sent[i:i+len(word)] == w:
#                                 add_item.append([p,i,i+len(word),w,type_dict[word]])
#                 #aa.append(m)  
                
            
#             if type_dict[word] == 'med_exam':
#                 word_replace = word.replace('X','[一二三四五六七八九零\d+]')
#                 m = re.findall(word_replace,sent)
#                 for w in m:
#                         for i in range(len(sent)-len(w)):
#                             if sent[i:i+len(w)] == w:
#                                 add_item.append([p,i,i+len(w),w,type_dict[word]])
#                 #aa.append(m)  
            
            
#             if type_dict[word] == 'money':
#                 word_replace = word.replace('X','[一二三四五六七八九零\d{1:7}]+')
#                 m = re.findall(word_replace,sent)
#                 for w in m:
#                         for i in range(len(sent)-len(w)):
#                             if sent[i:i+len(w)] == w:
#                                 add_item.append([p,i,i+len(w),w,type_dict[word]])
#                 #aa.append(m)  
                
#             if type_dict[word] == 'ID':
#                 word_replace = word.replace('X','[一二三四五六七八九零\d{1,4}]+')
#                 m = re.findall(word_replace,sent)
#                 for w in m:
#                         for i in range(len(sent)-len(w)):
#                             if sent[i:i+len(w)] == w:
#                                 add_item.append([p,i,i+len(w),w,type_dict[word]])
#                 #aa.append(m)  
            
#             if type_dict[word] == 'contact':
#                 if word[0:3] == 'www':
#                     word_replace = word.replace('X','[A-Za-z0-9]+')
#                 else :
#                     word_replace = word.replace('X','[\d]')
#                 m = re.findall(word_replace,sent)
#                 for w in m:
#                         for i in range(len(sent)-len(w)):
#                             if sent[i:i+len(w)] == w:
#                                 add_item.append([p,i,i+len(w),w,type_dict[word]])
                #aa.append(m)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            