def count_bases (dna, sig_figs):
    bases = "ATGC"
    for base in bases:
        numbases= dna.upper ().count(base)
        print (f"{base}{numbases}")

count_bases("GCGTAGTCATCT")        
    


   # [x for x in dna]
