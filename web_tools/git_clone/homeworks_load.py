# coding: utf-8
"""
  клонирует все git каологи группы в указанную папку
"""
import os, os.path
import pprint

import conf
trace = False

def create_foldiers(path_domain, list_repo):
    for user in list_repo:
        dir_user = os.path.join(path_domain, user[0])
        if not os.path.exists(dir_user):
            if not trace:
                os.makedirs(dir_user)
            else:
                print dir_user

        repositories = user[1]
        for (repo_name, repo_path) in repositories:
            dir_repo = os.path.join(dir_user, repo_name)
            print dir_repo, repo_path

            cmd = 'git clone {}'.format(repo_path)
            print cmd
            os.chdir(dir_user)
            os.system(cmd)



def main():
    print conf.path_target
    pprint.pprint(conf.user_lst)
    print '__start clone repository__'
    create_foldiers(conf.path_target, conf.user_lst)
    input('press any key ...')


if __name__ == "__main__":
    main()
