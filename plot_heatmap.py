import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import os
import argparse


sns.set()

def read_data(path):
    if path.split('.')[-1]:
        data = pd.read_csv(path)
    else:
        data = pd.read_csv(path, sep='\t')
    return data


def plot_heatmap(data):
    plt.figure(figsize=(16, 6))
    heatmap = sns.heatmap(data.corr(), vmin=-1, vmax=1, annot=True, cmap='rainbow')
    heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12)
    plt.savefig('heatmaps/' + '_heatmap.png', dpi=300, bbox_inches='tight')




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot heatmap of correlation matrix')
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-p', '--path', help='path to dataset')
    args = argparser.parse_args()
    # filename = os.path.join('data/',args.path)
    # filename = os.path.basename(filename)
    data = read_data(args.path)
    plot_heatmap(data)