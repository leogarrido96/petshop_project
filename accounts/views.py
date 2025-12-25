from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer
from .forms import CustomUserCreationForm

User = get_user_model()


class SignUpView(CreateView):
    """
    View para permitir que novos clientes se cadastrem no hotsite.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        # Apenas administradores podem listar todos os usuários
        if self.action == 'list':
            return [permissions.IsAdminUser()]
        # Outras ações exigem estar logado
        return [permissions.IsAuthenticated()]

    @action(detail=False, methods=['get', 'put', 'patch'])
    def me(self, request):
        """
        Endpoint: /api/v1/accounts/me/
        Retorna ou atualiza os dados do usuário que está logado.
        """
        serializer = self.get_serializer(request.user)
        if request.method == 'GET':
            return Response(serializer.data)

        # Para atualizações (PUT/PATCH)
        serializer = self.get_serializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
