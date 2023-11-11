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

    def create(self, request, *args, **kwargs):
        # super().create(request, *args, **kwargs)
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            create_serializer = TodoCreateSerializer(data= serializer.data)
            if create_serializer.is_valid(raise_exception=True):
                return Response(data= create_serializer.data)
            
    def get(self, request, *args, **kwargs):
        return Response(data = {
            "tasks": TodoSerializer(TodoItem.objects.all(),many = True).data
        })
                    
    
todo_list_create_view = TodoListCreateView.as_view()

class TodoRetrieveView(generics.RetrieveAPIView):
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    queryset = TodoItem.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     pk = kwargs["pk"]
    #     qs = self.get_queryset()
    #     data = qs.filter(pk=pk).values()
    #     print(data)
    #     serializer = self.serializer_class(data=list(data),many = True)
    #     serializer.is_valid(raise_exception=True)
    #     print(serializer.data)
    #     if data:
    #         print(serializer.data)
    #         return Response(data = serializer.data)
    #     else:
    #         return Response(data = {
    #             "error":"There is no task at that id"
    #         })

    
        

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

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

todo_delete_view = TodoDeleteView.as_view()