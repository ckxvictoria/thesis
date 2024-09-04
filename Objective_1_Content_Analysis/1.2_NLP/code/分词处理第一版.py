import os

content = ""
words_list = list()
import pandas as pd
data = pd.read_csv(r'new_data_file.csv', sep=',', header='infer', encoding='utf-8')
text_list = list()
for i in data['page_text']:
    text_list.append(i)
list1 = list()
list2 = list()
list3 = list()
list4 = list()
for text, url in zip(text_list, data['url_absolute']):
    text = str(text)
    content += text
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer()
    # print(text)
    try:
        X = vectorizer.fit_transform([text])
    except:
        continue
    tokens = vectorizer.get_feature_names_out()
    # print("分词结果：", tokens)
    words_list.extend(tokens)
    number_list = list()
    for i in tokens:
        number = text.count(i)
        number_list.append(number)
    list1.append(url)
    list2.append(tokens)
    list3.append(number_list)
    list4.append(sum(number_list))

# words_list = set(words_list)
words_list = "Child, child, Children, children, children’s, Kids, kids, Kid, kid, Baby, baby, baby’s, Babies, babies, babies’, Family, family, Families, families, Play, play, Rhyme, rhyme, Rhymes, rhymes, Rhyme Time, rhyme time, Rhyme time, Rhymetime, Rhymetimes, rhymetime, Rhymetime, Toy, toy, Toys, toys, Baby bounce, baby bounce, Bookstart, bookstart, Book Start, book start, Book start, Under 5s, Storytelling, storytelling, Storytellings, storytellings, Lego, lego, Crafts, crafts, Craft, craft, Childcare, childcare, Child Care, Child care, child care, Day Care, day care, Day care, day bare, Nursery, nursery".split(", ")

print(words_list)
# 读取停用词
with open('English_stop.txt', 'r', encoding='utf-8') as f:
    text_temp_list = f.read().split("\n")
# 去除停用词
for stop_word in text_temp_list:
    try:
        words_list.remove(stop_word)
    except:
        continue
word_frequency_pairs = list()
for word in words_list:
    word_number_list = list()
    for text in text_list:
        word_number = text.count(word)
        word_number_list.append(word_number)
    word_number = sum(word_number_list)
    if word_number==0:
        continue
    word_frequency_pairs.append((word, word_number))
# 使用 sorted 函数结合 lambda 表达式进行排序
sorted_pairs = sorted(word_frequency_pairs, key=lambda x: x[1], reverse=True)

word_list = list()
frequency_list = list()
page_html_list = list()
page_web_list = list()
count_list = list()
for word, frequency in sorted_pairs:
    word_list.append(word)
    frequency_list.append(frequency)
    page_list = list()
    web_list = list()
    number_list = list()
    for text, page, web in zip(data['page_text'], data['page_html'], data['url_absolute']):
        if word in text:
            page_list.append(page)
            web_list.append(web)
            number_list.append(text.count(word))
    page_html_list.append(page_list)
    page_web_list.append(web_list)
    count_list.append(number_list)
#保存为Excel
import pandas
writeData = {
    '网址': page_web_list,
    '关键字': word_list,
    '词频': count_list,
    # 'page_html': page_html_list,
    '总评': frequency_list,

}
fwrite = pandas.DataFrame(writeData)
fwrite.to_excel(f"关键字.xlsx", index=False)

url_list = list()
key_list = list()
key_number_list = list()
sum_number_list = list()
# 读取csv
import pandas as pd
# name_list = os.listdir("dataset")
name_list = list(pd.read_csv(r'Library_for_Kali.csv', sep=',', header='infer', encoding='utf-8')['url'])
print(name_list)
for name_temp in name_list:
    name = name_temp.replace("http://", "").replace("https://", "").replace("/", "_").replace(".", "_").replace("#", "_").replace("-", "_").replace(">", "_").replace("<", "_").replace('"', "_").replace("*", "_").replace("\\", "_").replace("|", "_").replace("?", "_").replace("%", "_") + ".csv"
    print(name)
    try:
        data = pd.read_csv(f'dataset/{name}', sep=',', header='infer', encoding='utf-8')

        url = data['url_absolute'][0]
        url_list.append(url)
        text = "".join([str(i) for i in data['page_text']]).replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
        from sklearn.feature_extraction.text import CountVectorizer
        vectorizer = CountVectorizer()

        # X = vectorizer.fit_transform([text])
        # tokens = vectorizer.get_feature_names_out()
        tokens = ['Kid', 'Play', 'play', 'Rhymetime', 'Storytelling', 'Children', 'Book Start', 'day bare', 'Nursery', 'families', 'Families', 'Toys', 'storytelling', 'Baby bounce', 'Storytellings', 'crafts', 'child care', 'Rhymetimes', 'Day care', 'Childcare', 'Day Care', 'childcare', 'children’s', 'Child', 'Rhymes', 'Rhyme', 'book start', 'Child Care', 'kid', 'Book start', 'storytellings', 'Crafts', 'kids', 'Rhyme Time', 'Craft', 'Bookstart', 'Babies', 'babies’', 'rhyme time', 'babies', 'rhyme', 'Toy', 'day care', 'baby', 'baby’s', 'children', 'child', 'rhymes', 'Kids', 'craft', 'nursery', 'rhymetime', 'bookstart', 'Family', 'family', 'baby bounce', 'lego', 'Child care', 'toys', 'Under 5s', 'Lego', 'toy', 'Baby', 'Rhyme time']
        key_list.append(tokens)
        count_list = list()
        for i in tokens:
            count = text.count(i)
            count_list.append(count)
        key_number_list.append(count_list)
        number = sum(count_list)
        sum_number_list.append(number)
    except:
        url_list.append('Null')
        key_list.append('Null')
        key_number_list.append('Null')
        sum_number_list.append('Null')



print(len(url_list))
print(len(key_list))
print(len(key_number_list))
print(len(sum_number_list))










#保存为Excel
import pandas
writeData = {
    '网址': url_list,
    '关键字': key_list,
    '词频': key_number_list,
    '总评': sum_number_list,
}
fwrite = pandas.DataFrame(writeData)
fwrite.to_excel(f"根据网址统计词频.xlsx", index=False)