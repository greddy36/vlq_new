#! /usr/bin/env python



# =====================================================

#  INPUTS		

# =====================================================

#ST SF for  TT and WJets, HT for WJets

#path2016 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv5/2016/11May2020_noToppt_applySTtoTTWJets/";

#path2017 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv5/2017/11May2020_noToppt_applySTtoTTWJets/";

#path2018 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv6/2018/11May2020_noToppt_applySTtoTTWJets/";



#WJets, no ST scaling,

#path2016 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv5/2016/30Apr2020_applyWt/";

#path2017 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv5/2017/30Apr2020_applyWt/";

#path2018 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv6/2018/30Apr2020_applyWt/";



#path2016 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv5/2016/17June2020_puidTig_noalignCR_noScale_fixHEMFlat_Skim/";

#path2017 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv5/2017/17June2020_puidTig_noalignCR_noScale_fixHEMFlat_Skim/";

#path2018 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv6/2018/17June2020_puidTig_noalignCR_noScale_fixHEMFlat_Skim/";



#path2016 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv5/2016/16June2020_puidTig_noalignCR_noScale_debugHEM/";

#path2017 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv5/2017/16June2020_puidTig_noalignCR_noScale_debugHEM/";

#path2018 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv6/2018/16June2020_puidTig_noalignCR_noScale_debugHEM/";



#path2016 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv5/2016/3Jul2020_nopuDR_noalignCR_Scale_fixHEM_Sys_Skim/";

#path2017 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv5/2017/3Jul2020_nopuDR_noalignCR_Scale_fixHEM_Sys_Skim/";

#path2018 = "/Users/amodak/VLQ/NanoPostProc/files/NanoAODv6/2018/3Jul2020_nopuDR_noalignCR_Scale_fixHEM_Sys_Skim/";



path2016 = "out_wjet/2016_hist/";

path2017 = "out_wjet/2017_hist/";

path2018 = "out_wjet/2018_hist/";



applyHTScale = True

CH = "Mu"

if (CH == "Mu"):

  print ("Using Muon Ch Data")

  f_Data_ReMiniAOD_2016 = TFile(path2016+'SingleMuon_2016'+'.root')

  f_Data_ReMiniAOD_2017 = TFile(path2017+'SingleMuon_2017'+'.root')

  f_Data_ReMiniAOD_2018 = TFile(path2018+'SingleMuon_2018'+'.root')

elif (CH == "Ele"):

  print ("Using Electron Ch Data")

  f_Data_ReMiniAOD_2016 = TFile(path2016+'SingleElectron_2016'+'.root')

  f_Data_ReMiniAOD_2017 = TFile(path2017+'SingleElectron_2017'+'.root')

  f_Data_ReMiniAOD_2018 = TFile(path2018+'SingleElectron_2018'+'.root')

  



f_2016DY100to200 = TFile(path2016+'DYJetsToLL_M-50_HT-100to200_2016'+'.root')

f_2016DY200to400 = TFile(path2016+'DYJetsToLL_M-50_HT-200to400_2016'+'.root')

f_2016DY400to600 = TFile(path2016+'DYJetsToLL_M-50_HT-400to600_2016'+'.root')

f_2016DY600to800 = TFile(path2016+'DYJetsToLL_M-50_HT-600to800_2016'+'.root')

f_2016DY800to1200 = TFile(path2016+'DYJetsToLL_M-50_HT-800to1200_2016'+'.root')

f_2016DY1200to2500 = TFile(path2016+'DYJetsToLL_M-50_HT-1200to2500_2016'+'.root')

f_2016DY2500toInf = TFile(path2016+'DYJetsToLL_M-50_HT-2500toInf_2016'+'.root')



f_2016WJ100to200 = TFile(path2016+'WJetsToLNu_HT-100To200_2016'+'.root')

f_2016WJ200to400 = TFile(path2016+'WJetsToLNu_HT-200To400_2016'+'.root')

f_2016WJ400to600 = TFile(path2016+'WJetsToLNu_HT-400To600_2016'+'.root')

f_2016WJ600to800 = TFile(path2016+'WJetsToLNu_HT-600To800_2016'+'.root')

f_2016WJ800to1200 = TFile(path2016+'WJetsToLNu_HT-800To1200_2016'+'.root')

f_2016WJ1200to2500 = TFile(path2016+'WJetsToLNu_HT-1200To2500_2016'+'.root')

f_2016WJ2500toInf = TFile(path2016+'WJetsToLNu_HT-2500ToInf_2016'+'.root')



f_2016ST_tW_top     = TFile(path2016+'ST_tW_top_2016'+'.root')

f_2016ST_tW_antitop = TFile(path2016+'ST_tW_antitop_2016'+'.root')

f_2016ST_t_top          = TFile(path2016+'ST_t-channel_top_2016'+'.root')

f_2016ST_t_antitop      = TFile(path2016+'ST_t-channel_antitop_2016'+'.root')



f_2016ttbar_pow         = TFile(path2016+'TT_TuneCUETP8M2T4_powheg-pythia8_2016'+'.root')

f_2016ttbar         = TFile(path2016+'TTJets_TuneCUETP8M1_13TeV-madgraphMLM_2016'+'.root')



f_2016QCD170to300    = TFile(path2016+'QCD_Pt_170to300_2016'+'.root') 

f_2016QCD300to470    = TFile(path2016+'QCD_Pt_300to470_2016'+'.root') 

f_2016QCD470to600    = TFile(path2016+'QCD_Pt_470to600_2016'+'.root') 

