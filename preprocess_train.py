import time
import uproot
import numpy as np
import pandas as pd
from glob import glob
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import warnings
warnings.filterwarnings(
    'ignore', category=pd.io.pytables.PerformanceWarning)

scaled_vars = [
        'Lepton_pt','Lepton_eta', 'LeadJet_pt','LeadJet_eta', 'MET',
        'DPHI_LepMet','DPHI_LepleadJet','DPHI_JetMet','DR_LepClosestJet',
        'bVsW_ratio','Angle_MuJet_Met'
]

selection_vars = ['HT','ST_v2','LeadJet_btag','nBTagMed_DeepFLV','DR_LepleadJet','nVetoElectrons','nVetoMuons','MT']

gSF = 1
corrSF = 1

lumi_2016 = 35920.0
lumi_2017 = 41530.0
lumi_2018 = 59200.0

nEvt_2016 = [1.01991e+07,1.10171e+07,9.60914e+06,9.72566e+06,8.29296e+06,2.67307e+06,596079,399492,7.8043e+07,3.89268e+07,7.7597e+06,1.86684e+07,7.83054e+06,6.87244e+06,2.63782e+06,6.95283e+06,6.93309e+06,6.71059e+07,3.8811e+07,1.47968e+07,2.24704e+07,3.96e+06,1.35247e+07,1.96971e+07,9.84662e+06,2.87343e+06,996130,996130,391735, 93600, 7.67481e+07]

#Without Ht 
WJ100to200_num_2016 =nEvt_2016[8]
WJ200to400_num_2016 =nEvt_2016[9]
WJ400to600_num_2016 =nEvt_2016[10]
WJ600to800_num_2016 =nEvt_2016[11]
WJ800to1200_num_2016=nEvt_2016[12]
WJ1200to2500_num_2016 =nEvt_2016[13]
WJ2500toInf_num_2016=nEvt_2016[14]

Top_pow_num_2016=nEvt_2016[30]

WJ100to200_xs_2016 = 1345.0*gSF *1.21 *1.0 *corrSF
WJ200to400_xs_2016 = 359.7 *gSF *1.21 *1.0 *corrSF
WJ400to600_xs_2016 = 48.9*gSF *1.21 *0.88842 *corrSF
WJ600to800_xs_2016 = 12.05 *gSF *1.21 *0.83367 *corrSF
WJ800to1200_xs_2016= 5.501 *gSF *1.21 *0.76412 *corrSF
WJ1200to2500_xs_2016 = 1.329 *gSF *1.21 *0.67636 *corrSF
WJ2500toInf_xs_2016= 0.03216 *gSF *1.21 *0.58820 *corrSF

Top_pow_xs_2016= 831.76*gSF

nEvt_2017 = [8.01696e+06,1.11801e+07,1.18968e+07,1.00037e+07,8.69161e+06,3.08971e+06,616923,401334,3.58046e+07,2.11922e+07,1.316e+07,2.15823e+07,2.0273e+07,1.99919e+07,2.06296e+07,2.72081e+08,2.79005e+08,5.98206e+06,3.67591e+06,9.3202e+07,5.91333e+07,6.02057e+07,5.6041e+07,4.74604e+07,1.64853e+07,1.15086e+07,5.82557e+06,100000, 6.4873e+08,1.31544e+10,4.7051e+09,2.92622e+10,3.99283e+10,1.69012e+06,560315,1.8384e+06,4.56491e+06]

#Without Ht 
WJ100to200_num_2017 =nEvt_2017[8]
WJ200to400_num_2017 =nEvt_2017[9]
WJ400to600_num_2017 =nEvt_2017[10]
WJ600to800_num_2017 =nEvt_2017[11]
WJ800to1200_num_2017=nEvt_2017[12]
WJ1200to2500_num_2017 =nEvt_2017[13]
WJ2500toInf_num_2017=nEvt_2017[14]

Top_num_2017_2L2NuPS=nEvt_2017[30]
Top_num_2017_SemiLepPS=nEvt_2017[31]
Top_num_2017_HadPS = nEvt_2017[32]

