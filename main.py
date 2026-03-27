# coding: utf-8

import sys
from PySide6.QtNetwork import QNetworkInterface, QHostAddress, QHostInfo
from PySide6.QtWidgets import QMainWindow,QListWidget, QGridLayout, QApplication,QLabel, QVBoxLayout, QWidget, QSizePolicy

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuration de la fenêtre
        self.setWindowTitle("Computer Info")
        self.setFixedSize(self.minimumSize())
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Différents labels de nom
        self.hostnameTitle = QLabel("Nom de l'ordinateur:")
        self.domainTitle = QLabel("Domaine:")
        self.ipTitle = QLabel(f"Adresses ip:")

        self.hostnameValue = QLabel(QHostInfo.localHostName())
        self.domainValue = QLabel(QHostInfo.localDomainName())

        # Mise en forme des widgets
        globalWidget = QWidget()
        globalLayout = QVBoxLayout(globalWidget)
        
        computerInfoWidget = QWidget()
        computerInfoLayout = QGridLayout(computerInfoWidget)
        computerInfoLayout.addWidget(self.hostnameTitle,0,0)
        computerInfoLayout.addWidget(self.hostnameValue,0,1)
        computerInfoLayout.addWidget(self.domainTitle,1,0)
        computerInfoLayout.addWidget(self.domainValue,1,1)
        globalLayout.addWidget(computerInfoWidget)

        self.interfacesInfosWidget = QListWidget()
        self.interfacesInfosWidget.setFixedHeight(150)
        self.loadInterfacesInfos()

        globalLayout.addWidget(self.interfacesInfosWidget)
        
        self.setCentralWidget(globalWidget)
        self.show()


    def loadInterfacesInfos(self):
        ip_list = []
        for interface in QNetworkInterface().allInterfaces():
            flags = interface.flags()
            is_loopback = bool(flags & QNetworkInterface.IsLoopBack)
            is_p2p = bool(flags & QNetworkInterface.IsPointToPoint)
            is_running = bool(flags & QNetworkInterface.IsRunning)
            is_up = bool(flags & QNetworkInterface.IsUp)

            if not is_running:
                continue
            if not interface.isValid() or is_loopback or is_p2p:
                continue

            for addr in interface.allAddresses():
                if addr == QHostAddress.LocalHost:
                    continue
                if not addr.toIPv4Address():
                    continue
                ip = addr.toString()
                if ip == '':
                    continue

                if ip not in ip_list:
                    ip_list.append(ip)
                    self.interfacesInfosWidget.addItem(f"Interface: {interface.name()} \nType de connexion: {interface.humanReadableName()}\nAdresse ip: {ip}")
                    break

            print(f"{interface}")
            print(f"{interface.humanReadableName()}")
            print(f"{interface.type()}")
            print(f"{interface.name()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    sys.exit(app.exec())
    