from .models import PROJECTInformation
def PROJECTInformations(request):
    try:
        projectInfo = PROJECTInformation.objects.get(pk=1)
        context = {
            'project': projectInfo,
            }
        return context
    except Exception:
        return {'project':''}




