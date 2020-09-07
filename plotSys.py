#! /usr/bin/env python

import sys

import os

import subprocess

import ROOT

from array import array

from ROOT import TH1D,TH2D,TFile,TMath,TCanvas,THStack,TLegend,TPave,TLine,TLatex

from ROOT import gROOT,gStyle,gPad,gStyle

#from ROOT import Double,kBlue,kRed,kOrange,kMagenta,kYellow,kCyan,kGreen,kGray,kBlack,kTRUE

from ROOT import kBlue,kRed,kOrange,kMagenta,kYellow,kCyan,kGreen,kGray,kBlack,kTRUE

import ctypes



#gROOT.Macro("~/rootlogon.C")

gStyle.SetOptStat(0)



# ===============

# options

# ===============

from optparse import OptionParser

parser = OptionParser()

parser.add_option('--Lumi', metavar='D', type='float', action='store',

                  default= 136650.0,

                  dest='Lumi',

                  help='Data Luminosity in pb-1')



parser.add_option('--globalSF', metavar='SF', type='float',

                  default = 1.0,

                  dest='globalSF',

                  help='Global trigger SF (%default default)')



parser.add_option('--plotDir', metavar='P', type='string', action='store',

                  default='Plots/wjet',

                  dest='plotDir',

                  help='output directory of plots')



parser.add_option('--skimType', metavar='S', type='string', action='store',

                  default='MuCh',

                  dest='skimType',

                  help='Skim type: CR_Zelel, CR_Zmumu, SR_Zelel, SR_Zmumu')



parser.add_option('--processDir', metavar='pD', type='string', action='store',

                  default='ana',

                  dest='processDir',

                  help='directory to read histograms from')



parser.add_option('--var', metavar='T', type='string', action='store',

                  default='ht_zsel',#cutflow, st

                  dest='var',

                  help='variable to plot')



parser.add_option('--xtitle', metavar='T', type='string', action='store',

                  default='',#cutflow, st

                  dest='xtitle',

                  help='x axis title')



parser.add_option('--sys', metavar='T', type='string', action='store',

                  default='nominal',

                  dest='sys',

                  help='nominal, BTagSFup, BTagSFdown, ScaleUp, ScaleDown, MatchUp, MatchDown')



parser.add_option('--verbose',action='store_true',

                  default=False,

                  dest='verbose',

                  help='verbose switch')



parser.add_option('--rebin', metavar='T', type='int', action='store',

                  default='1',

                  dest='rebin',

                  help='rebin the histograms')



(options,args) = parser.parse_args()

# ==========end: options =============

var = options.var

lumi = options.Lumi

gSF  = options.globalSF

rebinS = options.rebin

pDir = options.processDir

plotDir = options.plotDir

skimType = options.skimType

verbose = options.verbose

xtitle = options.xtitle



lumi_2016 = 35920.0

lumi_2017 = 0#41530.0

lumi_2018 = 0#59200.0

if 'elel' in skimType: title = 'e^{#pm}+jets'

elif 'mumu' in skimType: title = '#mu^{#pm}+jets'

else: title = ''

# ==========add the input ============



#execfile("input.py")

#exec(compile(open("input.py","rb").read(),"input.py",'exec'))

exec(open("./input.py").read())



#Systematics Part

Sys = False



#varNom = var+"_TTJets_ST_Scaling_16"

varNom = var+"_nominal_16"



#if (Sys and 'Counter' not in var): 

#  varNom = var+"_nominal_16"

#else:

#  varNom = var

shapeSys = ["PileupUp", "PileupDown", "BTagSFUp", "BTagSFDown", "topptweightUp", "topptweightDown",  "jerUp", "jerDown", "jesUp", "jesDown", "LHEScale1", "LHEScale2", "LHEScale3", "LHEScale4", "LHEScale6", "LHEScale8", "LHEScaleUpWeight", "LHEScaleDownWeight"]



# === prepare the input labels and legends ===========

dataLabel     = 'Data_'

topLabel      = 'Top_'

topxLabel      = 'Top+X_'

dyLabel       = 'DY_'

wjLabel       = 'WJets_'

sTLabel       = 'ST_'

qcdLabel      = 'QCD_'

dibLabel      = 'Diboson_'

sigLabel      = 'Signal_'



#AI:

dataLeg       = 'Data'

topLeg        = 't#bar{t} + jets'

topxLeg        = 't#bar{t}+W/Z'

dyLeg         = 'Drell-Yan'

wjLeg         = 'W+jets'

