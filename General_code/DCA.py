import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


def net_benefit_model(thresh_group, y_pred_score, y_label):
    net_benefit_model = np.array([])
    for thresh in thresh_group:
        y_pred_label = y_pred_score > thresh
        tn, fp, fn, tp = confusion_matrix(y_label, y_pred_label).ravel()
        n = len(y_label)
        net_benefit = (tp / n) - (fp / n) * (thresh / (1 - thresh))
        net_benefit_model = np.append(net_benefit_model, net_benefit)
    return net_benefit_model


def net_benefit_all(thresh_group, y_label):
    net_benefit_all = np.array([])
    tn, fp, fn, tp = confusion_matrix(y_label, y_label).ravel()
    total = tp + tn
    for thresh in thresh_group:
        net_benefit = (tp / total) - (tn / total) * (thresh / (1 - thresh))
        net_benefit_all = np.append(net_benefit_all, net_benefit)
    return net_benefit_all


def plot_DCA(ax, thresh_group, net_benefit_model, net_benefit_all):
    #Plot
    ax.plot(thresh_group, net_benefit_model, color = 'crimson', label = 'Model')
    ax.plot(thresh_group, net_benefit_all, color = 'black',label = 'Treat all')
    ax.plot((0, 1), (0, 0), color = 'black', linestyle = ':', label = 'Treat none')

    #Fill，显示出模型较于treat all和treat none好的部分
    y2 = np.maximum(net_benefit_all, 0)
    y1 = np.maximum(net_benefit_model, y2)
    ax.fill_between(thresh_group, y1, y2, color = 'crimson', alpha = 0.2)

    #Figure Configuration， 美化一下细节
    ax.set_xlim(0,1)
    ax.set_ylim(-0.02, net_benefit_model.max() + 0.15)#adjustify the y axis limitation
    ax.set_xlabel(
        xlabel = 'Threshold Probability', 
        fontdict= {'family': 'Times New Roman', 'fontsize': 15}
        )
    ax.set_ylabel(
        ylabel = 'Net Benefit', 
        fontdict= {'family': 'Times New Roman', 'fontsize': 15}
        )
    ax.grid('major')
    ax.spines['right'].set_color((0.8, 0.8, 0.8))
    ax.spines['top'].set_color((0.8, 0.8, 0.8))
    ax.legend(loc = 'upper right')

    return ax


if __name__ == '__main__':
    #构造一个分类效果不是很好的模型
    y_pred_score = np.arange(0, 1, 0.001)
    y_label = np.array([1]*25 + [0]*25 + [0]*450 + [1]*25 + [0]*25+ [1]*25 + [0]*25 + [1]*25 + [0]*25+ [1]*25 + [0]*25 + [1]*25 + [0]*25 + [1]*25 + [0]*25 + [1]*25 + [0]*50 + [1]*125)

    thresh_group = np.arange(0,1,0.01)
    net_benefit_model = net_benefit_model(thresh_group, y_pred_score, y_label)
    net_benefit_all = net_benefit_all(thresh_group, y_label)
    fig, ax = plt.subplots()
    ax = plot_DCA(ax, thresh_group, net_benefit_model, net_benefit_all)
    # fig.savefig('fig1.png', dpi = 300)
    plt.figure(dpi=300)
    plt.show()
