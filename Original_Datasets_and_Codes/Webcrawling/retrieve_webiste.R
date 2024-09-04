# Load libraries
library(rvest)
library(httr)
library(tidyverse)

# Set folder where to save the dataset and HTML files
folder_dataset <- "~/Downloads/"
folder_html_files <- "~/Downloads/html_files/"

# Set URL of the main webpage to scrape
start_url <- "https://hackney.gov.uk/libraries"

# Initialise dataset
website <-
  tibble(
    url_relative = c("__index__"), # relative url from links
    url_absolute = c(start_url),   # absolute url
    retireved = c(FALSE),          # whether the page has been retrieved or not
    page_html = c(NA),             # file where the HTML content has been saved
    page_text = c(NA)              # text from the page paragraphs
  )

# Starting from that webiste
# retrieve all linked pages with the same base url
while(
    (website %>% filter(!retireved) %>% nrow) > 0
  ){
  
  # Select page not yet retrieved
  current_url <-
    website %>% 
    filter(!retireved) %>% 
    slice_head(n = 1) %>% 
    pull(url_absolute)
  
  # File name for the current page
  current_url_filename <-
    current_url %>% 
    str_replace_all("(http|https)://", "") %>% 
    str_replace_all("/", "_") %>% 
    str_replace_all("\\.", "_") %>% 
    str_replace_all("#", "_") %>% 
    str_replace_all("-", "_") %>% 
    paste0(".html") %>% 
    paste0(folder_html_files, .)
  
  # Keep track while retrieving pages
  cat(
    paste(
      website %>% filter(retireved) %>% nrow,
      "/",
      website %>% nrow,
      "done, working on",
      current_url,
      "\n"
    )
  )
  
  # Retrieve and parse webpage at start url
  response <- GET(current_url)
  
  # Extract HTML
  html_content <- 
    response %>% 
    content(as = "text") %>% 
    writeLines(current_url_filename)
  
  
  # Extract text
  html_text <- 
    response %>% 
    content(as = "parsed") %>% 
    html_nodes("p") %>% 
    html_text() %>% 
    paste(collapse = "\n\n")
  
  # Update the current page content in the dataset
  website <-
    website %>% 
    mutate(
      page_html = if_else(
        url_absolute == current_url,
        #html_content,
        current_url_filename,
        page_html
      ),
      page_text = if_else(
        url_absolute == current_url,
        html_text,
        page_text
      ),
      retireved = if_else(
        url_absolute == current_url,
        TRUE,
        retireved
      ),
    )

  # Extracting all links
  links <- 
    # get the links
    response %>% 
    content(as = "parsed") %>% 
    html_nodes("a") %>% 
    html_attr("href") %>% 
    # transform the list to a table
    as_tibble_col() %>% 
    rename(url_relative = value) %>% 
    # filter out unnecessary links
    filter(
      !is.na(url_relative) &
      !url_relative %in% c("/", "#") &
      !str_starts(url_relative, "mailto:") &
      !str_starts(url_relative, "tel:")
    ) %>% 
    # Filter out reference to anchors in the current page
    filter(
      !str_starts(url_relative, "#") &
      !str_starts(url_relative, "/#")
    ) %>% 
    # transform to absolute url
    mutate(
      url_absolute = if_else(
        str_starts(url_relative, "(http|https)://"),
        url_relative,
        URLencode(paste0(start_url, url_relative))
      ),
      retireved = FALSE,
      page_html = NA,
      page_text = NA
    ) %>% 
    # remove duplicates
    distinct() %>% 
    filter(str_starts(url_absolute, start_url)) %>% 
    anti_join(website, by="url_absolute")

  # Bind new links to current dataset
  if(nrow(links) > 0){
    website <-
      website %>% 
      bind_rows(links)
  }
  
  # Clean up
  rm(current_url)
  rm(response)
  rm(html_content)
  rm(html_text)
  rm(links)

}

# Save dataset
website %>% 
  write_csv(
    start_url %>% 
      str_replace_all("(http|https)://", "") %>% 
      str_replace_all("/", "_") %>% 
      str_replace_all("\\.", "_") %>% 
      str_replace_all("#", "_") %>% 
      str_replace_all("-", "_") %>% 
      paste0(".csv") %>% 
      paste0(folder_dataset, .)
  )
website %>% 
  saveRDS(
    start_url %>% 
      str_replace_all("(http|https)://", "") %>% 
      str_replace_all("/", "_") %>% 
      str_replace_all("\\.", "_") %>% 
      str_replace_all("#", "_") %>% 
      str_replace_all("-", "_") %>% 
      paste0(".rds") %>% 
      paste0(folder_dataset, .)
  )

cat("... DONE!")