f_2016QCD600to800    = TFile(path2016+'QCD_Pt_600to800_2016'+'.root') 

f_2016QCD800to1000   = TFile(path2016+'QCD_Pt_800to1000_2016'+'.root') 

f_2016QCD1000to1400  = TFile(path2016+'QCD_Pt_1000to1400_2016'+'.root') 

f_2016QCD1400to1800  = TFile(path2016+'QCD_Pt_1400to1800_2016'+'.root') 

f_2016QCD1800to2400  = TFile(path2016+'QCD_Pt_1800to2400_2016'+'.root') 

f_2016QCD2400to3200  = TFile(path2016+'QCD_Pt_2400to3200_2016'+'.root') 

f_2016QCD3200toInf   = TFile(path2016+'QCD_Pt_3200toInf_2016'+'.root') 



f_2016SIG1200         = TFile(path2016+'TprimeBToBW_M-1200_2016'+'.root')



#===== cross sections (pb)==========



Top_xs_2016            = 831.76  *gSF

#2016 Muon Scaling

#DeepCSV

#Top_xs_2016            = 831.76  *gSF * 0.794 

#DeepFLV

#Top_xs_2016            = 831.76  *gSF * 0.783



#2016 Ele Scaling

#DeepCSV

#Top_xs_2016            = 831.76  *gSF * 0.931

#DeepFLV

#Top_xs_2016            = 831.76  *gSF * 0.925



DY100to200_xs_2016     = 147.4   *gSF

DY200to400_xs_2016     = 41.04   *gSF

DY400to600_xs_2016     = 5.674   *gSF

DY600to800_xs_2016     = 1.358   *gSF

DY800to1200_xs_2016     = 0.6229   *gSF

DY1200to2500_xs_2016     = 0.1512   *gSF

DY2500toInf_xs_2016     = 0.003659   *gSF

##With LHE correction

#For Ele Ch

corrSF = 1.0

#corrSF = 1.171





if (applyHTScale):

  WJ100to200_xs_2016     = 1345.0  *gSF *1.21 *1.0 *corrSF

  WJ200to400_xs_2016     = 359.7   *gSF *1.21 *1.0 *corrSF

  WJ400to600_xs_2016     = 48.9    *gSF *1.21 *0.88842 *corrSF

  WJ600to800_xs_2016     = 12.05   *gSF *1.21 *0.83367 *corrSF

  WJ800to1200_xs_2016    = 5.501   *gSF *1.21 *0.76412 *corrSF

  WJ1200to2500_xs_2016   = 1.329   *gSF *1.21 *0.67636 *corrSF

  WJ2500toInf_xs_2016    = 0.03216 *gSF *1.21 *0.58820 *corrSF

else:

  WJ100to200_xs_2016     = 1345.0  *gSF *1.21 *corrSF

  WJ200to400_xs_2016     = 359.7   *gSF *1.21 *corrSF

  WJ400to600_xs_2016     = 48.9    *gSF *1.21 *corrSF

  WJ600to800_xs_2016     = 12.05   *gSF *1.21 *corrSF

  WJ800to1200_xs_2016    = 5.501   *gSF *1.21 *corrSF

  WJ1200to2500_xs_2016   = 1.329   *gSF *1.21 *corrSF

  WJ2500toInf_xs_2016    = 0.03216 *gSF *1.21 *corrSF

'''

#From Julie

WJ100to200_xs_2016     = 1345.0  *gSF *1.21 *0.998056 *corrSF

WJ200to400_xs_2016     = 359.7   *gSF *1.21 *0.978569 *corrSF

WJ400to600_xs_2016     = 48.9    *gSF *1.21 *0.928054 *corrSF

WJ600to800_xs_2016     = 12.05   *gSF *1.21 *0.856705 *corrSF

WJ800to1200_xs_2016    = 5.501   *gSF *1.21 *0.757463 *corrSF

WJ1200to2500_xs_2016   = 1.329   *gSF *1.21 *0.608292 *corrSF

WJ2500toInf_xs_2016    = 0.03216 *gSF *1.21 *0.454246 *corrSF

'''

#Without LHE correction

#WJ100to200_xs_2016     = 1345.0  *gSF *1.21  

#WJ200to400_xs_2016     = 359.7   *gSF *1.21

#WJ400to600_xs_2016     = 48.9    *gSF *1.21

#WJ600to800_xs_2016     = 12.05   *gSF *1.21

#WJ800to1200_xs_2016    = 5.501   *gSF *1.21

#WJ1200to2500_xs_2016   = 1.329   *gSF *1.21

#WJ2500toInf_xs_2016    = 0.03216 *gSF *1.21

ST_tW_top_xs_2016      = 35.6    *gSF

ST_tW_antitop_xs_2016  = 35.6    *gSF 

ST_t_top_xs_2016       = 44.33   *gSF

ST_t_antitop_xs_2016   = 26.38   *gSF 

#QCD NLO XS

fact = 1

QCD170to300_xs_2016    = 117276 * fact

QCD300to470_xs_2016    = 7823 *fact

QCD470to600_xs_2016    = 648 *fact

QCD600to800_xs_2016    = 187 *fact

QCD800to1000_xs_2016   = 32 *fact

QCD1000to1400_xs_2016  = 9.4 *fact

QCD1400to1800_xs_2016  = 0.84 *fact

QCD1800to2400_xs_2016  = 0.12 *fact

QCD2400to3200_xs_2016  = 0.007 *fact

QCD3200toInf_xs_2016   = 0.0002 *fact



WW1L2Q_xs_2016         = 45.85 #powheg nnlo 50.0

