from PyQt6.QtWidgets import (QLabel, QWidget, QPushButton,
                             QVBoxLayout, QDialog, QTextEdit, QInputDialog, QMessageBox)
from PyQt6.QtGui import QMovie, QPalette, QColor, QPixmap
from PyQt6.QtCore import Qt

from utils import darklinks
import utils.phonenumber_search as pn
from utils.imports import *
from utils import darkforgui


class AboutWindow(QDialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About SHIROMU")
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(0, 0, 0))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.text_edit = QTextEdit(self)
        self.text_edit.setText(text)
        self.text_edit.setReadOnly(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)
        self.resize(600, 400)


class InstagramInfoDialog(QMessageBox):
    def __init__(self, info):
        super().__init__()
        self.setWindowTitle("Информация об Instagram профиле")
        self.setText(info)
        self.addButton(QMessageBox.StandardButton.Ok)


class DoxbinSearchh(QMessageBox):
    def __init__(self, info):
        super().__init__()
        self.setWindowTitle('DOXBIN INFO')
        self.setText(info)
        self.addButton(QMessageBox.StandardButton.Ok)


class DarkLinkss(QWidget):
    def __init__(self, content):
        super().__init__()
        self.setWindowTitle("Darklist")
        self.text_edit = QTextEdit(self)
        self.text_edit.setHtml(content)
        self.text_edit.setReadOnly(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)
        self.resize(600, 400)


class zabilhui(QWidget):
    def __init__(self, content):
        super().__init__()
        self.setWindowTitle("LATER...")
        self.text_edit = QTextEdit(self)
        self.text_edit.setHtml(content)
        self.text_edit.setReadOnly(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)
        self.resize(600, 400)


class bd_search(QWidget):
    def __init__(self, content):
        super().__init__()
        self.setWindowTitle("Результаты поиска")
        self.text_edit = QTextEdit(self)
        self.text_edit.setHtml(content)
        self.text_edit.setReadOnly(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)
        self.resize(600, 400)


