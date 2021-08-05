#pip install facebook-scraper
import pandas as pd

from facebook_scraper import get_posts
for post in get_posts('PazALaCalleP', pages=800):
    #print ('[ ' + 'LIKES: ' +str(post['likes']) + ',' + ' COMENTARIOS: ' + str(post['comments']) + ',' + ' URL: ' + str(post['post_url']) + ',' + ' FECHA: ' + str(post['time']) + ',' + ' TEXTO: ' + str(post['text']) + ',' + ' TEXTO DEL POST: ' + str(post['post_text']) + ',' + ' TEXTO COMPARTIDO: ' + str(post['shared_text']) + ',' + ' IMAGEN: ' + str(post['image']) + ' ]' )

    print (str(post['text']) + str(post['shared_text']) + str(post['post_text']))

    #print ('INICIO - ' + str(post['post_text']) +  ' - FIN')
    #print(post)
    #print(post['image'])
    #print(post['reactions']) ESTE PARECE QUE NO FUNCIONA