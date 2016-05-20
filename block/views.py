from django.shortcuts import render_to_response

from models import Block


def block_list(request):
    blocks = Block.objects.all().order_by("-id")
    return render_to_response("block_list.html", {"blocks": blocks})