WZ1L2Q_xs_2016         = 10.71



SIG1200_xs_2016        = 1.0

Top_pow_xs_2016            = 831.76  *gSF



#===== Number of generated events ======



nEvt_2016 = [1.01991e+07,1.10171e+07,9.60914e+06,9.72566e+06,8.29296e+06,2.67307e+06,596079,399492,7.8043e+07,3.89268e+07,7.7597e+06,1.86684e+07,7.83054e+06,6.87244e+06,2.63782e+06,6.95283e+06,6.93309e+06,6.71059e+07,3.8811e+07,1.47968e+07,2.24704e+07,3.96e+06,1.35247e+07,1.96971e+07,9.84662e+06,2.87343e+06,996130,996130,391735, 93600, 7.67481e+07]



Top_num_2016          =  nEvt_2016[0]

DY100to200_num_2016   =  nEvt_2016[1]

DY200to400_num_2016   =  nEvt_2016[2]

DY400to600_num_2016   =  nEvt_2016[3]

DY600to800_num_2016   =  nEvt_2016[4]

DY800to1200_num_2016   =  nEvt_2016[5]

DY1200to2500_num_2016   =  nEvt_2016[6]

DY2500toInf_num_2016   =  nEvt_2016[7]

#Without Ht 

WJ100to200_num_2016   =  nEvt_2016[8]

WJ200to400_num_2016   =  nEvt_2016[9]

WJ400to600_num_2016   =  nEvt_2016[10]

WJ600to800_num_2016   =  nEvt_2016[11]

WJ800to1200_num_2016  =  nEvt_2016[12]

WJ1200to2500_num_2016 =  nEvt_2016[13]

WJ2500toInf_num_2016  =  nEvt_2016[14]



ST_tW_top_num_2016    =  nEvt_2016[15]

ST_tW_antitop_num_2016=  nEvt_2016[16]

ST_t_top_num_2016     =  nEvt_2016[17]

ST_t_antitop_num_2016 =  nEvt_2016[18] 



QCD170to300_num_2016    = nEvt_2016[19] 

QCD300to470_num_2016    = nEvt_2016[20] 

QCD470to600_num_2016    = nEvt_2016[21] 

QCD600to800_num_2016    = nEvt_2016[22] 

QCD800to1000_num_2016   = nEvt_2016[23] 

QCD1000to1400_num_2016  = nEvt_2016[24] 

QCD1400to1800_num_2016  = nEvt_2016[25] 

QCD1800to2400_num_2016  = nEvt_2016[26] 

QCD2400to3200_num_2016  = nEvt_2016[27] 

QCD3200toInf_num_2016   = nEvt_2016[28] 



#WW1L2Q_num_2016         = nEvt_2016[26]

#WZ1L2Q_num_2016         = nEvt_2016[27]



SIG1200_num_2016        = nEvt_2016[29]

Top_pow_num_2016          =  nEvt_2016[30]





#2017

f_2017DY100to200 = TFile(path2017+'DYJetsToLL_M-50_HT-100to200_2017'+'.root')

f_2017DY200to400 = TFile(path2017+'DYJetsToLL_M-50_HT-200to400_2017'+'.root')

f_2017DY400to600 = TFile(path2017+'DYJetsToLL_M-50_HT-400to600_2017'+'.root')

f_2017DY600to800 = TFile(path2017+'DYJetsToLL_M-50_HT-600to800_2017'+'.root')

f_2017DY800to1200 = TFile(path2017+'DYJetsToLL_M-50_HT-800to1200_2017'+'.root')

f_2017DY1200to2500 = TFile(path2017+'DYJetsToLL_M-50_HT-1200to2500_2017'+'.root')

f_2017DY2500toInf = TFile(path2017+'DYJetsToLL_M-50_HT-2500toInf_2017'+'.root')



f_2017WJ100to200 = TFile(path2017+'WJetsToLNu_HT-100To200_2017'+'.root')

f_2017WJ200to400 = TFile(path2017+'WJetsToLNu_HT-200To400_2017'+'.root')

f_2017WJ400to600 = TFile(path2017+'WJetsToLNu_HT-400To600_2017'+'.root')

f_2017WJ600to800 = TFile(path2017+'WJetsToLNu_HT-600To800_2017'+'.root')

f_2017WJ800to1200 = TFile(path2017+'WJetsToLNu_HT-800To1200_2017'+'.root')

f_2017WJ1200to2500 = TFile(path2017+'WJetsToLNu_HT-1200To2500_2017'+'.root')

f_2017WJ2500toInf = TFile(path2017+'WJetsToLNu_HT-2500ToInf_2017'+'.root')



f_2017ST_tW_top     = TFile(path2017+'ST_tW_top_2017'+'.root')

f_2017ST_tW_antitop = TFile(path2017+'ST_tW_antitop_2017'+'.root')

f_2017ST_t_top          = TFile(path2017+'ST_t-channel_top_2017'+'.root')

f_2017ST_t_antitop      = TFile(path2017+'ST_t-channel_antitop_2017'+'.root')



f_2017ttbar         = TFile(path2017+'TTJets_TuneCP5_13TeV-madgraphMLM_2017'+'.root')

f_2017ttbar_2L2Nu         = TFile(path2017+'TTTo2L2Nu_TuneCP5_powheg-pythia8_2017'+'.root')

f_2017ttbar_SemiLep         = TFile(path2017+'TTToSemiLeptonic_TuneCP5_powheg-pythia8_2017'+'.root')

