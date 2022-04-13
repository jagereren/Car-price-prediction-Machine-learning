import pandas as pd

def supprimer_unit(dataset,colonne,unite):
    for i,elt in enumerate(dataset[colonne]):
        dataset.loc[i,colonne] = elt.replace(' '+unite,'')
    
    dataset[colonne] = pd.to_numeric(dataset[colonne], errors='coerce')

def binary_transformation(dataset,colonne,feature1,feature2):    
    for i,elt in enumerate(dataset[colonne]):
        if(dataset.loc[i,colonne]==feature1):
            dataset.loc[i,colonne] = '0'
        elif(dataset.loc[i,colonne]==feature2):
            dataset.loc[i,colonne] = '1'

    dataset[colonne] = pd.to_numeric(dataset[colonne], errors='coerce') # convertir le string de transmission en int


