#!q
#/bin/python

import subprocess

CH = "Mu"
if (CH == "Mu"):
    options = [

           ['mu_WJets_lepPt', 5, "LepPt"],
           ['mu_WJets_lepEta', 5, "LepEta"],
           ['mu_WJets_leadjetPt', 10, "LeadJetPt"],
           ['mu_WJets_met', 5, "Met"],
           ['mu_WJets_st', 10, "ST"],
           ['mu_WJets_stv2', 5, "ST_v2"],
           ['mu_WJets_drLepleadjet', 10, "DR_Lep_leadJet"],
           ['mu_WJets_ht', 10, "HT"],
           ['mu_WJets_nbtagmedDeepFlv', 10, "NBTagMed_DeepFLV"],
           ['mu_WJets_ncentralJets', 1, "NJetsCentral"],
           ['mu_WJets_dphiLepmet', 5, "DPhi_Lep_Met"],
           ['mu_WJets_dphiLepleadjet', 5, "DPhi_Lep_leadJet"],
           ['mu_WJets_drLepclosestJet', 10, "DR_Lep_ClosestJet"],
           ['mu_WJets_bvswRatio', 10, "bVsW_ratio"],
           ['mu_WJets_angleMujetMet',10, "Angle_MuJet_Met"],
           ['mu_WJets_NNscore', 10, "NN_score"],
           ['mu_WJets_nfwdjets', 1, "NFwdJets"],
           ['mu_WJets_mass_v2', 10, "Mass"],
           ['mu_WJets_massT', 5, "MT"], 
           ['mu_WJets_fwdjetpt', 5, "FwdJet_Pt"],
           ['mu_WJets_fwdjeteta', 5, "FwdJet_Eta"],
           ['mu_WJets_leadjetEta', 5, "LeadJetEta"],
           ['mu_WJets_leadjetPhi', 5, "LeadJetPhi"],
           ['mu_WJets_ht_over_leadjetpt', 1, "HT/LeadJet_pt"],

           ['mu_TTJets_lepPt', 5, "LepPt"],
           ['mu_TTJets_lepEta', 5, "LepEta"],
           ['mu_TTJets_leadjetPt', 10, "LeadJetPt"],
           ['mu_TTJets_met', 5, "Met"],
           ['mu_TTJets_st', 10, "ST"],
           ['mu_TTJets_stv2', 5, "ST_v2"],
           ['mu_TTJets_drLepleadjet', 10, "DR_Lep_leadJet"],
           ['mu_TTJets_ht', 10, "HT"],
           ['mu_TTJets_nbtagmedDeepFlv', 10, "NBTagMed_DeepFLV"],
           ['mu_TTJets_ncentralJets', 1, "NJetsCentral"],
           ['mu_TTJets_dphiLepmet', 5, "DPhi_Lep_Met"],
           ['mu_TTJets_dphiLepleadjet', 5, "DPhi_Lep_leadJet"],
           ['mu_TTJets_drLepclosestJet', 10, "DR_Lep_ClosestJet"],
           ['mu_TTJets_bvswRatio', 10, "bVsW_ratio"],
           ['mu_TTJets_angleMujetMet',10, "Angle_MuJet_Met"],
           ['mu_TTJets_NNscore', 10, "NNscore"],
           ['mu_TTJets_nfwdjets', 1, "NFwdJets"],
           ['mu_TTJets_mass_v2', 10, "Mass"],
           ['mu_TTJets_massT', 5, "MT"], 
           ['mu_TTJets_fwdjetpt', 5, "FwdJet_Pt"],
           ['mu_TTJets_fwdjeteta', 5, "FwdJet_Eta"],
           ['mu_TTJets_leadjetEta', 5, "LeadJetEta"],
           ['mu_TTJets_leadjetPhi', 5, "LeadJetPhi"],
           ['mu_TTJets_ht_over_leadjetpt', 1, "HT/LeadJet_pt"],

           ['mu_PreSig_lepPt', 5, "LepPt"],
           ['mu_PreSig_lepEta', 5, "LepEta"],
           ['mu_PreSig_leadjetPt', 10, "LeadJetPt"],
           ['mu_PreSig_met', 5, "Met"],
           ['mu_PreSig_st', 10, "ST"],
           ['mu_PreSig_stv2', 5, "ST_v2"],
           ['mu_PreSig_drLepleadjet', 10, "DR_Lep_leadJet"],
           ['mu_PreSig_ht', 10, "HT"],
           ['mu_PreSig_nbtagmedDeepFlv', 10, "NBTagMed_DeepFLV"],
           ['mu_PreSig_ncentralJets', 1, "NJetsCentral"],
           ['mu_PreSig_dphiLepmet', 5, "DPhi_Lep_Met"],
           ['mu_PreSig_dphiLepleadjet', 5, "DPhi_Lep_leadJet"],
           ['mu_PreSig_drLepclosestJet', 10, "DR_Lep_ClosestJet"],
           ['mu_PreSig_bvswRatio', 10, "bVsW_ratio"],
           ['mu_PreSig_angleMujetMet',10, "Angle_MuJet_Met"],
           ['mu_PreSig_NNscore', 10, "NNscore"],
           ['mu_PreSig_nfwdjets', 1, "NFwdJets"],
           ['mu_PreSig_mass_v2', 10, "Mass"],
           ['mu_PreSig_massT', 5, "MT"], 
           ['mu_PreSig_fwdjetpt', 5, "FwdJet_Pt"],
           ['mu_PreSig_fwdjeteta', 5, "FwdJet_Eta"],
           ['mu_PreSig_leadjetEta', 5, "LeadJetEta"],
           ['mu_PreSig_leadjetPhi', 5, "LeadJetPhi"],
           ['mu_PreSig_ht_over_leadjetpt', 1, "HT/LeadJet_pt"],

    ]