f_2017ttbar_2L2NuPS         = TFile(path2017+'TTTo2L2Nu_TuneCP5_PSweights_powheg-pythia8_2017'+'.root')

f_2017ttbar_SemiLepPS         = TFile(path2017+'TTToSemiLeptonic_TuneCP5_PSweights_powheg-pythia8_2017'+'.root')

f_2017ttbar_HadPS         = TFile(path2017+'TTToHadronic_TuneCP5_PSweights_powheg-pythia8_2017'+'.root')

f_2017TTWJetsToLNu         = TFile(path2017+'TTWJetsToLNu_TuneCP5_PSweights_amcatnloFXFX-madspin-pythia8_2017'+'.root')

f_2017TTWJetsToQQ         = TFile(path2017+'TTWJetsToQQ_TuneCP5_amcatnloFXFX-madspin-pythia8_2017'+'.root')

f_2017TTZToLLNuNu         = TFile(path2017+'TTZToLLNuNu_M-10_TuneCP5_amcatnlo-pythia8_2017'+'.root')

f_2017TTZToQQ         = TFile(path2017+'TTZToQQ_TuneCP5_amcatnlo-pythia8_2017'+'.root')



#f_2017QCD100to200    = TFile(path2017+'QCD_HT100to200_2017'+'.root') 

#f_2017QCD200to300    = TFile(path2017+'QCD_HT200to300_2017'+'.root') 

f_2017QCD300to500    = TFile(path2017+'QCD_HT300to500_2017'+'.root') 

f_2017QCD500to700    = TFile(path2017+'QCD_HT500to700_2017'+'.root') 

f_2017QCD700to1000   = TFile(path2017+'QCD_HT700to1000_2017'+'.root') 

f_2017QCD1000to1500  = TFile(path2017+'QCD_HT1000to1500_2017'+'.root') 

f_2017QCD1500to2000  = TFile(path2017+'QCD_HT1500to2000_2017'+'.root') 

f_2017QCD2000toInf  = TFile(path2017+'QCD_HT2000toInf_2017'+'.root') 



f_2017SIG1200         = TFile(path2017+'TprimeBToBW_M-1200_2017'+'.root')



#===== cross sections (pb)==========



Top_xs_2017            = 831.76  *gSF

#2017 Ele Ch SF

#DeepCSV

#Top_xs_2017            = 831.76  *gSF *0.864

#DeepFLV

#Top_xs_2017            = 831.76  *gSF *0.914



DY100to200_xs_2017     = 147.4   *gSF

DY200to400_xs_2017     = 41.04   *gSF

DY400to600_xs_2017     = 5.674   *gSF

DY600to800_xs_2017     = 1.358   *gSF

DY800to1200_xs_2017     = 0.6229   *gSF

DY1200to2500_xs_2017     = 0.1512   *gSF

DY2500toInf_xs_2017     = 0.003659   *gSF



if (applyHTScale):

  WJ100to200_xs_2017     = 1345.0  *gSF *1.21 *1.0 *corrSF

  WJ200to400_xs_2017     = 359.7   *gSF *1.21 *1.0 *corrSF

  WJ400to600_xs_2017     = 48.9    *gSF *1.21 *0.88842 *corrSF

  WJ600to800_xs_2017     = 12.05   *gSF *1.21 *0.83367 *corrSF

  WJ800to1200_xs_2017    = 5.501   *gSF *1.21 *0.76412 *corrSF

  WJ1200to2500_xs_2017   = 1.329   *gSF *1.21 *0.67636 *corrSF

  WJ2500toInf_xs_2017    = 0.03216 *gSF *1.21 *0.58820 *corrSF

else:

  WJ100to200_xs_2017     = 1345.0  *gSF *1.21 *corrSF

  WJ200to400_xs_2017     = 359.7   *gSF *1.21 *corrSF

  WJ400to600_xs_2017     = 48.9    *gSF *1.21 *corrSF

  WJ600to800_xs_2017     = 12.05   *gSF *1.21 *corrSF

  WJ800to1200_xs_2017    = 5.501   *gSF *1.21 *corrSF

  WJ1200to2500_xs_2017   = 1.329   *gSF *1.21 *corrSF

  WJ2500toInf_xs_2017    = 0.03216 *gSF *1.21 *corrSF

'''

##From Julie

WJ100to200_xs_2017     = 1345.0  *gSF *1.21 *0.998056 

WJ200to400_xs_2017     = 359.7   *gSF *1.21 *0.978569

WJ400to600_xs_2017     = 48.9    *gSF *1.21 *0.928054

WJ600to800_xs_2017     = 12.05   *gSF *1.21 *0.856705 

WJ800to1200_xs_2017    = 5.501   *gSF *1.21 *0.757463

WJ1200to2500_xs_2017   = 1.329   *gSF *1.21 *0.608292

WJ2500toInf_xs_2017    = 0.03216 *gSF *1.21 *0.454246

'''

#Without LHE correction

#WJ100to200_xs_2017     = 1345.0  *gSF *1.21  

#WJ200to400_xs_2017     = 359.7   *gSF *1.21

#WJ400to600_xs_2017     = 48.9    *gSF *1.21

#WJ600to800_xs_2017     = 12.05   *gSF *1.21

#WJ800to1200_xs_2017    = 5.501   *gSF *1.21

#WJ1200to2500_xs_2017   = 1.329   *gSF *1.21

#WJ2500toInf_xs_2017    = 0.03216 *gSF *1.21

ST_tW_top_xs_2017      = 35.6    *gSF

ST_tW_antitop_xs_2017  = 35.6    *gSF 

