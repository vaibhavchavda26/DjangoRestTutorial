from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippets
from snippets.serializers import SnippetSerializer

def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, stats = 201)
        return JsonResponse(serializer.errors, status = 400)

def snippet_detail(request, pk):
    try:
        snippet = Snippets.objects.get(id = pk)
    except Snippets.DoesNotExist:
        return HttpResponse(status = 400)

    if request.method == 'GET':
        seriliazer = SnippetSerializer(snippet)
        return JsonResponse(seriliazer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        seriliazer = SnippetSerializer(snippet, data = data)
        if seriliazer.is_valid():
            seriliazer.save()
            return JsonResponse(seriliazer.data)
        return JsonResponse(seriliazer.errors, status = 400)

    elif request.method == 'DELETE':
        snippet.delete()
        return JsonResponse(status = 204)