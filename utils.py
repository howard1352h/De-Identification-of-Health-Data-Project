import logging, sys, argparse


def str2bool(v):
    # copy from StackOverflow
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_entity(tag_seq, char_seq):
    all_start_position,all_end_position,all_entity_text,all_entity_type = get_position_entity(tag_seq, char_seq)
#    all_predict = []
#    all_start_position = []
#    all_end_position = []
#    label_list = ["name","location","time","contact",
#              "ID","profession","biomarker","family","clinical_event",
#              "special_skills","unique_treatment","account","organization",
#              "education","money","belonging_mark","med_exam","others"]
#    for i in label_list:
#        predict,start_position,end_position = get_type_entity(i,tag_seq, char_seq)
#        all_predict.append(predict)
#        all_start_position.append(start_position)
#        all_end_position.append(end_position)
        

    return  all_start_position,all_end_position,all_entity_text,all_entity_type

"""
locals()返回具有(key, value)对的dict-，一个在本地范围内声明的变數字典
而value是變數本身的值(例如数字1，另一个dict，函数，类等)。
"""

def get_position_entity(tag_seq, char_seq):

    length = len(tag_seq)
    all_entity_type = []
    all_start_position = []
    all_end_position = []
    all_entity_text = []
    
    for i in range(length):
        tag = str(tag_seq[i])
        # 代表有找到
        if str(tag_seq[i])[:2]=="B-":
            entity_type = tag[2:]
            text = char_seq[i]
            start_position = i
            for j in range(i+1, length):
                if str(tag_seq[j])[:2]=="I-":
                    text = text + char_seq[j]
                else:
                    end_position = j
                    break
            all_entity_type.append(entity_type)
            all_start_position.append(start_position)
            all_end_position.append(end_position)
            all_entity_text.append(text)
    return all_start_position,all_end_position,all_entity_text,all_entity_type 

    
        
        
            
            



#def get_type_entity(desire_type,tag_seq, char_seq):
#    length = len(tag_seq)
#    predict_result = []
#    position_start_result = []
#    position_end_result = []
#    for i in range(length):
#        Btype = 'B-'+ desire_type
#        Itype = 'I-'+ desire_type
#        char = ''
#        if tag_seq[i] == Btype:
#            start_position = i
#            char = char_seq[i]
#            for j in range(i+1, length):
#                if tag_seq[j] == Itype:
#                    char = char + char_seq[j]
#                elif tag_seq[j] != Itype:
#                    end_position = j
#                    break
#            position_start_result.append(start_position)
#            position_end_result.append(end_position)
#            predict_result.append(char)
#    return predict_result,position_start_result,position_end_result



def get_logger(filename):
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.getLogger().addHandler(handler)
    return logger
