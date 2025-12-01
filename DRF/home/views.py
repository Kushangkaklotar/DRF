from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.serializers import *

@api_view(['GET', 'POST'])
def hello_world(request):
    course = {
            'course_name' : 'Python',
            'learn' : ['flask', 'fast', 'DRF', 'Pandas', 'matplotlib'],
            'course_provider' : 'Self',
            'course_price': 499
        }

    if request.method == 'POST':
        print('*******************')
        print('HIT A POST METHOD')
        print('*******************')
        return Response(course)

    elif request.method == 'GET':
        print('*******************')
        print('HIT A GET METHOD')
        print('*******************')
        return Response(course)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        peopleData = Person.objects.all()
        peopleSerializer = PeopleSerializer(peopleData, many = True)
        return Response(peopleSerializer.data)

    elif request.method == 'POST':
        data = request.data
        ser = PeopleSerializer(data = data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        
        return Response(ser.errors)

    elif request.method == "PUT":
        person = Person.objects.get(id=request.data['id'])
        peopleSerializer = PeopleSerializer(person, data = request.data)
        if peopleSerializer.is_valid():
            peopleSerializer.save()
            return Response(peopleSerializer.data)
        
        return Response(peopleSerializer.errors)
    
    elif request.method == "PATCH":
        person = Person.objects.get(id=request.data['id'])
        peopleSerializer = PeopleSerializer(person, data = request.data, partial = True)
        if peopleSerializer.is_valid():
            peopleSerializer.save()
            return Response(peopleSerializer.data)
        
        return Response(peopleSerializer.errors)
    
    elif request.method == "DELETE":
        person = Person.objects.get(id=request.data['id'])
        person.delete()
        return Response({'message' : 'Person deleted successfully!'})