from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from authentication.settings import MEDIA_ROOT
from accounts.transcription import process
import os

@csrf_exempt
def upload_video(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video_file = request.FILES['video']
        name = request.POST.get('name')  # Get the name from the request

        print(name)


        # Make sure the name is not empty
        if not name:
            return JsonResponse({'message': 'Name is required.'}, status=400)

        video_path = os.path.join(MEDIA_ROOT, video_file.name)
        with open(video_path, 'wb') as destination:
            for chunk in video_file.chunks():
                destination.write(chunk)

        # Now, you have the video file saved in the "media" folder
        # Pass the video_path and name to the process function in transcription.py
        transcript = process(video_path)

        # Return a response, for example:
        return JsonResponse({'message': 'Video uploaded and transcription started.'})
    else:
        return JsonResponse({'message': 'Invalid request.'}, status=400)
