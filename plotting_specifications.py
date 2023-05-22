# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:02:52 2022

@author: maout
"""

#plotting specs
import matplotlib.pyplot as plt

import seaborn as sns
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 'figure'
plt.rcParams['savefig.facecolor'] = (1,1,1,0)
plt.rcParams['savefig.bbox'] = 'standard'#"tight"
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'sans-serif'     # not available in Colab
plt.rcParams['font.sans-serif'] = 'Verdana'#'Helvetica'  # not available in Colab
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.linewidth'] = 2
plt.rc('axes',edgecolor='#4f4949')
plt.rcParams['figure.frameon'] = False
#plt.rcParams['figure.subplot.hspace'] = 0.05
#plt.rcParams['figure.subplot.wspace'] = 0.05
#plt.rcParams['figure.subplot.left'] = 0.4
#plt.rcParams['figure.subplot.right'] = 0.5            
plt.rcParams['text.usetex'] = True
