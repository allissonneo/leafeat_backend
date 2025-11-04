from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate

class UsuarioList(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def login_view(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Método inválido.'}, status=405)

    try:
        data = json.loads(request.body)
        email = data.get('email')
        senha = data.get('senha')

        if not email or not senha:
            return JsonResponse({'success': False, 'message': 'Preencha todos os campos.'}, status=400)

        user = authenticate(request, username=email, password=senha)

        if user is not None:
            return JsonResponse({
                'success': True,
                'id': user.id,
                'email': user.email,
                'nome_completo': user.nome_completo or '',
            })
        else:
            return JsonResponse({'success': False, 'message': 'Email ou senha incorretos.'}, status=401)

    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Erro interno: {str(e)}'}, status=500)
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def registrar_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')

        if not nome or not email or not senha:
            return JsonResponse({'success': False, 'message': 'Preencha todos os campos.'})

        User = get_user_model()

        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Este email já está cadastrado.'})

        user = User(email=email, nome_completo=nome)
        user.set_password(senha)  # 🔒 importante: salva a senha criptografada
        user.save()

        return JsonResponse({'success': True, 'message': 'Usuário cadastrado com sucesso!'})
    
    return JsonResponse({'success': False, 'message': 'Método inválido.'})