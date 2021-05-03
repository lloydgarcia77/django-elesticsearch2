from .models import Customer
from haystack import indexes
 
 
class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True, template_name="search\indexes\customers\customers_text.txt")
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    other_names = indexes.CharField(model_attr='other_names')
    email = indexes.CharField(model_attr='email', default=" ")
    phone = indexes.CharField(model_attr='phone', default=" ")
    balance = indexes.IntegerField(model_attr='balance', default="0")
    customer_status = indexes.CharField(model_attr='customer_status')
    address = indexes.CharField(model_attr='address', default=" ")
 
    def get_model(self):
        return Customer
 
    def index_queryset(self, using=None):
        return self.get_model().objects.all()