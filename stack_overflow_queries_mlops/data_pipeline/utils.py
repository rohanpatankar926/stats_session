#convert the xml to json
#read_json file
import os 
import json
import xmltodict
import sys
sys.path.append(os.getcwd())
import random
import re
import tqdm
from xml.etree import ElementTree

#convert the xml data to the json data
def convert_xml_to_json(file_path):
    try:
        with open(file_path,"r") as data:
            xml_data=xmltodict.parse(data.read())
        return xml_data
    except Exception as e:
        raise e

def save_json_xml(input_file, output_path):
    try:
        output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(output_dir, exist_ok=True)
        data = convert_xml_to_json(input_file)
        json_data = json.dumps(data)  # convert JSON data to a string
        with open(f"{output_dir}/{output_path}", "w") as f:
            f.write(json_data)  # write the string to file
    except Exception as e:
        raise e

def save_json(data,output_file_name):
    try:
        data_save=json.dump(data,open(output_file_name,"w"))
        return data_save
    except Exception as e:
        raise e

def read_json_data(file_path):
    try:
        with open(file_path,"r") as data:
            cvat_data=json.load(data)
        return cvat_data
    except Exception as e:
        raise e



def process_data(data_in,data_out_train,data_out_test,target_tag,split):
    try:
        line_num=1
        for line in tqdm(data_in):
            f_output=data_out_train if random.random()>split else data_out_test
            print(f_output)
            attr=ElementTree.fromstring(line).attrib
            pid=attr.get("Id","")
            label =1 if target_tag in attr.get("Tags","") else 0
            title=re.sub(r"\s+"," ",attr.get("Title","")).strip()
            body=re.sub(r"\s+"," ",attr.get("Title","")).strip()
            text=title+ " "+body
            f_output.write(f"{pid}\t{label}\t{text}")
            line_num+=1
    except Exception as e:
        raise e

if __name__=="__main__":
    data_path=os.path.join(os.getcwd(),"main_data","data.xml")
    print(process_data(data_in=data_path,data_out_train="data.tsv",data_out_test="data_test.tsv",target_tag="<python>",split=0.25))