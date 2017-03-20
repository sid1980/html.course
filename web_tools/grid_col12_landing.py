# coding: utf-8
'''
col = [406,
       450,
       548,
       691,
       782,
       959.5,
       975.5,
       1021,
       1070,
       1166,
       1261.5,
       1530]
'''

begin_text ="""
* {
    box-sizing: border-box;
    font: "Arial";
}

.container{
    width: 1920px;
    margin: auto;
}

.row {
    width: 100%;
    float: left;
    text-align: justify;
}
"""
print  begin_text
col = []
num_col = 12
num_col = 16
for i in range(1, num_col):
    col_value = (i/float(num_col))*1920
    col.append(col_value)

print col

for i, _ in enumerate(col):
    counter = i+1
    if i == (len(col)-1):
        print '.col-{} {}float: left;{}'.format(counter, '{', '}')
    else:
        print '.col-{},'.format(counter)


for i,pos in enumerate(col):
    print ".col-{}{}width: {:.6}%; {}".format((i+1),
                                               '{',
                                               (pos/1920.0)*100,
                                              '}')
for i,pos in enumerate(col):
    print ".offset-{}{}margin-left: {:.6}%; {}".format((i+1),
                                               '{',
                                               (pos/1920.0)*100,
                                              '}')