from rest_framework.response import Response
from rest_framework.views import APIView
from haystack.query import SearchQuerySet
from .models import Words
import json


class WordSearchView(APIView):
    def get(self, request):
        search_query = request.query_params.get('q')
        word_query_result = SearchQuerySet().autocomplete(word_auto=search_query)[:25]

        word_suggestions = [search_result.word for search_result in word_query_result]
        
        response_data = json.dumps({
            'suggestions': word_suggestions
        })
        return Response(response_data)

# Create your views here.
