#aula 340-341-342-343

"""
QMainWindow e CentralWidget
-> QApplication (app)
  ->QmainWindow (Window ->setCentralWidget)
    -> CentralWidget (central_widget)
        ->Layout (layout)
            ->widget 1 (botao1)
            ->widget 2 (botao2)
            ->widget 3 (botao3)
  -> Show
->exec

"""

import sys
from PySide6.QtWidgets import QApplication , QPushButton, QWidget, QVBoxLayout , QHBoxLayout, QGridLayout, QMainWindow

Janela = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela de estudos')

botao1 = QPushButton('Nome do Botão')
botao1.setStyleSheet('font-size 40px')
botao1.show() #adiciona o widget na hierarquia e exibe na janela

botao2 = QPushButton('Botão 2 ')
botao2.setStyleSheet('font-size: 40px; ')
botao2.show()

botao3 = QPushButton('Botão 3 ')
botao3.setStyleSheet('font-size: 40px; ')
botao3.show()


layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1,1,1,1,1) #linha, coluna, expanção linha, expanção coluna
layout.addWidget(botao2,1,2,1,1)
layout.addWidget(botao3,3,1,1,2)

#statusbar
status_bar = window.statusBar()
status_bar.showMessage('Aqui mostra a mensagem de estatus')


#slot para usar como exemplo de ação ao clicar no menubar primeira ação
def slot_exemple():
    print("William Souza")

def slot_exemple2(status_bar):
    status_bar.showMessage('A segunda ação foi executada')

#menubar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Ações')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(slot_exemple)
segunda_acao = primeiro_menu.addAction('Seguda Ação')
segunda_acao.triggered.connect( lambda : slot_exemple2(status_bar))



window.show()

Janela.exec() #executa o loop da aplicação
