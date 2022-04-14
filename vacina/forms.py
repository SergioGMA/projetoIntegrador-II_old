from django import forms


class Login(forms.Form):
    cpf = forms.CharField(label='CPF', max_length=100)
    password = forms.CharField(
        label='Senha', widget=forms.PasswordInput, max_length=100)


class Profile(forms.Form):
    username = forms.CharField(label='Usuário', max_length=100)
    first_name = forms.CharField(label='Nome', max_length=30)
    last_name = forms.CharField(label='Sobrenome', max_length=30)
    endereco = forms.CharField(label='Endereço', max_length=100)
    telefone = forms.CharField(
        label='Telefone', max_length=100, help_text="ex: (00)000000000")
    email = forms.EmailField(label='Informe seu Email', max_length=254)
    cidade = forms.CharField(label='Cidade', max_length=100)
    Comorbidade = forms.CharField(label='Possui Comorbidade?', max_length=100)
    alergia = forms.CharField(
        label='Apresenta algum tipo de alergia?', max_length=100)
    cpf = forms.CharField(label='CPF', max_length=14,
                          help_text="ex: 000.000.000-00")
    password = forms.CharField(
        label='Nova senha', widget=forms.PasswordInput, max_length=100, help_text="(8 Caracteres Mínimo)")
    confirm = forms.CharField(
        label='Confirmar nova senha', widget=forms.PasswordInput, max_length=100, help_text="(8 Caracteres Mínimo)")
