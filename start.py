import menu_gui as guistart

def initialize():
	global processType, status, isProcessingBinerFile
	processType = ''
	status = ''
	isProcessingBinerFile = False

initialize()

if __name__ == '__main__':
	guistart.vp_start_gui()