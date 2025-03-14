import os, sys

BASE = os.path.dirname(os.path.abspath(__file__))

FILES_PATH       = os.path.join(BASE, "files")
TRAINED_NN_PATH  = os.path.join(FILES_PATH, "NN")
TRAINED_NN_MSEED = os.path.join(TRAINED_NN_PATH, "NN_MS.npz")
TRAINED_NN_BIGG  = os.path.join(TRAINED_NN_PATH, "NN_BG.npz")

MODELS_PATH      = os.path.join(FILES_PATH, "models")

BIOCHEMISTRY_PATH   = os.path.join(FILES_PATH, "biochemistry")
MODELSEED_REACTIONS = os.path.join(BIOCHEMISTRY_PATH, "reactions.tsv")
MODELSEED_COMPOUNDS = os.path.join(BIOCHEMISTRY_PATH, "compounds.tsv")
MODELSEED_EXCHANGES = os.path.join(FILES_PATH, "models", "MS_exchanges.sbml")
BIGG_REACTIONS      = os.path.join(BIOCHEMISTRY_PATH, "bigg_reactions.tsv")
BIGG_EXCHANGES      = os.path.join(FILES_PATH, "models", "BiGG_exchanges.sbml")
BIGG_COMPOUNDS      = os.path.join(BIOCHEMISTRY_PATH, "bigg_compounds.tsv")
