# Autcomplete
Autocomplete using Haystack and ElasticSearch in Django

## Prerequisites

ElasticSearch - 1.4.5

Run the elasticsearch server.

### Install requirements
 
        pip install -r requirements.txt 


### Build Index

        python manage.py rebuild_index
        
      
### Runserver

        python manage.py runserver

### URL


      GET http://127.0.0.1:8000/search/?q=abc
      
 RESPONSE
 
      {"suggestions": ['abc', 
                      'abcam', 
                      'abcaz', 
                      'abcd', 
                      'abcde', 
                      'abcdef',
                      'abcdefg',
                      'abcdefgh', 
                      'abcdefghijklmnopqrstu',
                      'abcdefghijklmnopqrstuvwxyz',
                      'abce', 
                      'abciximab',
                      'abcnews', 
                      'abco',
                      'abcs', 
                      'iabc',
                      'nabc', 
                      'rabck',
                      'sabc', 
                      'tabc', 
                      'wabc',
                      'wabcams'
                      'kabc',
                      'babcock',
                      'homeabc',
                     ]}
                     
                    
