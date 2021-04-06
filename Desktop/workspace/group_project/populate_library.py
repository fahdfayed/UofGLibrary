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
         'url':'http://127.0.0.1:8000/library/bookp/1',
         'likes':20, 'quantity':5},
        {'title':'Girl, Woman, Other',
         'url':'http://127.0.0.1:8000/library/bookp/2',
         'likes':7, 'quantity':8},
        {'title':'The Guest List',
         'url':'http://127.0.0.1:8000/library/bookp/3',
         'likes':10, 'quantity':4},
        {'title':'Briefly Gorgeous',
         'url':'http://127.0.0.1:8000/library/bookp/4',
         'likes':8, 'quantity':8},
        {'title':'The Alchemist',
         'url':'http://127.0.0.1:8000/library/bookp/5',
         'likes':30, 'quantity':1},
        {'title':'Fake Accounts',
         'url':'http://127.0.0.1:8000/library/bookp/6',
         'likes':40, 'quantity':2},
        {'title':'Murder Club',
         'url':'http://127.0.0.1:8000/library/bookp/7',
         'likes':12, 'quantity':3},
        {'title':'Insatiable',
         'url':'http://127.0.0.1:8000/library/bookp/8',
         'likes':4, 'quantity':6}]
    
    nonfiction_books = [
        {'title':'Becoming',
         'url':'http://127.0.0.1:8000/library/bookp/9',
         'likes':11, 'quantity':7},
        {'title':'The Boy, the Mole, the Fox, the Horse',
         'url':'http://127.0.0.1:8000/library/bookp/10',
         'likes':13, 'quantity':4},
        {'title':'House of Glass',
         'url':'http://127.0.0.1:8000/library/bookp/11',
         'likes':20, 'quantity':3},
        {'title':'Consensual Hex',
         'url':'http://127.0.0.1:8000/library/bookp/12',
         'likes':22, 'quantity':5},
        {'title':'Woman on the Edge of Time',
         'url':'http://127.0.0.1:8000/library/bookp/13',
         'likes':26, 'quantity':2},
        {'title':'How to Avoid a Climate Disaster',
         'url':'http://127.0.0.1:8000/library/bookp/14',
         'likes':20, 'quantity':9},
        {'title':'War and Peace',
         'url':'http://127.0.0.1:8000/library/bookp/15',
         'likes':14, 'quantity':2},
        {'title':'Destination Wedding',
         'url':'http://127.0.0.1:8000/library/bookp/16',
         'likes':20, 'quantity':5}]
    
    children_books = [
        {'title':'Chain of Iron',
         'url':'http://127.0.0.1:8000/library/bookp/17',
         'likes':18, 'quantity':4},
        {'title':'Kays Anatomy',
         'url':'http://127.0.0.1:8000/library/bookp/18',
         'likes':26, 'quantity':3},
        {'title':'One Hundred Steps',
         'url':'http://127.0.0.1:8000/library/bookp/19',
         'likes':30, 'quantity':2},
        {'title':'They Both Die at the End',
         'url':'http://127.0.0.1:8000/library/bookp/20',
         'likes':13, 'quantity':3},
        {'title':'FING',
         'url':'http://127.0.0.1:8000/library/bookp/21',
         'likes':2, 'quantity':7},
        {'title':'The Girl and the Dinosaur',
         'url':'http://127.0.0.1:8000/library/bookp/22',
         'likes':42, 'quantity':1},
        {'title':'Six of Crows',
         'url':'http://127.0.0.1:8000/library/bookp/23',
         'likes':32, 'quantity':4},
        {'title':'The Gilded Ones',
         'url':'http://127.0.0.1:8000/library/bookp/24',
         'likes':3, 'quantity':10}]
    
    cats = {'FICTION': {'books': fiction_books},
            'NONFICTION': {'books': nonfiction_books},
            "CHILDREN": {'books': children_books}}
    
    for cat, cat_data in cats.items():
        c = add_genre(cat)
        for p in cat_data['books']:
            add_bookpage(c, p['title'],p['url'], p['likes'], p['quantity'])
            

    for c in Genre.objects.all():
        for p in Book.objects.filter(genre=c):
            print(f'- {c}: {p}')

def add_book(cat,title,url, likes=0, quantity=0):
    p = Book.objects.get_or_create(genre=cat, title=title)[0]
    p.url=url
    p.likes=likes
    p.quantity=quantity
    p.save()
    return p

def add_genre(name):
    c = Genre.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_bookpage(cat,title,url, likes=0, quantity=0):
    temp = add_book(cat, title,url, likes=likes, quantity=quantity)
    b = Bookpage.objects.get_or_create(name=title)[0]
    b.book = temp
    b.name=title
    b.save()
    return b


#Startexecutionhere!
if __name__=='__main__':
    print('Starting Library population script...')
    populate()