WJ100to200_xs_2017 = 1345.0*gSF *1.21 *1.0 *corrSF
WJ200to400_xs_2017 = 359.7 *gSF *1.21 *1.0 *corrSF
WJ400to600_xs_2017 = 48.9*gSF *1.21 *0.88842 *corrSF
WJ600to800_xs_2017 = 12.05 *gSF *1.21 *0.83367 *corrSF
WJ800to1200_xs_2017= 5.501 *gSF *1.21 *0.76412 *corrSF
WJ1200to2500_xs_2017 = 1.329 *gSF *1.21 *0.67636 *corrSF
WJ2500toInf_xs_2017= 0.03216 *gSF *1.21 *0.58820 *corrSF

Top_xs_2017_2L2NuPS=88.29 *gSF
Top_xs_2017_SemiLepPS= 365.34*gSF
Top_xs_2017_HadPS = 377.96 *gSF

nEvt_2018 = [1.02304e+07, 1.15167e+07,1.12046e+07,3.84234e+07,8.82624e+06,3.12098e+06,531567,415517,2.83323e+07,2.54151e+07,5.9136e+06,1.96908e+07,8.35792e+06,7.56707e+06,3.1894e+06,3.34875e+08,2.6647e+08,1.66035e+10,5.126e+09,9.39482e+07,5.4247e+07,5.45941e+07,5.50468e+07,4.80282e+07,1.54035e+07,1.08839e+07,5.41226e+06, 100000, 4.62208e+09,6.00504e+10,6.26094e+10]

#Without Ht 
WJ100to200_num_2018 =nEvt_2018[8]
WJ200to400_num_2018 =nEvt_2018[9]
WJ400to600_num_2018 =nEvt_2018[10]
WJ600to800_num_2018 =nEvt_2018[11]
WJ800to1200_num_2018=nEvt_2018[12]
WJ1200to2500_num_2018 =nEvt_2018[13]
WJ2500toInf_num_2018=nEvt_2018[14]

Top_num_20182L2Nu =nEvt_2018[28]
Top_num_2018SemiLep =nEvt_2018[29]
Top_num_2018Had =nEvt_2018[30]

WJ100to200_xs_2018 = 1345.0*gSF *1.21 *1.0 *corrSF
WJ200to400_xs_2018 = 359.7 *gSF *1.21 *1.0 *corrSF
WJ400to600_xs_2018 = 48.9*gSF *1.21 *0.88842 *corrSF
WJ600to800_xs_2018 = 12.05 *gSF *1.21 *0.83367 *corrSF
WJ800to1200_xs_2018= 5.501 *gSF *1.21 *0.76412 *corrSF
WJ1200to2500_xs_2018 = 1.329 *gSF *1.21 *0.67636 *corrSF
WJ2500toInf_xs_2018= 0.03216 *gSF *1.21 *0.58820 *corrSF

Top_xs_20182L2Nu=88.29 *gSF
Top_xs_2018SemiLep= 365.34*gSF
Top_xs_2018Had= 377.96*gSF


