from django import forms

class Formulario(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login", 
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Ex: João Vitor"
            }
        )
    )

    senha = forms.CharField(
        label="Senha", 
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder":"Digite sua senha"
            }
        
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro", 
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Ex: João Vitor"
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Ex: joaosilva@email.com"
        }

        )
    )

    senha_1 = forms.CharField(
       label="Senha", 
       required=True,
       max_length=100,
       widget=forms.PasswordInput(
           attrs={
               "class": "form-control",
               "placeholder":"Digite sua senha"
           }
       
       )
   )
    senha_2 = forms.CharField(
       label="Senha", 
       required=True,
       max_length=100,
       widget=forms.PasswordInput(
           attrs={
               "class": "form-control",
               "placeholder":"Digite sua senha novamente"
           }
       
       )
   )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()  # Remove espaços no início e no fim
            if ' ' in nome:  # Verifica se ainda há espaços em qualquer parte do nome
                raise forms.ValidationError('Não é possível inserir espaços dentro do campo nome de cadastro')
            else:
                return nome