//
// Copyright (C) 2002-2017 CERN for the benefit of the ATLAS collaboration
//

// ROOT include(s):
#include <TH1.h>

// EDM include(s):
#include "xAODBase/IParticleContainer.h"

// Local include(s):
#include "AnalysisPackage/AnalysisAlgorithm.h"

AnalysisAlgorithm::AnalysisAlgorithm( const std::string& name,
                                      ISvcLocator* svcLoc )
   : EL::AnaAlgorithm( name, svcLoc ) {

   /// Declare the algorithm's properties:
   declareProperty( "InputContainer", m_inputContainer = "Electrons" );
}

StatusCode AnalysisAlgorithm::initialize() {

   // Greet the user:
   ATH_MSG_INFO( "Will produce pT histogram from container \""
                 << m_inputContainer << "\"" );

   // Book the output histogram:
   ATH_CHECK( book( TH1D( ( m_inputContainer + "_pt" ).c_str(),
                          ( "p_{T} distribution for " +
                            m_inputContainer ).c_str(),
                          100, 0.0, 100000.0 ) ) );
   m_hist = hist( m_inputContainer + "_pt" );
   if( ! m_hist ) {
      ATH_MSG_ERROR( "Failed to book the output histogram" );
      return StatusCode::FAILURE;
   }

   // Return gracefully:
   return StatusCode::SUCCESS;
}

StatusCode AnalysisAlgorithm::execute() {

   // Retrieve the particle container:
   const xAOD::IParticleContainer* particles = nullptr;
   ATH_CHECK( evtStore()->retrieve( particles, m_inputContainer ) );

   // Plot the transverse momentum of the particles:
   for( const xAOD::IParticle* particle : *particles ) {
      m_hist->Fill( particle->pt() );
   }

   // Return gracefully:
   return StatusCode::SUCCESS;
}

StatusCode AnalysisAlgorithm::finalize() {

   // Print some summary for the user:
   ATH_MSG_INFO( "Processed a total of " << m_hist->GetEntries()
                 << " particles" );

   // Return gracefully:
   return StatusCode::SUCCESS;
}