def scaleing(weights,fname):
    if 'WJetsToLNu_HT-100To200_2016' in fname:
        weights *= (WJ100to200_xs_2016/WJ100to200_num_2016)*lumi_2016
    elif 'WJetsToLNu_HT-200to400_2016' in fname:
        weights *= (WJ200to400_xs_2016/WJ200to400_num_2016)*lumi_2016
    elif 'WJetsToLNu_HT-400To600_2016' in fname:
        weights *= (WJ400to600_xs_2016/WJ400to600_num_2016)*lumi_2016
    elif 'WJetsToLNu_HT-600To800_2016' in fname:
        weights *= (WJ600to800_xs_2016/WJ600to800_num_2016)*lumi_2016
    elif 'WJetsToLNu_HT-800To1200_2016' in fname:
        weights *= (WJ800to1200_xs_2016/WJ800to1200_num_2016)*lumi_2016
    elif 'WJetsToLNu_HT-1200To2500_2016' in fname:
        weights *= (WJ1200to2500_xs_2016/  WJ1200to2500_num_2016)*lumi_2016
    elif 'WJetsToLNu_HT-2500ToInf_2016' in fname:
        weights *= (WJ2500toInf_xs_2016/WJ2500toInf_num_2016)*lumi_2016
    elif 'WJetsToLNu_HT-100To200_2017' in fname:
        weights *= (WJ100to200_xs_2017/WJ100to200_num_2017)*lumi_2017
    elif 'WJetsToLNu_HT-200to400_2017' in fname:
        weights *= (WJ200to400_xs_2017/WJ200to400_num_2017)*lumi_2017
    elif 'WJetsToLNu_HT-400To600_2017' in fname:
        weights *= (WJ400to600_xs_2017/WJ400to600_num_2017)*lumi_2017
    elif 'WJetsToLNu_HT-600To800_2017' in fname:
        weights *= (WJ600to800_xs_2017/WJ600to800_num_2017)*lumi_2017
    elif 'WJetsToLNu_HT-800To1200_2017' in fname:
        weights *= (WJ800to1200_xs_2017/WJ800to1200_num_2017)*lumi_2017
    elif 'WJetsToLNu_HT-1200To2500_2017' in fname:
        weights *= (WJ1200to2500_xs_2017/  WJ1200to2500_num_2017)*lumi_2017
    elif 'WJetsToLNu_HT-2500ToInf_2017' in fname:
        weights *= (WJ2500toInf_xs_2017/WJ2500toInf_num_2017)*lumi_2017
    elif 'WJetsToLNu_HT-100To200_2018' in fname:
        weights *= (WJ100to200_xs_2018/WJ100to200_num_2018)*lumi_2018
    elif 'WJetsToLNu_HT-200to400_2018' in fname:
        weights *= (WJ200to400_xs_2018/WJ200to400_num_2018)*lumi_2018
    elif 'WJetsToLNu_HT-400To600_2018' in fname:
        weights *= (WJ400to600_xs_2018/WJ400to600_num_2018)*lumi_2018
    elif 'WJetsToLNu_HT-600To800_2018' in fname:
        weights *= (WJ600to800_xs_2018/WJ600to800_num_2018)*lumi_2018
    elif 'WJetsToLNu_HT-800To1200_2018' in fname:
        weights *= (WJ800to1200_xs_2018/WJ800to1200_num_2018)*lumi_2018
    elif 'WJetsToLNu_HT-1200To2500_2018' in fname:
        weights *= (WJ1200to2500_xs_2018/WJ1200to2500_num_2018)*lumi_2018
    elif 'WJetsToLNu_HT-2500ToInf_2018' in fname:
        weights *= (WJ2500toInf_xs_2018/WJ2500toInf_num_2018)*lumi_2018

    elif 'TT_TuneCUETP8M2T4_powheg-pythia8_2016' in fname:
        weights *= (Top_pow_xs_2016/Top_pow_num_2016)*lumi_2016
    elif 'TTTo2L2Nu_TuneCP5_PSweights_powheg-pythia8_2017' in fname:
        weights *= (Top_xs_2017_2L2NuPS/Top_num_2017_2L2NuPS)*lumi_2017
    elif 'TTToSemiLeptonic_TuneCP5_PSweights_powheg-pythia8_2017' in fname:
        weights *= (Top_xs_2017_SemiLepPS/Top_num_2017_SemiLepPS)*lumi_2017
    elif 'TTToHadronic_TuneCP5_PSweights_powheg-pythia8_2017' in fname:
        weights *= (Top_xs_2017_HadPS/Top_num_2017_HadPS)*lumi_2017
    elif 'TTTo2L2Nu_TuneCP5_powheg-pythia8_2018' in fname:
        weights *= (Top_xs_20182L2Nu/Top_num_20182L2Nu)*lumi_2018
    elif 'TTToSemiLeptonic_TuneCP5_powheg-pythia8_2018' in fname:
        weights *= (Top_xs_2018SemiLep/Top_num_2018SemiLep)*lumi_2018
    elif 'TTToHadronic_TuneCP5_powheg-pythia8_2018' in fname:
        weights *= (Top_xs_2018Had/Top_num_2018Had)*lumi_2018

    elif 'TprimeBToBW_COMBINED_2016' in fname:
        weights *= 0.045793
    elif 'TprimeBToBW_COMBINED_2017' in fname:
        weights *= 0.0531173
    elif 'TprimeBToBW_COMBINED_2018' in fname:
        weights *= 0.0759167
    return weights


