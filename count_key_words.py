import os
path_key=os.path.join(os.getcwd(),"key_word")
path_content=os.path.join(os.getcwd(),"key_words_content")
def get_outkey(path):
    with open(path,mode="r",encoding="utf8")as f:
        s=f.readlines()
    for iss in s:
        keys=iss.split()
        yield keys[0]
def get_outline(path):
    with open(path,mode="r",encoding="utf8")as f:
        s = f.readlines()
    for iss in s:
        lines = iss.split()
        yield lines[0]
def count_it(path_cont,key_words):
    final_work={}
    for keyword in get_outkey(key_words):
        final_work[keyword]=0
    for lines in get_outline(path_cont):
        for keyword in get_outkey(key_words):
            n=lines.count(keyword)
            final_work[keyword]+=n
    return final_work
if __name__ == '__main__':
    print(count_it(path_content,path_key))
