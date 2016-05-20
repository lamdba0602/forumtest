from block.models import Block
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Article


def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")
    print(articles)
    return render_to_response("article_list.html", {"articles": articles, "blocks": block},
                                context_instance=RequestContext(request))
