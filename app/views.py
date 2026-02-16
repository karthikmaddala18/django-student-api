from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student


@api_view(['GET', 'POST'])
def student_list(request):

    # GET request
    if request.method == 'GET':
        students = Student.objects.all()

        data = []
        for student in students:
            data.append({
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "course": student.course
            })

        return Response(data)

    # POST request
    elif request.method == 'POST':
        student = Student.objects.create(
            name=request.data.get("name"),
            age=request.data.get("age"),
            course=request.data.get("course")
        )

        return Response({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": student.course
        }, status=201)