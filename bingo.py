#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from random import sample
import uuid
import subprocess, os

# global variables for reading content from files
with open("source.txt", "r") as source:
    sourceLines = source.readlines()

with open("prefix.txt", "r") as pre:
    prefix = pre.read()

with open("postfix.txt", "r") as post:
    postfix = post.read()

with open("image.txt", "r") as img:
    image = img.read()

def insert_content_in_latex_table_structure(f, list_of_items, i):
    for item in list_of_items:
        content = item + "&";
        
        # signify new row at the end of the list
        if item == list_of_items[-1]:
            content = item + "\\\\\hline\n"
        
        # table is a 5 x 5 squares - the square in the middle is a heart
        elif item == list_of_items[2] and i == 2:
            content = image
      
        f.write(content)

def create_tex_files():
    # create tex files based on content in provided text files
    generated = []

    # file has hash in its name to avoid overwriting existing files by mistake
    file_name = "bingo%s.tex" % str(uuid.uuid4())[:8]

    # for each file, append content from text files
    with open(file_name, "w+") as f:
        f.write(prefix)
        for i in range(5):
            # we don't want to add items from the source multiple times
            # so only sample from the source the first time
            if i == 0:
                random_sample = random.sample(sourceLines, 5)
            # otherwise, compare to the list containing generated items
            # and only add new items that is not in the list of generated items
            else:
                not_in_list = [x for x in sourceLines if x not in generated]
                random_sample = random.sample(not_in_list, 5)

            generated.extend(random_sample)
            
            insert_content_in_latex_table_structure(f, random_sample, i)

        f.write(postfix)
    return file_name
     

def generate_PDFs_from_tex(file_name):
    cmd = ['xelatex', '--halt-on-error', file_name]
    latex = subprocess.Popen(cmd, shell=False,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    message = latex.communicate()[0] #get the stdout

def delete_tmp_files(file_name):
    # we are only interested in keeping the pdf files, delete other files
    raw_file_name = os.path.splitext(file_name)[0]
    logfile = "%s.log" % raw_file_name
    auxfile = "%s.aux" % raw_file_name
    texfile = "%s.tex" % raw_file_name
    os.remove(logfile)
    os.remove(auxfile)
    os.remove(texfile)
    
def main():
    file_name = create_tex_files()
    generate_PDFs_from_tex(file_name)
    delete_tmp_files(file_name)

if __name__ == "__main__":
    main()
