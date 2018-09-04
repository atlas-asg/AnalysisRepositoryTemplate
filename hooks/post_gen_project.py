#
# Copyright (C) 2002-2018 CERN for the benefit of the ATLAS collaboration
#

# Import(s).
import os
import sys
import mimetypes
import glob
import base64
import gitlab

# Constants:
server = 'https://gitlab.cern.ch'
gitlabname = '{{cookiecutter.gitlab_name}}'
useremail = '{{cookiecutter.contact_email}}'
token = '{{cookiecutter.gitlab_token}}'
projectname = '{{cookiecutter.project_name}}'
description = '{{cookiecutter.short_descr}}'
baserelease = '{{cookiecutter.base_release}}'

# As a first thing, clean up the generated project. The logic here is that
# files ending in ".AnalysisBase", ".AthAnalysis" or ".Hybrid" are renamed to
# not have this postfix, if they are the ones to use for the project. While the
# non-appropriate files get removed.
#
# If specialisations for a given file do exist, but just not for this specific
# project, then the second loop takes care of removing the files completely.
postfixes = ( '.AnalysisBase', '.AthAnalysis', '.Hybrid' )
fileSpecialisationsSeen = {}
for root, subdirs, files in os.walk( os.getcwd() ):
    for project_file in files:
        file_path = os.path.relpath( os.path.join( root, project_file ) )
        file_base = os.path.splitext( file_path )[ 0 ]
        file_ext  = os.path.splitext( file_path )[ 1 ]
        if file_ext == '.%s' % baserelease:
            os.rename( file_path, file_base )
            for other_template in glob.glob( '%s.*' % file_base ):
                os.remove( other_template )
                pass
            fileSpecialisationsSeen[ file_base ] = True
            continue
        elif file_ext in postfixes:
            fileSpecialisationsSeen[ file_base ] = False
            pass
        pass
    pass
for filename, specFound in fileSpecialisationsSeen.iteritems():
    if specFound:
        continue
    for other_template in glob.glob( '%s.*' % filename ):
        os.remove( other_template )
        pass
    pass
print( 'Finished the generation of the project' )

def findGroup( mgr, name ):
    """Find a group in GitLab

    This is unfortunately more than just a single call, one needs to filter
    through the groups returned by GitLab, and select just the one that has
    the exact name that we're looking for.

    The function returns a gitlab.Group object if the group could be found,
    or None if it could not be.

    Keyword arguments:
      mgr -- The gitlab.Gitlab object we are using
      name -- The (full) name of the (sub-)group to search for
    """

    # Tokenize the name:
    names = name.split( '/' )

    # Find the "main" group:
    current_group = None
    ids = mgr.groups.list( search = names[ 0 ] )
    for candidate_group in ids:
        if candidate_group.path == names[ 0 ]:
            current_group = candidate_group
            break
        pass

    # Now look for sub-groups in this main group recursively:
    for group_name in names[ 1 : ]:
        # Make sure that we still have a valid group to operate on:
        if not current_group:
            return None
        # Look for a subgroup in the current group with this name:
        ids = current_group.subgroups.list( search = group_name )
        for candidate_group in ids:
            if candidate_group.path == group_name:
                # If we found it, make this the current group, and look
                # for the next sub-group:
                current_group = mgr.groups.get( candidate_group.id )
                break
            pass
        pass

    # A final security check:
    if current_group:
        if current_group.full_path != name:
            raise LookupError( 'There was a problem in finding group "%s"' %
                               name )
        pass

    # Return what we found:
    return current_group

# Access GitLab.
gl = gitlab.Gitlab( server, private_token = token,
                    api_version = 4 )
gl.auth()
print( 'Opened connection to: %s' % server )

# Find the user/group to create the repository for.
user_id = None
user_ids = gl.users.list( username = gitlabname )
if len( user_ids ) == 1:
    user_id = user_ids[ 0 ]
    pass

group_id = findGroup( gl, gitlabname )

id = None
if user_id:
    id = user_id
elif group_id:
    id = group_id
    pass

if not id:
    print( 'Could not find user/group with name "%s"' % gitlabname )
    sys.exit( 1 )
    pass

# Make sure that if a user ID was specified, we are authenticating as that user.
if user_id:
    if gitlabname != gl.user.username:
        print( 'Requesting repository for "%s", but authenticated as "%s"' %
               ( gitlabname, gl.user.username ) )
        sys.exit( 1 )
        pass
    pass

# Find the atlas-physics group.
atlas_id = findGroup( gl, 'atlas-physics' )
if not atlas_id:
    print( 'Could not find the "atlas-physics" group!' )
    sys.exit( 1 )
    pass

# Make sure that the repository doesn't exist yet.
projects = id.projects.list( search = projectname )
if len( projects ) != 0:
    print( 'Project/repository "%s" already exists for "%s"' %
           ( projectname, gitlabname ) )
    print( project[ 0 ] )
    sys.exit( 1 )
    pass

# Create the (private) repository.
args = { 'name' : projectname,
         'path' : projectname,
         'description' : description,
         'visibility' : 'private',
         'wiki_enabled' : False }
if group_id:
    args[ 'namespace_id' ] = group_id.id
    pass
project = gl.projects.create( args )
print( 'Created project "%s"' % projectname )

# Set its properties.
project.share( atlas_id.id, gitlab.REPORTER_ACCESS )

# Commit/upload all files to it.
commit_data = {
    'branch'        : 'master',
    'commit_message': 'Initial commit',
    'author_email'  : useremail,
    'actions'       : []
    }
for root, subdirs, files in os.walk( os.getcwd() ):
    for upload_file in files:
        file_path = os.path.relpath( os.path.join( root, upload_file ) )
        file_type = mimetypes.guess_type( file_path )
        content = open( file_path, 'r' ).read()
        action = { 'action'    : 'create',
                   'file_path' : file_path }
        if file_type[ 0 ] == 'image/png':
            action[ 'content' ] = base64.b64encode( content )
            action[ 'encoding' ] = 'base64'
        else:
            action[ 'content' ] = content
            pass
        commit_data[ 'actions' ].append( action )
        pass
    pass
commit = project.commits.create( commit_data )
print( 'Uploaded the initial commit to it' )
