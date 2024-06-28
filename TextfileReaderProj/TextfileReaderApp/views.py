import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def read_text(request):
    file_path = os.path.join(settings.BASE_DIR, 'files', 'file_name')
# stores in the file name called file_name in the base directory
# Handle POST request to append content
    if request.method == 'POST':
        new_content = request.POST.get('content', '')
        if new_content:
            try:
                with open(file_path, 'a+') as file:
                    file.write(new_content + '\n')
                    file.seek(0)
                    content = file.read()
                return HttpResponse(content, content_type='text/plain')
            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}", status=500)
# Handle GET request to read content
    try:
        with open(file_path, 'a+') as file:
            file.seek(0)
            content = file.read()
        return HttpResponse(content, content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse("File not found.", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)
def form_view(request):
    return render(request, 'TextfileReaderApp/form.html')