elif (CH == "Ele"):
    options = [

           ['ele_WJets_lepPt', 5, "LepPt"],
           ['ele_WJets_lepEta', 5, "LepEta"],
           ['ele_WJets_leadjetPt', 10, "LeadJetPt"],
           ['ele_WJets_met', 5, "Met"],
           ['ele_WJets_st', 10, "ST"],
           ['ele_WJets_stv2', 5, "ST_v2"],
           ['ele_WJets_drLepleadjet', 10, "DR_Lep_leadJet"],
           ['ele_WJets_ht', 10, "HT"],
           ['ele_WJets_nbtagmedDeepFlv', 10, "NBTagMed_DeepFLV"],
           ['ele_WJets_ncentralJets', 1, "NJetsCentral"],
           ['ele_WJets_dphiLepmet', 5, "DPhi_Lep_Met"],
           ['ele_WJets_dphiLepleadjet', 5, "DPhi_Lep_leadJet"],
           ['ele_WJets_drLepclosestJet', 10, "DR_Lep_ClosestJet"],
           ['ele_WJets_bvswRatio', 10, "bVsW_ratio"],
           ['ele_WJets_angleMujetMet',10, "Angle_MuJet_Met"],
           ['ele_WJets_NNscore', 10, "NNscore"],
           ['ele_WJets_nfwdjets', 1, "NFwdJets"],
           ['ele_WJets_mass_v2', 10, "Mass"],
           ['ele_WJets_massT', 5, "MT"], 
           ['ele_WJets_fwdjetpt', 5, "FwdJet_Pt"],
           ['ele_WJets_fwdjeteta', 5, "FwdJet_Eta"],
           ['ele_WJets_leadjetEta', 5, "LeadJetEta"],
           ['ele_WJets_leadjetPhi', 5, "LeadJetPhi"],
           ['ele_WJets_ht_over_leadjetpt', 1, "HT/LeadJet_pt"],

           ['ele_TTJets_lepPt', 5, "LepPt"],
           ['ele_TTJets_lepEta', 5, "LepEta"],
           ['ele_TTJets_leadjetPt', 10, "LeadJetPt"],
           ['ele_TTJets_met', 5, "Met"],
           ['ele_TTJets_st', 10, "ST"],
           ['ele_TTJets_stv2', 5, "ST_v2"],
           ['ele_TTJets_drLepleadjet', 10, "DR_Lep_leadJet"],
           ['ele_TTJets_ht', 10, "HT"],
           ['ele_TTJets_nbtagmedDeepFlv', 10, "NBTagMed_DeepFLV"],
           ['ele_TTJets_ncentralJets', 1, "NJetsCentral"],
           ['ele_TTJets_dphiLepmet', 5, "DPhi_Lep_Met"],
           ['ele_TTJets_dphiLepleadjet', 5, "DPhi_Lep_leadJet"],
           ['ele_TTJets_drLepclosestJet', 10, "DR_Lep_ClosestJet"],
           ['ele_TTJets_bvswRatio', 10, "bVsW_ratio"],
           ['ele_TTJets_angleMujetMet',10, "Angle_MuJet_Met"],
           ['ele_TTJets_NNscore', 10, "NNscore"],
           ['ele_TTJets_nfwdjets', 1, "NFwdJets"],
           ['ele_TTJets_mass_v2', 10, "Mass"],
           ['ele_TTJets_massT', 5, "MT"], 
           ['ele_TTJets_fwdjetpt', 5, "FwdJet_Pt"],
           ['ele_TTJets_fwdjeteta', 5, "FwdJet_Eta"],
           ['ele_TTJets_leadjetEta', 5, "LeadJetEta"],
           ['ele_TTJets_leadjetPhi', 5, "LeadJetPhi"],
           ['ele_TTJets_ht_over_leadjetpt', 1, "HT/LeadJet_pt"],

           ['ele_PreSig_lepPt', 5, "LepPt"],
           ['ele_PreSig_lepEta', 5, "LepEta"],
           ['ele_PreSig_leadjetPt', 10, "LeadJetPt"],
           ['ele_PreSig_met', 5, "Met"],
           ['ele_PreSig_st', 10, "ST"],
           ['ele_PreSig_stv2', 5, "ST_v2"],
           ['ele_PreSig_drLepleadjet', 10, "DR_Lep_leadJet"],
           ['ele_PreSig_ht', 10, "HT"],
           ['ele_PreSig_nbtagmedDeepFlv', 10, "NBTagMed_DeepFLV"],
           ['ele_PreSig_ncentralJets', 1, "NJetsCentral"],
           ['ele_PreSig_dphiLepmet', 5, "DPhi_Lep_Met"],
           ['ele_PreSig_dphiLepleadjet', 5, "DPhi_Lep_leadJet"],
           ['ele_PreSig_drLepclosestJet', 10, "DR_Lep_ClosestJet"],
           ['ele_PreSig_bvswRatio', 10, "bVsW_ratio"],
           ['ele_PreSig_angleMujetMet',10, "Angle_MuJet_Met"],
           ['ele_PreSig_NNscore', 10, "NNscore"],
           ['ele_PreSig_nfwdjets', 1, "NFwdJets"],
           ['ele_PreSig_mass_v2', 10, "Mass"],
           ['ele_PreSig_massT', 5, "MT"], 
           ['ele_PreSig_fwdjetpt', 5, "FwdJet_Pt"],
           ['ele_PreSig_fwdjeteta', 5, "FwdJet_Eta"],
           ['ele_PreSig_leadjetEta', 5, "LeadJetEta"],
           ['ele_PreSig_leadjetPhi', 5, "LeadJetPhi"],
           ['ele_PreSig_ht_over_leadjetpt', 1, "HT/LeadJet_pt"],

    ]

command = 'python plotSys.py --var={0} --rebin={1} --xtitle={2}'
#command = 'python plot.py --var={0} --rebin={1} --xtitle={2}'

for option in options :
    s = command.format(
        option[0], option[1], option[2]
        )

    subprocess.call( ["echo --------------------------------------------------------------------------",""], shell=True)
    subprocess.call( ["echo --------------------------------------------------------------------------",""], shell=True)
    subprocess.call( ["echo %s"%s,""]                                                                      , shell=True)
    subprocess.call( ["echo --------------------------------------------------------------------------",""], shell=True)
    subprocess.call( ["echo --------------------------------------------------------------------------",""], shell=True)
    subprocess.call( [s, ""]                                                                               , shell=True)