sTLeg         = 'Single t'

qcdLeg        = 'Multi-jet'

dibLeg        = 'Diboson'

sigLeg        = 'Y (1200 GeV)'



# === create structure ============

data     = [

            [f_Data_ReMiniAOD_2016, 1., 1., 1.],

            [f_Data_ReMiniAOD_2017, 1., 1., 0.],

            [f_Data_ReMiniAOD_2018, 1., 1., 0.],

           ] # this corresponds to 36 fb-1



dy       = [

            [f_2016DY100to200,    DY100to200_xs_2016,      DY100to200_num_2016,    lumi_2016],

            [f_2016DY200to400,    DY200to400_xs_2016,      DY200to400_num_2016,    lumi_2016],

            [f_2016DY400to600,    DY400to600_xs_2016,      DY400to600_num_2016,    lumi_2016],

            [f_2016DY600to800,    DY600to800_xs_2016,      DY600to800_num_2016,    lumi_2016],

            [f_2016DY800to1200,    DY800to1200_xs_2016,      DY800to1200_num_2016,    lumi_2016],

            [f_2016DY1200to2500,    DY1200to2500_xs_2016,      DY1200to2500_num_2016,    lumi_2016],

            [f_2016DY2500toInf,    DY2500toInf_xs_2016,      DY2500toInf_num_2016,    lumi_2016],

            [f_2017DY100to200,    DY100to200_xs_2017,      DY100to200_num_2017,    lumi_2017],

            [f_2017DY200to400,    DY200to400_xs_2017,      DY200to400_num_2017,    lumi_2017],

            [f_2017DY400to600,    DY400to600_xs_2017,      DY400to600_num_2017,    lumi_2017],

            [f_2017DY600to800,    DY600to800_xs_2017,      DY600to800_num_2017,    lumi_2017],

            [f_2017DY800to1200,    DY800to1200_xs_2017,      DY800to1200_num_2017,    lumi_2017],

            [f_2017DY1200to2500,    DY1200to2500_xs_2017,      DY1200to2500_num_2017,    lumi_2017],

            [f_2017DY2500toInf,    DY2500toInf_xs_2017,      DY2500toInf_num_2017,    lumi_2017],

            [f_2018DY100to200,    DY100to200_xs_2018,      DY100to200_num_2018,    lumi_2018],

            [f_2018DY200to400,    DY200to400_xs_2018,      DY200to400_num_2018,    lumi_2018],

            [f_2018DY400to600,    DY400to600_xs_2018,      DY400to600_num_2018,    lumi_2018],

            [f_2018DY600to800,    DY600to800_xs_2018,      DY600to800_num_2018,    lumi_2018],

            [f_2018DY800to1200,    DY800to1200_xs_2018,      DY800to1200_num_2018,    lumi_2018],

            [f_2018DY1200to2500,    DY1200to2500_xs_2018,      DY1200to2500_num_2018,    lumi_2018],

            [f_2018DY2500toInf,    DY2500toInf_xs_2018,      DY2500toInf_num_2018,    lumi_2018],

           ]



#top      = [[f_2017ttbar,         Top_xs_2017,            Top_num_2017,            lumi]]

top      = [

            [f_2016ttbar_pow,         Top_pow_xs_2016,            Top_pow_num_2016,            lumi_2016],

            #[f_2017ttbar_2L2Nu,         Top_xs_2017_2L2Nu,            Top_num_2017_2L2Nu,            lumi],

            #[f_2017ttbar_SemiLep,         Top_xs_2017_SemiLep,            Top_num_2017_SemiLep,            lumi],

            [f_2017ttbar_2L2NuPS,         Top_xs_2017_2L2NuPS,            Top_num_2017_2L2NuPS,            lumi_2017],

            [f_2017ttbar_SemiLepPS,         Top_xs_2017_SemiLepPS,            Top_num_2017_SemiLepPS,            lumi_2017],

            [f_2017ttbar_HadPS,         Top_xs_2017_HadPS,            Top_num_2017_HadPS,            lumi_2017],

            [f_2018ttbar_2L2Nu,         Top_xs_20182L2Nu,            Top_num_20182L2Nu,            lumi_2018],

            [f_2018ttbar_SemiLep,         Top_xs_2018SemiLep,            Top_num_2018SemiLep,            lumi_2018],

            [f_2018ttbar_Had,         Top_xs_2018Had,            Top_num_2018Had,            lumi_2018],

           ]



