from fabric.contrib.files import append,exists,sed
from fabric.api import env,local,run
import random

REPO_URL = 'https:github.com/'
def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    source_folder = site_folder + '/source'
    _create_directory_struct_if_necessary(site_folder)
    _get_lasts_source(source_folder)
    _update_settings(source_folder,env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)
    _
