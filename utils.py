from stemmer import *

def contains_illegal_characters(text):
    if '@' in text:
        return True
    if '#' in text:
        return True
    if '<' in text:
        return True
    if ':' in text:
        return True
    if ';' in text:
        return True
    if '\'' in text:
        return True
    if '*' in text:
        return True
    if '&' in text:
        return True
    if '$' in text:
        return True
    return False

def preprocess_data(file_name):
    word_tag = []
    filtered_text = []
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            if line[0].isdigit():
                line_split = line.split('\t')
                if (line_split[3] != '_' and line_split[3] != 'SYM') and not contains_illegal_characters(line_split[2]):
                    filtered_text.append(line_split[2])
                    word_tag.append(line_split[3])
    return filtered_text, word_tag

def get_stem_dicts(filtered_text, word_tag):
    stem_counter_dict = dict()
    stem_tag_dict = dict()
    counter = 0

    for line in filtered_text:
        stems = stem_arr(line)
        if stems[0] in stem_counter_dict:
            stem_counter_dict[stems[0]]+=1
        else:
            stem_counter_dict[stems[0]]=1
            stem_tag_dict[stems[0]]=word_tag[counter]
        counter+=1

    return stem_counter_dict, stem_tag_dict

def extract_stopwords(stem_counter_dict, ratio=0.05):

    if ratio < 0 or ratio > 1:
        raise Exception('Invalid parameter value.','Must be >0 and <1.')
    stem_sorted = sorted(stem_counter_dict.items(), key=lambda x: x[1], reverse=True)
    number_of_stopwords = int(round(ratio*len(stem_sorted)))
    stopwords = stem_sorted[:number_of_stopwords]
    return stopwords