def get_columns(fname):
    """
    Return variables to be kept and dropped. File specific reading
    can be done using the fname parameter.

    Parameters:
        fname (string): name of input file
    
    Returns:
        columns (list): columns to be read from the root file
        todrop (list): columns to be dropped after some processing
    """
    columns = scaled_vars + selection_vars + ['EvtWt']
    todrop = ['EvtWt']#, 'index']#, 'index_toDrop']
    return columns, todrop


def build_filelist(input_dir):
    """
    Build a list of input files to be processed. Files are split into
    a few key groups. The systematics return value can be implemented
    later to process systematics uncertainty files separately.

    Parameters:
        input_dir (string): path to input files

    Returns:
        nominal (map[string]list): map file group to list of files
        systematics (map[string]list): empty map for now
    """
    files = [ifile for ifile in glob('{}/*.root'.format(input_dir))]

    nominal = {
        'tprime': [],  # in case you need to do anything special with these
        'others': []
    }
    systematics = {}  # not used for now
    for fname in files:
        if 'Tprime' in fname:
            nominal['tprime'].append(fname)
        else:
            nominal['others'].append(fname)

    return nominal, systematics

def process_files(all_data, files, is_signal):
    """
    Process input files, split into appropriate columns, do scaling, etc...

    Parameters:
        all_data (map[string]pandas.DataFrame): map from string to dataframes that are
        to be filled. The "meta" key is for meta-information (non-training variables) like
        the event weights, indexes, and unscaled selection variables. The "training" key
        is for variables to be scaled and used in NN training.
        files (list): list of input files
        is_signal (bool): label for if file is signal or not
    
    Returns:
        all_data (map[string]pandas.DataFrame): returns the provided map after filling
        the DataFrames with rows from the processed files
    """
    for ifile in files:
        print (ifile)
        columns, todrop = get_columns(ifile)  # if you need special branches from some files
        # open the TTree (named Skim) inside the file and read the specified columns into
        # a pandas dataframe. Also, get integral of hEventCount_wt for number of events.
        input_file = uproot.open(ifile)
        input_df = input_file['Skim'].pandas.df(columns)
        nevents = sum(input_file['Entry'].values)
        
        # set some file info
        filename = ifile.split('/')[-1].replace('.root', '')
        input_df['index'] = np.array([i for i in xrange(0, len(input_df))])  # event index before selection

        # do selection

        slim_df = input_df[(input_df['Lepton_pt']>40)&(input_df['Lepton_eta']<2.1)&(input_df['LeadJet_pt']>200)&(abs(input_df['LeadJet_eta'])<2.4)&(input_df['LeadJet_btag']<1)&(input_df['MT']>40)&(input_df['nBTagMed_DeepFLV']==0)&(input_df['ST_v2']>500)&(input_df['HT']>500)&(input_df['DR_LepClosestJet']>-1)&(input_df['DR_LepleadJet']>0.5)&(abs(input_df['DPHI_LepMet'])<1.0)&(abs(input_df['DPHI_LepleadJet'])>2.0)&((input_df['nVetoElectrons']+input_df['nVetoMuons'])==1)]
        #slim_df = input_df[(input_df['HT'] > 500)&(input_df['ST'] > 500)&(input_df['nBTagMed_DeepFLV'] >= 0)]#&(input_df['LeadJet_btag'] == 1)] 
	#drop_idx = slim_df[(slim_df['nBTagMed_DeepFLV'] < 2)|(slim_df['DR_LepClosestJet'] >= 1.5)].index_toDrop
        #print(drop_idx)
        #slim_df = slim_df.drop(drop_idx, inplace=False)
        #print (slim_df.index[-1])
        #clean our input data in case of mistakes in writing the tree
        slim_df = slim_df.dropna(axis=0, how='any')  # drop events with a NaN
        slim_df = slim_df.drop_duplicates()

        #slim_df['index'] = np.array([i for i in xrange(0, len(slim_df))]) #event index after selection      
        #print (slim_df['index'].values)
        #print (slim_df['index_toDrop'].values)
        # Dataframe of variables used for selection, but not for training the
        # network. These variables are NOT rescaled.
        single_meta_df = pd.DataFrame(
            slim_df[selection_vars + ['index']].values,
            columns=slim_df[selection_vars + ['index']].columns.values
        )
			
        # add filenames to distinguish in training
        single_meta_df['names'] = np.full(len(slim_df), filename)

        # add signal vs. background labels
        isSignal = np.ones(len(slim_df)) if is_signal == 1 else np.zeros(len(slim_df))
        single_meta_df['isSignal'] = isSignal
        
        #print(input_df['EvtWt'].values)
        # Get the event weight and scale by xs if needed
        weight_df = scaleing(slim_df['EvtWt'], filename)
        #print(weight_df)
        # scale event weights between 1 - 2
        weight_df = MinMaxScaler(feature_range=(1., 2.)).fit_transform(
            weight_df.values.reshape(-1, 1))

        # save event weights
        single_meta_df['weights'] = weight_df

        # cleanup training variable dataframe
        single_training_df = slim_df.drop(selection_vars+todrop, axis=1)
        single_training_df = single_training_df.astype('float64')
        single_training_df['isSM'] = np.zeros(len(slim_df)) if is_signal == 1 else np.ones(len(slim_df))
        #new variable for training
        single_training_df['HToverLeadJet_pt'] = slim_df['HT']/slim_df['LeadJet_pt']
        
        # combine with other files 
        all_data['meta'] = pd.concat([all_data['meta'], single_meta_df])
        all_data['train'] = pd.concat([all_data['train'], single_training_df])

    return all_data

    
