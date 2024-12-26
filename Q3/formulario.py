nome: str = input("Informe seu nome: ");
anoAtual: int = 2025;

try:
    ano: int = int(input("Informe o ano em que você nasceu (1922 até 2024): "));
except ValueError:
    print("Ano inválido Por favor, informe um valor numérico.");
    exit();

if ano < 1922 or ano > 2024:
    print("Erro! Informe um ano dentro do escopo (1922 até 2024).");
    exit();

anos = anoAtual - ano;
print(f"Olá {nome}, você tera {anos} anos em {anoAtual}.");
