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
    #     # qs = self.get_queryset()
    #     # data = qs.filter(pk=pk).values()
    #     qs = self.queryset
    #     title = qs.get(pk=pk).title
    #     status = qs.get(pk=pk).status
    #     id = qs.get(pk=pk).pk
    #     data = {
    #         "id":id,
    #         "title":title,
    #         "status":status
    #     }
    #     print(data)
    #     # serializer = self.get_serializer(data=data)
    #     # serializer.is_valid(raise_exception=True)
    #     # print(serializer.data)
    #     if data:
    #         # print(serializer.data)
    #         return Response(data = data)
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

# when we use same url for retrieve, delete and update endpoints and define different views from them 
# it doesn't work becuase all the required http methods are not allowed for it
# so we can just use different endpoints or define a single view for them all
class TodoDeleteView(generics.DestroyAPIView):
    serializer_class = TodoSerializer
    lookup_field ='pk'
    queryset = TodoItem.objects.all()

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

todo_delete_view = TodoDeleteView.as_view()

class TodoRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    lookup_field ='pk'
    queryset = TodoItem.objects.all()

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        super().put(request, *args, **kwargs)
        return Response(status=204)
    
todo_retrieve_delete_update_view = TodoRetrieveDeleteUpdateView.as_view()