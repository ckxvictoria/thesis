import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

cw_url = list()

# Set folder where to save the dataset and HTML files
folder_dataset = os.path.expanduser("dataset")
folder_html_files = os.path.expanduser("html_files")
os.makedirs(folder_dataset, exist_ok=True)
os.makedirs(folder_html_files, exist_ok=True)

# Set URL of the main webpage to scrape
# Read the CSV file into a DataFrame
df = pd.read_csv('library_for_kali.csv')

# Get the rows and convert it to a string
urls = df['url'].iloc[11:].tolist()

print(urls)

index=0
while index< len(urls):
    start_url=urls[index]

    # Initialize dataset
    website = pd.DataFrame({
        'url_relative': ["__index__"],  # relative url from links
        'url_absolute': [start_url],    # absolute url
        'retrieved': [False],           # whether the page has been retrieved or not
        'page_html': [None],            # file where the HTML content has been saved
        'page_text': [None]             # text from the page paragraphs
    })

    # Function to clean and generate filename for HTML
    def generate_filename(url):
        return os.path.join(folder_html_files,
                            url.replace("http://", "").replace("https://", "")
                               .replace("/", "_").replace(".", "_")
                               .replace("#", "_").replace("-", "_").replace(">", "_").replace("<", "_").replace('"', "_").replace("*", "_").replace("\\", "_").replace("|", "_").replace("?", "_").replace("%", "_") + ".html")

    # Function to scrape webpage
    def scrape_page(url):
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            return response.text
        else:
            return None

    website['filename'] = website['url_absolute'].apply(generate_filename)

    website_flag=-1
    while not website[website['retrieved'] == False].empty:
        current_url = website.loc[website['retrieved'] == False, 'url_absolute'].values[0]
        current_url_filename = generate_filename(current_url)

        if(website_flag==len(website[website['retrieved'] == True])):
            break
        else:
            website_flag=-1

        # Keep track while retrieving pages
        print(f"{len(website[website['retrieved'] == True])} / {len(website)} done, working on {current_url}")

        website_flag=len(website[website['retrieved'] == True])

        # Retrieve and parse webpage at start url
        try:
            html_content = scrape_page(current_url)
        except:
            cw_url.append(current_url)
            continue

        if html_content:
            # Save HTML content to file
            with open(current_url_filename, 'w', encoding='utf-8') as file:
                file.write(html_content)

            # Extract text
            soup = BeautifulSoup(html_content, 'html.parser')
            page_text = "\n\n".join([p.get_text() for p in soup.find_all('p')])

            # Update the current page content in the dataset
            website.loc[website['url_absolute'] == current_url, 'page_html'] = current_url_filename
            website.loc[website['url_absolute'] == current_url, 'page_text'] = page_text
            website.loc[website['url_absolute'] == current_url, 'retrieved'] = True

            # Extracting all links
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            links = [link for link in links if link and not link.startswith(('mailto:', 'tel:', '#', '/#'))]
            links = [urljoin(start_url, link) if not link.startswith(('http://', 'https://')) else link for link in links]
            links = list(set(filter(lambda x: x.startswith(start_url), links)))

            # Add new links to the dataset
            new_links = pd.DataFrame({'url_relative': links, 'url_absolute': links})
            new_links['retrieved'] = False
            new_links['page_html'] = None
            new_links['page_text'] = None

            website = pd.concat([website, new_links]).drop_duplicates(subset=['url_absolute']).reset_index(drop=True)

    # Save dataset to CSV and RDS (using pickle for RDS equivalent)
    csv_filename = os.path.join(folder_dataset,
                                current_url.replace("http://", "").replace("https://", "").replace("/", "_").replace(".", "_").replace(
                                    "#", "_").replace("-", "_").replace(">", "_").replace("<", "_").replace('"', "_").replace("*", "_").replace("\\", "_").replace("|", "_").replace("?", "_").replace("%", "_") + ".csv")
    website.to_csv(csv_filename, index=False)

    # rds_filename = os.path.join(folder_dataset,
    #                             current_url.replace("http://", "").replace("https://", "").replace("/", "_").replace(".",
    #                                                                                                                  "_").replace(
    #                                 "#", "_").replace("-", "_") + ".pkl")
    # website.to_pickle(rds_filename)

    print("... DONE!")

    index=index+1

import os
print(os.getcwd())

print(os.path.abspath("web_scraping_data"))

#保存为Excel
import pandas
writeData = {
    'url': cw_url,
}
fwrite = pandas.DataFrame(writeData)
fwrite.to_excel(f"错误网址.xlsx", index=False)