top_plus_x = [

             [f_2017TTWJetsToLNu,         TTWJetsToLNu_xs_2017,            TTWJetsToLNu_num_2017,            lumi_2017],

             [f_2017TTWJetsToQQ,         TTWJetsToQQ_xs_2017,            TTWJetsToQQ_num_2017,            lumi_2017],

             [f_2017TTZToLLNuNu,         TTZToLLNuNu_xs_2017,            TTZToLLNuNu_num_2017,            lumi_2017],

             [f_2017TTZToQQ,         TTZToQQ_xs_2017,            TTZToQQ_num_2017,            lumi_2017],

           ]

wjets    = [

            [f_2016WJ100to200,    WJ100to200_xs_2016,      WJ100to200_num_2016,    lumi_2016],

            [f_2016WJ200to400,    WJ200to400_xs_2016,      WJ200to400_num_2016,    lumi_2016],

            [f_2016WJ400to600,    WJ400to600_xs_2016,      WJ400to600_num_2016,    lumi_2016],

            [f_2016WJ600to800,    WJ600to800_xs_2016,      WJ600to800_num_2016,    lumi_2016],     

            [f_2016WJ800to1200,   WJ800to1200_xs_2016,     WJ800to1200_num_2016,   lumi_2016],

            [f_2016WJ1200to2500,  WJ1200to2500_xs_2016,    WJ1200to2500_num_2016,  lumi_2016],

            [f_2016WJ2500toInf,   WJ2500toInf_xs_2016,     WJ2500toInf_num_2016,   lumi_2016], 

            [f_2017WJ100to200,    WJ100to200_xs_2017,      WJ100to200_num_2017,    lumi_2017],

            [f_2017WJ200to400,    WJ200to400_xs_2017,      WJ200to400_num_2017,    lumi_2017],

            [f_2017WJ400to600,    WJ400to600_xs_2017,      WJ400to600_num_2017,    lumi_2017],

            [f_2017WJ600to800,    WJ600to800_xs_2017,      WJ600to800_num_2017,    lumi_2017],     

            [f_2017WJ800to1200,   WJ800to1200_xs_2017,     WJ800to1200_num_2017,   lumi_2017],

            [f_2017WJ1200to2500,  WJ1200to2500_xs_2017,    WJ1200to2500_num_2017,  lumi_2017],

            [f_2017WJ2500toInf,   WJ2500toInf_xs_2017,     WJ2500toInf_num_2017,   lumi_2017], 

            [f_2018WJ100to200,    WJ100to200_xs_2018,      WJ100to200_num_2018,    lumi_2018],

            [f_2018WJ200to400,    WJ200to400_xs_2018,      WJ200to400_num_2018,    lumi_2018],

            [f_2018WJ400to600,    WJ400to600_xs_2018,      WJ400to600_num_2018,    lumi_2018],

            [f_2018WJ600to800,    WJ600to800_xs_2018,      WJ600to800_num_2018,    lumi_2018],     

            [f_2018WJ800to1200,   WJ800to1200_xs_2018,     WJ800to1200_num_2018,   lumi_2018],

            [f_2018WJ1200to2500,  WJ1200to2500_xs_2018,    WJ1200to2500_num_2018,  lumi_2018],

            [f_2018WJ2500toInf,   WJ2500toInf_xs_2018,     WJ2500toInf_num_2018,   lumi_2018], 



            ]



st       = [

            [f_2016ST_tW_top,     ST_tW_top_xs_2016,       ST_tW_top_num_2016,     lumi_2016],

            [f_2016ST_tW_antitop, ST_tW_antitop_xs_2016,   ST_tW_antitop_num_2016, lumi_2016],

            [f_2016ST_t_top,      ST_t_top_xs_2016,        ST_t_top_num_2016,      lumi_2016],

            [f_2016ST_t_antitop,  ST_t_antitop_xs_2016,    ST_t_antitop_num_2016,  lumi_2016],

            [f_2017ST_tW_top,     ST_tW_top_xs_2017,       ST_tW_top_num_2017,     lumi_2017],

            [f_2017ST_tW_antitop, ST_tW_antitop_xs_2017,   ST_tW_antitop_num_2017, lumi_2017],

            [f_2017ST_t_top,      ST_t_top_xs_2017,        ST_t_top_num_2017,      lumi_2017],

            [f_2017ST_t_antitop,  ST_t_antitop_xs_2017,    ST_t_antitop_num_2017,  lumi_2017],

            [f_2018ST_tW_top,     ST_tW_top_xs_2018,       ST_tW_top_num_2018,     lumi_2018],

            [f_2018ST_tW_antitop, ST_tW_antitop_xs_2018,   ST_tW_antitop_num_2018, lumi_2018],

            [f_2018ST_t_top,      ST_t_top_xs_2018,        ST_t_top_num_2018,      lumi_2018],

            [f_2018ST_t_antitop,  ST_t_antitop_xs_2018,    ST_t_antitop_num_2018,  lumi_2018],

           ]



