def save1():
    import pandas as pd
    page_web_list = list()
    count_list = list()
    frequency_list = list()
    data = pd.read_csv(r'new_data_file.csv', sep=',', header='infer', encoding='utf-8')
    print(data['page_text'])
    words_list = ['Rhyme', 'Play', 'rhymes', 'children', 'toy', 'Baby bounce', 'Children', 'Toys', 'families', 'Book start', 'babies', 'Rhyme Time', 'bookstart', 'babies’', 'Families', 'craft', 'kid', 'Kid', 'Baby', 'rhymetime', 'child care', 'Kids', 'rhyme time', 'day bare', 'Rhymetimes', 'crafts', 'child', 'Rhymetime', 'Crafts', 'baby', 'toys', 'children’s', 'Rhymes', 'book start', 'Lego', 'Under 5s', 'Child', 'Nursery', 'Storytelling', 'Day care', 'Family', 'Child Care', 'Toy', 'family', 'Bookstart', 'Storytellings', 'day care', 'storytelling', 'kids', 'Childcare', 'nursery', 'Rhyme time', 'baby bounce', 'rhyme', 'Craft', 'baby’s', 'lego', 'childcare', 'Child care', 'Babies', 'Day Care', 'Book Start', 'storytellings', 'play']
    for word in words_list:
        page_web_temp_list = list()
        count_temp_list = list()
        for text, web_html in zip(list(data['page_text']), list(data['url_absolute'])):
            word_count = str(text).count(word)
            print(word_count)
            if word_count != 0:
                page_web_temp_list.append(web_html)
                count_temp_list.append(word_count)
        page_web_list.append(page_web_temp_list)
        count_list.append(count_temp_list)
        frequency_list.append(sum(count_temp_list))
    print(len(page_web_list))
    print(len(words_list))
    print(len(count_list))
    print(len(frequency_list))


    #保存为Excel
    import pandas
    writeData = {
        '网址': page_web_list,
        '关键字': words_list,
        '词频': count_list,
        '总评': frequency_list,

    }
    fwrite = pandas.DataFrame(writeData)
    fwrite.to_excel(f"关键字.xlsx", index=False)
    df = pd.read_excel("关键字.xlsx")
    sorted_df = df.sort_values(by='总评', ascending=False)
    sorted_df.to_excel('关键字.xlsx', index=False)

def save2():
    words_list = ['Rhyme', 'Play', 'rhymes', 'children', 'toy', 'Baby bounce', 'Children', 'Toys', 'families', 'Book start', 'babies', 'Rhyme Time', 'bookstart', 'babies’', 'Families', 'craft', 'kid', 'Kid', 'Baby', 'rhymetime', 'child care', 'Kids', 'rhyme time', 'day bare', 'Rhymetimes', 'crafts', 'child', 'Rhymetime', 'Crafts', 'baby', 'toys', 'children’s', 'Rhymes', 'book start', 'Lego', 'Under 5s', 'Child', 'Nursery', 'Storytelling', 'Day care', 'Family', 'Child Care', 'Toy', 'family', 'Bookstart', 'Storytellings', 'day care', 'storytelling', 'kids', 'Childcare', 'nursery', 'Rhyme time', 'baby bounce', 'rhyme', 'Craft', 'baby’s', 'lego', 'childcare', 'Child care', 'Babies', 'Day Care', 'Book Start', 'storytellings', 'play']
    import pandas as pd
    data = pd.read_csv(r'new_data_file.csv', sep=',', header='infer', encoding='utf-8')
    url_list = data['url_absolute']
    key_list = list()
    key_number_list = list()
    sum_number_list = list()
    for text in data['page_text']:
        word_temp_list = list()
        key_list.append(words_list)
        for word in words_list:
            word_temp = str(text).count(word)
            word_temp_list.append(word_temp)
        key_number_list.append(word_temp_list)
        sum_number_list.append(sum(sum_number_list))


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
    df = pd.read_excel("根据网址统计词频.xlsx")
    sorted_df = df.sort_values(by='总评', ascending=False)
    sorted_df.to_excel('根据网址统计词频.xlsx', index=False)
save1()
save2()