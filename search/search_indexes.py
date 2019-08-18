from haystack import indexes
from search.models import Words
import datetime

class WordDocumentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    occurence_count = indexes.IntegerField()

    word_auto = indexes.EdgeNgramField(model_attr='word')
    
    def get_model(self):
        return Words

    def index_queryset(self):
        return self.get_model().all().order_by('occurence_count')