qcd      = [

            [f_2016QCD170to300,   QCD170to300_xs_2016,     QCD170to300_num_2016,     lumi_2016],

            [f_2016QCD300to470,   QCD300to470_xs_2016,     QCD300to470_num_2016,     lumi_2016],

            [f_2016QCD470to600,   QCD470to600_xs_2016,     QCD470to600_num_2016,     lumi_2016],

            [f_2016QCD600to800,   QCD600to800_xs_2016,     QCD600to800_num_2016,     lumi_2016],

            [f_2016QCD800to1000,  QCD800to1000_xs_2016,    QCD800to1000_num_2016,    lumi_2016],

            [f_2016QCD1000to1400, QCD1000to1400_xs_2016,   QCD1000to1400_num_2016,   lumi_2016],

            [f_2016QCD1400to1800, QCD1400to1800_xs_2016,   QCD1400to1800_num_2016,   lumi_2016],

            [f_2016QCD1800to2400, QCD1800to2400_xs_2016,   QCD1800to2400_num_2016,   lumi_2016],

            [f_2016QCD2400to3200, QCD2400to3200_xs_2016,   QCD2400to3200_num_2016,   lumi_2016],

            [f_2016QCD3200toInf,  QCD3200toInf_xs_2016,    QCD3200toInf_num_2016,    lumi_2016],

            #[f_2017QCD100to200,   QCD100to200_xs_2017,     QCD100to200_num_2017,     lumi_2017],

            #[f_2017QCD200to300,   QCD200to300_xs_2017,     QCD200to300_num_2017,     lumi_2017],

            [f_2017QCD300to500,   QCD300to500_xs_2017,     QCD300to500_num_2017,     lumi_2017],

            [f_2017QCD500to700,   QCD500to700_xs_2017,     QCD500to700_num_2017,     lumi_2017],

            [f_2017QCD700to1000,  QCD700to1000_xs_2017,    QCD700to1000_num_2017,    lumi_2017],

            [f_2017QCD1000to1500, QCD1000to1500_xs_2017,   QCD1000to1500_num_2017,   lumi_2017],

            [f_2017QCD1500to2000, QCD1500to2000_xs_2017,   QCD1500to2000_num_2017,   lumi_2017],

            [f_2017QCD2000toInf, QCD2000toInf_xs_2017,   QCD2000toInf_num_2017,   lumi_2017],

            #[f_2018QCD100to200,   QCD100to200_xs_2018,     QCD100to200_num_2018,     lumi_2018],

            #[f_2018QCD200to300,   QCD200to300_xs_2018,     QCD200to300_num_2018,     lumi_2018],

            [f_2018QCD300to500,   QCD300to500_xs_2018,     QCD300to500_num_2018,     lumi_2018],

            [f_2018QCD500to700,   QCD500to700_xs_2018,     QCD500to700_num_2018,     lumi_2018],

            [f_2018QCD700to1000,  QCD700to1000_xs_2018,    QCD700to1000_num_2018,    lumi_2018],

            [f_2018QCD1000to1500, QCD1000to1500_xs_2018,   QCD1000to1500_num_2018,   lumi_2018],

            [f_2018QCD1500to2000, QCD1500to2000_xs_2018,   QCD1500to2000_num_2018,   lumi_2018],

            [f_2018QCD2000toInf, QCD2000toInf_xs_2018,   QCD2000toInf_num_2018,   lumi_2018],

           ]



sig      = [

            [f_2016SIG1200, SIG1200_xs_2016,  SIG1200_num_2016,  lumi_2016],

            [f_2017SIG1200, SIG1200_xs_2017,  SIG1200_num_2017,  lumi_2017],

            [f_2018SIG1200, SIG1200_xs_2018,  SIG1200_num_2018,  lumi_2018],

           ]

#AI:

h_data     = getHisto(dataLabel,       dataLeg,        pDir, varNom,  data,     kBlack,     verbose, True)

h_top      = getHisto(topLabel,        topLeg,         pDir, varNom,  top,      206,          verbose, True)

