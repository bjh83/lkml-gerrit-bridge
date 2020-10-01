# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
import os

# TODO(willliu@google.com): bump this value up
MAX_NUMBER_OF_RECENT_COMMITS = 2
    
def fill_message_directory(archive_path: str, directory: str, last_used_commit_hash: str) -> str:
    '''Updates the git repo, then retrieves the MAX_NUMBER_OF_RECENT_COMMITS recent commits and converts them into files stored
    in the directory corresponding to the passed in directory path. 
    
    Args:
        archive_path: path to the email archive
        directory: where to store files
        last_used_commit_hash: ending point for filling the directory
    
    Returns:
        The most recent processed commit hash
    
    Raises:
        CalledProcessError: when git fetch, git log, or git show fails
        Exception: when the log from git log shows no hashes
    '''
    
    subprocess.check_call(['git', '-C', archive_path, 'fetch'])
    
    output = subprocess.check_output(
        ['git', '-C', archive_path, 'log', '--format=format:%H', '-n',str(MAX_NUMBER_OF_RECENT_COMMITS)])
    message_hashes = output.decode('utf-8').split()
    
    if len(message_hashes) == 0:
        raise Exception(f'There are no commits in git repo: {archive_path}')
    
    for hash in message_hashes:
        if hash == last_used_commit_hash:
            break
        file = os.path.join(directory, f'{hash}.txt')
        # TODO(willliu@google.com): fetch the message contents on demand. We also don't check for errors creating the file
        with open(file, 'w') as f:
            subprocess.call(['git', '-C', archive_path, 'show', f'{hash}:m'],
                            stdout=f)
        
    return message_hashes[0]
    
def main():
    print(fill_message_directory('../linux-kselftest/git/0.git', '../lkml-gerrit-bridge/test_data', '5227e860278407173cbfdab594676764153c27e1'))
    
if __name__ == '__main__':
    main()