ST_t_top_xs_2017       = 44.33   *gSF

ST_t_antitop_xs_2017   = 26.38   *gSF 

#QCD NLO XS

fact = 1

QCD100to200_xs_2017    = 27990000 * fact

QCD200to300_xs_2017    = 1710000 *fact

QCD300to500_xs_2017    = 347500 *fact

QCD500to700_xs_2017    = 32060 *fact

QCD700to1000_xs_2017   = 6829 *fact

QCD1000to1500_xs_2017  = 1207 *fact

QCD1500to2000_xs_2017  = 120 *fact

QCD2000toInf_xs_2017  = 25.25 *fact



SIG1200_xs_2017        = 1.0



Top_xs_2017_2L2Nu            =  88.29 *gSF

Top_xs_2017_SemiLep            = 365.34  *gSF

Top_xs_2017_2L2NuPS            =  88.29 *gSF

Top_xs_2017_SemiLepPS            = 365.34  *gSF

Top_xs_2017_HadPS         = 377.96 *gSF



TTWJetsToLNu_xs_2017  = 0.2001 * gSF

TTWJetsToQQ_xs_2017   = 0.405 * gSF

TTZToLLNuNu_xs_2017   = 0.2529 * gSF

TTZToQQ_xs_2017       = 0.5297 * gSF



#===== Number of generated events ======

#More samples added

nEvt_2017 = [8.01696e+06,1.11801e+07,1.18968e+07,1.00037e+07,8.69161e+06,3.08971e+06,616923,401334,3.58046e+07,2.11922e+07,1.316e+07,2.15823e+07,2.0273e+07,1.99919e+07,2.06296e+07,2.72081e+08,2.79005e+08,5.98206e+06,3.67591e+06,9.3202e+07,5.91333e+07,6.02057e+07,5.6041e+07,4.74604e+07,1.64853e+07,1.15086e+07,5.82557e+06,100000, 6.4873e+08,1.31544e+10,4.7051e+09,2.92622e+10,3.99283e+10,1.69012e+06,560315,1.8384e+06,4.56491e+06]



Top_num_2017        =  nEvt_2017[0]

DY100to200_num_2017   =  nEvt_2017[1]

DY200to400_num_2017   =  nEvt_2017[2]

DY400to600_num_2017   =  nEvt_2017[3]

DY600to800_num_2017   =  nEvt_2017[4]

DY800to1200_num_2017   =  nEvt_2017[5]

DY1200to2500_num_2017   =  nEvt_2017[6]

DY2500toInf_num_2017   =  nEvt_2017[7]

#Without Ht 

WJ100to200_num_2017   =  nEvt_2017[8]

WJ200to400_num_2017   =  nEvt_2017[9]

WJ400to600_num_2017   =  nEvt_2017[10]

WJ600to800_num_2017   =  nEvt_2017[11]

WJ800to1200_num_2017  =  nEvt_2017[12]

WJ1200to2500_num_2017 =  nEvt_2017[13]

WJ2500toInf_num_2017  =  nEvt_2017[14]



ST_tW_top_num_2017    =  nEvt_2017[15]

ST_tW_antitop_num_2017=  nEvt_2017[16]

ST_t_top_num_2017     =  nEvt_2017[17]

ST_t_antitop_num_2017 =  nEvt_2017[18] 



QCD100to200_num_2017    = nEvt_2017[19] 

QCD200to300_num_2017    = nEvt_2017[20] 

QCD300to500_num_2017    = nEvt_2017[21] 

QCD500to700_num_2017    = nEvt_2017[22] 

QCD700to1000_num_2017   = nEvt_2017[23] 

QCD1000to1500_num_2017  = nEvt_2017[24] 

QCD1500to2000_num_2017  = nEvt_2017[25] 

QCD2000toInf_num_2017  = nEvt_2017[26] 

SIG1200_num_2017        = nEvt_2017[27]

Top_num_2017_2L2Nu          =  nEvt_2017[28]

Top_num_2017_SemiLep          =  nEvt_2017[29]

Top_num_2017_2L2NuPS          =  nEvt_2017[30]

Top_num_2017_SemiLepPS          =  nEvt_2017[31]

Top_num_2017_HadPS     = nEvt_2017[32]

TTWJetsToLNu_num_2017  = nEvt_2017[33]

TTWJetsToQQ_num_2017   = nEvt_2017[34]

TTZToLLNuNu_num_2017   = nEvt_2017[35]

TTZToQQ_num_2017       = nEvt_2017[36]



#2018

f_2018DY100to200 = TFile(path2018+'DYJetsToLL_M-50_HT-100to200_2018'+'.root')

f_2018DY200to400 = TFile(path2018+'DYJetsToLL_M-50_HT-200to400_2018'+'.root')

f_2018DY400to600 = TFile(path2018+'DYJetsToLL_M-50_HT-400to600_2018'+'.root')

f_2018DY600to800 = TFile(path2018+'DYJetsToLL_M-50_HT-400to600_2018'+'.root')

f_2018DY600to800 = TFile(path2018+'DYJetsToLL_M-50_HT-600to800_2018'+'.root')

f_2018DY800to1200 = TFile(path2018+'DYJetsToLL_M-50_HT-800to1200_2018'+'.root')

f_2018DY1200to2500 = TFile(path2018+'DYJetsToLL_M-50_HT-1200to2500_2018'+'.root')

f_2018DY2500toInf = TFile(path2018+'DYJetsToLL_M-50_HT-2500toInf_2018'+'.root')