#h_top_plus_x      = getHisto(topxLabel,        topxLeg,         pDir, varNom,  top_plus_x,      kGreen,          verbose, True)

h_top_plus_x      = getHisto(topxLabel,        topxLeg,         pDir, varNom,  top_plus_x,      208,          verbose, True)

h_wjets    = getHisto(wjLabel,         wjLeg,          pDir, varNom,  wjets,    210,      verbose, True)

h_st       = getHisto(sTLabel,         sTLeg,          pDir, varNom,  st,       226,      verbose, True)

h_dy       = getHisto(dyLabel,         dyLeg,          pDir, varNom,  dy,       220,         verbose, True)

h_qcd      = getHisto(qcdLabel,        qcdLeg,         pDir, varNom,  qcd,      kMagenta+4,      verbose, True)

h_sig      = getHisto(sigLabel,        sigLeg,         pDir, varNom,  sig,      kBlack,      verbose, True)



#h_data     = getHisto(dataLabel,       dataLeg,        pDir, varNom,  data,     kBlack,     verbose, True)

#h_top      = getHisto(topLabel,        topLeg,         pDir, varNom,  top,      8,          verbose, True)

#h_top_plus_x      = getHisto(topxLabel,        topxLeg,         pDir, varNom,  top_plus_x,      kGreen,          verbose, True)

#h_wjets    = getHisto(wjLabel,         wjLeg,          pDir, varNom,  wjets,    kBlue,      verbose, True)

#h_st       = getHisto(sTLabel,         sTLeg,          pDir, varNom,  st,       kCyan,      verbose, True)

#h_dy       = getHisto(dyLabel,         dyLeg,          pDir, varNom,  dy,       90,         verbose, True)

#h_qcd      = getHisto(qcdLabel,        qcdLeg,         pDir, varNom,  qcd,      kMagenta+4,      verbose, True)

##h_dib      = getHisto(dibLabel,        dibLeg,         pDir, varNom,  dib,      kMagenta,      verbose, True)

##h_sig      = getHisto(sigLabel,        sigLeg,         pDir, varNom,  sig,      kRed,      verbose, True)

#AI:

#h_sig      = getHisto(sigLabel,        sigLeg,         pDir, varNom,  sig,      kBlack,      verbose, True)



#h_data     = getHisto(dataLabel,       dataLeg,        pDir, varNom,  data,     kBlack,     verbose, True)

#h_top      = getHisto(topLabel,        topLeg,         pDir, varNom,  top,      8,          verbose, True)

#h_top_plus_x      = getHisto(topxLabel,        topxLeg,         pDir, varNom,  top_plus_x,      kGreen,          verbose, True)

#h_dy       = getHisto(dyLabel,         dyLeg,          pDir, varNom,  dy,       90,         verbose, True)

#h_wjets    = getHisto(wjLabel,         wjLeg,          pDir, varNom,  wjets,    kBlue,      verbose, True)

#h_st       = getHisto(sTLabel,         sTLeg,          pDir, varNom,  st,       kCyan,      verbose, True)

#h_qcd      = getHisto(qcdLabel,        qcdLeg,         pDir, varNom,  qcd,      kMagenta+4,      verbose, True)

##h_dib      = getHisto(dibLabel,        dibLeg,         pDir, varNom,  dib,      kMagenta,      verbose, True)

#h_sig      = getHisto(sigLabel,        sigLeg,         pDir, varNom,  sig,      kRed,      verbose, True)



templates = []

#AI:

#templates.append(h_qcd)

#templates.append(h_dy)

#templates.append(h_st)

#templates.append(h_top_plus_x)

#templates.append(h_top)

#templates.append(h_wjets)

templates.append(h_qcd)

templates.append(h_st)

templates.append(h_dy)

templates.append(h_top)

templates.append(h_top_plus_x)

templates.append(h_wjets)

#templates.append(h_dib)



#f = TFile(plotDir+"/"+skimType+"/"+varNom+".root", "RECREATE")

#for ihist in templates:

#    ihist.Write()

#f.Close()



#get background uncertainty

h_bkg = h_top.Clone()

h_bkg.Reset()

h_bkg.SetName("total bkg")

h_bkg.Add(h_qcd)

h_bkg.Add(h_st)

h_bkg.Add(h_dy)

h_bkg.Add(h_top)

h_bkg.Add(h_top_plus_x)

h_bkg.Add(h_wjets)

#h_bkg.Add(h_dib)



#histo properties

nBins = h_bkg.GetNbinsX()

bMin = h_bkg.GetBinLowEdge(1)

