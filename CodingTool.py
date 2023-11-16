#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : auto
@File           : CodingTool.py
@Software       : PyCharm
@Time           : 2023-02-02 10:08
@Description    : 1、支持base64文字和图片的编码解码，2、支持url编码解码，3、支持Unicode编码解码。
"""
from time import strftime
from logging import info, error
from urllib.parse import quote, unquote
from base64 import b64encode, b64decode
from os import getenv, path, mkdir, system
from CloseButtonPopup import CloseButtonPopup
from DuplicateFilename import DuplicateFilename
from LogGeneration import display_and_save_logs
from PyQt5.Qt import Qt, QFont, QColor, QPoint, QEnterEvent, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton, QListWidget, QStackedWidget, QFileDialog, QTextEdit


class CodingTool(QWidget):
    def __init__(self):
        super().__init__()
        log_dir_path = r"%s\log" % path.dirname(path.abspath(__file__))
        if not path.exists(log_dir_path):
            mkdir(log_dir_path)
        else:
            log_dir_path = log_dir_path
        log_path = r"%s\CodingTool.log" % log_dir_path
        display_and_save_logs(log_path)
        # 获取表格展示数据，使用以下路径做示例，文件夹下（包括子文件夹）的所有文件不能有重名，有重名的文件则返回为空列表
        self.pic_dir_path = r"%s\pic" % path.dirname(path.abspath(__file__))
        if not path.exists(self.pic_dir_path):
            mkdir(self.pic_dir_path)
        else:
            self.pic_dir_path = self.pic_dir_path
        # 初始化路径
        self.result_file_path = r"%s\file" % path.dirname(path.abspath(__file__))
        if not path.exists(self.result_file_path):
            mkdir(self.result_file_path)
        else:
            self.result_file_path = self.result_file_path
        self.file_path = path.dirname(path.abspath(__file__))
        self.full_path = self.file_path.replace("\\", "/")
        # 设置ICO
        self.setWindowIcon(QIcon('%s/icon/main.png' % self.full_path))
        # 初始化全局参数
        self.button_1 = QPushButton()
        # self.button_2 = QPushButton()
        self.button_3 = QPushButton()
        self.button_4 = QPushButton()
        self.button_5 = QPushButton()
        self.button_6 = QPushButton()
        self.button_7 = QPushButton()
        self.button_8 = QPushButton()
        self.button_9 = QPushButton()
        self.button_10 = QPushButton()
        self.button_11 = QPushButton()
        self.button_12 = QPushButton()
        self.button_13 = QPushButton()
        self.button_2_1 = QPushButton()
        self.button_2_2 = QPushButton()
        self.button_2_3 = QPushButton()
        self.button_2_4 = QPushButton()
        self.button_2_5 = QPushButton()
        self.button_2_6 = QPushButton()
        self.button_2_7 = QPushButton()
        self.button_2_8 = QPushButton()
        self.button_2_9 = QPushButton()
        self.layout_ui_1 = QVBoxLayout()
        self.layout_ui_1_1 = QHBoxLayout()
        self.layout_ui_2 = QHBoxLayout()
        self.layout_ui_2_1 = QVBoxLayout()
        self.textedit_1 = QTextEdit()
        self.textedit_2 = QTextEdit()
        self.textedit_3 = QTextEdit()
        self.textedit_4 = QTextEdit()
        self.pic_file_full_path = ""
        self.txt_file_full_path = ""
        self.label_ui_1_5 = QLabel()
        self.label_ui_1_7 = QLabel()
        # 获取显示器分辨率
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        # 设置无边框窗口，且保留点击Windows任务栏图标也能正常最小化和恢复窗口的功能
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.setStyleSheet("border-radius:0px;background-color:white;")
        self.setContentsMargins(0, 0, 0, 0)
        # 设置透明背景
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 设置程序宽高度
        self.height = 614
        self.width = 914
        self.setWindowTitle("编码解码工具")
        self.setFixedSize(self.width, self.height)
        # 鼠标事件参数初始化
        self._right_rect = None
        self._bottom_rect = None
        self._corner_rect = None
        self.move_DragPosition = None
        # 设置鼠标跟踪判断扳机默认值
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False
        # 设置鼠标跟踪
        self.setMouseTracking(True)
        # 整个应用的透明设置,1.0最不透明
        self.setWindowOpacity(1.0)
        # 第三页布局全局参数初始化
        self.hbox_1 = None
        self.hbox_2 = None
        self.right_half_1 = None
        self.right_half_2 = None
        self.right_half_2_1 = QWidget()
        self.right_half_2_2 = QWidget()
        self.label_1 = QLabel()
        # 初始化事件过滤器
        self.label_1.installEventFilter(self)
        self.label_ui_1_1 = QLabel("单个编码解码")
        self.label_ui_1_2 = QLabel("批量文字编码解码")
        self.label_ui_1_3 = QLabel()
        self.tab_ui_1()
        self.tab_ui_2()
        self.left_half_1 = None
        self.left_half_2 = None
        self.vhox_1 = None
        self.hbox_3 = None
        self.vhox_2 = None
        self.hbox_4 = None
        self.hbox_5 = None
        self.hbox_6 = None
        # 初始化关闭弹窗
        self.one = CloseButtonPopup(self)
        self.four = DuplicateFilename(self)
        self.main_page_ui()

    def main_page_ui(self):
        """
        :title 主页面整体布局
        :return: None
        """
        # 主页面分为顶端最大化、最小化、关闭部分和下半部分功能操作部分，所以整体采用垂直布局
        # 顶端部分采用水平布局
        self.hbox_1 = QHBoxLayout()
        self.hbox_1.setSpacing(0)
        self.hbox_1.setContentsMargins(0, 0, 0, 0)
        self.right_half_1 = QWidget()
        self.right_half_1.setMinimumSize(150, 40)
        self.right_half_1.setMaximumSize(self.screenwidth, 40)
        self.left_half_1 = QWidget()
        self.left_half_1.setMinimumSize(80, 40)
        self.left_half_1.setMaximumSize(self.screenwidth, 40)
        self.right_half_1.setStyleSheet("background-color: rgb(246,246,246);padding: 0px;margin: 0px;border-width: 0px;")
        self.left_half_1.setStyleSheet("background-color: rgb(246,246,246);padding: 0px;margin: 0px;border-width: 0px;")
        self.hbox_1.addWidget(self.right_half_1, 98)
        self.hbox_1.addWidget(self.left_half_1, 2)

        # 下半部分功能操作部分采用水平布局
        self.hbox_2 = QHBoxLayout()
        self.hbox_2.setSpacing(0)
        self.hbox_2.setContentsMargins(0, 0, 0, 0)
        self.vhox_1 = QVBoxLayout()
        self.vhox_1.setSpacing(0)
        self.vhox_1.setContentsMargins(0, 0, 0, 0)
        self.vhox_1.addLayout(self.hbox_1)
        self.vhox_1.addLayout(self.hbox_2)
        self.setLayout(self.vhox_1)

        # 顶端左半部分图片采用栅格布局
        layout_1 = QGridLayout()
        layout_1.setSpacing(0)
        layout_1.setContentsMargins(0, 0, 0, 0)
        self.right_half_1.setLayout(layout_1)
        layout_0 = QHBoxLayout()
        layout_0.setSpacing(10)
        layout_0.setContentsMargins(0, 0, 0, 0)
        label_0 = QLabel()
        label_0.setText("®")
        label_0.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        label_0.setStyleSheet("background-color: rgb(55,99,214,255);border: 0px;border-radius: 10px;padding: 0px;margin-left: 10px;width: 16px;height: 16px;font-size: 26px;font-family: Arial-BoldItalicMT, Arial;color: rgba(255,255,255,255);")
        label_0.setMaximumSize(31, 21)
        label_0.setMinimumSize(31, 21)
        layout_0.addWidget(label_0, Qt.AlignCenter | Qt.AlignVCenter)
        layout_1.addLayout(layout_0, 1, 1, 1, 1, Qt.AlignLeft)
        self.label_1 = QLabel()
        self.label_1.setText("编码解码工具")
        self.label_1.setMaximumSize(self.screenwidth, 40)
        self.label_1.setMinimumSize(160, 40)
        self.label_1.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_1.setStyleSheet("background-color: rgb(246,246,246);border: 0px;border-radius: 10px;padding: 0px;margin: 0px;width: 16px;height: 16px;font-size: 18px;font-family: KaiTi;color: rgba(0,0,0,255);")
        layout_0.addWidget(self.label_1, Qt.AlignCenter | Qt.AlignVCenter)

        # 顶端右半部分采用水平布局
        layout_2 = QHBoxLayout()
        layout_2.setContentsMargins(0, 0, 0, 0)
        layout_2.setSpacing(0)
        self.left_half_1.setLayout(layout_2)

        # 设置最小化按钮
        self.button_1.setText("－")
        self.button_1.setToolTip("最小化")
        self.button_1.setMaximumSize(40, 40)
        self.button_1.setMinimumSize(40, 40)
        self.button_1.setObjectName("MinButton")
        self.button_1.setStyleSheet("#MinButton{background-color: rgb(246,246,246);border: 0px;padding: 0px;margin: 0px;width: 40px;height: 40px;color: rgb(10,10,10,255);font-size:20px;font-family:SimSun;}#MinButton:hover{background-color: rgb(195,195,194);}#MinButton:pressed{background-color: rgb(208,208,208);}")
        layout_2.addWidget(self.button_1, Qt.AlignCenter | Qt.AlignVCenter)
        self.button_1.clicked.connect(self.showMinimized)

        # 设置关闭按钮
        self.button_3.setText("×")
        self.button_3.setToolTip("关闭")
        self.button_3.setMaximumSize(40, 40)
        self.button_3.setMinimumSize(40, 40)
        self.button_3.setObjectName("CloseButton")
        self.button_3.setStyleSheet("#CloseButton{background-color: rgb(246,246,246);border: 0px;padding: 0px;margin: 0px;width: 40px;height: 40px;color: rgb(10,10,10,255);font-size:20px;font-family:SimSun;}#CloseButton:hover{background-color: rgb(251,115,115);}#CloseButton:pressed{background-color: rgb(225,72,72);}")
        layout_2.addWidget(self.button_3, Qt.AlignCenter | Qt.AlignVCenter)
        self.button_3.clicked.connect(self.select_btn)

        # 下半部分功能操作布局：常用的左右布局套路
        self.left_half_2 = QListWidget()
        self.left_half_2.setMinimumSize(185, 575)
        self.left_half_2.setMaximumSize(185, self.screenheight)
        self.left_half_2.setObjectName("left_half_2")
        p = self.left_half_2.palette()
        p.setColor(self.left_half_2.backgroundRole(), QColor("#B23AEE"))
        self.left_half_2.setPalette(p)
        self.left_half_2.insertItem(0, '\nBase64编码解码\n')
        self.left_half_2.insertItem(1, '\n其它类型编码解码\n')
        self.left_half_2.setFont(QFont('楷体', 15, QFont.Black))
        self.left_half_2.item(0).setTextAlignment(Qt.AlignCenter)
        self.left_half_2.item(0).setSelected(True)
        self.left_half_2.item(1).setTextAlignment(Qt.AlignCenter)
        # 去除选中虚线框和背景
        self.left_half_2.setFocusPolicy(Qt.NoFocus)
        self.left_half_2.setStyleSheet("#left_half_2{background-color: rgb(60,94,206,255);}#left_half_2::item:hover{background-color: rgb(60,60,255);}#left_half_2::item:selected{background-color: rgb(45,76,166);}")
        self.right_half_2 = QStackedWidget()
        self.right_half_2.addWidget(self.right_half_2_1)
        self.right_half_2.addWidget(self.right_half_2_2)
        self.hbox_2.addWidget(self.left_half_2)
        self.hbox_2.addWidget(self.right_half_2)
        self.left_half_2.currentRowChanged.connect(self.display)

    def display(self, index):
        """
        :title 功能操作根据序号显示对应不同的页面内容
        :param index:页面序号
        :return: None
        """
        self.right_half_2.setCurrentIndex(index)

    def tab_ui_1(self):
        """
        :title 【Base64编码解码】页面整体布局
        :return: None
        """
        try:
            self.label_ui_1_1.setObjectName("FirstInformationLabel")
            self.label_ui_1_1.setMaximumSize(self.screenwidth, 35)
            self.label_ui_1_1.setMinimumSize(400, 35)
            self.label_ui_1_1.setAlignment(Qt.AlignCenter)
            self.label_ui_1_1.setStyleSheet("#FirstInformationLabel{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border-width: 0px;font-weight: bold;color: rgb(0,0,0);font-size: 14pt;vertical-align:middle;}")
            self.layout_ui_1_1.setContentsMargins(0, 0, 0, 0)
            self.layout_ui_1_1.setSpacing(0)
            self.layout_ui_1_1.addWidget(self.label_ui_1_1)

            # 设置编码输入框
            enter_text = """  ★★★单个编码解码使用说明★★★    
