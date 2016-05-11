import os
from bagofwords_vector import bowVector # генератор с векторами bag-of-words (присутсвие/отсутствие леммы), для абзацев
from length_of_paragraph import meanLengthPar # генератор со средними длинами абзацев в предложениях
from length_of_sentences import meanLengthSent # генератор со средними длинами предложений в абзацах
from count_pos import verbsRatio # генератор с ratio глаголы vs. остальные части речи, для абзацев
from verbs_in_past_tense import pastVerbsRatio # генератор с ratio глаголы в прош.вр. vs. все глаголы, для абзацев
from finitnefinit import finitRatio # генератор с ratio финитные vs. нефинитные глаголы, для абзацев
