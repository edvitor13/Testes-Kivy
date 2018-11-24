# Geral
import time
import threading

# Kivy
import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

# Código Kvlang
kvcode = """
# Conteúdo do Popup
<ConteudoPopup@BoxLayout>:
	
	BoxLayout:
		orientation: 'vertical'
		size: root.size
		pos: root.pos

		canvas.before:
			Color:
				rgba: 0, 0, 0, .7
			Rectangle:
				size: self.size
				pos: self.pos

		# Apenas para espaçamento
		Widget:

		# Texto
		Label:
			size_hint: 1, None
			height: 100
			text: 'Baixando Vídeo'
			font_size: 40

		# Barra de Progresso
		Label:
			id: barra_progresso
			porcento: 0
			size_hint: 1, None
			height: 100
			text: str(round(self.porcento * 100)) + '%'
			font_size: 30
			canvas.before:
				Color:
					rgba: 0, 1, 0, 1
				Rectangle:
					size: self.size[0] * self.porcento, self.size[1] 
					pos: self.pos

		# Apenas para espaçamento
		Widget:

# Tela Principal
<Tela@Screen>:
	BoxLayout:
		orientation: 'vertical'
		
		# Texto e Número de Donwloads
		BoxLayout:
			orientation: 'vertical'

			# Texto
			Label:
				text: 'Vídeos Baixados:'
				font_size: 50

			# Número de Donwloads
			Label:
				id: numero_downloads
				text: '0'
				font_size: 100

		# Botão
		Button:
			text: 'Baixar'
			on_release: root.bt_baixar()
"""

Builder.load_string(kvcode)

class ConteudoPopup(BoxLayout):
	def atualizar_progresso(self, porcento):
		bp = self.ids.barra_progresso
		bp.porcento = porcento

class Tela(Screen):
	baixando = False

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def bt_baixar(self):
		if (self.baixando == False):
			self.baixando = True

			# Criando Popup
			self.popup = Popup(title='', separator_height=0, size_hint=(1.1, 1.1), auto_dismiss=False, content=ConteudoPopup(), border=(0, 0, 0, 0), background='pixel_transparente.png')

			# Executando método baixar com Thread
			t = threading.Thread(
				target=self.baixar
			)
			t.daemon = True
			t.start()
	
	def baixar(self):
		# Abrindo Popup
		self.popup.open()
		cp = self.popup.content

        # Simulação de Download
		for i in range(100):
			pc = i / 100
			cp.atualizar_progresso(pc)
			time.sleep(0.025)

		# Finalizando
		# Fechando Popup
		self.popup.dismiss()
		
		# Somando +1 ao número de downloads
		nd = self.ids.numero_downloads
		nd.text = str(int(nd.text) + 1)
		
		# Alterar "self.baixando" para False
		self.baixando = False

# Gerenciador de Telas
sm = ScreenManager()
sm.add_widget(Tela(name='tela'))

class Programa(App):
	def build(self):
		return sm

Programa().run()
