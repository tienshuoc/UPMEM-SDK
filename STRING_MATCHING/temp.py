QUERY = "AAC"
corpus = "ACAAATACGATCGGGATAGGTTCATTTGACGCGCTGCCATAGCAAACGAGTTGAATCATTCGTGGCATAACCCCCGGCGTCGAGTATCACAGCAGTGTCCGGGACGGCGTGCGCAGGTTTTTATTCTGCAGGCGTACCTATCATGGTACTCCATGCATTGTCAATGATCTTCAACCCGTGCGAGAGTGCACGCCGTTCGACTAAAAGCGCTAACTTATAATATCTACCCATGTTTGTAACTTCCTGCCAGAATAGAGGGCTATGCCTTACTTCCGGCTGATCGACTACCCTCCTGACTTAATCAGCTGGCCTCACGCGTGCAAGTCACCGGCTGCTATGTGTGTCTATCTGACTACACTCAAATCGCGACGGCCTGCAGTCACCAGGTCCTAGCCGAGAGTATAGTTTGAGTTGACTAAATGTGGGAACGCGTAGACATAGTATCACACCGCTGGGTATGCCGTATCTTACGCTGGAAAAGAAAGTTGGAGTTCAAGACCTGAACATCCGGGTGTAAGGGTTTGTAAGAGCGCCTTCCTATCCCTGATGGCACCCCTGGTAAGGGGGTAGGGCATGGGAATATAGTCTATACCGTACGTGAGCCCCGA"
match = 0
count = 0
for pos, token, in enumerate(corpus):
    match = match + 1 if token in QUERY[match] else 0
    if match == len(QUERY):
        count += 1
        match = 0

print(count)
