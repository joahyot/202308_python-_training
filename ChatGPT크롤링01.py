
import requests
from bs4 import BeautifulSoup

def crawl_naver_search_results(search_keyword):
    base_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    results = []

    blog_elements = soup.find_all('li', {'class':'bx _svp_item'})
    for blog_element in blog_elements:
        blog_name = blog_element.find('a', class_='api_txt_lines total_tit cross_').text
        blog_post_address = blog_element.find('a', class_='api_txt_lines total_tit')['href']
        post_date = blog_element.find('span', class_='sub_time sub_text').text
        
        results.append({
            'blog_name': blog_name,
            'blog_post_address': blog_post_address,
            'post_date': post_date
        })
    
    return results

if __name__ == "__main__":
    search_keyword = "맥북에어"
    search_results = crawl_naver_search_results(search_keyword)
    
    for result in search_results:
        print("Blog Name:", result['blog_name'])
        print("Blog Post Address:", result['blog_post_address'])
        print("Post Date:", result['post_date'])
        print("--------------------")
