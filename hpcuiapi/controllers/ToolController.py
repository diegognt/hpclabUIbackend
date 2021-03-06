from ..serializers import ToolSerializer
from ..models import Tool
from ..imports import *
from rest_framework.decorators import permission_classes


class ToolsView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)

    @staticmethod
    @permission_classes(IsAuthenticated,)
    def get(request):
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    @permission_classes(IsAdminUser,)
    def post(request):
        serializer = ToolSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ToolDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_object(self, fk):
        try:
            tool = Tool.objects.get(pk=fk)
            self.check_object_permissions(self.request, tool)
            return tool
        except Tool.DoesNotExist:
            raise Http404

    @permission_classes(IsAuthenticated,)
    def get(self, request, fk):
        tool = self.get_object(fk)
        serializer = ToolSerializer(tool)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes(IsAdminUser,)
    def put(self, request, fk):
        tool = self.get_object(fk)
        serializer = ToolSerializer(tool, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes(IsAdminUser,)
    def delete(self, request, fk):
        tool = self.get_object(fk)
        tool.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)