f_2018WJ100to200 = TFile(path2018+'WJetsToLNu_HT-100To200_2018'+'.root')

f_2018WJ200to400 = TFile(path2018+'WJetsToLNu_HT-200To400_2018'+'.root')

f_2018WJ400to600 = TFile(path2018+'WJetsToLNu_HT-400To600_2018'+'.root')

f_2018WJ600to800 = TFile(path2018+'WJetsToLNu_HT-600To800_2018'+'.root')

f_2018WJ800to1200 = TFile(path2018+'WJetsToLNu_HT-800To1200_2018'+'.root')

f_2018WJ1200to2500 = TFile(path2018+'WJetsToLNu_HT-1200To2500_2018'+'.root')

f_2018WJ2500toInf = TFile(path2018+'WJetsToLNu_HT-2500ToInf_2018'+'.root')



f_2018ST_tW_top     = TFile(path2018+'ST_tW_top_2018'+'.root')

f_2018ST_tW_antitop = TFile(path2018+'ST_tW_antitop_2018'+'.root')

f_2018ST_t_top          = TFile(path2018+'ST_t-channel_top_2018'+'.root')

f_2018ST_t_antitop      = TFile(path2018+'ST_t-channel_antitop_2018'+'.root')



#f_2018ttbar         = TFile(path2018+'TTJets_TuneCP5_13TeV-madgraphMLM_2018'+'.root')

f_2018ttbar_2L2Nu         = TFile(path2018+'TTTo2L2Nu_TuneCP5_powheg-pythia8_2018'+'.root')

f_2018ttbar_SemiLep         = TFile(path2018+'TTToSemiLeptonic_TuneCP5_powheg-pythia8_2018'+'.root')

f_2018ttbar_Had         = TFile(path2018+'TTToHadronic_TuneCP5_powheg-pythia8_2018'+'.root')



#f_2018QCD100to200    = TFile(path2018+'QCD_HT100to200_2018'+'.root') 

#f_2018QCD200to300    = TFile(path2018+'QCD_HT200to300_2018'+'.root') 

f_2018QCD300to500    = TFile(path2018+'QCD_HT300to500_2018'+'.root') 

f_2018QCD500to700    = TFile(path2018+'QCD_HT500to700_2018'+'.root') 

f_2018QCD700to1000   = TFile(path2018+'QCD_HT700to1000_2018'+'.root') 

f_2018QCD1000to1500  = TFile(path2018+'QCD_HT1000to1500_2018'+'.root') 

f_2018QCD1500to2000  = TFile(path2018+'QCD_HT1500to2000_2018'+'.root') 

f_2018QCD2000toInf   = TFile(path2018+'QCD_HT2000toInf_2018'+'.root') 



f_2018SIG1200        = TFile(path2018+'TprimeBToBW_M-1200_2018'+'.root')



#===== cross sections (pb)==========



Top_xs_2018            = 831.76  *gSF

#2018 Muon Ch SF

#DeepCSV

#Top_xs_2018            = 831.76  *gSF *0.895

#DeepFLV

#Top_xs_2018            = 831.76  *gSF *0.877

#2018 Ele Ch SF

#DeepCSV

#Top_xs_2018            = 831.76  *gSF *0.852

#DeepFLV

#Top_xs_2018            = 831.76  *gSF *0.843



DY100to200_xs_2018     = 147.4   *gSF

DY200to400_xs_2018     = 41.04   *gSF

DY400to600_xs_2018     = 5.674   *gSF

DY600to800_xs_2018     = 1.358   *gSF 

DY800to1200_xs_2018     = 0.6229   *gSF

DY1200to2500_xs_2018     = 0.1512   *gSF

DY2500toInf_xs_2018     = 0.003659   *gSF



if (applyHTScale):

  WJ100to200_xs_2018     = 1345.0  *gSF *1.21 *1.0 *corrSF

  WJ200to400_xs_2018     = 359.7   *gSF *1.21 *1.0 *corrSF

  WJ400to600_xs_2018     = 48.9    *gSF *1.21 *0.88842 *corrSF

  WJ600to800_xs_2018     = 12.05   *gSF *1.21 *0.83367 *corrSF

  WJ800to1200_xs_2018    = 5.501   *gSF *1.21 *0.76412 *corrSF

  WJ1200to2500_xs_2018   = 1.329   *gSF *1.21 *0.67636 *corrSF

  WJ2500toInf_xs_2018    = 0.03216 *gSF *1.21 *0.58820 *corrSF

else:

  WJ100to200_xs_2018     = 1345.0  *gSF *1.21 *corrSF

  WJ200to400_xs_2018     = 359.7   *gSF *1.21 *corrSF

  WJ400to600_xs_2018     = 48.9    *gSF *1.21 *corrSF

  WJ600to800_xs_2018     = 12.05   *gSF *1.21 *corrSF

  WJ800to1200_xs_2018    = 5.501   *gSF *1.21 *corrSF

  WJ1200to2500_xs_2018   = 1.329   *gSF *1.21 *corrSF

  WJ2500toInf_xs_2018    = 0.03216 *gSF *1.21 *corrSF



'''

##From Julie

WJ100to200_xs_2018     = 1345.0  *gSF *1.21 *0.998056 

WJ200to400_xs_2018     = 359.7   *gSF *1.21 *0.978569

WJ400to600_xs_2018     = 48.9    *gSF *1.21 *0.928054

WJ600to800_xs_2018     = 12.05   *gSF *1.21 *0.856705 

WJ800to1200_xs_2018    = 5.501   *gSF *1.21 *0.757463

WJ1200to2500_xs_2018   = 1.329   *gSF *1.21 *0.608292

WJ2500toInf_xs_2018    = 0.03216 *gSF *1.21 *0.454246

'''

