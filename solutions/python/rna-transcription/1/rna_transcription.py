dna_to_rna = dict({
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
})

def to_rna(dna_strand):
    rna = ''
    for c in dna_strand:
        rna += dna_to_rna[c]
    return rna

