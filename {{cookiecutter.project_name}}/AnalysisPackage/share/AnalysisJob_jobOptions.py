#
# Copyright (C) 2002-2017 CERN for the benefit of the ATLAS collaboration
#
# Script running an analysis job using the algorithm(s) of the package, using
# Athena.
#

# Set up the reading of the input file(s):
import os
from AthenaCommon.JobProperties import jobproperties as jps
jps.AthenaCommonFlags.FilesInput = [
    os.environ.get( 'INPUT_FILE', os.environ[ 'ASG_TEST_FILE_MC' ] )
    ]
import AthenaRootComps.ReadAthenaxAODHybrid

# Access the algorithm sequence:
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()

# Add the analysis algorithm(s). First, demonstrate how to set properties for
# an algorithm instance in its constructor.
from AnalysisPackage.AnalysisPackageConf import AnalysisAlgorithm
electronPlotter = AnalysisAlgorithm( 'ElectronPlotter',
                                     InputContainer = 'Electrons',
                                     RootStreamName = '/ANALYSIS' )
topSequence += electronPlotter

# Then, show how to achieve the same after the algorithm's configuration was
# already created.
muonPlotter = AnalysisAlgorithm( 'MuonPlotter' )
muonPlotter.InputContainer = 'Muons'
muonPlotter.RootStreamName = '/ANALYSIS'
topSequence += muonPlotter

# Configure THistSvc to know about the "/ANALYSIS" stream:
ServiceMgr += CfgMgr.THistSvc()
ServiceMgr.THistSvc.Output += [
    "ANALYSIS DATAFILE='hist.root' TYP='ROOT' OPT='RECREATE'"
    ]
