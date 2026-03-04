# 🪄 Grammify

**Grammify** é um assistente de escrita desktop moderno e minimalista. Ele utiliza a potência da Inteligência Artificial do Google (Gemini 1.5 Flash) para oferecer correções gramaticais precisas e resumos inteligentes de textos diretamente no seu computador.

---

## 🚀 Funcionalidades

* **Corretor Inteligente**: Corrige erros ortográficos, gramaticais e de pontuação mantendo o sentido original.
* **Resumidor Automático**: Sintetiza textos longos em parágrafos curtos e objetivos.
* **Interface Moderna**: Desenvolvida com `CustomTkinter` para um visual Dark Mode elegante.
* **Processamento em Segundo Plano**: A interface não trava enquanto a IA processa sua solicitação.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* **Google GenAI API**: Modelo `gemini-1.5-flash`.
* **CustomTkinter**: Para a interface gráfica (GUI).
* **Python-dotenv**: Para gerenciamento seguro de chaves de API.

---

## 📦 Como Instalar e Rodar
1. **Clone o repositório:**
   ```bash
   git clone (https://github.com/obrunis/Grammify.git)
   cd Grammify

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

3. **Configure sua API Key:**
-Crie um arquivo .env na raiz do projeto.
-Adicione sua chave do Google AI Studio:
   ```bash
   GEMINI_API_KEY=SUA_CHAVE_AQUI

4. **Execute o aplicativo:**
   ```bash
   python main.py

## ⚖️ Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.   
