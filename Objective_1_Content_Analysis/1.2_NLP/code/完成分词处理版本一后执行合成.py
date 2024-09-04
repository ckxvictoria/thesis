words_list = "Child, child, Children, children, children’s, Kids, kids, Kid, kid, Baby, baby, baby’s, Babies, babies, babies’, Family, family, Families, families, Play, play, Rhyme, rhyme, Rhymes, rhymes, Rhyme Time, rhyme time, Rhyme time, Rhymetime, Rhymetimes, rhymetime, Rhymetime, Toy, toy, Toys, toys, Baby bounce, baby bounce, Bookstart, bookstart, Book Start, book start, Book start, Under 5s, Storytelling, storytelling, Storytellings, storytellings, Lego, lego, Crafts, crafts, Craft, craft, Childcare, childcare, Child Care, Child care, child care, Day Care, day care, Day care, day bare, Nursery, nursery".split(", ")
a = list()

for i in words_list:
    a.append(i)
print(list(set(a)))
tokens = ['Baby', 'Craft', 'Baby bounce', 'Child Care', 'Day Care', 'Storytellings', 'Rhyme Time', 'Childcare',
          'baby bounce', 'Rhymetimes', 'kid', 'Rhymes', 'nursery', 'bookstart', 'rhyme time', 'Bookstart', 'Book start',
          'lego', 'Crafts', 'Child care', 'Families', 'storytellings', 'Child', 'family', 'day care', 'Toys',
          'Under 5s', 'Children', 'Family', 'toys', 'Rhyme', 'Kid', 'Nursery', 'Kids', 'storytelling', 'baby', 'Lego',
          'Storytelling', 'Rhyme time', 'Rhymetime', 'Toy', 'Babies', 'child care', 'babies', 'toy', 'day bare',
          'families', 'rhymetime', 'kids', 'Play', 'childcare', 'baby’s', 'Book Start', 'rhymes', 'Day care', 'child',
          'crafts', 'children', 'rhyme', 'book start', 'craft', 'children’s', 'play', 'babies’']
print(len(tokens))

words_list = "Child, child, Children, children, children’s, Kids, kids, Kid, kid, Baby, baby, baby’s, Babies, babies, babies’, Family, family, Families, families, Play, play, Rhyme, rhyme, Rhymes, rhymes, Rhyme Time, rhyme time, Rhyme time, Rhymetime, Rhymetimes, rhymetime, Rhymetime, Toy, toy, Toys, toys, Baby bounce, baby bounce, Bookstart, bookstart, Book Start, book start, Book start, Under 5s, Storytelling, storytelling, Storytellings, storytellings, Lego, lego, Crafts, crafts, Craft, craft, Childcare, childcare, Child Care, Child care, child care, Day Care, day care, Day care, day bare, Nursery, nursery".split(", ")
print(len(words_list))

# 读取CSV文件
import pandas as pd
df = pd.read_csv('Library_for_Kali.csv')

# 将DataFrame保存为Excel文件
df.to_excel('Library_for_Kali.xlsx', index=False)  # index=False表示不保存行索引
