// Dear emacs, this is -*- c++ -*-
//
// Copyright (C) 2002-2017 CERN for the benefit of the ATLAS collaboration
//
#ifndef ANALYSISPACKAGE_ANALYSISALGORITHM_H
#define ANALYSISPACKAGE_ANALYSISALGORITHM_H

// System include(s):
#include <string>

// Core include(s):
#include "AnaAlgorithm/AnaAlgorithm.h"

// Forward declaration(s):
class TH1;

/// Analysis algorithm template
///
/// Starting point for writing an EventLoop based analysis algorithm.
/// Remember that you should use multiple algorithms in your job, don't just
/// use a single algorithm, developed from this skeleton.
///
class AnalysisAlgorithm : public EL::AnaAlgorithm {

public:
   /// Algorithm constructor
   AnalysisAlgorithm( const std::string& name, ISvcLocator* svcLoc = nullptr );

   /// @name Functions "implementing" @c EL::AnaAlgorithm
   /// @{

   /// Function executed as part of the job initialisation
   virtual StatusCode initialize();

   /// Function executed once per event
   virtual StatusCode execute();

   /// Function executed as part of the job finalisation
   virtual StatusCode finalize();

   /// @}

private:
   /// @name Algorithm properties
   ///
   /// These are member variables of the class that can be set during the
   /// job configuration to configure the algorithm. They are regular variables,
   /// with the usual variable naming rules applying to them.
   ///
   /// Since these properties need to be declared to the framework in the
   /// algorithm's constructor, usually it's best to initialise them to some
   /// default value there.
   ///
   /// @{

   /// Name of the input particle container
   std::string m_inputContainer;

   /// @}

   /// @name Private member variables
   ///
   /// Variables not acting as properties, but being handled by the algorithm
   /// internally.
   ///
   /// Note that it's good practice with C++11 to initialise member variables in
   /// the class declaration.
   ///
   /// @{

   /// Particle pT histogram
   TH1* m_hist = nullptr;

   /// @}

}; // class AnalysisAlgorithm

#endif // ANALYSISPACKAGE_ANALYSISALGORITHM_H
