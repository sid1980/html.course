# coding: utf-8

path_target = r"c:\OpenServer\domains\itmo.homeworks"

user_lst = [('stetuxa_egor', [('homeworks', r'https://github.com/erikokos/homeworks.git'),
                              ('git-rep', r'https://github.com/erikokos/git-rep.git')]),
            ('ax_malinovskiy', [('git-git', r'https://github.com/axmalinovskiy/git-git.git')]),
            ('anna_kubanceva', [('git-lesson', r'https://github.com/caulfieldanna/git-lesson.git')]),
            ('alexander_kovzhut', [('itmo-study', r'https://github.com/backattack/itmo-study.git')]),
            ('alexander_pozdnakov', [('git-lesson1', r'https://github.com/Bodrbu/git-lesson1.git')]),
            ('igor_zaytcev', [('homeworks', r'https://github.com/Rinelsia/homeworks.git')])
            ]

def main():
    print path_target
    print user_lst

if __name__ == "__main__":
    main()