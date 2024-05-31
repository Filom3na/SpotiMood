from rest_framework import generics

class ObjectOwnerView(generics.GenericAPIView):
    # Custom view logic
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)