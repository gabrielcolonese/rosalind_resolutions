# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 00:50:54 2021

@author: Gabriel
"""

amino_dict = { #dicionario que traduz cada codon em um aminoacido
    "UUU" : "F",      "CUU" : "L",      "AUU" : "I",
    "GUU" : "V",      "UUC" : "F",      "CUC" : "L",
    "AUC" : "I",      "GUC" : "V",      "UUA" : "L",
    "CUA" : "L",      "AUA" : "I",      "GUA" : "V",
    "UUG" : "L",      "CUG" : "L",      "AUG" : "M", #Metionina, comeco de qqr proteina
    "GUG" : "V",      "UCU" : "S",      "CCU" : "P",    
    "ACU" : "T",      "GCU" : "A",      "UCC" : "S",
    "CCC" : "P",      "ACC" : "T",      "GCC" : "A",
    "UCA" : "S",      "CCA" : "P",      "ACA" : "T",     
    "GCA" : "A",      "UCG" : "S",      "CCG" : "P",
    "ACG" : "T",      "GCG" : "A",      "UAU" : "Y",
    "CAU" : "H",      "AAU" : "N",      "GAU" : "D",
    "UAC" : "Y",      "CAC" : "H",      "AAC" : "N",  
    "GAC" : "D",      "UAA" : "Stop",   "CAA" : "Q",     
    "AAA" : "K",      "GAA" : "E",      "UAG" : "Stop",  
    "CAG" : "Q",      "AAG" : "K",      "GAG" : "E",
    "UGU" : "C",      "CGU" : "R",      "AGU" : "S",     
    "GGU" : "G",      "UGC" : "C",      "CGC" : "R",     
    "AGC" : "S",      "GGC" : "G",      "UGA" : "Stop",   
    "CGA" : "R",      "AGA" : "R",      "GGA" : "G",
    "UGG" : "W",      "CGG" : "R",      "AGG" : "R",    
    "GGG" : "G"   
    }

frequencies = {}

for item in amino_dict:
    codon = amino_dict[item]
    if codon in frequencies:
        frequencies[codon] += 1
    else:
        frequencies[codon] = 1
        
polipeptyde = "MDCGYLYWQSITADCNMAKDRWDGYMKKYYSWMKDKVEIKNWGAMPGSQRWHLHEDCTNERKLCMMCHFKAYSAKPFQTETSFDWSVKNDASYDSVEINNIFENFDYSCKKDNKIHEITKCKATYSVIYMAATTCCGGPESLYGNQQDVDEWEYMMIIHQTDVLESSFFLGCVAIEAILWCMHERQSKNWYTAVHTIQCLNSWAFDNMLYWRWTLLALSHLWNPVCQYCPHRNWSQMRFPLHSIQRWRVDGHQSKEIPCTVPDAVYDVEGGIIKQQLDWPKDYCMSLFNCFWPTQVCYDTANPEMRMVFPECNFQFPNEMYVSVQMIQSLIKQLVMRWKPMAVQMKHPNRNDMINHLYCGPYVYEISVKGYNDATEDAWTWPNIWDVVCYDYRCLLMDPATCMEVYFVDIVMCMVNVDLTGCPNPMSMNVIPMERKERASHHLHCELSWKKCQKHWTNCLEEERWNGKRDRRNPFHQIRMLSQPRINPCMGVECIVITQIHQFTSICGDCIMEQDDWLSQCVVNEQFRFGILDHPGKWRLRPHMDISDPPQVWMDWTARHGLVPWGRRIMVQNSTIVMKGPNHQCWHFSKADLWVMYDAWQANHWTQTLAMSHQDVIMPCYQPYTYHTMVYQPMQWWKDIDECQCEVYPFEPGLMPNRGKNVPWNYTHTQIIQGSWEHDMKSGGIFACCKNQRLQGLTKRGPCADEQLVTVVLYEHTKYSTWKWTVSKHDTCNQIVREYQHIIMGKDQTWQLWPAPCWDTSRPNPHKRDHATGSKISSRGPEFGRIWRCLMCKCNHHKDTSVYSLKCPPHCWGEALTYWTAMWHIYFLIALQNIRRAYYGPWFIIERGEGVTHTPWGQIEPERSELNEARIDPPTHEDHPNVYQEMLWGFFGLLISSTINTYGTKMTLLYDSFLPYSCFEFWTMDQWHLKLLVWWCRREVGPWRPEKDMGKGGPVWMSKIHCFPWFHMTMVCGGQNEKNAQFTYCMHLTAKMCDNQQ"
out = 1

for aa in polipeptyde:
    out *= frequencies[aa] #pode usar [] ou .get()
    out = out%1e6
out *= frequencies["Stop"]
out = out%1e6

print(out)    
