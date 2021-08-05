#pip install facebook-scraper
import pandas as pd

from facebook_scraper import get_posts
for post in get_posts('Voto-NO-al-plebiscito-de-Santos-546777902190989', pages=800):
    print ((post['likes']) + ';' + str(post['comments']) + ';' + str(post['post_url']) + ';' + str(post['time']) + ';' + str(post['text']) + ';' + str(post['post_text']) + ';' + str(post['shared_text']) + ';' + str(post['image'])
           )


    #print(post)
    #print(post['likes'])
    #print(post['reactions']) ESTE PARECE QUE NO FUNCIONA