●文字编码解码：
（1）在左侧方框内输入需要编码解码的文字；
（2）再点击【文字编码】或者【文字解码】按钮，右侧方框则会出现结果；
●图片编码：
（1）点击【选择文件】按钮选择需要编码的图片；
（2）再点击【图片编码】按钮，左侧方框显示图片路径，右侧方框则会显示图片的编码结果；
●图片解码：
（1）在左侧方框内输入图片的编码；
（2）再点击【图片解码】按钮，右侧方框则会出现生成图片的保存路径。
"""
            self.hbox_3 = QHBoxLayout()
            self.hbox_3.setSpacing(10)
            self.hbox_3.setContentsMargins(0, 0, 0, 0)
            self.textedit_1.setObjectName("FirstEnterText")
            self.textedit_1.setPlaceholderText(enter_text)
            self.textedit_1.setMinimumSize(300, 300)
            self.textedit_1.setMaximumSize(300, 300)
            self.textedit_1.setStyleSheet("#FirstEnterText{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border: 1px solid rgba(0,0,0);color: rgb(69,84,96);font-size: 12pt;}")
            self.hbox_3.addWidget(self.textedit_1)

            # 中间设置功能按钮
            self.vhox_2 = QVBoxLayout()
            self.vhox_2.setSpacing(0)
            self.vhox_2.setContentsMargins(0, 0, 0, 0)
            label_ui_1_2 = QLabel("文 字：")
            label_ui_1_2.setObjectName("PageOneLabel")
            label_ui_1_2.setMaximumSize(90, 35)
            label_ui_1_2.setMinimumSize(90, 35)
            label_ui_1_2.setAlignment(Qt.AlignCenter)
            label_ui_1_2.setStyleSheet("#PageOneLabel{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border-width: 0px;font-weight: bold;color: rgb(69,84,96);font-size: 12pt;vertical-align:middle;}")
            self.vhox_2.addWidget(label_ui_1_2)
            self.hbox_3.addLayout(self.vhox_2)

            self.button_4.setText("文字编码")
            self.button_4.setObjectName("FunctionBtn")
            self.button_4.setMinimumSize(90, 35)
            self.button_4.setMaximumSize(90, 35)
            self.button_4.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
            self.vhox_2.addWidget(self.button_4, Qt.AlignCenter)
            self.button_4.clicked.connect(self.word_encoding)

            self.button_5.setText("文字解码")
            self.button_5.setObjectName("FunctionBtn")
            self.button_5.setMinimumSize(90, 35)
            self.button_5.setMaximumSize(90, 35)
            self.button_5.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
            self.vhox_2.addWidget(self.button_5, Qt.AlignCenter)
            self.button_5.clicked.connect(self.word_decoding)

            label_ui_1_3 = QLabel("图 片：")
            label_ui_1_3.setObjectName("PageOneLabel")
            label_ui_1_3.setMaximumSize(90, 35)
            label_ui_1_3.setMinimumSize(90, 35)
            label_ui_1_3.setAlignment(Qt.AlignCenter)
            label_ui_1_3.setStyleSheet("#PageOneLabel{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border-width: 0px;font-weight: bold;color: rgb(69,84,96);font-size: 12pt;vertical-align:middle;}")
            self.vhox_2.addWidget(label_ui_1_3)

            self.button_6.setText("打开文件")
            self.button_6.setObjectName("FunctionBtn")
            self.button_6.setMinimumSize(90, 35)
            self.button_6.setMaximumSize(90, 35)
            self.button_6.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
            self.vhox_2.addWidget(self.button_6)
            self.button_6.clicked.connect(self.select_pic_file)

            self.button_7.setText("图片编码")
            self.button_7.setObjectName("FunctionBtn")
            self.button_7.setMinimumSize(90, 35)
            self.button_7.setMaximumSize(90, 35)
            self.button_7.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
            self.vhox_2.addWidget(self.button_7)
            self.button_7.clicked.connect(self.pic_encoding)

            self.button_8.setText("图片解码")
            self.button_8.setObjectName("FunctionBtn")
            self.button_8.setMinimumSize(90, 35)
            self.button_8.setMaximumSize(90, 35)
            self.button_8.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
            self.vhox_2.addWidget(self.button_8)
            self.button_8.clicked.connect(self.pic_decoding)

            self.button_13.setText("清空内容")
            self.button_13.setToolTip("清空左右两边输入框所有内容！")
            self.button_13.setObjectName("ClearBtn")
            self.button_13.setMinimumSize(90, 35)
            self.button_13.setMaximumSize(90, 35)
            self.button_13.setStyleSheet("""#ClearBtn{margin: 0px;margin: 0px;border: 1px solid rgb(255,77,79);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(255,77,79);font-size: 12pt;vertical-align:middle;}#ClearBtn:hover{border: 1px solid rgb(255,165,117);color: rgb(255,165,117);}#ClearBtn:pressed{border: 1px solid rgb(217,54,62);color: rgb(217,54,62);}""")
            self.vhox_2.addWidget(self.button_13)
            self.button_13.clicked.connect(self.clear_content_1)

            output_text = """★★★批量文字编码解码使用说明★★★   
1、点击【选择文件】按钮，选择需要批量编码或者解码的txt文件，批量数据之间以换行隔开；
2、如果是批量文字编码的话，再点击【开始编码】按钮；
3、如果是批量文字解码的话，再点击【开始解码】按钮；
4、等结果出来后，会显示结果文件路径，再点击【打开文件】即可打开结果文件。
"""
            self.textedit_2.setObjectName("FirstEnterText")
            self.textedit_2.setPlaceholderText(output_text)
            self.textedit_2.setMinimumSize(300, 300)
            self.textedit_2.setMaximumSize(300, 300)
            self.textedit_2.setStyleSheet("#FirstEnterText{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border: 1px solid rgba(0,0,0);color: rgb(69,84,96);font-size: 12pt;}")
            self.hbox_3.addWidget(self.textedit_2)

            self.label_ui_1_3.setObjectName("SeparateLabel")
            self.label_ui_1_3.setMaximumSize(self.screenwidth, 5)
            self.label_ui_1_3.setMinimumSize(400, 5)
            self.label_ui_1_3.setAlignment(Qt.AlignCenter)
            self.label_ui_1_3.setStyleSheet("#SeparateLabel{background-color: rgb(60,94,206);padding: 0px;margin: 0px;border-width: 0px;font-weight: bold;color: rgb(69,84,96);font-size: 12pt;vertical-align:middle;}")

            self.label_ui_1_2.setObjectName("SecondInformationLabel")
            self.label_ui_1_2.setMaximumSize(self.screenwidth, 35)
            self.label_ui_1_2.setMinimumSize(400, 35)
            self.label_ui_1_2.setAlignment(Qt.AlignCenter)
            self.label_ui_1_2.setStyleSheet("#SecondInformationLabel{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border-width: 0px;font-weight: bold;color: rgb(0,0,0);font-size: 14pt;vertical-align:middle;}")

            self.hbox_4 = QHBoxLayout()
            self.hbox_4.setContentsMargins(0, 0, 0, 0)
            self.hbox_4.setSpacing(0)
            label_ui_1_4 = QLabel("原始文件路径：")
            label_ui_1_4.setObjectName("PathLabel")
            label_ui_1_4.setMaximumSize(120, 35)
            label_ui_1_4.setMinimumSize(120, 35)
            label_ui_1_4.setAlignment(Qt.AlignCenter)
            label_ui_1_4.setStyleSheet("#PathLabel{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border-width: 0px;font-weight: bold;color: rgb(69,84,96);font-size: 12pt;vertical-align:middle;}")
            self.hbox_4.addWidget(label_ui_1_4)

            self.label_ui_1_5.setObjectName("OriginalFilePath")
            self.label_ui_1_5.setMaximumSize(480, 35)
            self.label_ui_1_5.setMinimumSize(480, 35)
            self.label_ui_1_5.setAlignment(Qt.AlignCenter)
            self.label_ui_1_5.setStyleSheet("#OriginalFilePath{border: 1px solid rgb(212,212,212);border-radius:4px;font-size: 10pt;vertical-align:middle;line-height: 100%;}""#OriginalFilePath:focus{border-color: rgb(58,96,207);}")
            self.hbox_4.addWidget(self.label_ui_1_5)

            self.button_9.setText("选择文件")
            self.button_9.setObjectName("SelectTxtFileBtn")
            self.button_9.setMinimumSize(90, 35)
            self.button_9.setMaximumSize(90, 35)
            self.button_9.setStyleSheet("""#SelectTxtFileBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#SelectTxtFileBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#SelectTxtFileBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
            self.hbox_4.addWidget(self.button_9)
            self.button_9.clicked.connect(self.select_txt_file)

            self.hbox_5 = QHBoxLayout()
            self.hbox_5.setContentsMargins(0, 0, 0, 0)
            self.hbox_5.setSpacing(0)
            label_ui_1_6 = QLabel("结果文件路径：")
            label_ui_1_6.setObjectName("PathLabel")
            label_ui_1_6.setMaximumSize(120, 35)
            label_ui_1_6.setMinimumSize(120, 35)
            label_ui_1_6.setAlignment(Qt.AlignCenter)
            label_ui_1_6.setStyleSheet("#PathLabel{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border-width: 0px;font-weight: bold;color: rgb(69,84,96);font-size: 12pt;vertical-align:middle;}")
            self.hbox_5.addWidget(label_ui_1_6)

            self.label_ui_1_7.setObjectName("ResultFilePath")
            self.label_ui_1_7.setMaximumSize(480, 35)
            self.label_ui_1_7.setMinimumSize(480, 35)
            self.label_ui_1_7.setAlignment(Qt.AlignCenter)
            self.label_ui_1_7.setStyleSheet("#ResultFilePath{border: 1px solid rgb(212,212,212);border-radius:4px;font-size: 10pt;vertical-align:middle;line-height: 100%;}""#ResultFilePath:focus{border-color: rgb(58,96,207);}")
            self.hbox_5.addWidget(self.label_ui_1_7)

            self.button_10.setText("打开文件夹")
            self.button_10.setObjectName("OpenTxtFileBtn")
            self.button_10.setMinimumSize(90, 35)
            self.button_10.setMaximumSize(90, 35)
            self.button_10.setStyleSheet("""#OpenTxtFileBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#OpenTxtFileBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#OpenTxtFileBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
            self.hbox_5.addWidget(self.button_10)
            self.button_10.clicked.connect(self.open_result_dir)

            self.hbox_6 = QHBoxLayout()
            self.hbox_6.setContentsMargins(0, 0, 0, 0)
            self.hbox_6.setSpacing(32)
            self.button_11.setText("开始编码")
            self.button_11.setObjectName("StartEncodingBtn")
            self.button_11.setMinimumSize(90, 35)
            self.button_11.setMaximumSize(90, 35)
            self.button_11.setStyleSheet("""#StartEncodingBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#StartEncodingBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#StartEncodingBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
            self.hbox_6.addWidget(self.button_11)
            self.button_11.clicked.connect(self.start_encoding)

            self.button_12.setText("开始解码")
            self.button_12.setObjectName("StartDecodingBtn")
            self.button_12.setMinimumSize(90, 35)
            self.button_12.setMaximumSize(90, 35)
            self.button_12.setStyleSheet("""#StartDecodingBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#StartDecodingBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#StartDecodingBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
            self.hbox_6.addWidget(self.button_12)
            self.button_12.clicked.connect(self.start_decoding)

            self.layout_ui_1.setContentsMargins(0, 0, 0, 0)
            self.layout_ui_1.setSpacing(0)
            self.layout_ui_1.addLayout(self.layout_ui_1_1)
            self.layout_ui_1.addLayout(self.hbox_3)
            self.layout_ui_1.addWidget(self.label_ui_1_3)
            self.layout_ui_1.addWidget(self.label_ui_1_2)
            self.layout_ui_1.addLayout(self.hbox_4)
            self.layout_ui_1.addLayout(self.hbox_5)
            self.layout_ui_1.addLayout(self.hbox_6)
            self.right_half_2_1.setLayout(self.layout_ui_1)
        except Exception as e:
            info("【Base64编码解码】页面整体布局报错，具体原因如下所示！")
            error(e)

    def tab_ui_2(self):
        """
        :title 【URL编码解码】页面布局
        :return: None
        """
        self.layout_ui_2.setContentsMargins(0, 0, 0, 0)
        self.layout_ui_2.setSpacing(0)

        self.textedit_3.setPlaceholderText("请输入需要转换的文本...")
        self.textedit_3.setObjectName("EnterText")
        self.textedit_3.setMinimumSize(300, 550)
        self.textedit_3.setMaximumSize(300, 550)
        self.textedit_3.setStyleSheet("#EnterText{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border: 1px solid rgba(0,0,0);color: rgb(69,84,96);font-size: 12pt;}")
        self.layout_ui_2.addWidget(self.textedit_3)

        self.layout_ui_2_1.setContentsMargins(0, 0, 0, 0)
        self.layout_ui_2_1.setSpacing(0)
        self.layout_ui_2.addLayout(self.layout_ui_2_1)

        label_ui_2_1 = QLabel("URL：")
        label_ui_2_1.setObjectName("PageTwoLabel")
        label_ui_2_1.setMaximumSize(90, 35)
        label_ui_2_1.setMinimumSize(90, 35)
        label_ui_2_1.setAlignment(Qt.AlignCenter)
        label_ui_2_1.setStyleSheet("#PageTwoLabel{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border-width: 0px;font-weight: bold;color: rgb(69,84,96);font-size: 12pt;vertical-align:middle;}")
        self.layout_ui_2_1.addWidget(label_ui_2_1)

        self.button_2_1.setText("URL编码")
        self.button_2_1.setObjectName("FunctionBtn")
        self.button_2_1.setMinimumSize(90, 35)
        self.button_2_1.setMaximumSize(90, 35)
        self.button_2_1.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
        self.layout_ui_2_1.addWidget(self.button_2_1, Qt.AlignCenter)
        self.button_2_1.clicked.connect(self.url_encoding)

        self.button_2_2.setText("URL解码")
        self.button_2_2.setObjectName("FunctionBtn")
        self.button_2_2.setMinimumSize(90, 35)
        self.button_2_2.setMaximumSize(90, 35)
        self.button_2_2.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
        self.layout_ui_2_1.addWidget(self.button_2_2, Qt.AlignCenter)
        self.button_2_2.clicked.connect(self.url_decoding)

        label_ui_2_2 = QLabel("Unicode：")
        label_ui_2_2.setObjectName("PageTwoLabel")
        label_ui_2_2.setMaximumSize(90, 35)
        label_ui_2_2.setMinimumSize(90, 35)
        label_ui_2_2.setAlignment(Qt.AlignCenter)
        label_ui_2_2.setStyleSheet("#PageTwoLabel{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border-width: 0px;font-weight: bold;color: rgb(69,84,96);font-size: 12pt;vertical-align:middle;}")
        self.layout_ui_2_1.addWidget(label_ui_2_2)

        self.button_2_3.setText("转中文")
        self.button_2_3.setObjectName("FunctionBtn")
        self.button_2_3.setMinimumSize(90, 35)
        self.button_2_3.setMaximumSize(90, 35)
        self.button_2_3.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
        self.layout_ui_2_1.addWidget(self.button_2_3, Qt.AlignCenter)
        self.button_2_3.clicked.connect(self.unicode_cn)

        self.button_2_4.setText("转ASCII")
        self.button_2_4.setObjectName("FunctionBtn")
        self.button_2_4.setMinimumSize(90, 35)
        self.button_2_4.setMaximumSize(90, 35)
        self.button_2_4.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
        self.layout_ui_2_1.addWidget(self.button_2_4, Qt.AlignCenter)
        self.button_2_4.clicked.connect(self.unicode_ascii)

        label_ui_2_3 = QLabel("中文：")
        label_ui_2_3.setObjectName("PageTwoLabel")
        label_ui_2_3.setMaximumSize(90, 35)
        label_ui_2_3.setMinimumSize(90, 35)
        label_ui_2_3.setAlignment(Qt.AlignCenter)
        label_ui_2_3.setStyleSheet("#PageTwoLabel{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border-width: 0px;font-weight: bold;color: rgb(69,84,96);font-size: 12pt;vertical-align:middle;}")
        self.layout_ui_2_1.addWidget(label_ui_2_3)

        self.button_2_5.setText("转Unicode")
        self.button_2_5.setObjectName("FunctionBtn")
        self.button_2_5.setMinimumSize(90, 35)
        self.button_2_5.setMaximumSize(90, 35)
        self.button_2_5.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
        self.layout_ui_2_1.addWidget(self.button_2_5, Qt.AlignCenter)
        self.button_2_5.clicked.connect(self.cn_unicode)

        self.button_2_6.setText("转ASCII")
        self.button_2_6.setObjectName("FunctionBtn")
        self.button_2_6.setMinimumSize(90, 35)
        self.button_2_6.setMaximumSize(90, 35)
        self.button_2_6.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
        self.layout_ui_2_1.addWidget(self.button_2_6, Qt.AlignCenter)
        self.button_2_6.clicked.connect(self.cn_ascii)

        label_ui_2_4 = QLabel("ASCII：")
        label_ui_2_4.setObjectName("PageTwoLabel")
        label_ui_2_4.setMaximumSize(90, 35)
        label_ui_2_4.setMinimumSize(90, 35)
        label_ui_2_4.setAlignment(Qt.AlignCenter)
        label_ui_2_4.setStyleSheet("#PageTwoLabel{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border-width: 0px;font-weight: bold;color: rgb(69,84,96);font-size: 12pt;vertical-align:middle;}")
        self.layout_ui_2_1.addWidget(label_ui_2_4)

        self.button_2_7.setText("转Unicode")
        self.button_2_7.setObjectName("FunctionBtn")
        self.button_2_7.setMinimumSize(90, 35)
        self.button_2_7.setMaximumSize(90, 35)
        self.button_2_7.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
        self.layout_ui_2_1.addWidget(self.button_2_7, Qt.AlignCenter)
        self.button_2_7.clicked.connect(self.ascii_unicode)

        self.button_2_8.setText("转中文")
        self.button_2_8.setObjectName("FunctionBtn")
        self.button_2_8.setMinimumSize(90, 35)
        self.button_2_8.setMaximumSize(90, 35)
        self.button_2_8.setStyleSheet("""#FunctionBtn{margin: 0px;margin: 0px;border: 1px solid rgb(0,0,0);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(0,0,0);font-size: 12pt;vertical-align:middle;}#FunctionBtn:hover{border: 1px solid rgb(54,136,199);color: rgb(54,136,199);}#FunctionBtn:pressed{border: 1px solid rgb(58,96,207);color: rgb(58,96,207);}""")
        self.layout_ui_2_1.addWidget(self.button_2_8, Qt.AlignCenter)
        self.button_2_8.clicked.connect(self.ascii_cn)

        self.button_2_9.setText("清空内容")
        self.button_2_9.setToolTip("清空左右两边输入框所有内容！")
        self.button_2_9.setObjectName("ClearBtn")
        self.button_2_9.setMinimumSize(90, 35)
        self.button_2_9.setMaximumSize(90, 35)
        self.button_2_9.setStyleSheet("""#ClearBtn{margin: 0px;margin: 0px;border: 1px solid rgb(255,77,79);background-color: rgb(255,255,255);border-radius:4px;font-weight: bold;color: rgb(255,77,79);font-size: 12pt;vertical-align:middle;}#ClearBtn:hover{border: 1px solid rgb(255,165,117);color: rgb(255,165,117);}#ClearBtn:pressed{border: 1px solid rgb(217,54,62);color: rgb(217,54,62);}""")
        self.layout_ui_2_1.addWidget(self.button_2_9)
        self.button_2_9.clicked.connect(self.clear_content_2)

        self.textedit_4.setPlaceholderText("转换之后的数据...")
        self.textedit_4.setObjectName("EnterText")
        self.textedit_4.setMinimumSize(300, 550)
        self.textedit_4.setMaximumSize(300, 550)
        self.textedit_4.setStyleSheet("#EnterText{background-color: rgb(255,255,255);padding: 0px;margin: 0px;border: 1px solid rgba(0,0,0);color: rgb(69,84,96);font-size: 12pt;}")
        self.layout_ui_2.addWidget(self.textedit_4)

        self.right_half_2_2.setLayout(self.layout_ui_2)

    def word_encoding(self):
        """
        :title 文字编码
        :return: None
        """
        src = self.textedit_1.toPlainText()
        if src:
            try:
                code1 = b64encode(src.encode("utf-8"))
                # 输出到界面
                self.textedit_2.clear()
                result_text = str(code1.decode("utf-8"))
                self.textedit_2.setPlainText(result_text)
            except Exception as e:
                self.textedit_2.clear()
                self.textedit_2.setPlainText("base64编码失败！具体原因如下所示！\n%s" % e)
                info("文字编码报错，具体原因如下所示！")
                error(e)
        else:
            self.textedit_2.clear()
            self.textedit_2.setPlainText("未获取到需要编码的原数据！请在左边方框内输入需要编码的数据！")
            info("未获取到需要编码的原数据！")

    def word_decoding(self):
        """
        :title 文字编码
        :return: None
        """
        src = self.textedit_1.toPlainText()
        if src:
            try:
                code1 = b64decode(src).decode("utf-8")
                # 输出到界面
                self.textedit_2.clear()
                result_text = str(code1)
                self.textedit_2.setPlainText(result_text)
            except Exception as e:
                self.textedit_2.clear()
                self.textedit_2.setPlainText("base64解码失败！具体原因如下所示！\n%s" % e)
                info("文字解码报错，具体原因如下所示！")
                error(e)
        else:
            self.textedit_2.clear()
            self.textedit_2.setPlainText("未获取到需要解码的原数据！请在左边方框内输入需要解码的数据！")
            info("未获取到需要解码的原数据！")

    def select_btn(self):
        """
        :title 确认选择弹窗，先禁用主窗口，再通过自写控件CloseButtonPopup的方法重新使能主窗口
        :return: None
        """
        self.setEnabled(False)
        if self.one.checkbox_1.isChecked() and self.one.rbutton_1.isChecked():
            self.one.select_method()
        elif self.one.checkbox_1.isChecked() and self.one.rbutton_2.isChecked():
            self.one.exit_win()
        else:
            self.one.show()
            # 使自写控件CloseButtonPopup显示在应用的中间
            x = int(self.pos().x())
            y = int(self.pos().y())
            if x == 0 and y == 0:
                self.one.move(int((self.screenwidth - self.one.width) / 2), int((self.screenheight - self.one.height) / 2))
            else:
                self.one.move(int(x + (self.width - self.one.width) / 2), int(y + (self.height - self.one.height) / 2))

    def select_pic_file(self):
        """
        :title 选择文件，并显示【机构单位职位文件】的完整路径
        :return: None
        """
        try:
            self.pic_file_full_path = QFileDialog.getOpenFileName(self, "选取文件", getenv("HOME"))[0]
            if self.pic_file_full_path.split(".")[-1] in ["png", "jpg", "jpeg"]:
                self.textedit_1.clear()
                self.textedit_1.setPlainText("需要编码的图片文件路径为：\n"+self.pic_file_full_path)
                info("需要编码的图片文件路径为：%s！" % self.pic_file_full_path)
            else:
                self.textedit_1.clear()
                self.textedit_1.setPlainText("您选择不是png、jpg和jpeg这三类图片文件，请重新选择！")
                info("选择的文件不是png、jpg和jpeg这三类图片文件！")
        except Exception as e:
            info("获取图片文件路径报错，具体原因如下所示！")
            error(e)

    def pic_encoding(self):
        """
        :title 单个图片编码
        :return: None
        """
        try:
            obtain_pic_path = self.pic_file_full_path
            info(obtain_pic_path)
            if obtain_pic_path == "":
                self.textedit_2.clear()
                self.textedit_2.setPlainText("未获取到原数据，请重新选择需要编码的图片！")
                info("未获取到原数据，请重新选择需要编码的图片！")
            else:
                open_pic = open("%s" % obtain_pic_path, 'rb')
                b64str = b64encode(open_pic.read())
                open_pic.close()
                pic_encoding_data = b64str.decode()
                self.textedit_2.clear()
                self.textedit_2.setPlainText(pic_encoding_data)
                info("图片文件的具体编码如下所示：%s！" % pic_encoding_data)
        except Exception as e:
            self.textedit_2.clear()
            self.textedit_2.setPlainText("图片文件编码报错，具体原因如下所示！\n%s" % e)
            info("图片文件编码报错，具体原因如下所示！")
            error(e)

    def pic_decoding(self):
        """
        :title 单个图片解码
        :return: None
        """
        try:
            decode_data = self.textedit_1.toPlainText()
            if decode_data == "":
                self.textedit_2.clear()
                self.textedit_2.setPlainText("未获取到原数据，请在左侧输入框内重新输入需要解码的图片编码！")
                info("未获取到原数据，请在左侧输入框内重新输入需要解码的图片编码！")
            else:
                if "," in decode_data:
                    pre_data = decode_data.split(",")[0]
                    decode_data = decode_data.split(",")[1]
                    pic_type = pre_data.split(";")[0].split("/")[1]
                    time_var = strftime("%Y%m%d%H%M%S")
                    full_pic_path = self.pic_dir_path + r"\%s." % time_var+pic_type
                    tmp = open(full_pic_path, 'wb')
                    tmp.write(b64decode(decode_data))
                    tmp.close()
                else:
                    decode_data = decode_data
                    time_var = strftime("%Y%m%d%H%M%S")
                    full_pic_path = self.pic_dir_path + r"\%s.png" % time_var
                    tmp = open(full_pic_path, 'wb')
                    tmp.write(b64decode(decode_data))
                    tmp.close()
                self.textedit_2.clear()
                self.textedit_2.setPlainText("图片文件解码成功，保存路径为：\n%s" % full_pic_path)
                info("图片文件解码成功，保存路径为：%s！" % full_pic_path)
        except Exception as e:
            self.textedit_2.clear()
            self.textedit_2.setPlainText("图片文件解码报错，具体原因如下所示！\n%s" % e)
            info("图片文件解码报错，具体原因如下所示！")
            error(e)

    def clear_content_1(self):
        """
        :title 清除单个编码解码左右两边输入框内所有内容
        :return: None
        """
        self.textedit_1.clear()
        self.textedit_2.clear()
        self.pic_file_full_path = ""

    def clear_content_2(self):
        """
        :title 清除单个编码解码左右两边输入框内所有内容
        :return: None
        """
        self.textedit_3.clear()
        self.textedit_4.clear()
        # self.pic_file_full_path = ""

    def select_txt_file(self):
        """
        :title 选择文件，并显示【机构单位职位文件】的完整路径
        :return: None
        """
        try:
            self.txt_file_full_path = QFileDialog.getOpenFileName(self, "选取文件", getenv("HOME"))[0]
            if self.txt_file_full_path.split(".")[-1] == "txt":
                self.label_ui_1_5.clear()
                self.label_ui_1_5.setText(self.txt_file_full_path)
                self.label_ui_1_5.setToolTip(self.txt_file_full_path)
                info("需要批量编码的文本文档路径为：%s！" % self.txt_file_full_path)
            else:
                self.label_ui_1_5.clear()
                self.label_ui_1_5.setText("您选择不是后缀名为txt的文本文档，请重新选择！")
                info("选择的文件不是后缀名为txt的文本文档！")
        except Exception as e:
            info("获取批量解码的文本文档路径报错，具体原因如下所示！")
            error(e)

    def read_txt(self):
        """
        :title 读取txt文件中的数据
        :return: txt_data：去掉换行符的列表
        """
        txt_data = list()
        try:
            txt_path = self.txt_file_full_path
            with open(txt_path, "r", encoding="utf-8") as f:
                pre_data = f.readlines()
            for i in range(0, len(pre_data)):
                data = pre_data[i].split("\n")[0]
                txt_data.append(data)
            return txt_data
        except Exception as e:
            info("处理txt数据报错，请检查txt数据格式是否符合规则。报错原因如下所示！")
            error(e)
            return txt_data

    def start_encoding(self):
        """
        :title 通过读取txt文件中的数据，对此数据进行批量编码并保存到新的txt文档中
        :return: None
        """
        standby_data = self.read_txt()
        result_txt_path = self.result_file_path+r"\编码结果文件_"+strftime("%Y%m%d%H%M%S")+".txt"
        try:
            if len(standby_data) == 0:
                self.label_ui_1_7.clear()
                self.label_ui_1_7.setText("数据处理异常，请检查所选文本数据是否正常。")
                self.label_ui_1_7.setToolTip("数据处理异常，请检查所选文本数据是否正常。")
                info("处理txt数据异常，请检查所选文本数据是否正常。")
            else:
                info("已正常获取到txt文档的数据！")
                with open(result_txt_path, "a+", encoding="utf-8") as f:
                    for i in range(0, len(standby_data)):
                        f.write(b64encode(standby_data[i].encode("utf-8")).decode("utf-8")+"\n")
                self.label_ui_1_7.clear()
                self.label_ui_1_7.setText(result_txt_path)
                self.label_ui_1_7.setToolTip(result_txt_path)
                info("批量编码已完成！")
        except Exception as e:
            self.label_ui_1_7.clear()
            self.label_ui_1_7.setText("批量编码报错，请查看日志详情！")
            self.label_ui_1_7.setToolTip("批量编码报错，请查看日志详情！")
            info("批量编码报错，错误原因如下所示！")
            error(e)

    def start_decoding(self):
        """
        :title 通过读取txt文件中的数据，对此数据进行批量解码并保存到新的txt文档中
        :return: None
        """
        standby_data = self.read_txt()
        result_txt_path = self.result_file_path + r"\解码结果文件_" + strftime("%Y%m%d%H%M%S") + ".txt"
        try:
            if len(standby_data) == 0:
                self.label_ui_1_7.clear()
                self.label_ui_1_7.setText("数据处理异常，请检查所选文本数据是否正常。")
                self.label_ui_1_7.setToolTip("数据处理异常，请检查所选文本数据是否正常。")
                info("处理txt数据异常，请检查所选文本数据是否正常。")
            else:
                info("已正常获取到txt文档的数据！")
                with open(result_txt_path, "a+", encoding="utf-8") as f:
                    for i in range(0, len(standby_data)):
                        f.write(b64decode(standby_data[i]).decode("utf-8") + "\n")
                self.label_ui_1_7.clear()
                self.label_ui_1_7.setText(result_txt_path)
                self.label_ui_1_7.setToolTip(result_txt_path)
                info("批量解码已完成！")
        except Exception as e:
            self.label_ui_1_7.clear()
            self.label_ui_1_7.setText("批量编解码报错，请查看日志详情！")
            self.label_ui_1_7.setToolTip("批量解码报错，请查看日志详情！")
            info("批量解码报错，错误原因如下所示！")
            error(e)

    def open_result_dir(self):
        """
        :title 打开保存结果文档的文件夹
        :return: None
        """
        result_dir_path = self.result_file_path
        system("start explorer %s" % result_dir_path)
        info("保存结果文件的文件夹已打开！")

    def url_encoding(self):
        """
        :title url编码
        :return: None
        """
        src = self.textedit_3.toPlainText()
        if src:
            try:
                # 输出到界面
                self.textedit_4.clear()
                result_text = str(quote(src))
                self.textedit_4.setPlainText(result_text)
                info("【%s】的url编码结果为：%s。" % (src, result_text))
            except Exception as e:
                self.textedit_4.clear()
                self.textedit_4.setPlainText("url编码失败！具体原因如下所示！\n%s" % e)
                info("url编码报错，具体原因如下所示！")
                error(e)
        else:
            self.textedit_4.clear()
            self.textedit_4.setPlainText("未获取到需要编码的原数据！请在左边方框内输入需要编码的数据！")
            info("未获取到需要编码的原数据！")

    def url_decoding(self):
        """
        :title url解码
        :return: None
        """
        src = self.textedit_3.toPlainText()
        if src:
            try:
                # 输出到界面
                self.textedit_4.clear()
                result_text = str(unquote(src))
                self.textedit_4.setPlainText(result_text)
                info("【%s】的url解码结果为：%s。" % (src, result_text))
            except Exception as e:
                self.textedit_4.clear()
                self.textedit_4.setPlainText("url解码失败！具体原因如下所示！\n%s" % e)
                info("url解码报错，具体原因如下所示！")
                error(e)
        else:
            self.textedit_4.clear()
            self.textedit_4.setPlainText("未获取到需要解码的原数据！请在左边方框内输入需要解码的数据！")
            info("未获取到需要解码的原数据！")

    def unicode_cn(self):
        """
        :title Unicode转中文
        :return: None
        """
        src = self.textedit_3.toPlainText()
        if src:
            try:
                self.textedit_4.clear()
                if "\\u" not in src and len(src) % 6 != 0:
                    result_text = src
                else:
                    result_text = str(src.encode("utf-8").decode("unicode_escape"))
                self.textedit_4.setPlainText(result_text)
                info("【%s】转中文的结果为：%s。" % (src, result_text))
            except Exception as e:
                self.textedit_4.clear()
                self.textedit_4.setPlainText("Unicode转中文失败！具体原因如下所示！\n%s" % e)
                info("Unicode转中文报错，具体原因如下所示！")
                error(e)
        else:
            self.textedit_4.clear()
            self.textedit_4.setPlainText("未获取到原数据！请在左边方框内输入需要转中文的Unicode原数据！")
            info("未获取到原数据！")

    def cn_unicode(self):
        """
        :title 中文转Unicode
        :return: None
        """
        src = self.textedit_3.toPlainText()
        if src:
            try:
                self.textedit_4.clear()
                result_text = str(src.encode("unicode_escape").decode("utf-8"))
                self.textedit_4.setPlainText(result_text)
                info("【%s】转unicode的结果为：%s。" % (src, result_text))
            except Exception as e:
                self.textedit_4.clear()
                self.textedit_4.setPlainText("中文转Unicode失败！具体原因如下所示！\n%s" % e)
                info("中文转Unicode报错，具体原因如下所示！")
                error(e)
        else:
            self.textedit_4.clear()
            self.textedit_4.setPlainText("未获取到原数据！请在左边方框内输入需要转Unicode的中文原数据！")
            info("未获取到原数据！")

    def unicode_ascii(self):
        """
        :title Unicode转ascii
        :return: None
        """
        src = self.textedit_3.toPlainText()
        result_text = ""
        if src:
            try:
                self.textedit_4.clear()
                for i in range(0, len(src)):
                    result_text = result_text + "&#"+str(ord(src[i]))+";"
                self.textedit_4.setPlainText(result_text)
                info("【%s】转unicode的结果为：%s。" % (src, result_text))
            except Exception as e:
                self.textedit_4.clear()
                self.textedit_4.setPlainText("Unicode转ascii失败！具体原因如下所示！\n%s" % e)
                info("Unicode转ascii报错，具体原因如下所示！")
                error(e)
        else:
            self.textedit_4.clear()
            self.textedit_4.setPlainText("未获取到原数据！请在左边方框内输入需要转ascii的Unicode原数据！")
            info("未获取到原数据！")

    def ascii_unicode(self):
        """
        :title ascii转Unicode
        :return: None
        """
        src = self.textedit_3.toPlainText()
        result_text = ""
        if src:
            try:
                self.textedit_4.clear()
                if ";" in src:
                    initial_list = src.split(";")
                    initial_list.remove(initial_list[-1])
                    for i in range(0, len(initial_list)):
                        # chr方法所传参数必须是整数
                        result_text = result_text + chr(int(initial_list[i].split("#")[-1]))
                else:
                    result_text = src
                self.textedit_4.setPlainText(result_text)
                info("【%s】转unicode的结果为：%s。" % (src, result_text))
            except Exception as e:
                self.textedit_4.clear()
                self.textedit_4.setPlainText("ascii转Unicode失败！具体原因如下所示！\n%s" % e)
                info("ascii转Unicode报错，具体原因如下所示！")
                error(e)
        else:
            self.textedit_4.clear()
            self.textedit_4.setPlainText("未获取到原数据！请在左边方框内输入需要转Unicode的ascii原数据！")
            info("未获取到原数据！")

    def ascii_cn(self):
        """
        :title ascii转中文；汉字的HTML实体由三部分组成，”&#+ASCII+;“ 即可。
        :return: None
        """
        src = self.textedit_3.toPlainText()
        result_text = ""
        if src:
            try:
                self.textedit_4.clear()
                if ";" in src:
                    initial_list = src.split(";")
                    initial_list.remove(initial_list[-1])
                    for i in range(0, len(initial_list)):
                        # chr方法所传参数必须是整数
                        result_text = result_text + chr(int(initial_list[i].split("#")[-1]))
                else:
                    result_text = src
                self.textedit_4.setPlainText(result_text)
                info("【%s】转中文的结果为：%s。" % (src, result_text))
            except Exception as e:
                self.textedit_4.clear()
                self.textedit_4.setPlainText("ascii转中文失败！具体原因如下所示！\n%s" % e)
                info("ascii转中文报错，具体原因如下所示！")
                error(e)
        else:
            self.textedit_4.clear()
            self.textedit_4.setPlainText("未获取到原数据！请在左边方框内输入需要转中文的ascii原数据！")
            info("未获取到原数据！")

    def cn_ascii(self):
        """
        :title 中文转ascii；汉字的HTML实体由三部分组成，”&#+ASCII+;“ 即可。
        :return: None
        """
        src = self.textedit_3.toPlainText()
        result_text = ""
        if src:
            try:
                self.textedit_4.clear()
                for i in range(0, len(src)):
                    result_text = result_text + "&#"+str(ord(src[i]))+";"
                self.textedit_4.setPlainText(result_text)
                info("【%s】转ascii的结果为：%s。" % (src, result_text))
            except Exception as e:
                self.textedit_4.clear()
                self.textedit_4.setPlainText("中文转ascii失败！具体原因如下所示！\n%s" % e)
                info("中文转ascii报错，具体原因如下所示！")
                error(e)
        else:
            self.textedit_4.clear()
            self.textedit_4.setPlainText("未获取到原数据！请在左边方框内输入需要转ascii的中文原数据！")
            info("未获取到原数据！")

    def view_log(self):
        """
        :title 【日志查看】按钮点击后跳转到【专业技术职业维护】页面，且左边与其对应的条目也默认被选中：
        :return: None
        """
        self.left_half_2.setCurrentItem(self.left_half_2.item(0))
        self.right_half_2.setCurrentIndex(0)

    def reshow(self):
        self.show()

    def close_app(self):
        """
        :title 关闭整个应用
        :return: None
        """
        self.sender()
        app = QApplication.instance()
        app.quit()

    def eventFilter(self, obj, event):
        """
        :title 事件过滤器,用于解决鼠标进入其它控件后还原为标准鼠标样式
        :param obj:对象
        :param event:鼠标事件
        :return: None
        """
        try:
            if isinstance(event, QEnterEvent):
                self.setCursor(Qt.ArrowCursor)
            # 注意 ,PhotoGenerator是所在类的名称
            return super(CodingTool, self).eventFilter(obj, event)
            # return QWidget.eventFilter(self, obj, event)  # 用这个也行，但要注意修改窗口类型
        except Exception as e:
            info("事件过滤器报错，具体原因如下所示！")
            error(e)

    def resizeEvent(self, qresizeevent):
        """
        :title 自定义窗口调整大小事件
        :param qresizeevent: 窗口事件
        :return: None
        """
        try:
            # 改变窗口大小的三个坐标范围
            self._right_rect = [QPoint(x, y) for x in range(self.width - 5, self.width + 5) for y in range(self.label_1.height() + 20, self.height - 5)]
            self._bottom_rect = [QPoint(x, y) for x in range(1, self.width - 5) for y in range(self.height - 5, self.height + 1)]
            self._corner_rect = [QPoint(x, y) for x in range(self.width - 5, self.width + 1) for y in range(self.height - 5, self.height + 1)]
        except Exception as e:
            info("自定义事件区域大小报错，具体原因如下所示！")
            error(e)

    def mousePressEvent(self, event):
        """
        :title 重写鼠标点击的事件
        :param event:鼠标点击事件
        :return: None
        """
        try:
            self.setMouseTracking(True)
            if (event.button() == Qt.LeftButton) and (event.pos() in self._corner_rect):
                # 鼠标左键点击右下角边界区域
                self._corner_drag = True
                event.accept()
            elif (event.button() == Qt.LeftButton) and (event.pos() in self._right_rect):
                # 鼠标左键点击右侧边界区域
                self._right_drag = True
                event.accept()
            elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_rect):
                # 鼠标左键点击下侧边界区域
                self._bottom_drag = True
                event.accept()
            elif (event.button() == Qt.LeftButton) and (event.y() < self.label_1.height()):
                # 鼠标左键点击标题栏区域
                self._move_drag = True
                self.move_DragPosition = event.globalPos() - self.pos()
                event.accept()
        except Exception as e:
            info("鼠标释放事件报错，具体原因如下所示！")
            error(e)

    def mouseMoveEvent(self, qmouseevent):
        """
        :title 重写鼠标移动事件
        :param qmouseevent: 鼠标事件
        :return: None
        """
        try:
            # 判断鼠标位置切换鼠标手势
            # qmouseevent.pos()获取相对位置
            if self.isMaximized():
                pass
            else:
                if qmouseevent.pos() in self._corner_rect:
                    self.setCursor(Qt.SizeFDiagCursor)
                elif qmouseevent.pos() in self._bottom_rect:
                    self.setCursor(Qt.SizeVerCursor)
                elif qmouseevent.pos() in self._right_rect:
                    self.setCursor(Qt.SizeHorCursor)
                # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
                # 没有定义左方和上方相关的5个方向，主要是因为实现起来不难，但是效果很差，拖放的时候窗口闪烁，再研究研究是否有更好的实现
                if Qt.LeftButton and self._right_drag:
                    # 右侧调整窗口宽度
                    self.resize(qmouseevent.pos().x(), self.height)
                    qmouseevent.accept()
                elif Qt.LeftButton and self._bottom_drag:
                    # 下侧调整窗口高度
                    self.resize(self.width, qmouseevent.pos().y())
                    qmouseevent.accept()
                elif Qt.LeftButton and self._corner_drag:
                    # 由于我窗口设置了圆角,这个调整大小相当于没有用了
                    # 右下角同时调整高度和宽度
                    self.resize(qmouseevent.pos().x(), qmouseevent.pos().y())
                    qmouseevent.accept()
                elif Qt.LeftButton and self._move_drag:
                    # 标题栏拖放窗口位置
                    self.move(qmouseevent.globalPos() - self.move_DragPosition)
                    qmouseevent.accept()
        except Exception as e:
            info("鼠标移动事件报错，具体原因如下所示！")
            error(e)

    def mouseReleaseEvent(self, qmouseevent):
        """
        :title 重写鼠标释放事件，鼠标释放后，各扳机复位
        :param qmouseevent: 鼠标事件
        :return: None
        """
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False


if __name__ == '__main__':
    from sys import argv, exit
    from SystemTray import TrayIcon
    app1 = QApplication(argv)
    demo = CodingTool()
    pic_path = demo.full_path
    tray = TrayIcon(demo, pic_path)
    tray.show()
    tray.show_window()
    exit(app1.exec_())
