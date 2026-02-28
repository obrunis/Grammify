import os
import threading
import customtkinter as ctk
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"
COLOR_PRIMARY = "#00E676"
COLOR_SECONDARY = "#FFFFFF"
COLOR_BG_TEXTBOX = "#1E1E1E"

class GrammifyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._configurar_janela()
        self._inicializar_api()
        self._criar_interface()

    def _configurar_janela(self):
        """Configura as propriedades básicas da janela principal."""
        self.title("Grammify Desktop")
        self.geometry("1100x800")
        self.minsize(900, 700)
        ctk.set_appearance_mode("dark")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def _inicializar_api(self):
        """Configura a conexão com a API do Gemini."""
        if API_KEY:
            try:
                genai.configure(api_key=API_KEY)
                self.model = genai.GenerativeModel(MODEL_NAME)
                print(f"API preparada com o modelo: {MODEL_NAME}")
            except Exception as e:
                print(f"Erro na inicialização da API: {e}")
                self.model = None
        else:
            print("Erro: GEMINI_API_KEY não encontrada no .env")
            self.model = None

    def _criar_interface(self):
        """Cria e organiza todos os elementos visuais da aplicação."""
        
        self.frame_logo = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_logo.grid(row=0, column=0, pady=(50, 20), sticky="n")

        self.lbl_grammi = ctk.CTkLabel(
            self.frame_logo, 
            text="Grammi", 
            font=("Arial", 56, "bold"), 
            text_color=COLOR_SECONDARY
        )
        self.lbl_grammi.grid(row=0, column=0)

        self.lbl_fy = ctk.CTkLabel(
            self.frame_logo, 
            text="fy", 
            font=("Arial", 56, "bold"), 
            text_color=COLOR_PRIMARY
        )
        self.lbl_fy.grid(row=0, column=1)

        self.frame_conteudo = ctk.CTkFrame(self, fg_color="transparent", width=850)
        self.frame_conteudo.grid(row=1, column=0, sticky="nsew", padx=100, pady=10)
        self.frame_conteudo.grid_columnconfigure(0, weight=1)
        self.frame_conteudo.grid_rowconfigure(0, weight=1)
        self.frame_conteudo.grid_propagate(False)

        self.caixa_texto = ctk.CTkTextbox(
            self.frame_conteudo, 
            corner_radius=20, 
            fg_color=COLOR_BG_TEXTBOX, 
            font=("Segoe UI", 16),
            border_width=1,
            border_color="#333333"
        )
        self.caixa_texto.grid(row=0, column=0, sticky="nsew")

        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.grid(row=2, column=0, pady=(20, 50), sticky="s")

        self.btn_corrigir = self._criar_botao("Corretor", self.acao_corrigir, 0)
        self.btn_resumir = self._criar_botao("Resumo", self.acao_resumir, 1)

    def _criar_botao(self, texto, comando, coluna):
        """Helper para criar botões padronizados."""
        btn = ctk.CTkButton(
            self.frame_botoes, 
            text=texto, 
            width=200, 
            height=55, 
            fg_color=COLOR_SECONDARY, 
            text_color="black", 
            hover_color=COLOR_PRIMARY, 
            corner_radius=28, 
            font=("Arial", 15, "bold"),
            command=comando
        )
        btn.grid(row=0, column=coluna, padx=25)
        return btn

    def acao_corrigir(self):
        """Função chamada pelo botão 'Corretor'."""
        prompt = "Corrija este texto, retorne apenas o texto corrigido: "
        self._iniciar_processamento(prompt)

    def acao_resumir(self):
        """Função chamada pelo botão 'Resumo'."""
        prompt = "Resuma este texto de forma clara: "
        self._iniciar_processamento(prompt)

    def _iniciar_processamento(self, prompt_base):
        """Prepara a interface e inicia a thread de IA."""
        texto_entrada = self.caixa_texto.get("1.0", "end-1c").strip()
        if not texto_entrada or not self.model:
            return
        
        self._alternar_estado_botoes("disabled")
        self.caixa_texto.delete("1.0", "end")
        self.caixa_texto.insert("1.0", "🪄 A processar a sua solicitação...")
        
        prompt_completo = f"{prompt_base}{texto_entrada}"
        
        threading.Thread(
            target=self._executar_ia, 
            args=(prompt_completo,), 
            daemon=True
        ).start()

    def _executar_ia(self, prompt):
        """Executa a chamada à API do Gemini."""
        try:
            response = self.model.generate_content(prompt)
            resultado = response.text
            self.after(0, lambda: self._atualizar_ui_sucesso(resultado))
        except Exception as e:
            erro_msg = f"Erro técnico: {str(e)}"
            self.after(0, lambda: self._atualizar_ui_erro(erro_msg))

    def _atualizar_ui_sucesso(self, resultado):
        self.caixa_texto.delete("1.0", "end")
        self.caixa_texto.insert("1.0", resultado)
        self._alternar_estado_botoes("normal")

    def _atualizar_ui_erro(self, mensagem):
        self.caixa_texto.delete("1.0", "end")
        self.caixa_texto.insert("1.0", mensagem)
        self._alternar_estado_botoes("normal")

    def _alternar_estado_botoes(self, estado):
        self.btn_corrigir.configure(state=estado)
        self.btn_resumir.configure(state=estado)

if __name__ == "__main__":
    app = GrammifyApp()
    app.mainloop()