# бля функции для кнопк


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.namer4 = None
        self.namer3 = None
        self.namer2 = None
        self.namer1 = None
        self.namer = None
        self.obvodka14 = None
        self.obvodka13 = None
        self.obvodka12 = None
        self.obvodka11 = None
        self.obvodka10 = None
        self.obvodka9 = None
        self.obvodka8 = None
        self.obvodka7 = None
        self.obvodka6 = None
        self.obvodka5 = None
        self.obvodka4 = None
        self.obvodka3 = None
        self.obvodka2 = None
        self.obvodka1 = None
        self.pixmap = None
        self.overlay_label = None
        self.button24 = None
        self.button23 = None
        self.button22 = None
        self.button20 = None
        self.button19 = None
        self.button18 = None
        self.button12 = None
        self.button11 = None
        self.button10 = None
        self.button9 = None
        self.button25 = None
        self.button13 = None
        self.button8 = None
        self.button7 = None
        self.button6 = None
        self.button5 = None
        self.button4 = None
        self.button3 = None
        self.about_window = None
        self.button2 = None
        self.stacked_layout = None
        self.button = None
        self.label = None
        self.background = None
        self.movie = None
        self.initilization()

    def initilization(self):
        self.setGeometry(600, 200, 800, 600)
        self.setWindowTitle('SHIROMU')
        self.setupMainWindow()
        self.resize(600, 800)
        self.show()

    def setupMainWindow(self):
        self.background = QLabel(self)
        self.background.setGeometry(0, 0, self.width(), self.height())

        try:
            self.movie = QMovie("main.gif")
            self.background.setMovie(self.movie)
            self.movie.start()
        except:
            print(f"Ошибка, пишите sh1ro")
            self.background.setText("Ошибка, пишите sh1ro")

        self.background.setScaledContents(True)

        self.overlay_label = QLabel(self)

        self.pixmap = QPixmap("SHIROMU.png")
        self.overlay_label.setPixmap(self.pixmap)
        self.overlay_label.setScaledContents(True)
        self.overlay_label.setGeometry(1000, 0, self.width(), self.height())

        self.overlay_label.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.overlay_label.raise_()

        # обводка
        self.label = QLabel('________________', self)
        self.label.move(88, 80)
        self.label.setStyleSheet("""
                            QLabel {
                                font-size: 100px;
                                font-weight: bold;
                                font-family: "Roboto"; 
                                color: black; 
                                background-color: None
                            }
                        """)

        self.label.raise_()

        self.obvodka1 = QLabel('|\n|\n|\n|\n|', self)
        self.obvodka1.move(80, 150)
        self.obvodka1.setStyleSheet("""
                            QLabel {
                                font-size: 100px;
                                font-weight: bold;
                                font-family: "Roboto"; 
                                color: black; 
                                background-color: None
                            }
                        """

                                    )
        self.obvodka1.raise_()

        self.obvodka2 = QLabel('________________', self)
        self.obvodka2.move(85, 640)
        self.obvodka2.setStyleSheet("""
                                    QLabel {
                                        font-size: 100px;
                                        font-weight: bold;
                                        font-family: "Roboto"; 
                                        color: black; 
                                        background-color: None
                                    }
                                """)

        self.obvodka2.raise_()

        self.obvodka3 = QLabel('|\n|\n|\n|\n|', self)
        self.obvodka3.move(800, 150)
        self.obvodka3.setStyleSheet("""
                                    QLabel {
                                        font-size: 100px;
                                        font-weight: bold;
                                        font-family: "Roboto"; 
                                        color: black; 
                                        background-color: None
                                    }
                                """

                                    )
        self.obvodka3.raise_()

        self.obvodka4 = QLabel('________________', self)
        self.obvodka4.move(85, 790)
        self.obvodka4.setStyleSheet("""
                                            QLabel {
                                                font-size: 100px;
                                                font-weight: bold;
                                                font-family: "Roboto"; 
                                                color: black; 
                                                background-color: None
                                            }
                                        """)

        self.obvodka4.raise_()

        self.obvodka5 = QLabel('|\n|\n|\n|', self)
        self.obvodka5.move(800, 870)
        self.obvodka5.setStyleSheet("""
                                            QLabel {
                                                font-size: 100px;
                                                font-weight: bold;
                                                font-family: "Roboto"; 
                                                color: black; 
                                                background-color: None
                                            }
                                        """

                                    )
        self.obvodka5.raise_()

        self.obvodka6 = QLabel('|\n|\n|\n|', self)
        self.obvodka6.move(80, 870)
        self.obvodka6.setStyleSheet("""
                                                    QLabel {
                                                        font-size: 100px;
                                                        font-weight: bold;
                                                        font-family: "Roboto"; 
                                                        color: black; 
                                                        background-color: None
                                                    }
                                                """

                                    )
        self.obvodka6.raise_()

        self.obvodka7 = QLabel('________________', self)
        self.obvodka7.move(90, 1240)
        self.obvodka7.setStyleSheet("""
                                        QLabel {
                                            font-size: 100px;
                                            font-weight: bold;
                                            font-family: "Roboto"; 
                                            color: black; 
                                            background-color: None
                                        }
                                    """)

        self.obvodka7.raise_()

        self.obvodka8 = QLabel('________', self)
        self.obvodka8.move(1060, 490)
        self.obvodka8.setStyleSheet("""
                                     QLabel {
                                         font-size: 100px;
                                         font-weight: bold;
                                         font-family: "Roboto"; 
                                         color: black; 
                                         background-color: None
                                     }
                                    """)

        self.obvodka8.raise_()

        self.obvodka9 = QLabel('|\n|\n|', self)
        self.obvodka9.move(1050, 570)
        self.obvodka9.setStyleSheet("""
                                                            QLabel {
                                                                font-size: 100px;
                                                                font-weight: bold;
                                                                font-family: "Roboto"; 
                                                                color: black; 
                                                                background-color: None
                                                            }
                                                        """

                                    )
        self.obvodka9.raise_()

        self.obvodka10 = QLabel('|\n|\n|', self)
        self.obvodka10.move(1410, 570)
        self.obvodka10.setStyleSheet("""
                                         QLabel {
                                             font-size: 100px;
                                             font-weight: bold;
                                             font-family: "Roboto"; 
                                             color: black; 
                                             background-color: None
                                         }
                                    """)

        self.obvodka10.raise_()

        self.obvodka11 = QLabel('________', self)
        self.obvodka11.move(1060, 820)
        self.obvodka11.setStyleSheet("""
                                             QLabel {
                                                 font-size: 100px;
                                                 font-weight: bold;
                                                 font-family: "Roboto"; 
                                                 color: black; 
                                                 background-color: None
                                             }
                                            """)

        self.obvodka11.raise_()

        self.obvodka12 = QLabel('___________________', self)
        self.obvodka12.move(1780, 100)
        self.obvodka12.setStyleSheet("""
                                        QLabel {
                                            font-size: 100px;
                                            font-weight: bold;
                                            font-family: "Roboto"; 
                                            color: black; 
                                            background-color: None
                                        }
                                    """)
        self.obvodka12.raise_()

        self.obvodka13 = QLabel('|\n|\n|\n|\n|', self)
        self.obvodka13.move(1770, 170)
        self.obvodka13.setStyleSheet("""
                                                 QLabel {
                                                     font-size: 100px;
                                                     font-weight: bold;
                                                     font-family: "Roboto"; 
                                                     color: black; 
                                                     background-color: None
                                                 }
                                            """)

        self.obvodka13.raise_()

        self.obvodka14 = QLabel('___________________', self)
        self.obvodka14.move(1780, 660)
        self.obvodka14.setStyleSheet("""
                                                QLabel {
                                                    font-size: 100px;
                                                    font-weight: bold;
                                                    font-family: "Roboto"; 
                                                    color: black; 
                                                    background-color: None
                                                }
                                            """)
        self.obvodka14.raise_()

        self.namer = QLabel('OSINT', self)
        self.namer.move(300, 80)
        self.namer.setStyleSheet("""
                                                        QLabel {
                                                            font-size: 100px;
                                                            font-weight: bold;
                                                            font-family: "Roboto"; 
                                                            color: blue; 
                                                            background-color: None
                                                        }
                                                    """)
        self.namer.raise_()

        self.namer1 = QLabel('VK', self)
        self.namer1.move(400, 790)
        self.namer1.setStyleSheet("""
                                                                QLabel {
                                                                    font-size: 100px;
                                                                    font-weight: bold;
                                                                    font-family: "Roboto"; 
                                                                    color: blue; 
                                                                    background-color: None
                                                                }
                                                            """)
        self.namer1.raise_()

        self.namer2 = QLabel('NETWORK', self)
        self.namer2.move(1000, 488)
        self.namer2.setStyleSheet("""
                                     QLabel {
                                         font-size: 100px;
                                         font-weight: bold;
                                         font-family: "Roboto"; 
                                         color: blue; 
                                         background-color: None
                                     }
                                     """)
        self.namer2.raise_()

        self.namer3 = QLabel('УРОН', self)
        self.namer3.move(1800, 100)
        self.namer3.setStyleSheet("""
                                     QLabel {
                                         font-size: 100px;
                                         font-weight: bold;
                                         font-family: "Roboto"; 
                                         color: blue; 
                                         background-color: None
                                     }
                                    """)
        self.namer3.raise_()

        self.namer4 = QLabel('Полезное', self)
        self.namer4.move(2200, 118)
        self.namer4.setStyleSheet("""
                                             QLabel {
                                                 font-size: 80px;
                                                 font-weight: bold;
                                                 font-family: "Roboto"; 
                                                 color: blue; 
                                                 background-color: None
                                             }
                                            """)
        self.namer4.raise_()

        # бля кнопки
        self.button = QPushButton('Информация о софте', self)
        self.button.setGeometry(100, 200, 300, 50)
        self.button.setStyleSheet("""
                    QPushButton {
                        font-size: 20px;
                        font-weight: bold;
                        font-family: "Roboto"; 
                        color: Black; 
                        background-color: pink
                    }
                """)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

        self.button2 = QPushButton('Поиск по номеру телефона', self)
        self.button2.setGeometry(500, 200, 300, 50)
        self.button2.setStyleSheet("""
                    QPushButton {
                        font-size: 20px;
                        font-weight: bold;
                        font-family: "Roboto"; 
                        color: Black; 
                        background-color: pink
                    }
                """)

        self.button2.setCheckable(True)
        self.button2.clicked.connect(self.phn_search)

        self.button3 = QPushButton('Поиск по документам', self)
        self.button3.setGeometry(100, 400, 300, 50)
        self.button3.setStyleSheet("""
                    QPushButton {
                        font-size: 20px;
                        font-weight: bold;
                        font-family: "Roboto"; 
                        color: Black; 
                        background-color: pink
                    }
                """)
        self.button3.clicked.connect(self.document_search)

        self.button4 = QPushButton('Поиск по адресу', self)
        self.button4.setGeometry(500, 400, 300, 50)
        self.button4.setStyleSheet("""
                            QPushButton {
                                font-size: 20px;
                                font-weight: bold;
                                font-family: "Roboto"; 
                                color: Black; 
                                background-color: pink
                            }
                        """)
        self.button4.clicked.connect(self.adress_search)

        self.button5 = QPushButton('Поиск по Instagram', self)
        self.button5.setGeometry(100, 300, 300, 50)
        self.button5.setStyleSheet("""
                                    QPushButton {
                                        font-size: 20px;
                                        font-weight: bold;
                                        font-family: "Roboto"; 
                                        color: Black; 
                                        background-color: pink
                                    }
                                """)
        self.button5.clicked.connect(self.insta_search)

        self.button6 = QPushButton('Поиск на DOXBIN', self)
        self.button6.setGeometry(500, 300, 300, 50)
        self.button6.setStyleSheet("""
                                            QPushButton {
                                                font-size: 20px;
                                                font-weight: bold;
                                                font-family: "Roboto"; 
                                                color: Black; 
                                                background-color: pink
                                            }
                                        """)
        self.button6.clicked.connect(self.doxbin_srch)

        self.button7 = QPushButton('Полезные форумы/ссылки', self)
        self.button7.setGeometry(100, 500, 300, 50)
        self.button7.setStyleSheet("""
                                                    QPushButton {
                                                        font-size: 20px;
                                                        font-weight: bold;
                                                        font-family: "Roboto"; 
                                                        color: Black; 
                                                        background-color: pink
                                                    }
                                                """)
        self.button7.clicked.connect(self.darknet_links)

        self.button8 = QPushButton('Создание итоговой пасты', self)
        self.button8.setGeometry(500, 500, 300, 50)
        self.button8.setStyleSheet("""
                                            QPushButton {
                                                font-size: 20px;
                                                font-weight: bold;
                                                font-family: "Roboto"; 
                                                color: Black; 
                                                background-color: pink
                                            }
                                    """)
        self.button8.clicked.connect(self.sozd_pasti)

        self.button9 = QPushButton('Поиск по ФИО', self)
        self.button9.setGeometry(100, 600, 300, 50)
        self.button9.setStyleSheet("""
                                                    QPushButton {
                                                        font-size: 20px;
                                                        font-weight: bold;
                                                        font-family: "Roboto"; 
                                                        color: Black; 
                                                        background-color: pink
                                                    }
                                            """)
        self.button9.clicked.connect(self.fio_search)

        self.button10 = QPushButton('Поиск по Никнейму', self)
        self.button10.setGeometry(500, 600, 300, 50)
        self.button10.setStyleSheet("""
                                                            QPushButton {
                                                                font-size: 20px;
                                                                font-weight: bold;
                                                                font-family: "Roboto"; 
                                                                color: Black; 
                                                                background-color: pink
                                                            }
                                                    """)
        self.button10.clicked.connect(self.nick_srch)

        self.button11 = QPushButton('IP-SCANNER', self)
        self.button11.setGeometry(1100, 600, 300, 50)
        self.button11.setStyleSheet("""
                                                                    QPushButton {
                                                                        font-size: 20px;
                                                                        font-weight: bold;
                                                                        font-family: "Roboto"; 
                                                                        color: Black; 
                                                                        background-color: pink
                                                                    }
                                                            """)
        self.button11.clicked.connect(self.ip_scan)

        self.button12 = QPushButton('Узнать IP домена', self)
        self.button12.setGeometry(1100, 700, 300, 50)
        self.button12.setStyleSheet("""
                                                                            QPushButton {
                                                                                font-size: 20px;
                                                                                font-weight: bold;
                                                                                font-family: "Roboto"; 
                                                                                color: Black; 
                                                                                background-color: pink
                                                                            }
                                                                    """)
        self.button12.clicked.connect(self.site_scanner)

        self.button13 = QPushButton('Сканер портов', self)
        self.button13.setGeometry(1100, 800, 300, 50)
        self.button13.setStyleSheet("""
                                                                                    QPushButton {
                                                                                        font-size: 20px;
                                                                                        font-weight: bold;
                                                                                        font-family: "Roboto"; 
                                                                                        color: Black; 
                                                                                        background-color: pink
                                                                                    }
                                                                            """)
        self.button13.clicked.connect(self.port_scanner)

        self.button14 = QPushButton('Спамер', self)
        self.button14.setGeometry(1800, 200, 300, 50)
        self.button14.setStyleSheet("""
                                                                                            QPushButton {
                                                                                                font-size: 20px;
                                                                                                font-weight: bold;
                                                                                                font-family: "Roboto"; 
                                                                                                color: Black; 
                                                                                                background-color: pink
                                                                                            }
                                                                                    """)
        self.button14.clicked.connect(self.spam_chat_attack)

        self.button15 = QPushButton('SMS-BOMBER', self)
        self.button15.setGeometry(1800, 300, 300, 50)
        self.button15.setStyleSheet("""
                                         QPushButton {
                                             font-size: 20px;
                                             font-weight: bold;
                                             font-family: "Roboto"; 
                                             color: Black; 
                                             background-color: pink
                                         }
                                    """)
        self.button15.clicked.connect(self.sms_boomb)

        self.button16 = QPushButton('Снос тг-аккаунта', self)
        self.button16.setGeometry(1800, 400, 300, 50)
        self.button16.setStyleSheet("""
                                                 QPushButton {
                                                     font-size: 20px;
                                                     font-weight: bold;
                                                     font-family: "Roboto"; 
                                                     color: Black; 
                                                     background-color: pink
                                                 }
                                            """)
        self.button16.clicked.connect(self.tgacc_snoska)

        self.button17 = QPushButton('Снос через сайт', self)
        self.button17.setGeometry(1800, 500, 300, 50)
        self.button17.setStyleSheet("""
                                                         QPushButton {
                                                             font-size: 20px;
                                                             font-weight: bold;
                                                             font-family: "Roboto"; 
                                                             color: Black; 
                                                             background-color: pink
                                                         }
                                                    """)
        self.button17.clicked.connect(self.tg_site_snos)

        self.button18 = QPushButton('Мануалы', self)
        self.button18.setGeometry(1800, 600, 300, 50)
        self.button18.setStyleSheet("""
                                         QPushButton {
                                             font-size: 20px;
                                             font-weight: bold;
                                             font-family: "Roboto"; 
                                             color: Black; 
                                             background-color: pink
                                         }
                                    """)
        self.button18.clicked.connect(self.manuals)

        self.button19 = QPushButton('Создание фейк-личности', self)
        self.button19.setGeometry(2250, 200, 300, 50)
        self.button19.setStyleSheet("""
                                                 QPushButton {
                                                     font-size: 20px;
                                                     font-weight: bold;
                                                     font-family: "Roboto"; 
                                                     color: Black; 
                                                     background-color: pink
                                                 }
                                            """)
        self.button19.clicked.connect(self.create_fake_person)

        self.button20 = QPushButton('Временная анонимная почта', self)
        self.button20.setGeometry(2250, 300, 310, 50)
        self.button20.setStyleSheet("""
                                                         QPushButton {
                                                             font-size: 20px;
                                                             font-weight: bold;
                                                             font-family: "Roboto"; 
                                                             color: Black; 
                                                             background-color: pink
                                                         }
                                                    """)
        self.button20.clicked.connect(self.crt_fake_mail)

        self.button21 = QPushButton('Проверка онлайна и устройства', self)
        self.button21.setGeometry(100, 900, 310, 50)
        self.button21.setStyleSheet("""
                                        QPushButton {
                                            font-size: 20px;
                                            font-weight: bold;
                                            font-family: "Roboto"; 
                                            color: Black; 
                                            background-color: pink
                                        }
                                                            """)
        self.button21.clicked.connect(self.proverka_ustr)

        self.button22 = QPushButton('id групп всех пользователя', self)
        self.button22.setGeometry(100, 1000, 310, 50)
        self.button22.setStyleSheet("""
                                                QPushButton {
                                                    font-size: 20px;
                                                    font-weight: bold;
                                                    font-family: "Roboto"; 
                                                    color: Black; 
                                                    background-color: pink
                                                }
                                                                    """)
        self.button22.clicked.connect(self.parce_vk_group)

        self.button22 = QPushButton('Все фотографии аккаунта', self)
        self.button22.setGeometry(100, 1100, 310, 50)
        self.button22.setStyleSheet("""
                                        QPushButton {
                                            font-size: 20px;
                                            font-weight: bold;
                                            font-family: "Roboto"; 
                                            color: Black; 
                                            background-color: pink
                                        }
                                                                            """)
        self.button22.clicked.connect(self.parce_vk_photo)

        self.button23 = QPushButton('Все друзья жертвы', self)
        self.button23.setGeometry(100, 1200, 310, 50)
        self.button23.setStyleSheet("""
                                                QPushButton {
                                                    font-size: 20px;
                                                    font-weight: bold;
                                                    font-family: "Roboto"; 
                                                    color: Black; 
                                                    background-color: pink
                                                }
                                                                                    """)
        self.button23.clicked.connect(self.id_kents_acc)

        self.button24 = QPushButton('Все комментарии жертвы', self)
        self.button24.setGeometry(500, 900, 310, 50)
        self.button24.setStyleSheet("""
                                        QPushButton {
                                            font-size: 20px;
                                            font-weight: bold;
                                            font-family: "Roboto"; 
                                            color: Black; 
                                            background-color: pink
                                        }
                                    """)
        self.button24.clicked.connect(self.target_comments)

        self.button25 = QPushButton('Поиск номера телефона', self)
        self.button25.setGeometry(500, 1000, 310, 50)
        self.button25.setStyleSheet("""
                                                QPushButton {
                                                    font-size: 20px;
                                                    font-weight: bold;
                                                    font-family: "Roboto"; 
                                                    color: Black; 
                                                    background-color: pink
                                                }
                                            """)
        self.button25.clicked.connect(self.phn_vk_srch)

    # бля еще функции для кнопк
    def the_button_was_clicked(self):
        try:
            with open("aboutshiromu.txt", "r", encoding="utf-8") as file:
                content = file.read()
                self.about_window = AboutWindow(content, self)
                self.about_window.show()
        except FileNotFoundError:
            print("Ошибка, пишите sh1ro")

    def phn_search(self):
        phone_number, ok = QInputDialog.getText(self, "Введите номер телефона",
                                                "Введите номер телефона в формате +79304669445:")

        if ok:
            info = (pn.for_windows(phone_number=phone_number))
            try:
                QMessageBox.information(self, "Информация о номере", info, QMessageBox.StandardButton.Ok)
            except:
                print(QMessageBox.critical(self))

    def insta_search(self):
        username, ok = QInputDialog.getText(self, "Введите username",
                                            "Введите username Instagram:")

        if ok and username:
            try:
                il = instaloader.Instaloader()
                profile = instaloader.Profile.from_username(il.context, username=username)

                info = (
                    f'Информация о профиле: {username}\n'
                    f'Биография: {profile.biography}\n'
                    f'Постов: {profile.mediacount}\n'
                    f'Подписчиков: {profile.followers}'
                )

                dialog = InstagramInfoDialog(info)
                dialog.exec()

            except instaloader.exceptions.ProfileNotExistsException:
                QMessageBox.critical(self, "Ошибка", "Пользователь не найден")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Произошла ошибка, включите vpn или пишите sh1ro")

    def doxbin_srch(self):
        while True:
            name_pasta, ok = QInputDialog.getText(self, "Поиск на Doxbin",
                                                  "Введите информацию о цели (без пробелов и подчеркиваний):")

            if ok:
                name_pasta = name_pasta.replace('_', '').replace(' ', '')

                if not name_pasta:
                    QMessageBox.warning(self, "Предупреждение", "Некорректно введена информация...")
                    continue

                url = f'https://doxbin.net/upload/{name_pasta}'
                try:
                    response = requests.get(url)
                    if response.status_code == 404:
                        QMessageBox.information(self, "Информация", "Ничего не найдено")

                    else:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        dox = soup.find_all('div')
                        info = ""
                        for text1 in dox:
                            info += text1.text + "\n"

                        dialog = DoxbinSearchh(info)
                        dialog.exec()
                    break
                except requests.exceptions.RequestException as e:
                    QMessageBox.critical(self, "Ошибка", f"Ошибка запроса {e}")
                    break
                except Exception as e:
                    QMessageBox.critical(self, "Ошибка", f"Произошла ошибка {e}")
                    break
            else:
                break

    def darknet_links(self):
        content = darkforgui.print_darklist(darklinks.darklist)
        self.about_window = DarkLinkss(content)
        self.about_window.show()

    def adress_search(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def document_search(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = bd_search(content)
        self.about_window.show()

    def sozd_pasti(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def fio_search(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def nick_srch(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def ip_scan(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def site_scanner(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def port_scanner(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def spam_chat_attack(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def sms_boomb(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def tgacc_snoska(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def tg_site_snos(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def manuals(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def create_fake_person(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def crt_fake_mail(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def proverka_ustr(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def parce_vk_group(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def parce_vk_photo(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def id_kents_acc(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def target_comments(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def phn_vk_srch(self):
        content = 'Данная функция доступна в консольной версии приложения и появится тут позже, следите за обновлениями'
        self.about_window = zabilhui(content)
        self.about_window.show()

    def resizeEvent(self, event):
        self.background.setGeometry(0, 0, self.width(), self.height())
        QWidget.resizeEvent(self, event)
        self.label.raise_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Widget()
    main_window.show()
    sys.exit(app.exec())

#+79304669445
