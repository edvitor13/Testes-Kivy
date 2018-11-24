from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

# Alterando cor de fundo para Branco
Window.clearcolor = 1, 1, 1, 1

# Código Kvlang
kvcode = """
<Circulo@Widget>:
    # Largura da linha de carregamento
    largura: 0.1

    # Angulo da linha
    angulo: 0

    canvas.before:
        # Linha cinza de fundo
        Color:
            rgba: .74, .76, .78, 1
        Line:
            width: 10.
            circle:
                (self.center_x, self.center_y, min(self.width, self.height)
                / 2, 0, 360)

        # Linha vermelha de carregamento
        Color:
            rgba: .90, .29, .23, 1
        Line:
            width: root.largura
            circle:
                (self.center_x, self.center_y, min(self.width, self.height)
                / 2, 0, root.angulo)
    Label:
        center: root.center
        text: '[b]'+ str(round((root.angulo * 100) / 360)) + '[/b][size=60]%[/size]'
        color: .49, .54, .55, 1
        font_size: '100sp'
        markup: True

<Tela@Screen>:
    BoxLayout:
        padding: 50
        orientation: 'vertical'
        Circulo:
            id: circulo
        Button:
            text: 'Iniciar'
            font_size: '40sp'
            size_hint: 1, .15
            on_release: root.iniciar()
"""

# Carregando KVCODE
Builder.load_string(kvcode)

class Tela(Screen):
    def __init__(self, **kwargs):
        super(Tela, self).__init__(**kwargs)

    def iniciar(self, *args):
        # Acessando Circulo pelo id
        circulo = self.ids.circulo
        # Alterando largura da linha
        circulo.largura = 10.5

        # Criando Animação
        if (circulo.angulo > 0):
            anim = Animation(angulo=0, duration=4) + Animation(largura=0.1, duration=0.1)
        else:
            anim = Animation(angulo=360, duration=4)

        # Iniciando animação
        anim.start(circulo)

# Adicionando tela ao Screen Manager
sm = ScreenManager()
sm.add_widget(Tela(name='tela'))

class Programa(App):
    def build(self):
        return sm

Programa().run()
