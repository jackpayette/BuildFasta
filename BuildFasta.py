#!/usr/bin/env python3
# coding: utf-8
from Bio import SeqIO
import sys
seqiter = SeqIO.parse(open(sys.argv[1]), 'fasta')      
keepers = {}
with open(sys.argv[2], "r") as id_handle:
    for curr_id in id_handle:
        keepers[curr_id.strip()] = True
keeper_seqs = [x for x in seqiter if x.id in keepers]
SeqIO.write(keeper_seqs,sys.argv[3], "fasta")
