from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess


@csrf_exempt
def github_webhook(request):
    if request.method == 'POST':
        # Ejecutar el script git pull
        try:
            subprocess.run(["bash","/home/omeza/online-shop/git_pull/pull.sh"], check=True)
            return HttpResponse('OK', status=200)
        except Exception as e:
            return HttpResponse(f'Error al ejecutar el pull: {e}', status=404)
        except subprocess.CalledProcessError as e:
            return HttpResponse(f'Error al ejecutar el pull: {e}', status=500)
    return HttpResponse('Solo se permiten solicitudes POST', status=405)