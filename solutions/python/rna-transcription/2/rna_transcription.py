DNA_SEQ = 'GCTA'
RNA_SEQ = 'CGAU'

def to_rna(dna_strand):
    return dna_strand.translate(
        str.maketrans(DNA_SEQ, RNA_SEQ)
    )