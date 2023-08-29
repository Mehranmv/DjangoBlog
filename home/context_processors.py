from posts.models import Category
from .forms import PostSearchForm


def global_context(request):
    context = {
        'categories': Category.objects.all(),
        'search': PostSearchForm,
    }
    return context
