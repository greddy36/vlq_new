#!q
#/bin/python

import subprocess

CH = "Mu"
if (CH == "Mu"):
    options = [

           ['Mu_PreSig_LepPt', 5, "LepPt"],
           ['Mu_PreSig_LepPhi', 5, "LepPhi"],
           ['Mu_PreSig_MET', 5, "Met"],
           ['Mu_PreSig_METphi', 5, "Met_Phi"],
           ['Mu_PreSig_LepEta', 5, "LepEta"],
           ['Mu_PreSig_JetPt', 10, "LeadJetPt"],
           ['Mu_PreSig_JetPhi', 5, "LeadJetPhi"],
           ['Mu_PreSig_JetEta', 5, "LeadJetEta"],
           ['Mu_PreSig_ST_v2', 10, "ST_v2"],
           ['Mu_PreSig_Mass_v2', 10, "Mass"],
           ['Mu_PreSig_MT', 5, "MT"],
           ['Mu_PreSig_HT', 10, "HT"],
           ['Mu_PreSig_DPHI', 5, "DPhi_Lep_leadJet"],
           ['Mu_PreSig_DPHILepMet', 5, "DPhi_Lep_Met"],
           ['Mu_PreSig_DR', 10, "DR_Lep_ClosestJet"],
           ['Mu_PreSig_DR_LepleadJet', 10, "DR_Lep_leadJet"],
           ['Mu_PreSig_NBTags_DeepFLV', 1, "NBTags_DeepFLV"],
           ['Mu_PreSig_NCentralJets', 1, "NJetsCentral"],
           ['Mu_PreSig_NFwdJets', 1, "NFwdJets"],
           ['Mu_PreSig_DPHIMetJet', 5, "DPhi_leadJet_Met"],
           ['Mu_PreSig_FwdJetEta', 5, "FwdJet_Eta"],
           ['Mu_PreSig_FwdJetPt', 5, "FwdJet_Pt"],
           ['Mu_PreSig_RelIso03', 1, "RelIso03"],


           #['Mu_PreSigV2_LepPt', 5, "LepPt"],
           #['Mu_PreSigV2_LepPhi', 5, "LepPhi"],
           #['Mu_PreSigV2_MET', 5, "Met"],
           #['Mu_PreSigV2_METphi', 5, "Met_Phi"],
           #['Mu_PreSigV2_LepEta', 5, "LepEta"],
           #['Mu_PreSigV2_JetPt', 10, "LeadJetPt"],
           #['Mu_PreSigV2_JetPhi', 5, "LeadJetPhi"],
           #['Mu_PreSigV2_JetEta', 5, "LeadJetEta"],
           #['Mu_PreSigV2_ST_v2', 10, "ST_v2"],
           #['Mu_PreSigV2_Mass_v2', 10, "Mass"],
           #['Mu_PreSigV2_MT', 5, "MT"],
           #['Mu_PreSigV2_HT', 10, "HT"],
           #['Mu_PreSigV2_DPHI', 5, "DPhi_Lep_leadJet"],
           #['Mu_PreSigV2_DPHILepMet', 5, "DPhi_Lep_Met"],
           #['Mu_PreSigV2_DR', 10, "DR_Lep_ClosestJet"],
           #['Mu_PreSigV2_DR_LepleadJet', 10, "DR_Lep_leadJet"],
           #['Mu_PreSigV2_NBTags_DeepFLV', 1, "NBTags_DeepFLV"],
           #['Mu_PreSigV2_NCentralJets', 1, "NJetsCentral"],
           #['Mu_PreSigV2_NFwdJets', 1, "NFwdJets"],
           #['Mu_PreSigV2_DPHIMetJet', 5, "DPhi_leadJet_Met"],
           #['Mu_PreSigV2_FwdJetEta', 5, "FwdJet_Eta"],
           #['Mu_PreSigV2_FwdJetPt', 5, "FwdJet_Pt"],
           #['Mu_PreSigV2_RelIso03', 1, "RelIso03"],

           #['Mu_WJets_Counter', 1, "Cutflow"],
           ['Mu_WJets_LepPt', 5, "LepPt"],
           ['Mu_WJets_LepEta', 5, "LepEta"],
           ['Mu_WJets_LepEta_HEMf', 5, "LepEta_HEMf"],
           ['Mu_WJets_LepEta_HEMp', 5, "LepEta_HEMp"],
           ['Mu_WJets_LepPhi', 5, "LepPhi"],
           ['Mu_WJets_LepPhi_HEMf', 5, "LepPhi_HEMf"],
           ['Mu_WJets_LepPhi_HEMp', 5, "LepPhi_HEMp"],
           ['Mu_WJets_MET', 5, "Met"],
           ['Mu_WJets_METphi', 5, "Met_Phi"],
           ['Mu_WJets_JetPt', 10, "LeadJetPt"],
           ['Mu_WJets_JetPhi', 5, "LeadJetPhi"],
           ['Mu_WJets_JetPhi_HEMf', 5, "LeadJetPhi_HEMf"],
           ['Mu_WJets_JetPhi_HEMp', 5, "LeadJetPhi_HEMp"],
           ['Mu_WJets_JetEta', 5, "LeadJetEta"],
           ['Mu_WJets_JetEta_HEMf', 5, "LeadJetEta_HEMf"],
           ['Mu_WJets_JetEta_HEMp', 5, "LeadJetEta_HEMp"],
           ['Mu_WJets_ST_v2', 10, "ST_v2"],
           ['Mu_WJets_ST', 10, "ST"],
           #['Mu_WJets_TranMom', 10, "TranMomentum"],
           ['Mu_WJets_WPt', 10, "WPt"],
           ['Mu_WJets_JetPt', 10, "LeadJetPt"],
           ['Mu_WJets_Mass_v2', 10, "Mass"],
           ['Mu_WJets_MT', 5, "MT"],
           ['Mu_WJets_HT', 10, "HT"],
           ['Mu_WJets_DPHI', 5, "DPhi_Lep_leadJet"],
           ['Mu_WJets_DPHILepMet', 5, "DPhi_Lep_Met"],
           ['Mu_WJets_DR', 10, "DR_Lep_ClosestJet"],
           ['Mu_WJets_DR_LepleadJet', 10, "DR_Lep_leadJet"],
           ['Mu_WJets_NCentralJets', 1, "NJetsCentral"],
           ['Mu_WJets_NFwdJets', 1, "NFwdJets"],
           ['Mu_WJets_DPHIMetJet', 5, "DPhi_leadJet_Met"],
           ['Mu_WJets_FwdJetEta', 5, "FwdJet_Eta"],
           ['Mu_WJets_FwdJetPt', 5, "FwdJet_Pt"],
           ['Mu_WJets_RelIso03', 5, "RelIso03"],
           ['Mu_WJets_RelIso04', 5, "RelIso04"],
           ['Mu_WJets_NBTags_DeepFLV', 1, "NBTags_DeepFLV"],

           #['Mu_TTJets_Counter', 1, "Cutflow"],
           ['Mu_TTJets_LepPt', 5, "LepPt"],
           ['Mu_TTJets_MET', 5, "Met"],
           ['Mu_TTJets_METphi', 5, "Met_Phi"],
           ['Mu_TTJets_LepEta', 5, "LepEta"],
           ['Mu_TTJets_JetPt', 10, "LeadJetPt"],
           ['Mu_TTJets_JetEta', 5, "LeadJetEta"],
           ['Mu_TTJets_ST_v2', 10, "ST_ak4"],
           #['Mu_TTJets_TranMom', 10, "TranMomentum"],
           ['Mu_TTJets_ST', 10, "ST"],
           ['Mu_TTJets_WPt', 10, "WPt"],
           ['Mu_TTJets_JetPt', 10, "LeadJetPt"],
           ['Mu_TTJets_Mass_v2', 10, "Mass"],
           ['Mu_TTJets_MT', 5, "MT"],
           ['Mu_TTJets_HT', 10, "HT"],
           ['Mu_TTJets_DPHI', 5, "DPhi_Lep_leadJet"],
           ['Mu_TTJets_DPHILepMet', 5, "DPhi_Lep_Met"],
           ['Mu_TTJets_DR', 10, "DR_Lep_ClosestJet"],
           ['Mu_TTJets_DR_LepleadJet', 10, "DR_Lep_leadJet"],
           ['Mu_TTJets_NBTags_DeepFLV', 1, "NBTags_DeepFLV"],
           ['Mu_TTJets_NCentralJets', 1, "NJetsCentral"],
           ['Mu_TTJets_NFwdJets', 1, "NFwdJets"],
           ['Mu_TTJets_DPHIMetJet', 5, "DPhi_leadJet_Met"],
           ['Mu_TTJets_FwdJetEta', 5, "FwdJet_Eta"],
           ['Mu_TTJets_FwdJetPt', 5, "FwdJet_Pt"],
           ['Mu_TTJets_RelIso03', 5, "RelIso03"],
           ['Mu_TTJets_RelIso04', 5, "RelIso04"],
           #['Mu_TTJets_Pt_lmj_select', 10, "Pt_lmj"],
           #['Mu_TTJets_Pt_lmj_select_alpha_up', 10, "Pt_lmj_alpha_up"],
           #['Mu_TTJets_Pt_lmj_select_alpha_down', 10, "Pt_lmj_alpha_down"],
           #['Mu_TTJets_Pt_lmj_select_beta_up', 10, "Pt_lmj_beta_up"],
           #['Mu_TTJets_Pt_lmj_select_beta_down', 10, "Pt_lmj_beta_down"],
           #['Mu_TTJets_Top_Score', 1, "TopCombination Score"],

    ]
