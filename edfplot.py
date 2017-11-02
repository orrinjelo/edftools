import matplotlib.pyplot as plt
import numpy as np
import datetime
import pyedflib

def plotDat(filen='', ch=4):  
    '''PLD - contains [u'MaskPress.2s',  u'Press.2s',  u'EprPress.2s', 
       u'Leak.2s',  u'RespRate.2s',  u'TidVol.2s',  u'MinVent.2s', 
       u'Snore.2s',  u'FlowLim.2s',  u'Crc16']
    '''
    edf = pyedflib.EdfReader(filen)
    fig = plt.figure()
    data = edf.readSignal(ch)
    plt.title(edf.getLabel(ch))
    plt.xlabel('Date/Time')
    plt.ylabel('{0} ({1})'.format(edf.getLabel(ch).split('.')[0], edf.getPhysicalDimension(ch)))
    plt.plot(time(ch), data)
    plt.show()
    fig.autofmt_xdate()

def plotDat(ch=0):  
    '''BRP - contains [u'Flow.40ms', u'Press.40ms', u'Crc16']'''
    time = lambda ch: [edf.getStartdatetime() + datetime.timedelta(milliseconds=40*x) for x in range(edf.getNSamples()[ch])]
    fig = plt.figure()
    data = edf.readSignal(ch)
    plt.title(edf.getLabel(ch))
    plt.xlabel('Date/Time')
    plt.ylabel('{0} ({1})'.format(edf.getLabel(ch).split('.')[0], edf.getPhysicalDimension(ch)))
    plt.plot(time(ch), data)
    plt.show()
    fig.autofmt_xdate()

# SAD is useless, only pulse (heart rate) data 
# CSL is classification of events.