#Without LHE correction

#WJ100to200_xs_2018     = 1345.0  *gSF *1.21  

#WJ200to400_xs_2018     = 359.7   *gSF *1.21

#WJ400to600_xs_2018     = 48.9    *gSF *1.21

#WJ600to800_xs_2018     = 12.05   *gSF *1.21

#WJ800to1200_xs_2018    = 5.501   *gSF *1.21

#WJ1200to2500_xs_2018   = 1.329   *gSF *1.21

#WJ2500toInf_xs_2018    = 0.03216 *gSF *1.21

ST_tW_top_xs_2018      = 35.6    *gSF

ST_tW_antitop_xs_2018  = 35.6    *gSF 

ST_t_top_xs_2018       = 44.33   *gSF

ST_t_antitop_xs_2018   = 26.38   *gSF 

#QCD NLO XS

fact = 1

QCD100to200_xs_2018    = 27990000 * fact

QCD200to300_xs_2018    = 1710000 *fact

QCD300to500_xs_2018    = 347500 *fact

QCD500to700_xs_2018    = 32060 *fact

QCD700to1000_xs_2018   = 6829 *fact

QCD1000to1500_xs_2018  = 1207 *fact

QCD1500to2000_xs_2018  = 120 *fact

QCD2000toInf_xs_2018  = 25.25 *fact



SIG1200_xs_2018        = 1.0

Top_xs_20182L2Nu            =  88.29 *gSF

Top_xs_2018SemiLep            = 365.34  *gSF

Top_xs_2018Had            = 377.96  *gSF



#===== Number of generated events ======

nEvt_2018 = [1.02304e+07, 1.15167e+07,1.12046e+07,3.84234e+07,8.82624e+06,3.12098e+06,531567,415517,2.83323e+07,2.54151e+07,5.9136e+06,1.96908e+07,8.35792e+06,7.56707e+06,3.1894e+06,3.34875e+08,2.6647e+08,1.66035e+10,5.126e+09,9.39482e+07,5.4247e+07,5.45941e+07,5.50468e+07,4.80282e+07,1.54035e+07,1.08839e+07,5.41226e+06, 100000, 4.62208e+09,6.00504e+10,6.26094e+10]



Top_num_2018          =  nEvt_2018[0]

DY100to200_num_2018   =  nEvt_2018[1]

DY200to400_num_2018   =  nEvt_2018[2]

DY400to600_num_2018   =  nEvt_2018[3]

DY600to800_num_2018   =  nEvt_2018[4]

DY800to1200_num_2018   =  nEvt_2018[5]

DY1200to2500_num_2018   =  nEvt_2018[6]

DY2500toInf_num_2018   =  nEvt_2018[7]

#Without Ht 

WJ100to200_num_2018   =  nEvt_2018[8]

WJ200to400_num_2018   =  nEvt_2018[9]

WJ400to600_num_2018   =  nEvt_2018[10]

WJ600to800_num_2018   =  nEvt_2018[11]

WJ800to1200_num_2018  =  nEvt_2018[12]

WJ1200to2500_num_2018 =  nEvt_2018[13]

WJ2500toInf_num_2018  =  nEvt_2018[14]



ST_tW_top_num_2018    =  nEvt_2018[15]

ST_tW_antitop_num_2018=  nEvt_2018[16]

ST_t_top_num_2018     =  nEvt_2018[17]

ST_t_antitop_num_2018 =  nEvt_2018[18] 



QCD100to200_num_2018    = nEvt_2018[19] 

QCD200to300_num_2018    = nEvt_2018[20] 

QCD300to500_num_2018    = nEvt_2018[21] 

QCD500to700_num_2018    = nEvt_2018[22] 

QCD700to1000_num_2018   = nEvt_2018[23] 

QCD1000to1500_num_2018  = nEvt_2018[24] 

QCD1500to2000_num_2018  = nEvt_2018[25] 

QCD2000toInf_num_2018   = nEvt_2018[26] 



SIG1200_num_2018        =  nEvt_2018[27]

Top_num_20182L2Nu       =  nEvt_2018[28]

Top_num_2018SemiLep     =  nEvt_2018[29]

Top_num_2018Had         =  nEvt_2018[30]



# Legend

#AI:

#leg = TLegend(0.76,0.88,0.94,0.50)

leg = TLegend(0.73,0.45,0.88,0.86)

leg.SetBorderSize(0)

leg.SetFillColor(10)

leg.SetLineColor(10)

leg.SetLineWidth(0)





# =====================================================

#  FUNCTIONS		

# =====================================================



def setTitle(hs,xTitle):

    y = hs.GetYaxis()

    x = hs.GetXaxis()

#AI:

    y.SetTitle("Events / bin")

    x.SetTitle(xTitle)

    y.SetLabelSize(0.05)

  #AI:

    y.SetTitleSize(0.06)

    y.SetTitleOffset(0.8)

    

    y.SetTitleFont(42)

    x.SetTitleSize(0.05)

    x.SetTitleFont(42)



