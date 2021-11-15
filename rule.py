from utilities import *
from flask import request
import collections

def rule_existence():
    a = request.form["act1"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile()   
    result = []
    for act in segments:
        if a in act:        
            result.append(act)
        else : 
            if act not in removeSegment:
                removeSegment.append(act)    
    writeOnSegmentFile(result)   
    writeOnRemoveSegmentFile(removeSegment) 
    return result, removeSegment

def rule_absence():
    a = request.form["act1"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile()   
    result = []
    for act in segments:
        if a not in act:
            result.append(act)
        else : 
            if act not in removeSegment:
                removeSegment.append(act)    
    writeOnSegmentFile(result)   
    writeOnRemoveSegmentFile(removeSegment) 
    return result, removeSegment

def rule_choice():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    result = []
    for act in segments:
        if a in act or b in act:
            result.append(act)
        else : 
            if act not in removeSegment:
                removeSegment.append(act)     
    writeOnSegmentFile(result)   
    writeOnRemoveSegmentFile(removeSegment)
    return result, removeSegment

def rule_exclusive_choice():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    result = []
    for act in segments:
        if a in act and b not in act:
            result.append(act)
        elif b in act and a not in act:
            result.append(act)
        else : 
            if act not in removeSegment:
                removeSegment.append(act)     
    writeOnSegmentFile(result)   
    writeOnRemoveSegmentFile(removeSegment)
    return result, removeSegment
     
def rule_responded_existence():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    result = []
    for act in segments:
        if b not in act and a  not in act:
            result.append(act)
        elif a in act and b in act:
            result.append(act) 
        elif a not in act:
            result.append(act)  
        else : 
            if act not in removeSegment:
                removeSegment.append(act)     
    writeOnSegmentFile(result)   
    writeOnRemoveSegmentFile(removeSegment)
    return result, removeSegment

def rule_response():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    result = []
    for act in segments:
        if a in act and b in act:
            position_a = act.index(a)
            position_b = act.index(b)     
            if position_b > position_a:
                result.append(act) 
        elif a not in act:
            result.append(act)   
        else : 
            if act not in removeSegment:
                removeSegment.append(act)     
    writeOnSegmentFile(result)   
    writeOnRemoveSegmentFile(removeSegment)
    return result, removeSegment

def rule_alternate_response():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    result = []
    for act in segments:
        if a in act and b in act:
            counter = collections.Counter(act)
            if counter[a] == 1:
                position_a = act.index(a)
                position_b = act.index(b)     
                if position_b > position_a:
                    result.append(act) 
            elif counter[a] > 1:
                list_a = []
                list_b = []
                count = -1
                for elem in act:
                    count += 1
                    if elem == a:
                        list_a.append(count)
                    elif elem == b:
                        list_b.append(count)            
                i = 0
                j = 0
                for i in range(len(list_a)-1):
                    for j in range(len(list_b)-1):
                        if list_a[i] < list_b[j] and list_b[j] < list_a[i+1]and list_b[j+1] > list_a[i+1]:
                            result.append(act)
        elif a not in act:
            result.append(act)  
        else : 
            if act not in removeSegment:
                removeSegment.append(act)     
    writeOnSegmentFile(result)   
    writeOnRemoveSegmentFile(removeSegment)
    return result, removeSegment

def rule_chain_response():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    result = []
    for act in segments:
        if a in act and b in act:
            counter = collections.Counter(act)
            if counter[a] == 1:
                for elem in range(len(act)-1):
                    if act[elem] == a and act[elem+1] == b:
                        result.append(act) 
            elif counter[a] > 1:
                list_a = []
                list_b = []
                count = -1
                for elem in act:
                    count += 1
                    if elem == a:
                        list_a.append(count)
                    elif elem == b:
                        list_b.append(count)            
                i = 0
                j = 0
                for i in range(len(list_a)):
                    for j in range(len(list_b)):
                        if list_a[i] + 1 == list_b[j]:
                            if act not in result:
                                result.append(act) 
                        else:
                            if act in result: 
                                result.remove(act)
                           
        elif a not in act:
            result.append(act)   
        else : 
            if act not in removeSegment:
                removeSegment.append(act)     
    writeOnSegmentFile(result)   
    writeOnRemoveSegmentFile(removeSegment)
    return result, removeSegment

def rule_precedence():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    result = []
    for act in segments:
        if a in act and b in act:
            position_a = act.index(a)
            position_b = act.index(b)     
            if position_b > position_a:
                result.append(act) 
        elif b not in act:
            result.append(act)  
        else : 
            if act not in removeSegment:
                removeSegment.append(act)     
    writeOnSegmentFile(result)   
    writeOnRemoveSegmentFile(removeSegment)
    return result, removeSegment

def rule_alternate_precedence():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    result = []
    for act in segments:
        if a in act and b in act:
            counter = collections.Counter(act)
            if counter[b] == 1:
                position_a = act.index(a)
                position_b = act.index(b)     
                if position_a < position_b:
                    result.append(act) 
            elif counter[b] > 1:
                list = []
                for elem in act:
                    if elem == a:
                        list.append(a)
                    elif elem == b:
                        list.append(b)            
                i = 0
                j = 0
                for i in range(len(list)-1):
                    if list[i] != list[i+1] and act not in result:
                        result.append(act)
                    elif list[i] == a and list[i+1] == a and act not in result:
                        result.append(act)
                    elif list[i] == b and list[i+1] == b and act in result:
                        result.remove(act)
                        break      
        elif b not in act:
            result.append(act)
        else : 
            if act not in removeSegment:
                removeSegment.append(act)     
    writeOnSegmentFile(result)   
    writeOnRemoveSegmentFile(removeSegment)
    return result, removeSegment
    
def rule_chain_precedence():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    result = []
    for act in segments:
        if a in act and b in act:
            counter = collections.Counter(act)
            if counter[b] == 1:
                position_a = act.index(a)
                position_b = act.index(b)     
                if position_a < position_b:
                    result.append(act) 
            elif counter[b] > 1:
                list_a = []
                list_b = []
                count = -1
                for elem in act:
                    count += 1
                    if elem == a:
                        list_a.append(count)
                    elif elem == b:
                        list_b.append(count)            
                i = 0
                j = 0
                for i in range(len(list_b)):
                    for j in range(len(list_a)):
                        if list_a[j] + 1 == list_b[i]:
                            if act not in result:
                                result.append(act)
                        else:
                            if act in result:
                                result.remove(act) 
        elif b not in act:
            result.append(act) 
        else : 
            if act not in removeSegment:
                removeSegment.append(act)     
    writeOnSegmentFile(result)   
    writeOnRemoveSegmentFile(removeSegment)
    return result, removeSegment        