bMax = h_bkg.GetBinLowEdge(nBins+1)

bin1 = h_bkg.GetXaxis().FindBin(bMin)

bin2 = h_bkg.GetXaxis().FindBin(bMax)





h_bkg_name_map = {}

h_bkg_names =  []

if (Sys):

  for item in shapeSys:

      hname = "h_bkg_"+str(item)

      hnamestr = hname

      #hname = ROOT.TH1D(str(hnamestr), "", nBins, bMin, bMax)

      hname = h_top.Clone()

      hname.Reset()

      h_bkg_name_map.update({str(hnamestr) : hname})

      h_bkg_names.append(str(hnamestr))



if (Sys):

  i = 0

  for item in shapeSys:

      #hname = "h_bkg_"+str(item)

      #hname = h_top.Clone()

      #hname.Reset()

      varTemp = var+"_"+str(item)+"_16"

      h_temp_top        = getHisto(topLabel,        topLeg,         pDir, varTemp,  top,      8,          verbose, False)

      h_temp_top_plus_x = getHisto(topxLabel,        topxLeg,         pDir, varTemp,  top_plus_x,      kGreen,          verbose, False)

      h_temp_dy         = getHisto(dyLabel,         dyLeg,          pDir, varTemp,  dy,       90,         verbose, False)

      h_temp_wjets      = getHisto(wjLabel,         wjLeg,          pDir, varTemp,  wjets,    kBlue,      verbose, False)

      h_temp_st         = getHisto(sTLabel,         sTLeg,          pDir, varTemp,  st,       kCyan,      verbose, False)

      h_temp_qcd        = getHisto(qcdLabel,        qcdLeg,         pDir, varTemp,  qcd,      kMagenta+4,      verbose, False)

      #h_temp_dib       = getHisto(dibLabel,        dibLeg,         pDir, varTemp,  dib,      kMagenta,      verbose, False)

      #h_temp_sig        = getHisto(sigLabel,        sigLeg,         pDir, varTemp,  sig,      kRed,      verbose, False)

      #Stack histograms

      h_bkg_name_map[h_bkg_names[i]].Add(h_temp_top)

      h_bkg_name_map[h_bkg_names[i]].Add(h_temp_top_plus_x)

      h_bkg_name_map[h_bkg_names[i]].Add(h_temp_dy)

      h_bkg_name_map[h_bkg_names[i]].Add(h_temp_wjets)

      h_bkg_name_map[h_bkg_names[i]].Add(h_temp_st)

      h_bkg_name_map[h_bkg_names[i]].Add(h_temp_qcd)

      #h_bkg_name_map[h_bkg_names[i]].Add(h_temp_sig)

      i = i + 1





StatErr = 0

SysErr  = 0

lheArray = ["h_bkg_LHEScale1", "h_bkg_LHEScale2", "h_bkg_LHEScale3", "h_bkg_LHEScale4", "h_bkg_LHEScale6", "h_bkg_LHEScale8"]

for ibin in range(0,nBins+1):    

    iTop     = h_top.GetBinContent(ibin)

    iST      = h_st.GetBinContent(ibin)

    iDY      = h_dy.GetBinContent(ibin)

    iWJ      = h_wjets.GetBinContent(ibin)

    # stat error

    stat_err = (h_bkg.GetBinError(ibin))**2 

    # add approximate systematic uncertainty to each bin

    lumi_err = 0.04**2

    ID_err   = 0.03**2

    dy_err   = (0.1*iDY)**2

    top_err  = (0.1*iTop)**2

    st_err   = (0.1*iST)**2

    wjet_err = (0.1*iWJ)**2



    if (Sys and 'Counter' not in var):

      pileup_err = ((h_bkg_name_map["h_bkg_PileupUp"].GetBinContent(ibin) - h_bkg_name_map["h_bkg_PileupDown"].GetBinContent(ibin))/2)

      BTagSF_err = ((h_bkg_name_map["h_bkg_BTagSFUp"].GetBinContent(ibin) - h_bkg_name_map["h_bkg_BTagSFDown"].GetBinContent(ibin))/2)

      topptweight_err = ((h_bkg_name_map["h_bkg_topptweightUp"].GetBinContent(ibin) - h_bkg_name_map["h_bkg_topptweightDown"].GetBinContent(ibin))/2)

      jer_err  = ((h_bkg_name_map["h_bkg_jerUp"].GetBinContent(ibin) - h_bkg_name_map["h_bkg_jerDown"].GetBinContent(ibin))/2) 

      jes_err  = ((h_bkg_name_map["h_bkg_jesUp"].GetBinContent(ibin) - h_bkg_name_map["h_bkg_jesDown"].GetBinContent(ibin))/2)

      maxlhe = 0

      for item in range(len(lheArray)):

        if ((abs(h_bkg_name_map[lheArray[item]].GetBinContent(ibin) - h_bkg.GetBinContent(ibin)))) > maxlhe:

          maxlhe = abs(h_bkg_name_map[lheArray[item]].GetBinContent(ibin) - h_bkg.GetBinContent(ibin))

      LHEScale_err =  maxlhe



    new_err = stat_err

    StatErr += (stat_err) 

    if (Sys):

      new_err = new_err +  pileup_err + BTagSF_err + topptweight_err + lumi_err + jer_err + jes_err + ID_err + dy_err + top_err + st_err + wjet_err + LHEScale_err

      SysErr += (pileup_err + BTagSF_err + topptweight_err + lumi_err + jer_err + jes_err + ID_err + dy_err + top_err + st_err + wjet_err +  LHEScale_err)



    if h_bkg.GetBinError(ibin) != 0: h_bkg.SetBinError(ibin, TMath.Sqrt(new_err))