def build_scaler(sm_only):
    """
    Build StandardScaler for training variables, do the fit, and save the
    results to be used later.

    Parameters:
        sm_only (pandas.DataFrame): DataFrame of processed Standard Model files.
        Non-Standard Model events should not be included.

    Returns:
        scaler (StandardScaler): mean-0, variance-1 scaler already fit to SM
        scaler_info (pandas.DataFrame): information used to scale variables
    """
    scaler = StandardScaler()
    # only fit the nominal backgrounds
    scaler.fit(sm_only.values)
    scaler_info = pd.DataFrame.from_dict({
        'mean': scaler.mean_,
        'scale': scaler.scale_,
        'variance': scaler.var_,
        'nsamples': scaler.n_samples_seen_
    })
    scaler_info.set_index(sm_only.columns.values, inplace=True)
    return scaler, scaler_info


def format_for_store(all_data, scaler):
    """
    Get the processed DataFrames ready for storage in our dataset file. "meta"
    and "train" DataFrames are merged and the "train" variables are scaled.

    Parameters:
        all_data (map[string]pandas.DataFrame): all processed data
        scaler (StandardScaler): mean-0, variance-1 scaler to be applied to
        all_data['train]
    
    Returns:
        formatted_data (pandas.DataFrame): merged DataFrame with all events/variables
        included and scaled appropriately.
    """
    # apply scaling to all samples
    formatted_data = pd.DataFrame(
        scaler.transform(all_data['train'].values),
        columns=all_data['train'].columns.values, dtype='float64'
    )

    formatted_data['idx'] = all_data['meta']['index'].values
    formatted_data['sample_names'] = all_data['meta']['names'].values
    formatted_data['signal'] = all_data['meta']['isSignal'].values
    formatted_data['EvtWt'] = all_data['meta']['weights'].values
    
    return formatted_data
    

def main(args):
    start = time.time()

    # create the store
    store = pd.HDFStore('datasets/{}.h5'.format(args.output),
                        complevel=9, complib='bzip2')

    all_data = {
        'meta': pd.DataFrame(),
        'train': pd.DataFrame(),
    }
    filelist, _ = build_filelist(args.input)  # list of files to process

    # process all files
    all_data = process_files(all_data, filelist['tprime'], is_signal=1)
    all_data = process_files(all_data, filelist['others'], is_signal=0)

    # build scaler using SM only
    sm_only = all_data['train'][(all_data['train']['isSM'] == 1)]
    scaler, store['scaler'] = build_scaler(sm_only)

    # format data and store
    store['nominal'] = format_for_store(all_data, scaler)
    print ('Complete! Preprocessing completed in {} seconds'.format(time.time() - start))

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--input', '-i', required=True, help='path to input files')
    parser.add_argument('--output', '-o', required=True, help='name of output file')
    main(parser.parse_args())
