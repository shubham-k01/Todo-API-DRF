from rest_framework import generics
from rest_framework.response import Response
from .serializers import TodoSerializer, TodoCreateSerializer
from .models import TodoItem

class TodoListView(generics.ListAPIView):
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    
todo_list_view  = TodoListView.as_view()

class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = TodoItem.objects.all()

    # doesn't work because create is called when we are creating a new object and at the time of creation of a new object id is not present . It is later added by the database
    def create(self, request, *args, **kwargs):
        # super().create(request, *args, **kwargs)
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            create_serializer = TodoCreateSerializer(data= serializer.data)
            if create_serializer.is_valid(raise_exception=True):
                return Response(data= create_serializer.data)

    
    # def perform_create(self, serializer):
    #     super().perform_create(serializer)
    #     serializer.save()
    #     print(serializer.data)
    #     print(type(serializer.data))
    #     serialized = TodoCreateSerializer(data = serializer.data)
    #     if serialized.is_valid(raise_exception=True):
    #         print(serialized.data)
    #         return Response(data={"ig":"2"})
    #     else:
    #         print("Hi")
    #         return Response(data={id:2})
    
    
            

        
    
todo_list_create_view = TodoListCreateView.as_view()

class TodoRetrieveView(generics.RetrieveAPIView):
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    queryset = TodoItem.objects.all()

todo_retrieve_view = TodoRetrieveView.as_view()

class TodoUpdateView(generics.UpdateAPIView):
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    queryset = TodoItem.objects.all()

todo_update_view = TodoUpdateView.as_view()

class TodoDeleteView(generics.DestroyAPIView):
    serializer_class = TodoSerializer
    lookup_field ='pk'
    queryset = TodoItem.objects.all()

todo_delete_view = TodoDeleteView.as_view()