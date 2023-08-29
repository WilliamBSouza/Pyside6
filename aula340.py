#aula 340-341-


from PySide6.QtWidgets import QApplication , QPushButton, QWidget, QVBoxLayout , QHBoxLayout, QGridLayout
import sys

Janela = QApplication(sys.argv)

botao = QPushButton('Nome do Botão')
botao.setStyleSheet('font-size 20px')
botao.show() #adiciona o widget na hierarquia e exibe na janela

botao2 = QPushButton('Botão 2 ')
botao.setStyleSheet('font-size: 40px; ')
botao2.show()

botao3 = QPushButton('Botão 3 ')
botao.setStyleSheet('font-size: 40px; ')
botao2.show()

central_widget = QWidget()
layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao,1,1,1,1)
layout.addWidget(botao2,1,2,1,1)
layout.addWidget(botao3,3,1,1,2)

central_widget.show()#Central Widget entra na hierarquia e mostra na janela

Janela.exec() #executa o loop da aplicação
