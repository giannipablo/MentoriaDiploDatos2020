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
def plot_roc_pr(y_real, y_pred, Title='', x_text=0.4, y_text=0.2, size_text=12, size=(14,6),
                ms=15, colorR='#ff7043', colorP='#5DADE2', label=None,ls='.--'):
    '''Figura de las curvas de ROC y PR.'''
    
    plt.figure(figsize=size)
    plt.suptitle(Title)
    
    ax1 = plt.subplot(1,2,1)
    
    roc = roc_curve(y_real, y_pred)
    plt.plot(roc[0], roc[1], ls, ms=ms, color=colorR, label=label)
    plt.text(x_text, y_text, f'Área bajo curva: {roc_auc_score(y_real, y_pred):.3f}', weight='bold',
             size=12, bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=colorR))
    plt.title('ROC', fontsize=size_text)
    plt.xlabel('FPR', fontsize=size_text)
    plt.ylabel('TPR', fontsize=size_text)
    
    ax2 = plt.subplot(1,2,2)
    PR  = precision_recall_curve(y_real, y_pred)
    plt.plot(PR[0], PR[1], ls, ms=ms, color=colorP, label=label)
    
    plt.title('PR', fontsize=size_text)
    plt.xlabel('Recall', fontsize=size_text)
    plt.ylabel('Precision', fontsize=size_text)
    
    return plt
    