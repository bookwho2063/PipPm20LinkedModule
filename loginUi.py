# -*- coding: utf-8 -*-

import sys, os, time
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QTextBrowser, QGridLayout, QMessageBox, QDesktopWidget, QVBoxLayout, QHBoxLayout, QSizePolicy)
from PyQt5.QtGui import QIcon
import webbrowser

class AppUi(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		"""
		UI 기본환경을 구성한다.
		:return:
		"""
		# self.setGeometry(600, 400, 1200, 660)		# 앞2 : 창의 위치x,y  | 뒤2 : 창의 너비/높이

		# 버튼 정보
		self.btnStart = QPushButton('실행', self)  # 시작버튼
		self.btnStop = QPushButton('중지', self)  # 중지버튼
		self.btnPage = QPushButton('내손안의약국-관리자시스템', self)  # 내손안의약국관리자 페이지 호출 버튼

		self.btnStop.setEnabled(False)		# 중지버튼 비활성화 처리
		# 버튼 사이즈 조정 안먹음..
		# self.btnStart.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		# self.btnStop.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		# self.btnPage.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		# self.btnStart.setMaximumHeight(250)
		# self.btnStop.setMaximumHeight(250)
		# self.btnPage.setMaximumHeight(250)

		# self.btnStart.setCheckable(True)  # 선택되거나 선택되지않은 상태 유지 (True | False)
		# self.btnStart.toggle()
		# self.btnStart.setEnabled(False)  # setEnabled False 이면 버튼 사용 불가 설정 (실행 버튼 클릭 시 중지버튼 조작)

		# 버튼 클릭 이벤트
		self.btnStart.clicked.connect(self.btnStartClickEvent)
		self.btnStop.clicked.connect(self.btnStopClickEvent)
		self.btnPage.clicked.connect(self.btnPageClickEvent)

		# 텍스트브라우저
		self.textBrowser = QTextBrowser()					# 텍스트 브라우저 객체 생성
		self.textBrowser.setAcceptRichText(True)			# 서식있는 긴 텍스트 허용 여부
		self.textBrowser.setOpenExternalLinks(False)		# 텍스트 브라우저에서 외부링크 연결 가능 여부
		self.textBrowser.setFixedSize(1200, 500)

		# 레이아웃 모음
		btnHBox = QHBoxLayout()			# 버튼 가로 레이아웃 박스 생성
		btnHBox.addStretch(1)			# 빈공간 추가 (순차적으로 적용되므로 '빈공간 버튼 버튼 버튼 빈공간' 형태로 생성됨)
		btnHBox.addWidget(self.btnStart)		# '실행' 버튼 위젯 추가
		btnHBox.addWidget(self.btnStop)			# '중지' 버튼 위젯 추가
		btnHBox.addWidget(self.btnPage)			# '내손안의약국-관리자시스템' 버튼 위젯 추가
		btnHBox.addStretch(1)			# 빈공간 추가

		textVBox = QVBoxLayout()  		# 텍스트 세로 레이아웃 박스 생성
		#textVBox.addStretch()			# 세로 3분할 위에서 아래로
		textVBox.addWidget(self.textBrowser)			# 텍스트브라우저 추가
		textVBox.addLayout(btnHBox)		# 버튼 가로 레이아웃 추가 (위젯은 버튼, 텍스트, 라벨 등이고.. 레이아웃은 addLayout)
		textVBox.addStretch(2)  		# 버튼 박스 아래 1공간 추가
		self.setLayout(textVBox)		# 레이아웃에 버튼 레이아웃박스 추가


		# UI 레이아웃 기본 설정
		self.setWindowTitle('내손안의약국-피엠플러스20 처방전 연계모듈')		# APP Title
		self.setWindowIcon(QIcon('./img/image_48.png'))					# 창 좌상단 아이콘 설정
		self.resize(1200, 660)				# 창 크기 조정
		self.windowCenter()					# 창위치를 센터로 정렬하는 함수
		self.show()							# UI 출력
		
	def btnStartClickEvent(self):
		"""
		실행 버튼 클릭 이벤트
		:return: 
		"""
		try:
			print("##### 실행버튼클릭")
			self.appendTextBrowser('실행버튼클릭')

			# 실행버튼 클릭 비활성화
			self.btnStart.setEnabled(False)
			self.btnStop.setEnabled(True)
		except Exception as e:
			print("##### 내손안의약국 약국관리자 실행버튼클릭중 오류발생")
			print("##### error :: " + e)

	def btnStopClickEvent(self):
		"""
		중지 버튼 클릭 이벤트
		:return:
		"""
		try:
			print("##### 중지버튼클릭")
			self.appendTextBrowser('중지버튼클릭')

			# 실행버튼 클릭 활성화
			self.btnStart.setEnabled(True)
			self.btnStop.setEnabled(False)
		except Exception as e:
			print("##### 내손안의약국 약국관리자 중지버튼클릭 중 오류발생")
			print("##### error :: " + e)

	def btnPageClickEvent(self):
		"""
		내손안의약국 관리자 페이지 버튼 클릭 이벤트
		:return: 내손안의약국 관리자 시스템 브라우저 오픈
		"""
		try:
			print("##### 내손안의약국 약국관리자 시스템 브라우저를 연결합니다.")
			url = "https://adm.drxsolution.co.kr/"
			webbrowser.open(url)
		except Exception as e:
			print("##### 내손안의약국 약국관리자 시스템 브라우저를 연결중 오류발생")
			print("##### error :: " + e)


	def appendTextBrowser(self, text):
		"""
		텍스트를 브라우저에 입력처리한다.
		:return:
		"""
		try:
			print("##### 현재시각과 텍스트를 브라우저에 입력합니다.")
			insertText = self.getTime() + text
			self.textBrowser.append(insertText)
		except Exception as e:
			print("##### 내손안의약국 텍스트를 브라우저에 입력중 오류발생")
			print("##### error :: " + e)


	def windowCenter(self):
		"""
		기본 UI 를모니터 화면 중앙에 배치한다.
		:return:
		"""
		fg = self.frameGeometry()								# 창의 위치와 크기 정보 조회
		dw = QDesktopWidget().availableGeometry().center()		# 현재 사용중인 모니터의 가운데 위치 파악
		fg.moveCenter(dw)										# 창의 직사각형 위치를 화면의 중심 위치로 이동
		self.move(fg.topLeft())									# 현재 창을 화면의 중심으로 이동했던 직사각형위치(fg)로 이동

	def closeEvent(self, event):
		"""
		모듈의 '닫기'버튼 클릭시 이벤트 처리
		내부 이벤트 리스너
		:param event:
		:return:
		"""
		reply = QMessageBox.question(self, '내손안의약국', '내손안의약국-피엠플러스20\n연계모듈을 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			print("내손안의약국-피엠플러스20 연계모듈을 종료합니다.")
			event.accept()
		else:
			print("내손안의약국-피엠플러스20 연계모듈을 종료하지않습니다.")
			event.ignore()

	def getTime(self):
		try:
			now = time.localtime()
			nowTime = " [%04d-%02d-%02d %02d:%02d:%02d] " % (
			now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
			print("##### nowTime : " + nowTime)
			return str(nowTime)
		except Exception as e:
			print("##### 현재시간 생성중 오류가 발생하였습니다.")
			print("##### error :: " + e)
			return "error time"


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = AppUi()
	sys.exit(app.exec_())

	# for idx in range(1, 5):
	# 	print("asdasd")
	# 	ex.appendTextBrowser('HI')