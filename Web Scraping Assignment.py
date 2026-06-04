# Install required libraries 
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime as dt
from tqdm import tqdm 

main_url = "https://anycallmobilemm.com/product-category/smartphone/"

############################################### Part 1 ################################################################
def create_urls(web_url):
    # Request data from the website
    

    # Request data by using url
    response = requests.get(web_url)

    web_data = response.text


    # Create a beautifulsoup object to read web data
    bsObj = BeautifulSoup(web_data, "html5lib")

    # Extract last page number
    last_page_tag_list = bsObj.find_all("a", "page-numbers")
    last_page_tag = last_page_tag_list[3]
    last_page_text = last_page_tag.text
    last_page_text = int(last_page_text)
    
    

    # Create urls for other pages
    created_url_list = []
    created_url_list.append(web_url)
    for num in range(2,last_page_text+1):
        new_url = web_url + "page/" + str(num) + "/"
        created_url_list.append(new_url)
        
    print("URL links are created successfully!")
    
    return created_url_list


def get_product_info_tags(url):
    response = requests.get(url)
    
    web_data = response.text


    # Create a beautifulsoup object to read web data
    bsObj = BeautifulSoup(web_data, "html5lib")

    #Extract all tags
    product_info_tags_list = bsObj.find_all("div", "product-element-bottom")
    
    return (product_info_tags_list)

def create_name_list(product_info_tags_list):
    name_list = []
    for product_info_tag in product_info_tags_list:


        #Extract product name tag
        product_name_tag = product_info_tag.find("h3", "wd-entities-title")

        product_name = product_name_tag.text
        #print(product_name)
        name_list.append(product_name)
    return name_list
    
def create_price_list(product_info_tags_list):
    price_list = []
    for product_info_tag in product_info_tags_list:
    
        # Extract product price
        product_price_tag = product_info_tag.find("span", "woocommerce-Price-amount amount")

        product_price = product_price_tag.text
        #Transform product price
        product_price = product_price.replace(",", "")
        product_price = product_price.replace("Ks", "")
        product_price = int(product_price)
        price_list.append(product_price)
    return price_list

def get_current_dt():
    # Get Current Date Time
    current_datetime = dt.now()
     
    # Change data to string
    current_datetime = str(current_datetime)
    
    # Replace
    current_datetime = current_datetime.replace(":", "-")
     
    # Remove milliseconds
    current_dt = current_datetime.split(".")[0]
    
    return current_datetime


######################################## Main Program #########################################
def main():
    ###################### Main Program to extract data from the website ####################
    # Create urls for all web pages
    url_list = create_urls(main_url)

    count = 0
    url_count = 0
    
    final_df = pd.DataFrame()
    # Extract Data From Each URL of the URL list
    
    for each_url in tqdm(url_list):
        # Extract product info tags
        p_info_tags_list = get_product_info_tags(each_url)
        
        
        #Creatr_name_list(p_info_tags_list)
        
        p_name_list = create_name_list(p_info_tags_list)
        
        #Creatr_price_list(p_info_tags_list)
        
        p_price_list = create_price_list(p_info_tags_list)
        
        #print(p_name_list)
        #print(p_price_list)

        # Create a page level dataframe
        page_df = pd.DataFrame({"Product Name":p_name_list,
                           "Price":p_price_list,})
         
        
        # Get current datetime as string
        current_dt = get_current_dt()
        
        # Export as page level excel file
        # Export as an Excel file
        page_df.to_excel(f"OutputB_{url_count}_{current_dt}.xlsx", index=False)
        
        url_count += 1
        print(f"Web {url_count} is completed successfully!")
    
        # Export data from all web pages
        final_df = pd.concat([final_df, page_df])
        
    #Export the final datafram as an Excel file
    final_df.to_excel(f"All Data_{current_dt}.xlsx", index=False)

    print("Project is completed successfully!")

if __name__ == "__main__":
    main()