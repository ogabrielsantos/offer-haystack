from offer.models import Offer
from haystack import indexes


class OfferSearchIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Offer

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
