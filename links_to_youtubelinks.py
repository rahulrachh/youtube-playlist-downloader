i = 1
for x in range(0, 4584, 100):
    new_links = []
    with open('newlinks3.txt') as f:
        links = f.readlines()[x:x+100]
        for x in links:
            new_links.append('https://www.youtube.com'+x.split('&')[0])



    with open('final_links'+str(i)+'.txt','w') as f_link:
        for x in new_links:
            f_link.write(x+'\n')

    i += 1


