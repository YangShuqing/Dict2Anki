from PyQt4 import QtCore, QtGui
from aqt.utils import showInfo, askUser, tooltip

class groupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(groupDialog, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.resize(349, 219)
        self.gridLayout = QtGui.QGridLayout(self)
        self.layout = QtGui.QHBoxLayout()
        self.groupList = QtGui.QListWidget(self)
        self.debug = QtGui.QPlainTextEdit(self)
        self.layout.addWidget(self.groupList)
        self.layout.addWidget(self.debug)
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.layout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.layout, 0, 0, 1, 1)
        self.setWindowTitle("Please select word group")
        self.groupList.itemChanged.connect(self.selectAll)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.saveSettings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)

    def selectAll(self):
        if self.groupList.item(0).checkState():
            for i in range(self.groupList.count()):
                self.groupList.item(i).setCheckState(2)

    def saveSettings(self):
        self.selectedGroups = [self.groupList.item(i).text() for i in range(self.groupList.count()) if self.groupList.item(i).checkState()]
        if self.selectedGroups:
            self.accept()
        else:
            showInfo('Please select one group at least')


    def addYoudaoGroup(self,groupNames):
        allGroup = QtGui.QListWidgetItem()
        allGroup.setText('All Groups')
        allGroup.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        allGroup.setCheckState(QtCore.Qt.Unchecked)
        self.groupList.addItem(allGroup)

        for name in groupNames:
            item = QtGui.QListWidgetItem()
            item.setText(name)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.groupList.addItem(item)

    def addEudictGroup(self,groupNames):
        allGroup = QtGui.QListWidgetItem()
        allGroup.setText('All Groups')
        allGroup.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        allGroup.setCheckState(QtCore.Qt.Unchecked)
        self.groupList.addItem(allGroup)

        for name in groupNames.values():
            item = QtGui.QListWidgetItem()
            item.setText(name)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.groupList.addItem(item)