def prepareRatio(h_ratio, h_ratiobkg, scale, xTitle):

    h_ratio.SetTitle("")

    h_ratio.GetYaxis().SetTitle("Data / Bkg")

    h_ratio.GetXaxis().SetTitle(xTitle)   

    h_ratio.SetMarkerStyle(8) 

    h_ratio.SetMaximum(1.5)

    h_ratio.SetMinimum(0.5)

    #h_ratio.SetMaximum(3.0)

    #h_ratio.SetMinimum(-1.0)

    h_ratio.GetYaxis().SetLabelSize(0.06*scale)

    #AI:

    h_ratio.GetYaxis().SetTitleOffset(1.20/scale*0.5)

    #AI:

    h_ratio.GetYaxis().SetTitleSize(0.07*scale)

    h_ratio.GetYaxis().SetTitleFont(42)

    h_ratio.GetXaxis().SetLabelSize(0.06*scale)

    #AI:

    h_ratio.GetXaxis().SetTitleOffset(0.5*scale)

     #AI:

    h_ratio.GetXaxis().SetTitleSize(0.08*scale)

    h_ratio.GetYaxis().SetNdivisions(505)

    h_ratio.GetXaxis().SetNdivisions(510)

    h_ratio.SetTickLength(0.06,"X")

    h_ratio.SetTickLength(0.05,"Y")



    ## The uncertainty band

    h_ratio_bkg.SetMarkerSize(0)

    h_ratio_bkg.SetFillColor(kGray+1)

    h_ratio_bkg.GetYaxis().SetLabelSize(0.6*scale)

    h_ratio_bkg.GetYaxis().SetTitleOffset(1.00/scale*0.6)

    h_ratio_bkg.GetYaxis().SetTitleSize(0.08*scale)

    h_ratio_bkg.GetYaxis().SetTitleFont(42)

    h_ratio_bkg.GetXaxis().SetLabelSize(0.08*scale)

    h_ratio_bkg.GetXaxis().SetTitleOffset(0.45*scale)

    h_ratio_bkg.GetXaxis().SetTitleSize(0.09*scale)

    h_ratio_bkg.GetYaxis().SetNdivisions(505)

    h_ratio_bkg.GetXaxis().SetNdivisions(510)

    h_ratio_bkg.SetTickLength(0.05,"X")

    h_ratio_bkg.SetTickLength(0.05,"y")

    h_ratio_bkg.SetTitle("")    

    h_ratio_bkg.SetMaximum(1.6)

    h_ratio_bkg.SetMinimum(0.4)

    

def overUnderFlow(hist):

    xbins = hist.GetNbinsX()

    hist.SetBinContent(xbins, hist.GetBinContent(xbins)+hist.GetBinContent(xbins+1))

    hist.SetBinContent(1, hist.GetBinContent(0)+hist.GetBinContent(1))

    hist.SetBinError(xbins, TMath.Sqrt(TMath.Power(hist.GetBinError(xbins),2)+TMath.Power(hist.GetBinError(xbins+1),2)))

    hist.SetBinError(1, TMath.Sqrt(TMath.Power(hist.GetBinError(0),2)+TMath.Power(hist.GetBinError(1),2)))

    hist.SetBinContent(xbins+1, 0.)

    hist.SetBinContent(0, 0.)

    hist.SetBinError(xbins+1, 0.)

    hist.SetBinError(0, 0.)

    

def setCosmetics(hist, legname, hname, color, doCosmetics):

    #hist.Rebin(rebinS)

    if (doCosmetics):

#AI:

#      hist.SetLineColor(color)

      hist.SetLineColor(1)

      hist.SetName(hname)

      if 'Data' in hname:

        leg.AddEntry(hist, legname, 'pl')

        hist.SetMarkerStyle(8)

      elif 'tZ' in hname:          

        hist.SetLineWidth(2)

        leg.AddEntry(hist, legname, 'l')

#AI:

      elif 'Signal' in hname:

        leg.AddEntry(hist,legname,'pl')

        hist.SetLineWidth(2)

        hist.SetLineStyle(7)

      else:

        hist.SetFillColor(color)

        leg.AddEntry(hist, legname, 'f')



        

def getHisto( label, leg, dir, var, Samples, color, verbose, doCosmetics) :

    histos = []

    for iSample in Samples :

        ifile = iSample[0]

        xs = iSample[1]

        nevt = iSample[2]

        lumi = iSample[3]

        readname = var

        #readname = dir+'/'+var

        hist  = ifile.Get(readname).Clone()

        hist.SetDirectory(0);

        if verbose:

            print ('file: {0:<20}, histo:{1:<10}, integral before weight:{2:<3.3f}, nEntries:{3:<3.0f}, weight:{4:<2.3f}'.format(

                ifile.GetName(),    

                hist.GetName(),

                hist.Integral(), hist.GetEntries(), xs * lumi /nevt

                ))

        #hist.Sumw2()    

        hist.Scale( xs * lumi /nevt)

        hist.Rebin(rebinS)

        histos.append( hist )

        

    histo = histos[0]

    setCosmetics(histo, leg, label+var, color, doCosmetics) 

    for ihisto in range(1, len(histos) ):

        #print 'ihisto =', ihisto, 'integral', histos[ihisto].Integral(), ', entries', histos[ihisto].GetEntries(), ", x low ", histos[ihisto].GetBinLowEdge(1), ", x high ", histos[ihisto].GetBinLowEdge(histos[ihisto].GetXaxis().GetNbins()+1), ", nBins ", histos[ihisto].GetXaxis().GetNbins(), ", bin width ", histos[ihisto].GetXaxis().GetBinWidth(1)

        histo.Add( histos[ihisto], 1 )

        #print 'after addition', histo.Integral()

    if verbose:    

        print ('newName: {0:<5}, Entries:{1:5.2f},  newIntegral: {2:5.2f}'.format(label+var, histo.GetEntries(), histo.Integral() )   )

    return histo




