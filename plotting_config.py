#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 21:39:11 2024

@author: dimi
"""

from matplotlib import rcParams
##from novelty paper
def update_rc_params():
    rcParams.update({
        'lines.linewidth': 1.5,
        'lines.linestyle': '-',
        'lines.marker': 'None',
        'lines.markeredgewidth': 0.,
        'lines.markersize': 6.,
        'lines.antialiased': True,
        'lines.solid_joinstyle': 'round',
        'lines.solid_capstyle': 'round',
    
        'patch.linewidth': 1.,
        'patch.facecolor': '#cccccc',
        'patch.edgecolor': 'none',
        'patch.antialiased': True,
    
        'font.size': 10,
        'text.usetex': False,
        'mathtext.default': 'regular',
    
        'axes.linewidth': 1.0,
        'axes.grid': False,
        'axes.titlesize': 10,
        'axes.labelsize': 10,
        'axes.labelweight': 'normal',
        'axes.axisbelow': True,
        'axes.formatter.use_mathtext': False,
        'axes.xmargin': 0.,
        'axes.ymargin': 0.,
        'polaraxes.grid': True,
    
        'xtick.direction': 'out',
        'xtick.labelsize': 10.,
        'xtick.major.size': 3.,
        'xtick.minor.size': 2.,
        'xtick.major.width': 1.,
        'xtick.minor.width': 1.,
    
        'ytick.direction': 'out',
        'ytick.labelsize': 10.,
        'ytick.major.size': 3.,
        'ytick.minor.size': 2.,
        'ytick.major.width': 1.,
        'ytick.minor.width': 1.,
    
        'grid.linestyle': 'dotted',
        'grid.alpha': 0.5,
        'grid.linewidth': 1.0,
    
        'legend.frameon': False,
        'legend.fancybox': True,
        'legend.fontsize': 10.,
        'legend.loc': 'best',
    
        'figure.figsize': (5, 3),
        'figure.dpi': 200,
        'figure.autolayout': True,
    
        'image.cmap': 'viridis',
        'image.interpolation': 'None',
        'image.aspect': 'equal',
    
        'savefig.format': 'pdf',
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.1,
        'pdf.fonttype': 42,
    })
     