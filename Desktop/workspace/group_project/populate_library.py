import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')


import django
django.setup()
from library.models import Genre,Book, Bookpage


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    
    fiction_books = [
        {'title':'The Girl with the Louding Voice',
         'url':'http://127.0.0.1:8000/library/bookp/1'},
        {'title':'Girl, Woman, Other',
         'url':'http://127.0.0.1:8000/library/bookp/2'},
        {'title':'The Guest List',
         'url':'http://127.0.0.1:8000/library/bookp/3'},
        {'title':'Briefly Gorgeous',
         'url':'http://127.0.0.1:8000/library/bookp/4'},
        {'title':'The Alchemist',
         'url':'http://127.0.0.1:8000/library/bookp/5'},
        {'title':'Fake Accounts',
         'url':'http://127.0.0.1:8000/library/bookp/6'},
        {'title':'Murder Club',
         'url':'http://127.0.0.1:8000/library/bookp/7'},
        {'title':'Insatiable',
         'url':'http://127.0.0.1:8000/library/bookp/8'}]
    
    nonfiction_books = [
        {'title':'Becoming',
         'url':'http://127.0.0.1:8000/library/bookp/9'},
        {'title':'The Boy, the Mole, the Fox, the Horse',
         'url':'http://127.0.0.1:8000/library/bookp/10'},
        {'title':'House of Glass',
         'url':'http://127.0.0.1:8000/library/bookp/11'},
        {'title':'Consensual Hex',
         'url':'http://127.0.0.1:8000/library/bookp/12'},
        {'title':'Woman on the Edge of Time',
         'url':'http://127.0.0.1:8000/library/bookp/13'},
        {'title':'How to Avoid a Climate Disaster',
         'url':'http://127.0.0.1:8000/library/bookp/14'},
        {'title':'War and Peace',
         'url':'http://127.0.0.1:8000/library/bookp/15'},
        {'title':'Destination Wedding',
         'url':'http://127.0.0.1:8000/library/bookp/16'}]
    
    children_books = [
        {'title':'Chain of Iron',
         'url':'http://127.0.0.1:8000/library/bookp/17'},
        {'title':'Kays Anatomy',
         'url':'http://127.0.0.1:8000/library/bookp/18'},
        {'title':'One Hundred Steps',
         'url':'http://127.0.0.1:8000/library/bookp/19'},
        {'title':'They Both Die at the End',
         'url':'http://127.0.0.1:8000/library/bookp/20'},
        {'title':'FING',
         'url':'http://127.0.0.1:8000/library/bookp/21'},
        {'title':'The Girl and the Dinosaur',
         'url':'http://127.0.0.1:8000/library/bookp/22'},
        {'title':'Six of Crows',
         'url':'http://127.0.0.1:8000/library/bookp/23'},
        {'title':'The Gilded Ones',
         'url':'http://127.0.0.1:8000/library/bookp/24'}]
    
    cats = {'FICTION': {'books': fiction_books},
            'NONFICTION': {'books': nonfiction_books},
            "CHILDREN": {'books': children_books}}
    
    for cat, cat_data in cats.items():
        c = add_genre(cat)
        for p in cat_data['books']:
            add_bookpage(c, p['title'],p['url'])
            

    for c in Genre.objects.all():
        for p in Book.objects.filter(genre=c):
            print(f'- {c}: {p}')

def add_book(cat,title,url,views=0):
    p = Book.objects.get_or_create(genre=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_genre(name):
    c = Genre.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_bookpage(cat,title,url,views=0):
    temp = add_book(cat, title,url, views=0)
    b = Bookpage.objects.get_or_create(name=title)[0]
    b.book = temp
    b.name=title
    b.save()
    return b




#Startexecutionhere!
if __name__=='__main__':
    print('Starting Library population script...')
    populate()