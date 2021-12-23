from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.patches as patches

class PlotStatistics():
    pass

class PlotCanvas(PlotStatistics):

    def __init__(self):
        pass

    def plot_plan(self, widgettable, data):
        x = []
        y = []
        for item in data:
            n = item.name.split(' ')
            #print(n)
            x.append(n[0] + '\n' + n[1])
            y.append(item.plan_prcntg)
        widgettable.axis.clear()
        widgettable.axis.vlines(x=x, ymin=0, ymax=y, color='firebrick', linewidth=20)
        for i in range(len(x)):
            widgettable.axis.text(x[i], y[i], str(y[i]) + '%', horizontalalignment='center',
                                    verticalalignment='bottom',
                                    fontdict={'fontweight': 500, 'size': 7})
        widgettable.axis.set_xticks(x)
        widgettable.axis.set_xticklabels(x, rotation=20, horizontalalignment='center')
        widgettable.axis.set_title("Выполнение плана", fontsize=16)
        widgettable.axis.set_ylabel('Выполнение, %')
        widgettable.axis.set_ylim(0, y[-1] + 20)

        '''p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green',
                               transform=view.mywidget.figure.transFigure)
        p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red',
                               transform=view.mywidget.figure.transFigure)
        view.mywidget.figure.add_artist(p1)
        view.mywidget.figure.add_artist(p2)'''

        widgettable.canvas.draw()
        return 0

    def plot_manager_plan(self, view, data):
        return self.plot_plan(view.mywidget, data)

    def plot_admin_plan(self, view, data):
        return self.plot_plan(view.mywidgett, data)

    def plot_director_plan(self, view, data):
        return self.plot_plan(view.mywidgettt, data)

    def plot_manager_deals(self, widgettable, data):
        x = []
        y = []
        for item in data:
            x.append(item.company)
            y.append(round(float(item.deal_sum / 1000000), 2))
        widgettable.axis.clear()
        widgettable.axis.bar(x, y)
        for i in range(len(x)):
            widgettable.axis.text(x[i], y[i], y[i], horizontalalignment='center', verticalalignment='bottom',
                     fontdict={'fontweight': 500, 'size': 10})
        widgettable.axis.set_xticks(x)
        widgettable.axis.set_xticklabels(x, horizontalalignment='center')
        widgettable.axis.set_title("Сумма сделок компаний", fontsize=10)
        widgettable.axis.set_ylabel('Сумма, млн.р.')
        widgettable.axis.set_ylim(0, y[-1] + 15)
        widgettable.canvas.draw()
        return

    def plot_deals_approve(self, widgettable, data):
        x = []
        y = []
        for item in data:
            x.append(item.name)
            y.append(item.approve_prcntg)
        widgettable.axis.clear()
        widgettable.axis.bar(x, y)
        for i in range(len(x)):
            widgettable.axis.text(x[i], y[i], str(y[i]) + '%', horizontalalignment='center', verticalalignment='bottom',
                     fontdict={'fontweight': 500, 'size': 10})
        widgettable.axis.set_xticks(x)
        widgettable.axis.set_xticklabels(x, horizontalalignment='center')
        widgettable.axis.set_title("Процент одобренных сделок", fontsize=10)
        widgettable.axis.set_ylabel('Одобрения, %')
        widgettable.axis.set_ylim(0, y[-1] + 15)
        widgettable.canvas.draw()
        return