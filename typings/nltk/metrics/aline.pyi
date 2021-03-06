"""
This type stub file was generated by pyright.
"""

"""
ALINE
http://webdocs.cs.ualberta.ca/~kondrak/
Copyright 2002 by Grzegorz Kondrak.

ALINE is an algorithm for aligning phonetic sequences, described in [1].
This module is a port of Kondrak's (2002) ALINE. It provides functions for
phonetic sequence alignment and similarity analysis. These are useful in
historical linguistics, sociolinguistics and synchronic phonology.

ALINE has parameters that can be tuned for desired output. These parameters are:
- C_skip, C_sub, C_exp, C_vwl
- Salience weights
- Segmental features

In this implementation, some parameters have been changed from their default
values as described in [1], in order to replicate published results. All changes
are noted in comments.

Example usage
-------------

# Get optimal alignment of two phonetic sequences

>>> align('θin', 'tenwis') # doctest: +SKIP
[[('θ', 't'), ('i', 'e'), ('n', 'n'), ('-', 'w'), ('-', 'i'), ('-', 's')]]

[1] G. Kondrak. Algorithms for Language Reconstruction. PhD dissertation,
University of Toronto.
"""
inf = float('inf')
C_skip = 10
C_sub = 35
C_exp = 45
C_vwl = 5
consonants = ['B', 'N', 'R', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'ç', 'ð', 'ħ', 'ŋ', 'ɖ', 'ɟ', 'ɢ', 'ɣ', 'ɦ', 'ɬ', 'ɮ', 'ɰ', 'ɱ', 'ɲ', 'ɳ', 'ɴ', 'ɸ', 'ɹ', 'ɻ', 'ɽ', 'ɾ', 'ʀ', 'ʁ', 'ʂ', 'ʃ', 'ʈ', 'ʋ', 'ʐ ', 'ʒ', 'ʔ', 'ʕ', 'ʙ', 'ʝ', 'β', 'θ', 'χ', 'ʐ', 'w']
R_c = ['aspirated', 'lateral', 'manner', 'nasal', 'place', 'retroflex', 'syllabic', 'voice']
R_v = ['back', 'lateral', 'long', 'manner', 'nasal', 'place', 'retroflex', 'round', 'syllabic', 'voice']
similarity_matrix = { 'bilabial': 1,'labiodental': 0.95,'dental': 0.9,'alveolar': 0.85,'retroflex': 0.8,'palato-alveolar': 0.75,'palatal': 0.7,'velar': 0.6,'uvular': 0.5,'pharyngeal': 0.3,'glottal': 0.1,'labiovelar': 1,'vowel': - 1,'stop': 1,'affricate': 0.9,'fricative': 0.85,'trill': 0.7,'tap': 0.65,'approximant': 0.6,'high vowel': 0.4,'mid vowel': 0.2,'low vowel': 0,'vowel2': 0.5,'high': 1,'mid': 0.5,'low': 0,'front': 1,'central': 0.5,'back': 0,'plus': 1,'minus': 0 }
salience = { 'syllabic': 5,'place': 40,'manner': 50,'voice': 5,'nasal': 20,'retroflex': 10,'lateral': 10,'aspirated': 5,'long': 0,'high': 3,'back': 2,'round': 2 }
feature_matrix = { 'p': { 'place': 'bilabial','manner': 'stop','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'b': { 'place': 'bilabial','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'t': { 'place': 'alveolar','manner': 'stop','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'d': { 'place': 'alveolar','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ʈ': { 'place': 'retroflex','manner': 'stop','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'plus','lateral': 'minus','aspirated': 'minus' },'ɖ': { 'place': 'retroflex','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'plus','lateral': 'minus','aspirated': 'minus' },'c': { 'place': 'palatal','manner': 'stop','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɟ': { 'place': 'palatal','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'k': { 'place': 'velar','manner': 'stop','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'g': { 'place': 'velar','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'q': { 'place': 'uvular','manner': 'stop','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɢ': { 'place': 'uvular','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ʔ': { 'place': 'glottal','manner': 'stop','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'m': { 'place': 'bilabial','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'plus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɱ': { 'place': 'labiodental','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'plus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'n': { 'place': 'alveolar','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'plus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɳ': { 'place': 'retroflex','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'plus','retroflex': 'plus','lateral': 'minus','aspirated': 'minus' },'ɲ': { 'place': 'palatal','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'plus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ŋ': { 'place': 'velar','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'plus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɴ': { 'place': 'uvular','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'plus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'N': { 'place': 'uvular','manner': 'stop','syllabic': 'minus','voice': 'plus','nasal': 'plus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ʙ': { 'place': 'bilabial','manner': 'trill','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'B': { 'place': 'bilabial','manner': 'trill','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'r': { 'place': 'alveolar','manner': 'trill','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'plus','lateral': 'minus','aspirated': 'minus' },'ʀ': { 'place': 'uvular','manner': 'trill','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'R': { 'place': 'uvular','manner': 'trill','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɾ': { 'place': 'alveolar','manner': 'tap','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɽ': { 'place': 'retroflex','manner': 'tap','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'plus','lateral': 'minus','aspirated': 'minus' },'ɸ': { 'place': 'bilabial','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'β': { 'place': 'bilabial','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'f': { 'place': 'labiodental','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'v': { 'place': 'labiodental','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'θ': { 'place': 'dental','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ð': { 'place': 'dental','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'s': { 'place': 'alveolar','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'z': { 'place': 'alveolar','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ʃ': { 'place': 'palato-alveolar','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ʒ': { 'place': 'palato-alveolar','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ʂ': { 'place': 'retroflex','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'plus','lateral': 'minus','aspirated': 'minus' },'ʐ': { 'place': 'retroflex','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'plus','lateral': 'minus','aspirated': 'minus' },'ç': { 'place': 'palatal','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ʝ': { 'place': 'palatal','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'x': { 'place': 'velar','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɣ': { 'place': 'velar','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'χ': { 'place': 'uvular','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ʁ': { 'place': 'uvular','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ħ': { 'place': 'pharyngeal','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ʕ': { 'place': 'pharyngeal','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'h': { 'place': 'glottal','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɦ': { 'place': 'glottal','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɬ': { 'place': 'alveolar','manner': 'fricative','syllabic': 'minus','voice': 'minus','nasal': 'minus','retroflex': 'minus','lateral': 'plus','aspirated': 'minus' },'ɮ': { 'place': 'alveolar','manner': 'fricative','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'plus','aspirated': 'minus' },'ʋ': { 'place': 'labiodental','manner': 'approximant','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɹ': { 'place': 'alveolar','manner': 'approximant','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɻ': { 'place': 'retroflex','manner': 'approximant','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'plus','lateral': 'minus','aspirated': 'minus' },'j': { 'place': 'palatal','manner': 'approximant','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'ɰ': { 'place': 'velar','manner': 'approximant','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'l': { 'place': 'alveolar','manner': 'approximant','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'plus','aspirated': 'minus' },'w': { 'place': 'labiovelar','manner': 'approximant','syllabic': 'minus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','aspirated': 'minus' },'i': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'high','back': 'front','round': 'minus','long': 'minus','aspirated': 'minus' },'y': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'high','back': 'front','round': 'plus','long': 'minus','aspirated': 'minus' },'e': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'mid','back': 'front','round': 'minus','long': 'minus','aspirated': 'minus' },'E': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'mid','back': 'front','round': 'minus','long': 'plus','aspirated': 'minus' },'ø': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'mid','back': 'front','round': 'plus','long': 'minus','aspirated': 'minus' },'ɛ': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'mid','back': 'front','round': 'minus','long': 'minus','aspirated': 'minus' },'œ': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'mid','back': 'front','round': 'plus','long': 'minus','aspirated': 'minus' },'æ': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'low','back': 'front','round': 'minus','long': 'minus','aspirated': 'minus' },'a': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'low','back': 'front','round': 'minus','long': 'minus','aspirated': 'minus' },'A': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'low','back': 'front','round': 'minus','long': 'plus','aspirated': 'minus' },'ɨ': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'high','back': 'central','round': 'minus','long': 'minus','aspirated': 'minus' },'ʉ': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'high','back': 'central','round': 'plus','long': 'minus','aspirated': 'minus' },'ə': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'mid','back': 'central','round': 'minus','long': 'minus','aspirated': 'minus' },'u': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'high','back': 'back','round': 'plus','long': 'minus','aspirated': 'minus' },'U': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'high','back': 'back','round': 'plus','long': 'plus','aspirated': 'minus' },'o': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'mid','back': 'back','round': 'plus','long': 'minus','aspirated': 'minus' },'O': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'mid','back': 'back','round': 'plus','long': 'plus','aspirated': 'minus' },'ɔ': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'mid','back': 'back','round': 'plus','long': 'minus','aspirated': 'minus' },'ɒ': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'low','back': 'back','round': 'minus','long': 'minus','aspirated': 'minus' },'I': { 'place': 'vowel','manner': 'vowel2','syllabic': 'plus','voice': 'plus','nasal': 'minus','retroflex': 'minus','lateral': 'minus','high': 'high','back': 'front','round': 'minus','long': 'plus','aspirated': 'minus' } }
def align(str1, str2, epsilon=...):
    """
    Compute the alignment of two phonetic strings.

    :type str1, str2: str
    :param str1, str2: Two strings to be aligned
    :type epsilon: float (0.0 to 1.0)
    :param epsilon: Adjusts threshold similarity score for near-optimal alignments

    :rtpye: list(list(tuple(str, str)))
    :return: Alignment(s) of str1 and str2

    (Kondrak 2002: 51)
    """
    ...

def _retrieve(i, j, s, S, T, str1, str2, out):
    """
    Retrieve the path through the similarity matrix S starting at (i, j).

    :rtype: list(tuple(str, str))
    :return: Alignment of str1 and str2
    """
    ...

def sigma_skip(p):
    """
    Returns score of an indel of P.

    (Kondrak 2002: 54)
    """
    ...

def sigma_sub(p, q):
    """
    Returns score of a substitution of P with Q.

    (Kondrak 2002: 54)
    """
    ...

def sigma_exp(p, q):
    """
    Returns score of an expansion/compression.

    (Kondrak 2002: 54)
    """
    ...

def delta(p, q):
    """
    Return weighted sum of difference between P and Q.

    (Kondrak 2002: 54)
    """
    ...

def diff(p, q, f):
    """
    Returns difference between phonetic segments P and Q for feature F.

    (Kondrak 2002: 52, 54)
    """
    ...

def R(p, q):
    """
    Return relevant features for segment comparsion.

    (Kondrak 2002: 54)
    """
    ...

def V(p):
    """
    Return vowel weight if P is vowel.

    (Kondrak 2002: 54)
    """
    ...

def demo():
    """
    A demonstration of the result of aligning phonetic sequences
    used in Kondrak's (2002) dissertation.
    """
    ...

cognate_data = """jo,ʒə
tu,ty
nosotros,nu
kjen,ki
ke,kwa
todos,tu
una,ən
dos,dø
tres,trwa
ombre,om
arbol,arbrə
pluma,plym
kabeθa,kap
boka,buʃ
pje,pje
koraθon,kœr
ber,vwar
benir,vənir
deθir,dir
pobre,povrə
ðis,dIzes
ðæt,das
wat,vas
nat,nixt
loŋ,laŋ
mæn,man
fleʃ,flajʃ
bləd,blyt
feðər,fEdər
hær,hAr
ir,Or
aj,awgə
nowz,nAzə
mawθ,munt
təŋ,tsuŋə
fut,fys
nij,knI
hænd,hant
hart,herts
livər,lEbər
ænd,ante
æt,ad
blow,flAre
ir,awris
ijt,edere
fiʃ,piʃkis
flow,fluere
staɾ,stella
ful,plenus
græs,gramen
hart,kordis
horn,korny
aj,ego
nij,genU
məðər,mAter
mawntən,mons
nejm,nomen
njuw,nowus
wən,unus
rawnd,rotundus
sow,suere
sit,sedere
θrij,tres
tuwθ,dentis
θin,tenwis
kinwawa,kenuaʔ
nina,nenah
napewa,napɛw
wapimini,wapemen
namesa,namɛʔs
okimawa,okemaw
ʃiʃipa,seʔsep
ahkohkwa,ahkɛh
pematesiweni,pematesewen
asenja,aʔsɛn"""
if __name__ == '__main__':
    ...