h_bkg.SetMarkerSize(0)

h_bkg.SetLineWidth(2)

h_bkg.SetFillColor(14)

h_bkg.SetLineColor(0)

h_bkg.SetFillStyle(3244)



#histogram to print the total background with stat uncertainty

h_tot = h_top.Clone()

h_tot.Reset()

h_tot.SetName("Total_"+h_tot.GetName().split('_',1)[1])

h_tot.Add(h_qcd)

h_tot.Add(h_st)

h_tot.Add(h_top)

h_tot.Add(h_top_plus_x)

h_tot.Add(h_dy)

h_tot.Add(h_wjets)

#h_tot.Add(h_dib)



#print h_tot.GetName().split('_',1)[1]



## =========Drawing==============

#integralError = Double(5)

integralError = ctypes.c_double(5)

# print the latex table:

print ('\\begin{tabular}{|c|c| }')

print ('\hline')

print ('Sample     & Events  \\\\ ')

print ('\hline')

count = 0

for ihist in templates :

    #if var != 'cutFlow':overUnderFlow(ihist)

    count = count+1

    if count == 10:

        print ('\hline')

    if count == 14:

        print ('\hline')

    ihist.IntegralAndError(bin1,bin2,integralError)



    if 'TT' in ihist.GetName() or 'BB' in ihist.GetName():

        print ('{0:<5} & {1:<5.2f} $\pm$ {2:<5.2f} \\\\ '.format(ihist.GetName().split('_')[1], ihist.Integral(bin1,bin2), integralError.value))

    else:

        print ('{0:<5} & {1:<5.2f} $\pm$ {2:<5.2f} \\\\ '.format(ihist.GetName().split('_')[0], ihist.Integral(bin1,bin2), integralError.value))



#print ('line 413')

print ('\hline')

print ('{0:<5} & {1:<5.0f} \\\\ '.format('Tot Bkg', h_tot.Integral(bin1,bin2), integralError))

print ('\hline')

#print ('{0:<5} & {1:<5.0f} \\\\ '.format(h_data.GetName().split('_')[0], h_data.Integral()))

#print ('line 417')

print ("Data/MC: ", h_data.Integral()/h_tot.Integral(bin1,bin2))

print ("Signal: ", h_sig.Integral(bin1,bin2))

print ('\end{tabular}')

#print 'bkg : ', h_bkg.Integral(ibin,bin2), 'tot : ', h_tot.Integral(ibin,bin2)



if (Sys): print ("Statistical  Error: ", TMath.Sqrt(StatErr), " Systematic Error: ", TMath.Sqrt(SysErr))



hs = THStack("","")



print(templates)

for ihist in reversed(templates[0:6]):

    print ('about to add', ihist.GetName())

    hs.Add(ihist)

    print ('histo added', ihist.GetName())

    

#print ("Done!")



# Canvas

c1 = TCanvas('c1', 'c1', 800, 600)

#print("line 438")

c1.Divide(1,2)

#print("line 439")

scale = (1.0 - 0.3)/0.35



#print("line 441")

# prepare top pad for original plot

pad = c1.cd(1)

pad.SetPad(0, 0.3, 1, 1)

pad.SetTopMargin(0.1)

pad.SetBottomMargin(0.005)

t = pad.GetTopMargin()



