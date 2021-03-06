import sys
import os
import re
import pprint

mail_first_pat = "[\w\'.'\-]+\@[\w\' '\-]{2,}\.[\w\-]+"
mail_sec_pat = "[\w\'.'\-]+\@[\w\-]+\.[\w\-]+\.[\w\-]+"
phone_first_pat = "[0-9]{3}[\-\' '\')']+[0-9]{3}[\-\' '\')'][0-9]{4}"
phone_sec_pat = '[0-9]{3,4}'
"""
TODO
"""
def process_file(name, f):
    res = []
    for line in f:
        m = re.sub(' (?:dt|dot) ', '.', line)
        m = re.sub(' at ', '@', m)
        m = re.sub(' \. ', '.', m)
        m = re.sub(' @ ', '@', m)
        #m = re.sub(' ', '', m)
        email_matches = re.findall(mail_first_pat,m)
        email_matches.extend(re.findall(mail_sec_pat , m))
        email_matches.extend(re.findall(mail_sec_pat , m))

        if email_matches:
            email_matches[-1] = re.sub('-', '', email_matches[-1])
            email_matches[-1] = re.sub(' ', '.', email_matches[-1])
            res.append((name , 'e' , email_matches[-1]))


        phone_matches = re.findall(phone_first_pat , line)

        for p in phone_matches:
            phone_match = re.findall( phone_sec_pat , p)
            phone = '%s-%s-%s' % (phone_match[0], phone_match[1], phone_match[2])
            res.append((name, 'p', phone))

    return res


def process_dir(data_path):
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path,fname)
        f = open(path,'r' , encoding='latin-1')
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)

    return guess_list

def get_gold(gold_path):
    # get gold answers
    gold_list = []
    f_gold = open(gold_path,'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list


def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    print('True Positives (%d): ' % len(tp))
    pp.pprint(tp)
    print('False Positives (%d): ' % len(fp))
    #pp.pprint(fp)
    print('False Negatives (%d): ' % len(fn))
    #pp.pprint(fn)
    print('Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn)))

def main(data_path, gold_path):
    guess_list = process_dir(data_path)
    gold_list =  get_gold(gold_path)
    score(guess_list, gold_list)


if __name__ == '__main__':
    if (len(sys.argv) == 1):
        main('../data/dev', '../data/devGOLD')
    elif (len(sys.argv) == 3):
        main(sys.argv[1],sys.argv[2])
    else:
        print('usage:\tSpamLord.py <data_dir> <gold_file>')
        sys.exit(0)
