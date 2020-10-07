# Generales
import os
import re
import pandas as pd
import numpy as np
from ast import literal_eval


# Figuras
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Métricas
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score

# Liberria para el manejo de emojis y emoticones
import emot
from emot.emo_unicode import UNICODE_EMO, EMOTICONS


############################################################################
def basic_metrics(y_real, y_pred, name='Train'):
    '''Imprimimos las métricas de interes (Ac, Pr, Re, F1, CM).'''
    
    infostring = 'Métricas {}:\n{}\nConfusion Matrix: \n{}'
    cm = confusion_matrix(y_real, y_pred)
    print(infostring.format(name, 
                            classification_report(y_real, y_pred, digits=3), 
                            cm))
    return cm



############################################################################
def plot_cm(cm, figsize=(10,6), title='', cmap='Blues'):
    '''Ploteo de la matriz de confusion'''
    
    plt.figure(figsize=figsize)
    ax = sns.heatmap(cm, annot=True, fmt="d", linewidths=1.2, square=True, linecolor='black', 
                     cbar=False, cmap=cmap, annot_kws={"weight":'bold', "size":'14'})
    plt.ylabel('Real', fontsize=14)
    plt.xlabel('Predicción', fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.title(title, fontsize=14) 
    return ax


############################################################################
def plot_roc_pr(y_real, y_pred, y_score, Title='', x_text=0.4, y_text=0.2, size_text=12, size=(14,6),
                ms=15, colorR='#ff7043', colorP='#5DADE2', label=None,ls='--'):
    '''Figura de las curvas de ROC y PR.'''
    
    plt.figure(figsize=size)
    plt.suptitle(Title)
    
    ax1 = plt.subplot(1,2,1)
    
    roc = roc_curve(y_real, y_score)
    plt.plot(roc[0], roc[1], ls, ms=ms, color=colorR, label=label)
    plt.plot([0,1], [0,1], 'r--')
    plt.text(x_text, y_text, f'Área bajo curva: {roc_auc_score(y_real, y_score):.3f}', weight='bold',
             size=12, bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=colorR))
    
    plt.text(0.4, 0.1, 'Predicción aleatoria', weight='bold',
             size=12, bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc="#ff0000"))
    
    plt.title('ROC', fontsize=size_text)
    plt.xlabel('FPR', fontsize=size_text)
    plt.ylabel('TPR', fontsize=size_text)
    plt.xlim([-0.05,1.05])
    plt.ylim([-0.05,1.05])
    plt.grid(True)
    
    
    ax2 = plt.subplot(1,2,2)
    PR  = precision_recall_curve(y_real, y_score)
    
    plt.plot(PR[1], PR[0], '--', ms=ms, color=colorP, label=label)
    plt.text(x_text, y_text, f'Precisión promedio: {average_precision_score(y_real, y_score):.3f}', weight='bold',
             size=12, bbox=dict(boxstyle="round", ec=(0.4, 0.7, 0.9), fc=colorP))
    
    plt.title('PR', fontsize=size_text)
    plt.xlabel('Recall', fontsize=size_text)
    plt.ylabel('Precision', fontsize=size_text)
    plt.xlim([-0.05,1.05])
    plt.ylim([-0.05,1.05])
    plt.grid(True)
    
    return plt
    

############################################################################
def ablation(df, tokeep=1.0, path=None):
    new_indexes = list()
    for si in df.session_id.unique():
        indexes = df[df.session_id==si].index
        N = np.ceil(indexes.shape[0]*tokeep).astype(int)-1
        new_indexes += list(indexes[-N:])

    dfo = df.loc[new_indexes]
    if path:
        dfo.to_csv(path)

    return dfo


############################################################################
def student_rating_category(x): 
    if x <= 2:
        return 0   
    if x >= 4:
        return 1
    return 'neutra'


############################################################################
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_some_info(x):
    print(f'{bcolors.OKGREEN}El conjunto de datos posee {x.shape[0]} filas y {x.shape[1]} columnas{bcolors.ENDC}')
    print(f'{bcolors.OKBLUE}')
    print(x.info())
    print(f'{bcolors.ENDC}')


############################################################################
def convert_emojis(text):
    """Funcion para convertir emojis a palabras"""
    text0 = [t for t in re.findall(r'\\x..\\x..\\x..\\x..', str(text.encode()))]
    text0 = [''.join(t.split('\\x')[1:]) for t in text0]
    text0 = [bytes.fromhex(t).decode() for t in text0 if t[0]=='f']
    text0 = [UNICODE_EMO[t] for t in text0 if t in UNICODE_EMO]
    text0 = ' '.join(text0)
    return text0 if text0 else text


############################################################################
def convert_emoticons(text):
    """Funcion para convertir emoticones a palabras"""
#     OUREMOTIC = dict([(e, f":{EMOTICONS[e].lower().split(',')[0].replace('or ','').replace(' ','_')}:") for e in EMOTICONS.keys()])
    try:
        text0 = emot.emoticons(text)
        if text0['flag']:
            return ':'+text0['mean'][0].replace(' ', '_').lower()+':'
        return text
    except Exception as e:
        return text