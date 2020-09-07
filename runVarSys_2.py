#!q
#/bin/python

import subprocess

CH = "Mu"
if (CH == "Mu"):
    options = [

           ['Mu_WJets_LepPt', 5, "LepPt"],
    ]
elif (CH == "Ele"):
    options = [

           ['Ele_WJets_LepPt', 5, "LepPt"],
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
