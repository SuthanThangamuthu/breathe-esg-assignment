from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Company
from .services.csv_processor import process_csv


@api_view(["POST"])
def upload_emissions(request):

    file = request.FILES.get("file")
    company_name = request.POST.get("company_name")
    source_type = request.POST.get("source_type")

    if not file:
        return Response({
            "error": "No file uploaded"
        }, status=400)

    company, created = Company.objects.get_or_create(
        name=company_name
    )

    file_path = f"uploads/{file.name}"

    with open(file_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    process_csv(
        file_path=file_path,
        company_id=company.id,
        source_type=source_type
    )

    return Response({
        "message": "CSV processed successfully"
    })