#print("line 449")

# prepare the 2nd pad

pad = c1.cd(2)

pad.SetPad(0, 0.0, 1, 0.3)

pad.SetTopMargin(0.06)

pad.SetBottomMargin(0.4)

pad.SetTickx(1)

pad.SetTicky(1)

c1.cd(1)



#print("line 459")

hs.SetMaximum(hs.GetMaximum()*6)

hs.SetMinimum(0.1)

#hs.SetMaximum(hs.GetMaximum()*5)

#hs.SetMinimum(0.1)

'''if 'NNscore' in var:
   pass
else:''' 
gPad.SetLogy()


#print ("line 466")

hs.Draw("Hist")

h_bkg.Draw("e2 same")

h_data.Draw("same")

#AI:

h_sig.Draw("histsame")





print(templates)

for ihist in reversed(templates[6:8]):

    print ('overlaying, ', ihist.GetName())

    ihist.Draw("ehist same")



xTitle= xtitle

#xTitle= h_top.GetXaxis().GetTitle()

#yTitle= h_top.GetYaxis().GetTitle()

print ("-----------------------")

print (var)

setTitle(hs, var)

gPad.RedrawAxis()

ll = TLatex()

ll.SetNDC(kTRUE)

ll.SetTextSize(0.05)

#AI:

ll.SetTextFont(42)

ll.DrawLatex(0.7,0.92, "136.65 fb^{-1} (13 TeV)");#2.2



cms = TLatex()

cms.SetNDC(kTRUE)

cms.SetTextFont(61)

#AI:

cms.SetTextSize(0.06)

cms.DrawLatex(0.16, 0.82,"CMS")

#print ("y-coord = ", 1-t+0.2*t)



sel = TLatex()

sel.SetNDC(kTRUE)

sel.SetTextSize(0.065)



chan = TLatex()

chan.SetNDC(kTRUE)

chan.SetTextSize(0.065)

chan.DrawLatex(0.50, 0.76, title)



prel = TLatex()

prel.SetNDC(kTRUE)

prel.SetTextFont(52)

#AI:

prel.SetTextSize(0.75*t*0.76)

prel.SetTextSize(0.06)

prel.DrawLatex(0.23,0.82,"Preliminary")



#AI:

Chi2Prob = h_bkg.Chi2Test(h_data,"p")

print ('Chi2Test = %2.3f' % Chi2Prob)

chi2result = '%2.3f' % Chi2Prob

chi2 = TLatex()

chi2.SetNDC(kTRUE)

chi2.SetTextFont(52)

chi2.SetTextSize(0.055)

chi2.DrawLatex(0.48,0.80,'#chi^{2} prob = '+chi2result)

#AI:

KSprob = h_bkg.KolmogorovTest(h_data,"X")

print('KStest = %2.3f' % KSprob)

KSresult = '%2.3f' % KSprob

ks = TLatex()

ks.SetNDC(kTRUE)

ks.SetTextFont(52)

ks.SetTextSize(0.055)

ks.DrawLatex(0.47,0.70,'KS prob = '+KSresult)



leg.Draw()

gPad.RedrawAxis()





c1.cd(2)

# add the systematic band

h_ratio = h_data.Clone()

h_ratio_bkg = h_bkg.Clone()

h_ratio_bkg.SetDirectory(0)

h_ratio.SetDirectory(0)

h_ratio.Divide(h_data, h_tot)

h_ratio_bkg.Divide(h_bkg, h_tot)



for ibin in range(1, nBins+1):

    if h_bkg.GetBinContent(ibin) == 0: h_ratio_bkg.SetBinContent(ibin,1)



prepareRatio(h_ratio, h_ratio_bkg, scale, xTitle)



line = TLine(bMin, 1, bMax, 1)

line.SetLineColor(kBlack)

h_ratio.Draw("")

h_ratio_bkg.Draw("e2same")

h_ratio.Draw("same")

line.Draw()



gPad.RedrawAxis()



#create a directory if it doesn't exist

m_1 = 'mkdir -p '+plotDir

m_2 = 'mkdir -p '+plotDir+"/"+skimType

if not os.path.isdir(plotDir):

    subprocess.call( [m_1], shell=True )

if not os.path.isdir(plotDir+"/"+skimType):

    subprocess.call( [m_2], shell=True )    

    

#c1.SaveAs(plotDir+"/"+skimType+"/"+var+"_.pdf")

c1.SaveAs(plotDir+"/"+skimType+"/"+var+"_.gif")

#raw_input("hold on")




