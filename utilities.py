import pandas as pd

def supprimer_unit(dataset,colonne,unite):
    for i,elt in enumerate(dataset[colonne]):
        dataset.loc[i,colonne] = elt.replace(' '+unite,'')
    
    dataset[colonne] = pd.to_numeric(dataset[colonne], errors='coerce')
