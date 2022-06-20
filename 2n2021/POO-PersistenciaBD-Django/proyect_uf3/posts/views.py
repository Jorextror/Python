from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Valoration
from django.template import loader
from django.urls import reverse
from django.views import generic


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(generic.ListView):
    template_name = 'views/index.html'
    context_object_name = 'latest_posts_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'views/detail.html'
    
class ResultsView(generic.ListView):
    model = Post
    template_name = 'views/results.html'
    context_object_name = 'latest_posts_list'

def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    try:
        selected_valoration = post.valoration_set.get(pk=request.POST['valoration'])
    except (KeyError, Valoration.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'views/detail.html', {
            'post': post,
            'error_message': "You didn't select a valoration.",
        })
    else:
        selected_valoration.votes += 1
        selected_valoration.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('detail', args=(post.id,)))