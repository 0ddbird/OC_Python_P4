from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem


class PlayersTable(QTableWidget):
    def __init__(self, players):
        super().__init__()
        self.players = players
        self.setWindowTitle("players")
        self.setColumnCount(len(players[0]))
        self.setRowCount(len(players))

        headers = list(players[0].keys())
        self.setHorizontalHeaderLabels(headers)
        self.verticalHeader().setVisible(False)

        for i, player in enumerate(players):
            for j, key in enumerate(player):
                value = player[key]
                self.setItem(i, j, QTableWidgetItem(str(value)))

        self.resizeColumnsToContents()
        self.horizontalHeader().sectionClicked.connect(self.sort_by_column)
        self.sort_order = Qt.DescendingOrder

    def sort_by_column(self, column):
        self.sort_order = (
            Qt.AscendingOrder
            if self.sort_order == Qt.DescendingOrder
            else Qt.DescendingOrder
        )
        self.sortItems(column, self.sort_order)
