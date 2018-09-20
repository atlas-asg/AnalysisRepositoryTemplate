#!/usr/bin/env python
#
# Copyright (C) 2002-2017 CERN for the benefit of the ATLAS collaboration
#
# Script running an analysis job using the algorithm(s) of the package, using
# EventLoop.
#

# Take some arguments from the command line:
import argparse
parser = argparse.ArgumentParser( description =
                                  "EventLoop Analysis Job" )
parser.add_argument( "-i", "--input-files", dest = "input",
                     nargs = "?",
                     default = "file://${ASG_TEST_FILE_MC}",
                     help = "Input file(s) to process" )
args = parser.parse_args()

# Set up (Py)ROOT:
import ROOT
ROOT.xAOD.Init().ignore()

# Set up the sample handler object:
sh = ROOT.SH.SampleHandler()
sh.setMetaString( "nc_tree", "CollectionTree" )

# Add a sample to it, made from the specified input file(s):
chain = ROOT.TChain( "CollectionTree" )
chain.Add( args.input )
sh.add( ROOT.SH.makeFromTChain( "input", chain ) )

# Create an EventLoop job:
job = ROOT.EL.Job()
job.sampleHandler( sh )

# Add the analysis algorithm(s). First, demonstrate how to set properties for
# an algorithm instance in its constructor.
from AnaAlgorithm.AnaAlgorithmConfig import AnaAlgorithmConfig
electronPlotter = AnaAlgorithmConfig( "AnalysisAlgorithm/ElectronPlotter",
                                      InputContainer = "Electrons" )
job.algsAdd( electronPlotter )

# Then, show how to achieve the same after the algorithm's configuration was
# already created.
muonPlotter = AnaAlgorithmConfig( "AnalysisAlgorithm/MuonPlotter" )
muonPlotter.InputContainer = "Muons"
job.algsAdd( muonPlotter )

# Run the job:
driver = ROOT.EL.DirectDriver()
driver.submit( job, "AnalysisJob" )
