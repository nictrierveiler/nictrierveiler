from datetime import datetime

def gerar_saudacao():
    hora = datetime.utcnow().hour - 3  # UTC-3 para horário de Brasília
    if hora < 0:
        hora += 24

    if 6 <= hora < 12:
        return "☀️ E aí! Bom dia!"
    elif 12 <= hora < 18:
        return "🌤️ Boa tarde, seja bem-vindo!"
    elif 18 <= hora < 24:
        return "🌙 Boa noite! 🦉"
    else:
        return "🌚 Obrigado por aparecer, mas tá tarde... vai dormir!"

def atualizar_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        conteudo = f.read()

    nova_saudacao = gerar_saudacao()
    conteudo_novo = reescrever_bloco(conteudo, nova_saudacao)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(conteudo_novo)

def reescrever_bloco(conteudo, nova_msg):
    import re
    return re.sub(
        r"<!-- saudacao -->(.*?)<!-- /saudacao -->",
        f"<!-- saudacao -->\n{nova_msg}\n<!-- /saudacao -->",
        conteudo,
        flags=re.DOTALL,
    )

if __name__ == "__main__":
    atualizar_readme()