elif (CH == "Ele"):
    options = [

           ['Ele_PreSig_LepPt', 5, "LepPt"],
           ['Ele_PreSig_LepPhi', 5, "LepPhi"],
           ['Ele_PreSig_MET', 5, "Met"],
           ['Ele_PreSig_METphi', 5, "Met_Phi"],
           ['Ele_PreSig_LepEta', 5, "LepEta"],
           ['Ele_PreSig_JetPt', 10, "LeadJetPt"],
           ['Ele_PreSig_JetPhi', 5, "LeadJetPhi"],
           ['Ele_PreSig_JetEta', 5, "LeadJetEta"],
           ['Ele_PreSig_ST_v2', 10, "ST_v2"],
           ['Ele_PreSig_Mass_v2', 10, "Mass"],
           ['Ele_PreSig_MT', 5, "MT"],
           ['Ele_PreSig_HT', 10, "HT"],
           ['Ele_PreSig_DPHI', 5, "DPhi_Lep_leadJet"],
           ['Ele_PreSig_DPHILepMet', 5, "DPhi_Lep_Met"],
           ['Ele_PreSig_DR', 10, "DR_Lep_ClosestJet"],
           ['Ele_PreSig_DR_LepleadJet', 10, "DR_Lep_leadJet"],
           ['Ele_PreSig_NBTags_DeepFLV', 1, "NBTags_DeepFLV"],
           ['Ele_PreSig_NCentralJets', 1, "NJetsCentral"],
           ['Ele_PreSig_NFwdJets', 1, "NFwdJets"],
           ['Ele_PreSig_DPHIMetJet', 5, "DPhi_leadJet_Met"],
           ['Ele_PreSig_FwdJetEta', 5, "FwdJet_Eta"],
           ['Ele_PreSig_FwdJetPt', 5, "FwdJet_Pt"],
           ['Ele_PreSig_RelIso03', 1, "RelIso03"],


           #['Ele_PreSigV2_LepPt', 5, "LepPt"],
           #['Ele_PreSigV2_LepPhi', 5, "LepPhi"],
           #['Ele_PreSigV2_MET', 5, "Met"],
           #['Ele_PreSigV2_METphi', 5, "Met_Phi"],
           #['Ele_PreSigV2_LepEta', 5, "LepEta"],
           #['Ele_PreSigV2_JetPt', 10, "LeadJetPt"],
           #['Ele_PreSigV2_JetPhi', 5, "LeadJetPhi"],
           #['Ele_PreSigV2_JetEta', 5, "LeadJetEta"],
           #['Ele_PreSigV2_ST_v2', 10, "ST_v2"],
           #['Ele_PreSigV2_Mass_v2', 10, "Mass"],
           #['Ele_PreSigV2_MT', 5, "MT"],
           #['Ele_PreSigV2_HT', 10, "HT"],
           #['Ele_PreSigV2_DPHI', 5, "DPhi_Lep_leadJet"],
           #['Ele_PreSigV2_DPHILepMet', 5, "DPhi_Lep_Met"],
           #['Ele_PreSigV2_DR', 10, "DR_Lep_ClosestJet"],
           #['Ele_PreSigV2_DR_LepleadJet', 10, "DR_Lep_leadJet"],
           #['Ele_PreSigV2_NBTags_DeepFLV', 1, "NBTags_DeepFLV"],
           #['Ele_PreSigV2_NCentralJets', 1, "NJetsCentral"],
           #['Ele_PreSigV2_NFwdJets', 1, "NFwdJets"],
           #['Ele_PreSigV2_DPHIMetJet', 5, "DPhi_leadJet_Met"],
           #['Ele_PreSigV2_FwdJetEta', 5, "FwdJet_Eta"],
           #['Ele_PreSigV2_FwdJetPt', 5, "FwdJet_Pt"],
           #['Ele_PreSigV2_RelIso03', 1, "RelIso03"],

           #['Ele_WJets_Counter', 1, "Cutflow"],
           ['Ele_WJets_LepPt', 5, "LepPt"],
           ['Ele_WJets_LepEta', 5, "LepEta"],
           ['Ele_WJets_LepEta_HEMf', 5, "LepEta_HEMf"],
           ['Ele_WJets_LepEta_HEMp', 5, "LepEta_HEMp"],
           ['Ele_WJets_LepPhi', 5, "LepPhi"],
           ['Ele_WJets_LepPhi_HEMf', 5, "LepPhi_HEMf"],
           ['Ele_WJets_LepPhi_HEMp', 5, "LepPhi_HEMp"],
           ['Ele_WJets_MET', 5, "Met"],
           ['Ele_WJets_METphi', 5, "Met_Phi"],
           ['Ele_WJets_JetPt', 10, "LeadJetPt"],
           ['Ele_WJets_JetPhi', 5, "LeadJetPhi"],
           ['Ele_WJets_JetPhi_HEMf', 5, "LeadJetPhi_HEMf"],
           ['Ele_WJets_JetPhi_HEMp', 5, "LeadJetPhi_HEMp"],
           ['Ele_WJets_JetEta', 5, "LeadJetEta"],
           ['Ele_WJets_JetEta_HEMf', 5, "LeadJetEta_HEMf"],
           ['Ele_WJets_JetEta_HEMp', 5, "LeadJetEta_HEMp"],
           ['Ele_WJets_ST_v2', 10, "ST_v2"],
           ['Ele_WJets_ST', 10, "ST"],
           #['Ele_WJets_TranMom', 10, "TranMomentum"],
           ['Ele_WJets_WPt', 10, "WPt"],
           ['Ele_WJets_JetPt', 10, "LeadJetPt"],
           ['Ele_WJets_Mass_v2', 10, "Mass"],
           ['Ele_WJets_MT', 5, "MT"],
           ['Ele_WJets_HT', 10, "HT"],
           ['Ele_WJets_DPHI', 5, "DPhi_Lep_leadJet"],
           ['Ele_WJets_DPHILepMet', 5, "DPhi_Lep_Met"],
           ['Ele_WJets_DR', 10, "DR_Lep_ClosestJet"],
           ['Ele_WJets_DR_LepleadJet', 10, "DR_Lep_leadJet"],
           ['Ele_WJets_NCentralJets', 1, "NJetsCentral"],
           ['Ele_WJets_NFwdJets', 1, "NFwdJets"],
           ['Ele_WJets_DPHIMetJet', 5, "DPhi_leadJet_Met"],
           ['Ele_WJets_FwdJetEta', 5, "FwdJet_Eta"],
           ['Ele_WJets_FwdJetPt', 5, "FwdJet_Pt"],
           ['Ele_WJets_RelIso03', 5, "RelIso03"],
           ['Ele_WJets_RelIso04', 5, "RelIso04"],
           ['Ele_WJets_NBTags_DeepFLV', 1, "NBTags_DeepFLV"],

           #['Ele_TTJets_Counter', 1, "Cutflow"],
           ['Ele_TTJets_LepPt', 5, "LepPt"],
           ['Ele_TTJets_MET', 5, "Met"],
           ['Ele_TTJets_METphi', 5, "Met_Phi"],
           ['Ele_TTJets_LepEta', 5, "LepEta"],
           ['Ele_TTJets_JetPt', 10, "LeadJetPt"],
           ['Ele_TTJets_JetEta', 5, "LeadJetEta"],
           ['Ele_TTJets_ST_v2', 10, "ST_ak4"],
           #['Ele_TTJets_TranMom', 10, "TranMomentum"],
           ['Ele_TTJets_ST', 10, "ST"],
           ['Ele_TTJets_WPt', 10, "WPt"],
           ['Ele_TTJets_JetPt', 10, "LeadJetPt"],
           ['Ele_TTJets_Mass_v2', 10, "Mass"],
           ['Ele_TTJets_MT', 5, "MT"],
           ['Ele_TTJets_HT', 10, "HT"],
           ['Ele_TTJets_DPHI', 5, "DPhi_Lep_leadJet"],
           ['Ele_TTJets_DPHILepMet', 5, "DPhi_Lep_Met"],
           ['Ele_TTJets_DR', 10, "DR_Lep_ClosestJet"],
           ['Ele_TTJets_DR_LepleadJet', 10, "DR_Lep_leadJet"],
           ['Ele_TTJets_NBTags_DeepFLV', 1, "NBTags_DeepFLV"],
           ['Ele_TTJets_NCentralJets', 1, "NJetsCentral"],
           ['Ele_TTJets_NFwdJets', 1, "NFwdJets"],
           ['Ele_TTJets_DPHIMetJet', 5, "DPhi_leadJet_Met"],
           ['Ele_TTJets_FwdJetEta', 5, "FwdJet_Eta"],
           ['Ele_TTJets_FwdJetPt', 5, "FwdJet_Pt"],
           ['Ele_TTJets_RelIso03', 5, "RelIso03"],
           ['Ele_TTJets_RelIso04', 5, "RelIso04"],
           #['Ele_TTJets_Pt_lmj_select', 10, "Pt_lmj"],
           #['Ele_TTJets_Pt_lmj_select_alpha_up', 10, "Pt_lmj_alpha_up"],
           #['Ele_TTJets_Pt_lmj_select_alpha_down', 10, "Pt_lmj_alpha_down"],
           #['Ele_TTJets_Pt_lmj_select_beta_up', 10, "Pt_lmj_beta_up"],
           #['Ele_TTJets_Pt_lmj_select_beta_down', 10, "Pt_lmj_beta_down"],
           #['Ele_TTJets_Top_Score', 1, "TopCombination Score"],

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
