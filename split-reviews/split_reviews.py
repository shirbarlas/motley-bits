"""
SplitReviews:
   This script takes 2 files:
   1. commiters file which contains a list of names that can commit code.
       alice
       #bob
       carl
   2. reviwers file which contains a list of names that should review this code

   Usage:
   python split_reviewers.py -c <committers_file> -r <reviewers_file>

"""
#!/bin/python

import random
import sys
import getopt


class Person(object):

    def __init__(self, name, group):
        self._name = name
        self._group = group

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.name == other.name and self.group == other.group

    def __repr__(self):
        return str(self._name)

    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group


class SplitReviews(object):

    commiters = []
    reviewers = {}

    def __init__(self, committers_file, reviewers_file):
        self._init_committers_list(committers_file)
        self._init_reviewers_dict(reviewers_file)

    def _init_committers_list(self, committers_file):
        self.committers = self._file_to_list(committers_file)

    def _init_reviewers_dict(self, reviewers_file):
        reviewers_list = self._file_to_list(reviewers_file)
        self.reviewers = {reviewer: [] for reviewer in reviewers_list}

    def _file_to_list(self, file_name):
        dummy_list = []
        with open(file_name, 'r') as fd:
            for line in fd:
                if not line.startswith('#') and line:
                    dummy_list.append(self.create_person(line))
        random.shuffle(dummy_list)
        return dummy_list

    def create_person(self, line):
        name, group = line.replace('\n', '').replace(' ', '').split(',')
        return Person(name, group)



    def split_evenly_or_almost_evenly(self):
        random.shuffle(self.committers)
        div = len(self.committers)/float(len(self.reviewers))
        return [self.committers[int(round(div * i)): int(round(div * (i + 1)))]
                for i in xrange(len(self.reviewers))]

    def who_review_whom(self):
        ppl_to_be_reviewed = self.split_evenly_or_almost_evenly()
        the_reviewers = self.reviewers.keys()
        random.shuffle(the_reviewers)
        for reviewer in the_reviewers:
            random.shuffle(ppl_to_be_reviewed)
            group_to_review = random.choice(ppl_to_be_reviewed)
            self.reviewers[reviewer] = group_to_review
            ppl_to_be_reviewed.remove(group_to_review)

    def print_reviewer_and_reviewee(self):
        for reviewer, group_to_review in self.reviewers.items():
            print("%s to review %s" % (reviewer, group_to_review))


def main(argv):
    committers = ''
    reviewers = ''
    try:
        if len(argv) == 0:
            raise getopt.GetoptError("No arguments given")
        opts, args = getopt.getopt(argv, "hc:r:", ["committers=", "reviewers="])
    except getopt.GetoptError:
        print 'split_reviewers.py -c <committers_file> -r <reviewers_file>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'split_reviewers.py -c <committers_file> -r <reviewers_file>'
            sys.exit()
        elif opt in ("-c", "--committers"):
            committers = arg
        elif opt in ("-r", "--reviewers"):
            reviewers = arg
    x = SplitReviews(committers, reviewers)
    x.who_review_whom()
    x.print_reviewer_and_reviewee()

if __name__ == "__main__":
    main(sys.argv[1:])
